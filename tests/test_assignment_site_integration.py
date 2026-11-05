"""Assignment numbering and website attribution should not silently regress."""
from pathlib import Path

from test_exam_modeling_review import builder

ROOT=Path(__file__).resolve().parents[1]


def test_assignment_order_is_stable():
    assignments=[(key,en,fa) for key,en,fa in builder.topics(ROOT) if key.startswith('assignment_')]
    assert assignments==[
        ('assignment_investment-budget','Assignment 01','تمرین اول'),
        ('assignment_transportation-python','Assignment 02','تمرین دوم'),
        ('assignment_fuzzy-numbers-max','Assignment 03','تمرین سوم'),
    ]


def test_python_only_assignment_points_to_existing_code():
    assert (ROOT/'examples/session_03/01_transportation.py').is_file()
    for lang in ('en','fa'):
        index=(ROOT/f'site_docs/assignments/index.{lang}.md').read_text()
        page=(ROOT/f'site_docs/assignments/transportation-python.{lang}.md').read_text()
        assert 'examples/session_03/01_transportation.py' in index
        assert 'examples/session_03/01_transportation.py' in page
        assert ('2550' in page.replace(',', '') if lang == 'en' else '۲۵۵۰' in page)


def test_third_assignment_complete_and_review_model_only():
    for lang in ('en','fa'):
        page=(ROOT/f'site_docs/assignments/fuzzy-numbers-max.{lang}.md').read_text()
        review=(ROOT/f'review_sources/assignment_fuzzy-numbers-max.{lang}.md').read_text()
        assert '17}{3}' in page
        assert 'assignment03_fuzzy_A_B.png' in page
        assert 'assignment03_fuzzy_max.png' in page
        assert 'sup' in review
        assert '17}{3}' not in review
