#!/usr/bin/env python3
"""Generate the one modeling-only, bilingual exam review from review_sources.

Every session and every published assignment must have both language excerpts.
Run `python scripts/build_exam_night.py` to regenerate EXAM_NIGHT.md and both
MkDocs review pages. Run with --check in CI to reject stale or missing material.
"""

from __future__ import annotations

import argparse
import json
import difflib
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "review_sources"
SESSION = re.compile(r"session_(\d+)$")
LINK = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)")
HEADING = re.compile(r"^(#{1,5})(\s+.*)$", re.MULTILINE)
PERSIAN_ORDINALS = {1: "اول", 2: "دوم", 3: "سوم", 4: "چهارم", 5: "پنجم", 6: "ششم", 7: "هفتم", 8: "هشتم", 9: "نهم", 10: "دهم", 11: "یازدهم"}


def fa_ordinal(n: int) -> str:
    return PERSIAN_ORDINALS.get(n, f"شمارهٔ {n}")


def topics(root: Path, period: str = "midterm") -> list[tuple[str, str, str]]:
    """List all published sessions followed by assignments, checking coverage."""
    session_root = root / "sessions"
    if not session_root.is_dir():
        raise ValueError("Missing sessions/ directory")
    numbers = sorted(
        int(match.group(1))
        for child in session_root.iterdir()
        if child.is_dir() and (match := SESSION.fullmatch(child.name))
    )
    if not numbers or len(numbers) != len(set(numbers)):
        raise ValueError("Missing sessions or duplicate numeric session IDs")

    result = [(f"session_{n:02d}", f"Session {n:02d}", f"جلسهٔ {fa_ordinal(n)}") for n in numbers]
    assignment_dir = root / "site_docs" / "assignments"
    if assignment_dir.exists():
        stems = sorted(p.name.removesuffix(".en.md") for p in assignment_dir.glob("*.en.md") if p.name != "index.en.md")
        persian = {p.name.removesuffix(".fa.md") for p in assignment_dir.glob("*.fa.md") if p.name != "index.fa.md"}
        if set(stems) != persian:
            raise ValueError("Every assignment must have both English and Persian site pages")
        # Keep numbering stable even when slug names are not alphabetically sorted.
        order_file = root / "assignments" / "ORDER.txt"
        if order_file.is_file():
            ordered = [line.strip() for line in order_file.read_text(encoding="utf-8").splitlines()
                       if line.strip() and not line.lstrip().startswith("#")]
            if len(ordered) != len(set(ordered)) or set(ordered) != set(stems):
                raise ValueError("Assignment ORDER.txt must list every published assignment exactly once")
            stems = ordered
        for i, slug in enumerate(stems, 1):
            result.append((f"assignment_{slug}", f"Assignment {i:02d}", f"تمرین {fa_ordinal(i)}"))

    expected = {f"{key}.{lang}.md" for key, _, _ in result for lang in ("en", "fa")}
    actual = {p.name for p in (root / SOURCE).glob("*.md")}
    if missing := expected - actual:
        raise ValueError(f"Missing modeling-only exam sources: {', '.join(sorted(missing))}")
    if extra := actual - expected:
        raise ValueError(f"Unexpected exam source without session/assignment: {', '.join(sorted(extra))}")
    if period not in {"midterm", "final", "all"}:
        raise ValueError("Unknown exam period")
    # In this course existing assignments are midterm. New assignments MUST be
    # explicitly classified; otherwise they might leak into the wrong review.
    assignment_keys={t[0] for t in result if t[0].startswith("assignment_")}
    periods_file = root / SOURCE / "exam_assignment_periods.json"
    if periods_file.is_file():
        assignment_periods = json.loads(periods_file.read_text(encoding="utf-8"))
        if set(assignment_periods) != assignment_keys or any(
            v not in ("midterm", "final") for v in assignment_periods.values()
        ):
            raise ValueError("Assignment exam periods must be complete and explicit")
    else:
        # Compatibility for legacy unit fixtures; the installation adds the map.
        assignment_periods={key: "midterm" for key in assignment_keys}
    if period == "all":
        return result
    return [t for t in result if
            (t[0].startswith("session_") and (int(t[0].split("_")[1]) <= 9) == (period=="midterm"))
            or (t[0].startswith("assignment_") and assignment_periods[t[0]]==period)]


