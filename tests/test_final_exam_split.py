"""Prevent post-midterm source leakage and stale review page generation."""
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('exam_build_final',ROOT/'scripts/build_exam_night.py')
assert spec and spec.loader
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def test_period_boundaries_and_sources():
    mid = mod.topics(ROOT,period='midterm')
    final = mod.topics(ROOT,period='final')
    assert {int(key.rsplit('_',1)[1]) for key,*_ in mid if key.startswith('session_')} == set(range(1,10))
    assert {int(key.rsplit('_',1)[1]) for key,*_ in final if key.startswith('session_')} == {10,11}
    assert all(key.startswith('session_') for key,*_ in final)
    assert any(key.startswith('assignment_') for key,*_ in mid)


def test_both_generated_reviews_match_published_files():
    for name, text in {**mod.generated(ROOT),**mod.generated_final(ROOT)}.items():
        assert (ROOT/name).read_text(encoding='utf-8') == text, name


def test_midterm_and_final_reviews_are_disjoint():
    for lang in ('en','fa'):
        mid = (ROOT/f'site_docs/exam.{lang}.md').read_text('utf-8')
        final = (ROOT/f'site_docs/exam-final.{lang}.md').read_text('utf-8')
        assert 'session-09/' in mid and 'session-10/' not in mid
        assert 'session-10/' in final and 'session-11/' in final
        assert 'session-09/' not in final
    rootmid=(ROOT/'EXAM_NIGHT.md').read_text('utf-8')
    rootfin=(ROOT/'EXAM_FINAL.md').read_text('utf-8')
    assert 'session-10' not in rootmid and 'session-10' in rootfin
    assert 'session-09' not in rootfin


def test_site_navigation_has_two_periods():
    nav=(ROOT/'mkdocs.yml').read_text('utf-8')
    assert 'Midterm Archive: exam.md' in nav
    assert 'Final Exam Review: exam-final.md' in nav
    assert 'Session 10:' in nav and 'Session 11:' in nav
