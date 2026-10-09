#!/usr/bin/env python3
"""Generate the one modeling-only, bilingual exam review from review_sources.

Every session and every published assignment must have both language excerpts.
Run `python scripts/build_exam_night.py` to regenerate EXAM_NIGHT.md and both
MkDocs review pages. Run with --check in CI to reject stale or missing material.
"""

from __future__ import annotations

import argparse
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
PERSIAN_ORDINALS = {1: "اول", 2: "دوم", 3: "سوم", 4: "چهارم", 5: "پنجم", 6: "ششم"}


def fa_ordinal(n: int) -> str:
    return PERSIAN_ORDINALS.get(n, f"شمارهٔ {n}")


def topics(root: Path) -> list[tuple[str, str, str]]:
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
        for i, slug in enumerate(stems, 1):
            result.append((f"assignment_{slug}", f"Assignment {i:02d}", f"تمرین {fa_ordinal(i)}"))

    expected = {f"{key}.{lang}.md" for key, _, _ in result for lang in ("en", "fa")}
    actual = {p.name for p in (root / SOURCE).glob("*.md")}
    if missing := expected - actual:
        raise ValueError(f"Missing modeling-only exam sources: {', '.join(sorted(missing))}")
    if extra := actual - expected:
        raise ValueError(f"Unexpected exam source without session/assignment: {', '.join(sorted(extra))}")
    return result


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


def generated(root: Path = ROOT) -> dict[str, str]:
    root = root.resolve()
    sections = topics(root)
    root_parts = [
        "# EXAM NIGHT — Mathematical Modeling Only | مرور شب امتحان — فقط مدل‌سازی",
        "",
        "> **Instructor clarification:** the examination focuses on **model formulation only**.",
        "> **طبق توضیح استاد:** در امتحان **فقط مدل‌سازی ریاضی** مدنظر است.",
        "",
        "This is one cumulative guide for **every course session and assignment**. Define decision variables,",
        "write the objective and all constraints, and specify domains and units. Numerical solutions,",
        "optimality proofs, simplex and software are intentionally excluded from this exam review.",
        "Full worked solutions remain available from the linked pages.",
        "",
        "این فایل شامل **تمام جلسات و تمرین‌ها** است. تمرکز مرور بر تعریف متغیرها، تابع هدف،",
        "قیود، واحدها و دامنهٔ متغیرهاست؛ حل عددی و اثبات بهینگی در صفحات کامل باقی می‌مانند.",
        "این مجموعه یک منبع دانشجویی مستقل است، نه بارم‌بندی رسمی امتحان.",
        "",
        "**Generated file:** Edit the bilingual files in `review_sources/`, not this file.",
        "Run `python scripts/build_exam_night.py` after adding or changing a session/assignment.",
        "",
        "## Contents | فهرست",
        "",
    ]
    for key, en, fa in sections:
        root_parts.append(f"- [{en} | {fa}](#{key.replace('_', '-')})")
    root_parts.append("")

    en_parts = [
        "# Exam Review — Mathematical Modeling Only",
        "",
        "**Instructor clarification:** only mathematical modeling is required for the examination.",
        "This single cumulative review covers **all sessions and assignments**, including future additions.",
        "Practice defining the decision variables, objective, constraints, units and domains.",
        "Numerical optimization and proof of optimality belong to the complete worked solutions, not this revision sheet.",
        "This is an independent study aid, not an official exam syllabus or grading rubric.",
        "",
    ]
    fa_parts = [
        "# مرور شب امتحان — فقط مدل‌سازی ریاضی",
        "",
        "**طبق توضیح استاد، فقط مدل‌سازی مسائل در امتحان مدنظر است.**",
        "این مرور واحد، **تمام جلسات و تمرین‌ها** را شامل می‌شود و با اضافه‌شدن مطالب جدید تکمیل خواهد شد.",
        "در هر مسئله متغیرها و واحدشان، تابع هدف، قیود و دامنهٔ متغیرها را تمرین کنید.",
        "حل عددی و اثبات بهینگی در صفحات تشریحی کامل موجودند و در این مرور نیامده‌اند.",
        "این مجموعه راهنمای مستقل مطالعه است، نه بارم‌بندی رسمی امتحان.",
        "",
    ]

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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if any generated review is stale")
    args = parser.parse_args()
    try:
        outputs = generated()
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
        print("Modeling-only exam review is up to date (sessions + assignments; EN/FA)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