def extract(root: Path, key: str, lang: str, *, site: bool) -> str:
    """Resolve standard MkDocs links into root-relative source links for GitHub."""
    source = root / SOURCE / f"{key}.{lang}.md"
    content = source.read_text(encoding="utf-8").strip()
    if not content or not content.startswith("### "):
        raise ValueError(f"Expected a nonempty model section starting with ### in {source}")

    def link(match: re.Match[str]) -> str:
        label, target = match.groups()
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc or target.startswith(("#", "mailto:")):
            return match.group(0)
        relative = unquote(parsed.path)
        if not relative.endswith(".md") or relative.startswith("/") or ".." in Path(relative).parts:
            raise ValueError(f"Unsupported or unsafe link in {source}: {target}")
        full_page = root / "site_docs" / Path(relative).with_suffix(f".{lang}.md")
        if not full_page.is_file():
            raise ValueError(f"Broken {lang} exam review link: {target} ({source})")
        if site:
            return match.group(0)
        suffix = (f"?{parsed.query}" if parsed.query else "") + (f"#{parsed.fragment}" if parsed.fragment else "")
        return f"[{label}](site_docs/{Path(relative).with_suffix(f'.{lang}.md').as_posix()}{suffix})"

    content = LINK.sub(link, content)
    if not site:
        # The root document has a language heading inside each topic.
        content = HEADING.sub(lambda m: "#" + m.group(1) + m.group(2), content)
    return content


def review_fragment(root: Path, name: str, lang: str) -> str:
    """Read editorial study sections outside the strict session-source registry."""
    path = root / "review_guides" / f"{name}.{lang}.md"
    if not path.is_file() and root.resolve() != ROOT.resolve():
        # Unit tests build a miniature course tree without editorial fragments.
        # Reuse immutable repository study-guidance, but keep all session data
        # and assignment coverage sourced from the supplied fixture tree.
        path = ROOT / "review_guides" / f"{name}.{lang}.md"
    content = path.read_text(encoding="utf-8").strip()
    if not content.startswith("## ") or len(content) < 100:
        raise ValueError(f"Missing or incomplete study guide: {path}")
    return content


