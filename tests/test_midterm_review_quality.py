"""Regression tests for the two explicitly named, independent study reviews."""
from pathlib import Path
import importlib.util
import re

ROOT = Path(__file__).resolve().parents[1]


def test_two_review_names_and_periods():
    fa_mid = (ROOT/'site_docs/exam.fa.md').read_text('utf-8')
    en_mid = (ROOT/'site_docs/exam.en.md').read_text('utf-8')
    fa_final = (ROOT/'site_docs/exam-final.fa.md').read_text('utf-8')
    en_final = (ROOT/'site_docs/exam-final.en.md').read_text('utf-8')
    assert fa_mid.startswith('# مرور میان‌ترم\n')
    assert fa_final.startswith('# مرور پایان‌ترم\n')
    assert en_mid.startswith('# Midterm Review\n')
    assert en_final.startswith('# Final Exam Review\n')
    assert 'session-09/' in fa_mid and 'session-10/' not in fa_mid
    assert 'session-10/' in fa_final and 'session-09/' not in fa_final
    assert (ROOT/'EXAM_NIGHT.md').read_text('utf-8').startswith('# مرور میان‌ترم\n')
    assert (ROOT/'EXAM_FINAL.md').read_text('utf-8').startswith('# مرور پایان‌ترم\n')
    nav = (ROOT/'mkdocs.yml').read_text('utf-8')
    assert '  - Midterm Review: exam.md' in nav
    assert '  - Final Exam Review: exam-final.md' in nav
    assert 'Midterm Review: مرور میان‌ترم' in nav
    assert 'Final Exam Review: مرور پایان‌ترم' in nav


def test_midterm_is_a_substantial_self_study_guide():
    fa = (ROOT/'site_docs/exam.fa.md').read_text('utf-8')
    assert len(fa) > 28000
    for required in (
        'نقشهٔ مطالعهٔ یک‌روزه', 'الگوی شش‌مرحله‌ای',
        'تولید و انبار', 'چارنز–کوپر', 'برش آلفا',
        'اصل گسترش', 'Kerre', 'آزمون خودآزمایی',
        'پاسخنامهٔ تشریحی کوتاه', 'سؤال ۱۶',
    ):
        assert required in fa, required
    for n in range(1, 10):
        assert f'session-{n:02d}/' in fa
    assert 'session-10/' not in fa
    for source in (ROOT/'review_sources').glob('session_0[1-9].fa.md'):
        assert 'خودآزمایی سریع' in source.read_text('utf-8'), source


def test_builder_reproducibility_and_study_fragments():
    spec = importlib.util.spec_from_file_location('review_builder', ROOT/'scripts/build_exam_night.py')
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    for name, content in {**mod.generated(ROOT), **mod.generated_final(ROOT)}.items():
        assert (ROOT/name).read_text('utf-8') == content, name
    for lang in ('en','fa'):
        for name in ('midterm_opening','midterm_practice'):
            assert (ROOT/'review_guides'/f'{name}.{lang}.md').is_file()


def test_final_review_does_not_absorb_midterm_curriculum():
    for lang in ('en', 'fa'):
        final = (ROOT/'site_docs'/f'exam-final.{lang}.md').read_text('utf-8')
        assert not re.search(r'\bsession-0[1-9]/', final)
        assert 'session-10/' in final and 'session-11/' in final
