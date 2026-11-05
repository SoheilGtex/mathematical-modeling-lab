"""Exact and defensive regression tests for the first final-exam sessions."""
from fractions import Fraction as F
import pytest
from modeling_lab.hesitant_final import (
    CLASS_HFS, HEIGHTS, RANK_A, RANK_B, Triangle, Trapezoid,
    common_support_interval, crisp_threshold, hesitant_set,
    hesitant_triangle_rank, hesitant_trapezoid_rank, ranked_production_scenario,
    tall_ramp,
)


def test_hesitant_degrees_from_page_one():
    assert CLASS_HFS['x1'] == (F(1,5), F(2,5), F(1,2))
    assert CLASS_HFS['x2'] == (F(3,10), F(2,5))
    assert CLASS_HFS['x3'] == (F(1,5),F(3,10),F(1,2),F(3,5))


def test_finite_set_not_multiset():
    assert hesitant_set({'x':[0.4,'0.4',F(2,5)]})['x'] == (F(2,5),)

@pytest.mark.parametrize('invalid', [[],[-0.01],[1.01]])
def test_invalid_degrees_rejected(invalid):
    with pytest.raises(ValueError): hesitant_set({'x': invalid})


def test_empty_universe_rejected():
    with pytest.raises(ValueError): hesitant_set({})


def test_source_crisp_threshold():
    assert crisp_threshold(HEIGHTS,180) == {'b','c'}
    assert crisp_threshold({'x':180, 'y':181},180) == {'y'}

@pytest.mark.parametrize('h,expected',[(145,0),(170,0),(173,F(3,10)),(179,F(9,10)),(180,1),(195,1)])
def test_height_ramp(h,expected):
    assert tall_ramp(h) == expected


def test_ramp_bounds_require_order():
    with pytest.raises(ValueError): tall_ramp(175,180,170)


def test_rank_source_example():
    assert hesitant_trapezoid_rank(RANK_A) == F(9,2)
    assert hesitant_trapezoid_rank(RANK_B) == F(15,4)
    assert hesitant_trapezoid_rank(RANK_A) > hesitant_trapezoid_rank(RANK_B)


def test_ranking_reduces_to_single_trapezoid():
    t=Trapezoid(1,2,4,5)
    assert hesitant_trapezoid_rank([t]) == t.rank == 3


def test_empty_ranking_rejected():
    with pytest.raises(ValueError): hesitant_trapezoid_rank([])
    with pytest.raises(ValueError): hesitant_triangle_rank([])


def test_malformed_trapezoid_rejected():
    with pytest.raises(ValueError): Trapezoid(50,55,40,60)


def test_triangle_embedding_differs_from_three_vertex_average():
    tri=Triangle(1,2,7)
    assert tri.rank == 3
    assert tri.rank != F(10,3)


def test_triangle_support_intersection():
    assert common_support_interval([Triangle(1,3,5),Triangle(3,4,8)]) == (F(3),F(5))
    assert common_support_interval([Triangle(1,2,3),Triangle(4,5,6)]) is None


def test_scenario_explicit_assumptions():
    m=ranked_production_scenario()
    assert m == {'profit_a':F(50),'profit_b':F(40),'time_a':F(2),'time_b':F(3),'capacity':F(105,2)}
    # Per-unit return favours product A under THIS ranking rule.
    assert m['profit_a']/m['time_a'] > m['profit_b']/m['time_b']
    x= m['capacity']/m['time_a']
    assert x == F(105,4)
    assert m['profit_a']*x == F(2625,2)