def generated(root: Path = ROOT) -> dict[str, str]:
    root = root.resolve()
    sections = topics(root)
    # Only two public reviews; their names are deliberately simple and stable.
    opening_en = review_fragment(root, "midterm_opening", "en")
    opening_fa = review_fragment(root, "midterm_opening", "fa")
    practice_en = review_fragment(root, "midterm_practice", "en")
    practice_fa = review_fragment(root, "midterm_practice", "fa")
    root_parts = [
        "# مرور میان‌ترم", "",
        "**Midterm Review — Sessions 01–09 and their assigned coursework.**", "",
        "این مرور برای مطالعهٔ جلسات **۱ تا ۹** و تمرین‌های مربوط به این دوره است.",
        "مرور پایان‌ترم، از جلسهٔ **۱۰** به بعد، در فایل `EXAM_FINAL.md` نگهداری می‌شود.",
        "این نوشته منبع مستقل دانشجویی است، نه اطلاعیه یا بارم‌بندی رسمی آزمون.", "",
        "**Generated file:** Edit `review_sources/` and `review_guides/`, then run `python scripts/build_exam_night.py`.", "",
        opening_fa, "", opening_en, "",
        "## فهرست جلسات | Contents", "",
    ]
    en_parts = [
        "# Midterm Review", "",
        "**Sessions 01–09 and the assignments for this period.** The final exam has its own independent review.",
        "This is a student-written guide, not an official exam announcement or grading rubric.", "",
        opening_en, "",
    ]
    fa_parts = [
        "# مرور میان‌ترم", "",
        "**ویژهٔ جلسات ۱ تا ۹ و تمرین‌های مربوط به این بخش.** برای جلسات ۱۰ به بعد، صفحهٔ مستقل «مرور پایان‌ترم» را بخوانید.",
        "این راهنمای دانشجویی برای یادگیری و تمرین مدل‌سازی نوشته شده و برنامه یا بارم‌بندی رسمی امتحان نیست.", "",
        opening_fa, "",
    ]

    for key, en, fa in sections:
        root_parts.append(f"- [{en} | {fa}](#{key.replace('_', '-')})")
    root_parts.append("")

    for key, en, fa in sections:
        en_excerpt = extract(root, key, "en", site=True)
        fa_excerpt = extract(root, key, "fa", site=True)
        if key.startswith("session_"):
            number = int(key.split("_")[1])
            en_title, fa_title = f"Session {number:02d}", f"جلسهٔ {fa_ordinal(number)}"
        else:
            en_title, fa_title = en, fa
        en_parts.extend([f"## {en_title}", "", en_excerpt, ""])
        fa_parts.extend([f"## {fa_title}", "", fa_excerpt, ""])
        en_root = extract(root, key, "en", site=False)
        fa_root = extract(root, key, "fa", site=False)
        root_parts.extend([
            "---", "", f'<a id="{key.replace("_", "-")}"></a>',
            f"## {en_title} | {fa_title}", "", "### English", "", en_root, "",
            "### فارسی", "", fa_root, "",
        ])

    # Place practice after the explanations, with its answer key intentionally
    # separated from the prompts for genuine active recall.
    en_parts.extend([practice_en, ""])
    fa_parts.extend([practice_fa, ""])
    root_parts.extend(["---", "", practice_fa, "", practice_en, ""])

    en_parts.extend([
        "## Modeling-only checklist", "",
        "- [ ] Define every decision variable, its meaning, units and domain.",
        "- [ ] State whether the objective is minimized or maximized.",
        "- [ ] Translate each resource limit, minimum requirement and balance into a constraint.",
        "- [ ] Check inequality directions, conversions, indices and boundary conditions.",
        "- [ ] Present the complete mathematical model; no numerical optimum is required.", "",
    ])
    fa_parts.extend([
        "## چک‌لیست مدل‌سازی", "",
        "- [ ] همهٔ متغیرهای تصمیم، معنا، واحد و دامنهٔ آن‌ها را مشخص کرده‌ام.",
        "- [ ] کمینه یا بیشینه بودن تابع هدف را درست انتخاب کرده‌ام.",
        "- [ ] قیود ظرفیت، حداقل نیاز و موازنه را از صورت مسئله استخراج کرده‌ام.",
        "- [ ] جهت نامساوی‌ها، تبدیل واحدها، اندیس‌ها و شرایط ابتدا و انتها را کنترل کرده‌ام.",
        "- [ ] مدل نهایی را کامل نوشته‌ام؛ نیازی به محاسبهٔ جواب بهینه نیست.", "",
    ])
    return {
        "EXAM_NIGHT.md": "\n".join(root_parts).rstrip() + "\n",
        "site_docs/exam.en.md": "\n".join(en_parts).rstrip() + "\n",
        "site_docs/exam.fa.md": "\n".join(fa_parts).rstrip() + "\n",
    }



