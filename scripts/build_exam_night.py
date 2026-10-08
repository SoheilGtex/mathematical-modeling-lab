#!/usr/bin/env python3
"""Build the single cumulative, bilingual, paper-exam review document.

Source excerpts live inside each sessions/session_NN/README.md, delimited by:
    <!-- EXAM_NIGHT_START -->
    <!-- EXAM_NIGHT_END -->

Never edit EXAM_NIGHT.md directly. CI uses --check to prevent stale material.
"""

from __future__ import annotations

import argparse
import difflib
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
START = "<!-- EXAM_NIGHT_START -->"
END = "<!-- EXAM_NIGHT_END -->"
SESSION_PATTERN = re.compile(r"session_(\d+)$")
LINK_PATTERN = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)")
HEADING_PATTERN = re.compile(r"^(#{1,5})(\s+.*)$", re.MULTILINE)


def _rewrite_links(content: str, session_dir: Path, root: Path) -> str:
    """Resolve local Markdown links relative to the generated root-level file."""

    def replace(match: re.Match[str]) -> str:
        label, target = match.groups()
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc or target.startswith(("/", "#", "mailto:")):
            return match.group(0)
        path = (session_dir / parsed.path).resolve()
        try:
            relative_path = path.relative_to(root)
        except ValueError as exc:
            raise ValueError(f"Link escapes repository: {target}") from exc
        if not path.exists():
            raise ValueError(f"Broken local link in {session_dir}: {target}")
        suffix = (f"?{parsed.query}" if parsed.query else "") + (
            f"#{parsed.fragment}" if parsed.fragment else ""
        )
        return f"[{label}]({relative_path.as_posix()}{suffix})"

    return LINK_PATTERN.sub(replace, content)


def build(root: Path = ROOT) -> str:
    root = root.resolve()
    session_root = root / "sessions"
    sessions: list[tuple[int, Path]] = []
    for child in session_root.iterdir():
        if child.is_dir() and (match := SESSION_PATTERN.fullmatch(child.name)):
            sessions.append((int(match.group(1)), child))
    sessions.sort(key=lambda item: item[0])
    if not sessions:
        raise ValueError("No sessions/session_NN directories found")
    if len({n for n, _ in sessions}) != len(sessions):
        raise ValueError("Duplicate numeric session indices")

    intro = [
        "# EXAM NIGHT — Cumulative Review | مرور یکپارچهٔ شب امتحان",
        "",
        "> **One file for the entire term.** Read this before the written, paper-based exam.",
        "> **یک فایل برای تمام ترم.** این راهنما خلاصهٔ مرور امتحان تشریحی است، نه جایگزین حل‌های کامل.",
        "",
        "This file is **generated** from marked review sections of each",
        "`sessions/session_NN/README.md`. Do not edit it directly; run",
        "`python scripts/build_exam_night.py` after adding/updating a session.",
        "CI runs `python scripts/build_exam_night.py --check` to reject stale output.",
        "",
        "توضیح منبع: صورت‌بندی مسائل جلسهٔ اول از جزوهٔ کلاس است؛ پاسخ‌های عددی،",
        "اثبات‌های بهینگی و نکات تکمیلی، محاسبات مستقل آموزشی هستند و محدودهٔ قطعی امتحان محسوب نمی‌شوند.",
        "",
        "## Contents | فهرست جلسات",
        "",
    ]
    for number, session_dir in sessions:
        intro.append(
            f"- [Session {number:02d} | جلسهٔ {number:02d}](#session-{number:02d})"
        )
    intro.append("")

    parts = ["\n".join(intro).rstrip()]
    for number, session_dir in sessions:
        readme = session_dir / "README.md"
        if not readme.is_file():
            raise ValueError(f"Missing required session guide: {readme}")
        source = readme.read_text(encoding="utf-8")
        if source.count(START) != 1 or source.count(END) != 1:
            raise ValueError(f"Session {number:02d} must have exactly one pair of review markers")
        before_end = source.split(END, 1)[0]
        if START not in before_end:
            raise ValueError(f"Incorrect review-marker order in {readme}")
        excerpt = before_end.split(START, 1)[1].strip()
        if not excerpt:
            raise ValueError(f"Empty review section in {readme}")
        # Shift excerpt headings down one level below the session heading.
        excerpt = HEADING_PATTERN.sub(lambda m: "#" + m.group(1) + m.group(2), excerpt)
        excerpt = _rewrite_links(excerpt, session_dir, root)
        parts.append(f"## Session {number:02d}\n\n**جلسهٔ {number:02d}**\n\n{excerpt}")
    return "\n\n---\n\n".join(parts).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if EXAM_NIGHT.md is stale")
    args = parser.parse_args()
    path = ROOT / "EXAM_NIGHT.md"
    try:
        expected = build()
    except (ValueError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    if args.check:
        current = path.read_text(encoding="utf-8") if path.exists() else ""
        if current != expected:
            diff = difflib.unified_diff(
                current.splitlines(keepends=True),
                expected.splitlines(keepends=True),
                fromfile=str(path),
                tofile="expected generated output",
            )
            sys.stderr.writelines(diff)
            print("EXAM_NIGHT.md is outdated; run python scripts/build_exam_night.py", file=sys.stderr)
            return 1
        print(f"EXAM_NIGHT.md is up to date ({expected.count('## Session ')} sessions)")
    else:
        path.write_text(expected, encoding="utf-8")
        print(f"Updated {path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
