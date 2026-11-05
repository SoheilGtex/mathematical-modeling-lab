"""Exact regression and property tests for classroom sessions 08–09."""
from fractions import Fraction as F

import pytest

from modeling_lab.fuzzy_sessions import Triangular, max_extension_membership
from modeling_lab.fuzzy_comparison import (
    SOURCE_M, SOURCE_N, compare, cut, extension_max_nodes, l1_exact,
    source_result, triangle_nodes,
)


def test_lesson_previous_maximum_reproduced_exactly():
    a, b = Triangular(0, 2, 5), Triangular(2, 3, 4)
    d = extension_max_nodes(a, b)
    expected = ((F(2),F(0)),(F(3),F(1)),(F(7,2),F(1,2)),(F(5),F(0)))
    assert d.nodes == expected
    assert compare(a, b).distance_first == F(3,2)
    assert compare(a, b).distance_second == F(1,4)
    assert compare(a, b).score == F(5,4)


def test_new_source_example_exact_result():
    result = source_result()
    assert result.max_membership == triangle_nodes(SOURCE_M)
    assert result.distance_first == 0
    assert result.distance_second == F(17,9)
    assert result.score == F(-17,9)
    assert result.relation == "first"


@pytest.mark.parametrize('alpha', [0, F(1,4), F(1,2), F(3,4), 1])
def test_source_max_alpha_cuts(alpha):
    a, b = cut(SOURCE_M, alpha), cut(SOURCE_N, alpha)
    assert a[0] >= b[0] and a[1] >= b[1]
    assert extension_max_nodes(SOURCE_M,SOURCE_N).at(5) == 1


@pytest.mark.parametrize('a,b', [
    (Triangular(0,1,5),Triangular(1,3,4)),
    (Triangular(-2,0,1),Triangular(-1,1,3)),
    (Triangular(1,6,10),Triangular(2,3,9)),
    (Triangular(-5,-3,0),Triangular(0,2,5)),
    (Triangular(0,3,7),Triangular(1,2,11)),
])
def test_score_antisymmetry(a,b):
    ab,ba = compare(a,b), compare(b,a)
    assert ab.score == -ba.score
    assert ab.max_membership == ba.max_membership
    assert ab.distance_first == ba.distance_second


@pytest.mark.parametrize('a,b', [
    (Triangular(0,1,5),Triangular(1,3,4)),
    (Triangular(-2,0,1),Triangular(-1,1,3)),
    (Triangular(1,6,10),Triangular(2,3,9)),
    (Triangular(-5,-3,0),Triangular(0,2,5)),
])
def test_extension_nodes_match_bisection_membership(a,b):
    d=extension_max_nodes(a,b)
    low,high=d.nodes[0][0],d.nodes[-1][0]
    for i in range(51):
        x=float(low+(high-low)*F(i,50))
        assert float(d.at(x)) == pytest.approx(max_extension_membership(a,b,x),abs=5e-11)


def test_source_triangular_memberships_and_inconsistent_handwritten_denominators():
    # N=(2,4,10) -> left span 2, right span 6; not 4 and 4.
    n = triangle_nodes(SOURCE_N)
    assert n.at(2)==0 and n.at(4)==1 and n.at(10)==0
    assert n.at(3)==F(1,2)
    assert n.at(7)==F(1,2)
    # Crossing of M's left branch and N's right branch:
    assert triangle_nodes(SOURCE_M).at(F(14,3)) == triangle_nodes(SOURCE_N).at(F(14,3))


def test_identity_and_translation_and_scaling():
    a,b=SOURCE_M,SOURCE_N
    assert compare(a,a).score==0
    shifted=lambda t,s: Triangular(t.left+s,t.mode+s,t.right+s)
    assert compare(shifted(a,13),shifted(b,13)).score==compare(a,b).score
    scaled=lambda t,k: Triangular(t.left*k,t.mode*k,t.right*k)
    assert compare(scaled(a,3),scaled(b,3)).score==3*compare(a,b).score


def test_invalid_level_and_knot_error():
    with pytest.raises(ValueError):cut(SOURCE_M,F(-1,2))
    with pytest.raises(ValueError):cut(SOURCE_N,F(5,4))
    with pytest.raises(TypeError): l1_exact(triangle_nodes(SOURCE_M),None)
