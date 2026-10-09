"""Coverage and modeling-only scope checks for the generated exam review."""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "scripts" / "build_exam_night.py"
spec = importlib.util.spec_from_file_location("exam_review_builder", MODULE)
assert spec and spec.loader
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


def test_all_exam_reviews_match_their_generated_sources():
    expected = builder.generated(ROOT)
    assert set(expected) == {"EXAM_NIGHT.md", "site_docs/exam.en.md", "site_docs/exam.fa.md"}
    for file, text in expected.items():
        assert (ROOT / file).read_text(encoding="utf-8") == text


def test_all_sessions_and_assignments_are_in_the_exam_review():
    sections = builder.topics(ROOT)
    en = (ROOT / "site_docs/exam.en.md").read_text(encoding="utf-8")
    fa = (ROOT / "site_docs/exam.fa.md").read_text(encoding="utf-8")
    for key, en_title, fa_title in sections:
        assert f"## {en_title}" in en
        assert f"## {fa_title}" in fa
    assert any(key.startswith("assignment_") for key, *_ in sections)


def test_exam_review_models_not_optimal_solutions():
    for page in ("EXAM_NIGHT.md", "site_docs/exam.en.md", "site_docs/exam.fa.md"):
        text = (ROOT / page).read_text(encoding="utf-8")
        for invalid_result in (r"\\boxed\{2550\}", "152300", "22.141826345", "160000", "159990"):
            assert not re.search(invalid_result, text), (page, invalid_result)
    assert "x_1-s_1=2" in (ROOT / "EXAM_NIGHT.md").read_text(encoding="utf-8")


def test_missing_new_assignment_fails_instead_of_silently_omitting_it(tmp_path):
    (tmp_path / "sessions" / "session_01").mkdir(parents=True)
    (tmp_path / "site_docs" / "assignments").mkdir(parents=True)
    (tmp_path / "review_sources").mkdir(parents=True)
    for lang in ("en", "fa"):
        (tmp_path / "site_docs" / "assignments" / f"new-assignment.{lang}.md").write_text("# example\n")
        (tmp_path / "review_sources" / f"session_01.{lang}.md").write_text("### source\n")
    with pytest.raises(ValueError, match="Missing modeling-only exam sources"):
        builder.topics(tmp_path)
