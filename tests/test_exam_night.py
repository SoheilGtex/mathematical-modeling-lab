"""Regression tests for the single generated end-of-term review."""

import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "exam_night_builder", ROOT / "scripts" / "build_exam_night.py"
)
assert SPEC is not None and SPEC.loader is not None
builder = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(builder)


def make_session(root: Path, number: int, body: str) -> None:
    directory = root / "sessions" / f"session_{number:02d}"
    directory.mkdir(parents=True)
    (directory / "README.md").write_text(
        f"# Session {number:02d}\n\n"
        f"{builder.START}\n{body}\n{builder.END}\n",
        encoding="utf-8",
    )


def test_committed_exam_night_matches_session_sources():
    assert (ROOT / "EXAM_NIGHT.md").read_text(encoding="utf-8") == builder.build()


def test_new_session_is_appended_and_sorted(tmp_path):
    make_session(tmp_path, 2, "### فارسی\nجلسه دوم")
    make_session(tmp_path, 1, "### English\n[Full solution](answer.md)")
    (tmp_path / "sessions" / "session_01" / "answer.md").write_text("Answer", encoding="utf-8")
    result = builder.build(tmp_path)
    assert result.index("## Session 01") < result.index("## Session 02")
    assert "sessions/session_01/answer.md" in result
    assert "جلسه دوم" in result


def test_missing_review_block_fails_loudly(tmp_path):
    directory = tmp_path / "sessions" / "session_02"
    directory.mkdir(parents=True)
    (directory / "README.md").write_text("# No excerpt\n", encoding="utf-8")
    with pytest.raises(ValueError, match="review markers"):
        builder.build(tmp_path)


def test_broken_local_links_are_not_silently_emitted(tmp_path):
    make_session(tmp_path, 1, "Read [missing file](does-not-exist.md).")
    with pytest.raises(ValueError, match="Broken local link"):
        builder.build(tmp_path)