def generated_final(root: Path = ROOT) -> dict[str, str]:
    """Generate the independent Session-10+ review without midterm material."""
    root=root.resolve()
    sections=topics(root, period="final")
    if not sections:
        raise ValueError("Final review requires at least one published Session 10+")
    en=[
        "# Final Exam Review", "",
        "**Scope:** this review includes only Sessions 10 onward. Sessions 01–09 have a separate Midterm Review.",
        "This is an independent study summary, not an official exam announcement. The final-exam question types have not been specified by the supplied scan.",
        "Retain definitions, modeling choices, complete formulations and any verified worked calculations; do not invent missing source data.", "",
    ]
    fa=[
        "# مرور پایان‌ترم", "",
        "**محدودهٔ این مرور:** فقط جلسات ۱۰ به بعد. مطالب جلسات ۱ تا ۹ در صفحهٔ مستقل «مرور میان‌ترم» قرار دارند.",
        "این متن راهنمای مستقل دانشجویی است، نه اطلاعیهٔ رسمی امتحان. نوع و جزئیات سؤال‌های پایان‌ترم از جزوهٔ ارسالی مشخص نیست.",
        "تعریف‌ها، فرض‌های مدل‌سازی، مدل کامل و محاسبات قابل‌راستی‌آزمایی را مرور کنید؛ برای داده‌های مبهم جواب ساختگی ندهید.", "",
    ]
    root_lines=[
        "# مرور پایان‌ترم", "",
        "**Final Exam Review: Sessions 10+ only. Sessions 01–09 are covered in EXAM_NIGHT.md.**", "",
        "**فقط جلسات ۱۰ به بعد. مرور میان‌ترمِ جلسات ۱ تا ۹ در EXAM_NIGHT.md قرار دارد.**", "",
        "This is an independent student learning aid, not a published exam syllabus.", "",
        "**Generated file:** edit review_sources, then run python scripts/build_exam_night.py.", "",
    ]
    for key,en_name,fa_name in sections:
        if key.startswith("session_"):
            number=int(key.split("_")[1])
            title_en=f"Session {number:02d}"
            title_fa=f"جلسهٔ {fa_ordinal(number)}"
        else:
            title_en, title_fa=en_name, fa_name
        en_excerpt=extract(root,key,"en",site=True)
        fa_excerpt=extract(root,key,"fa",site=True)
        en.extend([f"## {title_en}","",en_excerpt,""])
        fa.extend([f"## {title_fa}","",fa_excerpt,""])
        root_lines.extend([
            f"## {title_en} | {title_fa}", "",
            "### English", "", extract(root,key,"en",site=False), "",
            "### فارسی", "", extract(root,key,"fa",site=False), "",
        ])
    en.extend(["## Final-exam preparation checklist", "",
               "- [ ] State whether the object is an ordinary fuzzy set, a hesitant fuzzy set, or a hesitant fuzzy number.",
               "- [ ] Verify each fuzzy tuple has ordered coordinates.",
               "- [ ] Give the source-defined ranking or explicitly state any additional rule.",
               "- [ ] Formulate variables, objective, constraints and units without fabricating ambiguous coefficients.", ""])
    fa.extend(["## چک‌لیست مرور پایان‌ترم", "",
               "- [ ] تفاوت مجموعهٔ فازی، مجموعهٔ فازی مردد و عدد فازی مردد را می‌دانم.",
               "- [ ] ترتیب مؤلفه‌های عددهای مثلثی و ذوزنقه‌ای را کنترل کرده‌ام.",
               "- [ ] روش رتبه‌بندیِ تعریف‌شده و فرض‌های اضافه را از هم جدا کرده‌ام.",
               "- [ ] متغیرها، تابع هدف، قیود و واحدها را بدون حدس‌زدن دادهٔ مبهم نوشته‌ام.", ""])
    return {
        "EXAM_FINAL.md":"\n".join(root_lines).rstrip()+"\n",
        "site_docs/exam-final.en.md":"\n".join(en).rstrip()+"\n",
        "site_docs/exam-final.fa.md":"\n".join(fa).rstrip()+"\n",
    }

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if any generated review is stale")
    args = parser.parse_args()
    try:
        outputs = {**generated(), **generated_final()}
    except (ValueError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    bad = False
    for name, expected in outputs.items():
        path = ROOT / name
        if args.check:
            current = path.read_text(encoding="utf-8") if path.exists() else ""
            if current != expected:
                sys.stderr.writelines(difflib.unified_diff(
                    current.splitlines(keepends=True), expected.splitlines(keepends=True),
                    fromfile=name, tofile="generated " + name,
                ))
                bad = True
        else:
            path.write_text(expected, encoding="utf-8")
            print(f"Updated {name}")
    if bad:
        print("Exam review is stale: run python scripts/build_exam_night.py", file=sys.stderr)
        return 1
    if args.check:
        print("Two independent reviews verified: Midterm Review (01–09), Final Exam Review (10+), EN/FA")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
