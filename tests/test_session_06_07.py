"""Source-focused numeric and mathematical regression for lecture scan pages 1–6."""
from __future__ import annotations

from fractions import Fraction
from pathlib import Path

import numpy as np
import pytest

from modeling_lab.fuzzy_sessions import (
    LR, Triangular, LECTURE_M, LECTURE_N, kerre_lecture_distances,
    large_scale_data, lecture_max_membership, max_alpha_cut,
    max_extension_membership, production_data, solve_ranked_lp,
)


def test_triangular_original_data_and_levels():
    t = Triangular(1.2, 2, 2.4)
    assert t.lr() == LR(2, 2, 0.8, 0.4) or np.allclose(
        [t.lr().left_core, t.lr().right_core, t.lr().left_spread, t.lr().right_spread],
        [2, 2, .8, .4]
    )
    assert t.membership(2) == 1
    assert t.membership(1.2) == t.membership(2.4) == 0
    assert t.membership(1.6) == pytest.approx(.5)
    assert t.alpha_cut(.5) == pytest.approx((1.6, 2.2))
    assert t.alpha_cut(0) == pytest.approx((1.2, 2.4))  # support closure, not R
    assert t.alpha_cut(1) == pytest.approx((2, 2))


@pytest.mark.parametrize("level", [-.1, 1.1])
def test_invalid_cut_levels(level):
    with pytest.raises(ValueError):
        Triangular(0, 2, 5).alpha_cut(level)
    with pytest.raises(ValueError):
        LR(2, 3, 1, 2).alpha_cut(level)


@pytest.mark.parametrize("abc", [(2, 2, 4), (2, 1, 4), (0, 3, 3),
                                     (float('nan'), 2, 4)])
def test_invalid_triangles(abc):
    with pytest.raises(ValueError):
        Triangular(*abc)


def test_trapezoid_cores_membership_and_cut():
    q = LR(2, 3, 1, 2)
    assert q.alpha_cut(0) == (1, 5)
    assert q.alpha_cut(.5) == (1.5, 4)
    assert q.alpha_cut(1) == (2, 3)
    assert q.membership(2) == q.membership(2.5) == q.membership(3) == 1
    assert q.membership(1.5) == pytest.approx(.5)
    assert q.membership(4) == pytest.approx(.5)
    assert q.membership(0) == q.membership(6) == 0


def test_lr_arithmetic_addition_negation_and_scaling():
    a = LR(2, 3, 1, 2)
    b = LR(4, 5, 2, 3)
    assert a + b == LR(6, 8, 3, 5)
    assert a.scaled(-1) == LR(-3, -2, 2, 1)
    assert a.scaled(2) == LR(4, 6, 2, 4)
    assert a.scaled(-2) == LR(-6, -4, 4, 2)
    assert a.scaled(0) == LR(0, 0, 0, 0)
    assert a.rank() == pytest.approx(2.75)
    assert (a + b).rank() == pytest.approx(a.rank() + b.rank())
    assert a.scaled(-2).rank() == pytest.approx(-2 * a.rank())


def test_triangular_scaling_negative_reorders_endpoints():
    assert Triangular(1, 2, 4).scaled(-2) == Triangular(-8, -4, -2)


def test_source_production_coefficients():
    obj, rows, limits = production_data()
    assert [v.rank() for v in obj] == pytest.approx((40, 50))
    assert [[v.rank() for v in row] for row in rows] == pytest.approx(
        np.array([[2, .9875], [.9375, 2.225]]))
    assert [v.rank() for v in limits] == pytest.approx((100, 80))


def test_production_ranked_optimum_and_binding_constraints():
    obj, rows, limits = production_data()
    x, z = solve_ranked_lp(obj, rows, limits)
    assert x == pytest.approx((40.718244292, 18.798492574), abs=1e-7)
    assert z == pytest.approx(2568.654400355, abs=1e-7)
    a = np.array([[v.rank() for v in row] for row in rows])
    b = np.array([v.rank() for v in limits])
    assert a @ x == pytest.approx(b, abs=1e-8)


def test_source_lr_coefficients_and_optimum():
    objective, rows, limits = large_scale_data()
    assert [v.rank() for v in objective] == pytest.approx((2.5, 3.75))
    assert [[v.rank() for v in row] for row in rows] == pytest.approx(
        np.array([[1.5, 2.75], [3, 1.5]]))
    assert [v.rank() for v in limits] == pytest.approx((5.5, 4.75))
    x, z = solve_ranked_lp(objective, rows, limits)
    assert x == pytest.approx((77/96, 25/16), abs=1e-9)
    assert z == pytest.approx(float(Fraction(755, 96)), abs=1e-9)


def test_rank_not_componentwise_order():
    # Same R but different fuzzy shapes: equality under R is not equality of sets.
    assert Triangular(0, 2, 4).lr().rank() == Triangular(1, 2, 3).lr().rank()
    assert Triangular(0, 2, 4).membership(0.5) != Triangular(1, 2, 3).membership(0.5)


@pytest.mark.parametrize("level,expected", [
    (0, (2, 5)), (.25, (2.25, 4.25)), (.5, (2.5, 3.5)),
    (.75, (2.75, 3.25)), (1, (3, 3)),
])
def test_extension_max_alpha_cuts(level, expected):
    assert max_alpha_cut(LECTURE_M, LECTURE_N, level) == pytest.approx(expected)


@pytest.mark.parametrize("z,value", [
    (-1, 0), (0, 0), (2, 0), (2.5, .5), (2.75, .75),
    (3, 1), (3.25, .75), (3.5, .5), (4, 1/3), (4.5, 1/6), (5, 0), (6, 0),
])
def test_extension_max_analytic_and_cut_inversion(z, value):
    assert lecture_max_membership(z) == pytest.approx(value)
    assert max_extension_membership(LECTURE_M, LECTURE_N, z) == pytest.approx(value, abs=1e-12)


def test_extension_max_is_not_pointwise_membership_max():
    z = 2.5
    assert lecture_max_membership(z) == pytest.approx(.5)
    assert max(LECTURE_M.membership(z), LECTURE_N.membership(z)) == pytest.approx(5 / 6)


def test_extension_max_agrees_over_dense_grid():
    for z in np.linspace(-1, 6, 561):
        assert max_extension_membership(LECTURE_M, LECTURE_N, float(z)) == pytest.approx(
            lecture_max_membership(float(z)), abs=1e-12)


def test_kerre_distances_and_score():
    dm, dn, score = kerre_lecture_distances()
    assert dm == pytest.approx(1.5, abs=1e-10)
    assert dn == pytest.approx(.25, abs=1e-10)
    assert score == pytest.approx(1.25, abs=1e-10)
    assert dn < dm


def test_lecture_pages_bilingual_and_source_separation():
    root = Path(__file__).resolve().parents[1] / "site_docs"
    for name in ("foundations", "arithmetic", "ranking-production"):
        for language in ("en", "fa"):
            page = (root / "session-06" / f"{name}.{language}.md").read_text("utf8")
            assert "$$" in page and len(page) > 500
    for name in ("lr-model", "extension-max", "kerre"):
        for language in ("en", "fa"):
            page = (root / "session-07" / f"{name}.{language}.md").read_text("utf8")
            assert "$$" in page and len(page) > 500
