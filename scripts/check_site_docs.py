#!/usr/bin/env python3
"""Check that the public documentation has complete EN/FA page pairs."""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1] / "site_docs"
PERSIAN = re.compile(r"[\u0600-\u06ff]")
LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
FENCE = re.compile(r"^\s*```", re.MULTILINE)
DIGIT_MAP = str.maketrans("۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩", "01234567890123456789")


def check() -> list[str]:
    errors: list[str] = []
    en = {p.relative_to(ROOT).as_posix().removesuffix(".en.md"): p
          for p in ROOT.rglob("*.en.md")}
    fa = {p.relative_to(ROOT).as_posix().removesuffix(".fa.md"): p
          for p in ROOT.rglob("*.fa.md")}
    for stem in sorted(en.keys() ^ fa.keys()):
        errors.append(f"Missing translation for {stem}")
    if len(en) < 18:
        errors.append("Missing a required public document (expected at least 18 topics per language)")
    for stem in sorted(en.keys() & fa.keys()):
        for lang, source in (("en", en[stem]), ("fa", fa[stem])):
            contents = source.read_text(encoding="utf-8")
            label = source.relative_to(ROOT)
            body = contents
            if contents.startswith("---\n"):
                _, marker, body = contents[4:].partition("\n---\n")
                if not marker:
                    errors.append(f"Unclosed front matter: {label}")
            if not body.lstrip().startswith("# "):
                errors.append(f"Missing page title: {label}")
            if len(contents.strip()) < 80:
                errors.append(f"Incomplete page: {label}")
            if len(FENCE.findall(contents)) % 2:
                errors.append(f"Unbalanced code fences: {label}")
            if contents.count("$$") % 2 or contents.count(r"\[") != contents.count(r"\]"):
                errors.append(f"Unbalanced display-math delimiters: {label}")
            # English prose must not contain Persian letters or Solar Hijri dates.
            if lang == "en" and PERSIAN.search(contents):
                errors.append(f"Persian script found in English page: {label}")
            if lang == "en" and re.search(r"\b(?:Fall|Autumn|Spring|Summer|Winter)\s+14(?:0[0-9])\b", contents):
                errors.append(f"Solar Hijri year found in English page: {label}")
            if lang == "fa" and re.search(r"\b(?:Fall|October|September)\s+2026\b", contents):
                errors.append(f"Gregorian course/date label found in Persian page: {label}")
            # Do not expose internal translation labels to readers.
            if re.search(r"(?m)^\s*\*\*(?:EN|FA|English|Persian|فارسی|انگلیسی):\*\*", contents):
                errors.append(f"Redundant language label in public page: {label}")
            for match in LINK.finditer(contents):
                dest = unquote(urlsplit(match.group(1)).path)
                if not dest or dest.startswith("/") or dest.startswith("#"):
                    continue
                if urlsplit(match.group(1)).scheme or dest.startswith("mailto:"):
                    continue
                candidate = (source.parent / dest).resolve()
                if dest.endswith(".md"):
                    candidate = candidate.with_name(candidate.stem + f".{lang}.md")
                if not candidate.is_file():
                    errors.append(f"Broken local link in {label}: {match.group(1)}")
    # The public homepages use the correct official course title and date calendar.
    for lang, expected in (("en", "Elementary Mathematical Modeling · Fall 2026"),
                           ("fa", "مدل‌سازی مقدماتی ریاضی · پاییز ۱۴۰۵")):
        homepage = (ROOT / f"index.{lang}.md").read_text(encoding="utf-8")
        if expected not in homepage:
            errors.append(f"Wrong course title or academic term in {lang} homepage")
        if not homepage.startswith("---\nhide:\n  - toc\n---\n"):
            errors.append(f"Homepage table of contents is not hidden: {lang}")
        if re.search(r"\]\(session-\d+/index\.md\)", homepage):
            errors.append(f"Homepage duplicates the session navigation: {lang}")
        if ("both sessions" in homepage or "دو جلسه" in homepage):
            errors.append(f"Homepage refers to a fixed number of sessions: {lang}")
        exam_page = (ROOT / f"exam.{lang}.md").read_text(encoding="utf-8")
        exam_heading = exam_page.splitlines()[0]
        if "Sessions 01–02" in exam_heading or "جلسات اول و دوم" in exam_heading:
            errors.append(f"Exam review title is tied to the current sessions: {lang}")
        # A single cumulative review should link to every published session.
        for session_dir in sorted(ROOT.glob("session-[0-9][0-9]")):
            if session_dir.is_dir() and f"{session_dir.name}/" not in exam_page:
                errors.append(f"Session missing from {lang} cumulative review: {session_dir.name}")
    # Key facts must appear in BOTH languages, not merely a language fallback.
    for lang in ("en", "fa"):
        src = (ROOT / f"session-02/televisions.{lang}.md").read_text("utf-8").translate(DIGIT_MAP)
        compact = re.sub(r"[,\u066c\s\\,]", "", src)
        if "60000" not in compact or "160000" not in compact or "159990" not in compact:
            errors.append(f"Missing verified TV capacity/objective results in {lang} page")
        transport = (ROOT / f"session-02/transportation.{lang}.md").read_text("utf-8")
        if "x_{ij}" not in transport or "c_{ij}" not in transport:
            errors.append(f"Incomplete symbolic transportation model in {lang} page")
    # Session 03 checks use the independently derived optima in both languages.
    for lang in ("en", "fa"):
        tfile = ROOT / f"session-03/transportation.{lang}.md"
        pfile = ROOT / f"session-03/production.{lang}.md"
        ttext = tfile.read_text("utf-8").translate(DIGIT_MAP)
        ptext = pfile.read_text("utf-8").translate(DIGIT_MAP)
        if lang == "en" and "toman" not in ttext:
            errors.append("Session 03 transportation currency missing from English page")
        if lang == "fa" and "تومان" not in ttext:
            errors.append("Session 03 transportation currency missing from Persian page")
        for name, txt, required in (
            ("transportation", ttext, ("2550", "650", "x_{12}", "u_i+v_j")),
            ("production", ptext, ("152300", "1200", "2100", "2400", "3000", "4000", "s_0=s_5=0")),
        ):
            compact = re.sub(r"[,\u066c\s\\,]", "", txt)
            for item in required:
                if item not in compact:
                    errors.append(f"Missing Session 03 {name} data/proof {item!r} in {lang}")
    return errors


if __name__ == "__main__":
    problems = check()
    if problems:
        for problem in problems:
            print(f"ERROR: {problem}", file=sys.stderr)
        sys.exit(1)
    print(f"Site docs verified: {len(list(ROOT.rglob('*.en.md')))} complete EN/FA pairs, local links and core data.")
