"""Exact analytic identities and regression tests for third course assignment."""
from __future__ import annotations

import math

import pytest

from modeling_lab.assignment03 import (
    A, B, CROSSOVER, TriangularFuzzy, max_alpha_cut,
    max_membership_via_extension, max_membership_piecewise,
)


@pytest.mark.parametrize('z,expected_a,expected_b', [
    (-1,0.,0.), (1,0.,0.), (2,.5,0.), (3,1.,0.),
    (4,.75,.5), (5,.5,1.), (6,.25,0.), (7,0.,0.), (10,0.,0.),
])
def test_individual_memberships(z,expected_a,expected_b):
    assert A.membership(z)==pytest.approx(expected_a)
    assert B.membership(z)==pytest.approx(expected_b)


@pytest.mark.parametrize('z,expected', [
    (2.,0.),(3.,0.),(4.,.5),(5.,1.),(5.5,.5),
    (17./3,1./3),(6.,.25),(7.,0.),(9.,0.),
])
def test_max_extension_piecewise_expected(z,expected):
    assert max_membership_via_extension(z)==pytest.approx(expected)
    assert max_membership_piecewise(z)==pytest.approx(expected)


def test_piecewise_and_extension_identical_on_dense_grid():
    for i in range(-100,801):
        z=i/100
        assert max_membership_piecewise(z)==pytest.approx(
            max_membership_via_extension(z), abs=1e-12)


def test_alpha_cuts_and_crossover():
    assert max_alpha_cut(0)==pytest.approx((3,7))
    assert max_alpha_cut(1./3)==pytest.approx((11./3,17./3))
    assert max_alpha_cut(.5)==pytest.approx((4.,5.5))
    assert max_alpha_cut(1.)==pytest.approx((5.,5.))
    assert CROSSOVER==pytest.approx(17./3)


def test_alpha_cut_nested_for_all_levels():
    old_lower,old_upper=max_alpha_cut(0.)
    for i in range(1,101):
        lower,upper=max_alpha_cut(i/100)
        assert old_lower<=lower<=upper<=old_upper
        old_lower,old_upper=lower,upper


def test_reject_invalid_triangle_or_argument():
    with pytest.raises(ValueError): TriangularFuzzy(1,1,7)
    with pytest.raises(ValueError): TriangularFuzzy(3,2,7)
    with pytest.raises(ValueError): TriangularFuzzy(1,3,math.inf)
    with pytest.raises(ValueError): A.membership(float('nan'))
    with pytest.raises(ValueError): A.alpha_cut(1.1)


def test_figure_assets_exist():
    from pathlib import Path
    root=Path(__file__).resolve().parents[1]
    for png in ('assignment03_fuzzy_A_B.png','assignment03_fuzzy_max.png'):
        assert (root/'site_docs/assets'/png).is_file()
