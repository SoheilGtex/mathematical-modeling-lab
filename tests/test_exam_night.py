"""Regression tests for the single generated, modeling-only exam review."""

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


def make_session(root: Path, number: int, en: str, fa: str) -> None:
    """Create a minimal published session and its bilingual modeling excerpts."""
    (root / "sessions" / f"session_{number:02d}").mkdir(parents=True)
    review = root / "review_sources"
    review.mkdir(parents=True, exist_ok=True)
    for lang, body in (("en", en), ("fa", fa)):
        (review / f"session_{number:02d}.{lang}.md").write_text(
            f"### Example\n{body}\n", encoding="utf-8"
        )


def test_committed_exam_night_matches_modeling_sources():
    assert (ROOT / "EXAM_NIGHT.md").read_text(encoding="utf-8") == (
        builder.generated(ROOT)["EXAM_NIGHT.md"]
    )


def test_new_session_is_appended_and_sorted(tmp_path):
    make_session(tmp_path, 2, "Second session", "جلسه دوم")
    make_session(tmp_path, 1, "Read [full solution](session-01/answer.md).", "جلسه اول")
    target = tmp_path / "site_docs" / "session-01" / "answer.en.md"
    target.parent.mkdir(parents=True)
    target.write_text("# Full solution\n", encoding="utf-8")
    result = builder.generated(tmp_path)["EXAM_NIGHT.md"]
    assert result.index("## Session 01") < result.index("## Session 02")
    assert "site_docs/session-01/answer.en.md" in result
    assert "جلسه دوم" in result


def test_missing_modeling_excerpt_fails_loudly(tmp_path):
    (tmp_path / "sessions" / "session_02").mkdir(parents=True)
    review = tmp_path / "review_sources"
    review.mkdir()
    (review / "session_02.en.md").write_text("### Model\nEnglish model\n", encoding="utf-8")
    with pytest.raises(ValueError, match="Missing modeling-only exam sources"):
        builder.generated(tmp_path)


def test_broken_local_links_are_not_silently_emitted(tmp_path):
    make_session(
        tmp_path, 1,
        "Read [missing file](session-01/does-not-exist.md).",
        "مدل فارسی",
    )
    with pytest.raises(ValueError, match="Broken en exam review link"):
        builder.generated(tmp_path)
