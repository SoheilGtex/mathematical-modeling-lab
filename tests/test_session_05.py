"""Regression checks for Session 05 lecture transcription and extensions."""
from __future__ import annotations

from pathlib import Path

import pytest

from modeling_lab.session05 import (
    DENOMINATOR, NUMERATOR, RESOURCE_LIMITS, RESOURCE_ROWS,
    fractional_objective, solve_fractional_example, triangular_membership,
)

ROOT = Path(__file__).resolve().parents[1]


def test_fractional_lecture_coefficients():
    assert NUMERATOR == (10., 20., 10.)
    assert DENOMINATOR == (3., 4., 20.)
    assert RESOURCE_ROWS == ((1., 3.), (3., 2.))
    assert RESOURCE_LIMITS == (50., 80.)


def test_transformed_lp_exact_solution():
    s = solve_fractional_example()
    assert s.x1 == pytest.approx(0., abs=1e-8)
    assert s.x2 == pytest.approx(50/3)
    assert s.y1 == pytest.approx(0., abs=1e-8)
    assert s.y2 == pytest.approx(5/26)
    assert s.t == pytest.approx(3/260)
    assert 3*s.y1 + 4*s.y2 + 20*s.t == pytest.approx(1.)
    assert s.y1 + 3*s.y2 <= 50*s.t + 1e-9
    assert 3*s.y1 + 2*s.y2 <= 80*s.t + 1e-9
    assert s.value == pytest.approx(103/26)
    assert 10*s.y1+20*s.y2+10*s.t == pytest.approx(s.value)


def test_fractional_optimality_certificate_at_all_vertices():
    vertices = ((0.,0.), (80/3,0.), (20.,10.), (0.,50/3))
    for x1,x2 in vertices:
        assert fractional_objective(x1,x2) <= 103/26 + 1e-10
    assert fractional_objective(0.,50/3) == pytest.approx(103/26)


def test_fractional_rejects_infeasible_points():
    for x1,x2 in ((-1,0),(0,-1),(0,17),(30,0),(float('nan'),0)):
        with pytest.raises(ValueError):
            fractional_objective(x1,x2)


def test_fuzzy_triangle_lecture_vertices_and_sample():
    assert triangular_membership(1.) == pytest.approx(0.)
    assert triangular_membership(5.) == pytest.approx(1.)
    assert triangular_membership(7.) == pytest.approx(0.)
    assert triangular_membership(1.2) == pytest.approx(0.05)


def test_fuzzy_triangle_both_slopes_and_outside():
    assert triangular_membership(3.) == pytest.approx(.5)
    assert triangular_membership(6.) == pytest.approx(.5)
    assert triangular_membership(-10.) == pytest.approx(0.)
    assert triangular_membership(50.) == pytest.approx(0.)


def test_fuzzy_membership_validates_shape():
    for params in ((1.,1.,7.),(7.,5.,1.),(1.,float('inf'),7.)):
        with pytest.raises(ValueError):
            triangular_membership(3.,*params)
    with pytest.raises(ValueError):
        triangular_membership(float('nan'))


def test_session05_bilingual_sources_and_exam_scope():
    for lang in ('en','fa'):
        for name in ('index','fractional','fuzzy','computation'):
            assert (ROOT/f'site_docs/session-05/{name}.{lang}.md').is_file()
        assert (ROOT/f'review_sources/session_05.{lang}.md').is_file()
        exam=(ROOT/f'site_docs/exam.{lang}.md').read_text(encoding='utf-8')
        assert 'session-05/fractional.md' in exam
        assert 'session-05/fuzzy.md' in exam
        # The modeling-only review has no new numerical optimizer result.
        assert '103/26' not in exam
    assert (ROOT/'examples/session_05/01_fractional_charnes_cooper.py').is_file()
    assert (ROOT/'examples/session_05/02_triangular_fuzzy.py').is_file()
