"""Exact, auditable Kerre-style comparison for triangular fuzzy numbers.

Continuing the classroom source dated 3 Aban (three scanned pages).
This module deliberately reuses Triangular from sessions 06–07, but computes
extension-principle maxima and L1 distances *exactly* with rational segments.

Definitions:
    D = extension_max(A, B) (Zadeh extension, NOT pointwise max of membership)
    d(X,Y) = integral |mu_X(z)-mu_Y(z)| dz
    r(A,B) = d(A,D)-d(B,D); r>0 favors B, r<0 favors A.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from modeling_lab.fuzzy_sessions import Triangular


def _q(value: int | float | Fraction) -> Fraction:
    """Convert finite course input to an exact rational decimal number."""
    return Fraction(str(value))


@dataclass(frozen=True)
class PiecewiseLinear:
    """Continuous membership function given by x-sorted (x, height) knots.

    The function is zero outside the first and last knot. All coordinates are
    fractions so that integration and intersections are exact.
    """
    nodes: tuple[tuple[Fraction, Fraction], ...]

    def __post_init__(self) -> None:
        if len(self.nodes) < 3:
            raise ValueError("At least three nodes required")
        if any(not (0 <= v <= 1) for _, v in self.nodes):
            raise ValueError("Membership heights must lie in [0,1]")
        if any(a[0] >= b[0] for a, b in zip(self.nodes, self.nodes[1:])):
            raise ValueError("Knots must have strictly increasing x values")

    def at(self, x: int | float | Fraction) -> Fraction:
        x = _q(x)
        if x < self.nodes[0][0] or x > self.nodes[-1][0]:
            return Fraction(0)
        for (x0, y0), (x1, y1) in zip(self.nodes, self.nodes[1:]):
            if x0 <= x <= x1:
                return y0 + (y1 - y0) * (x - x0) / (x1 - x0)
        return Fraction(0)


def triangle_nodes(t: Triangular) -> PiecewiseLinear:
    return PiecewiseLinear(((_q(t.left), Fraction(0)),
                            (_q(t.mode), Fraction(1)),
                            (_q(t.right), Fraction(0))))


def cut(t: Triangular, alpha: int | float | Fraction) -> tuple[Fraction, Fraction]:
    alpha = _q(alpha)
    if not Fraction(0) <= alpha <= Fraction(1):
        raise ValueError("alpha must lie in [0,1]")
    left, mode, right = map(_q, (t.left, t.mode, t.right))
    return (left + alpha * (mode - left),
            right - alpha * (right - mode))


def _crossing_levels(first0: Fraction, first1: Fraction,
                     second0: Fraction, second1: Fraction) -> list[Fraction]:
    """Interior alpha at which two affine endpoints exchange dominance."""
    slope_diff = (first1 - first0) - (second1 - second0)
    if slope_diff == 0:
        return []
    alpha = (second0 - first0) / slope_diff
    return [alpha] if 0 < alpha < 1 else []


def extension_max_nodes(a: Triangular, b: Triangular) -> PiecewiseLinear:
    """Piecewise-affine membership of max(A,B) under Zadeh extension.

    The alpha-cut of the maximum is
    [max(L_A(alpha),L_B(alpha)), max(R_A(alpha),R_B(alpha))].
    Intersections of cut-endpoint lines are the only possible new breakpoints.
    """
    a0, a1 = cut(a, 0), cut(a, 1)
    b0, b1 = cut(b, 0), cut(b, 1)
    l_alphas = sorted({Fraction(0), Fraction(1), *_crossing_levels(
        a0[0], a1[0], b0[0], b1[0])})
    r_alphas = sorted({Fraction(0), Fraction(1), *_crossing_levels(
        a0[1], a1[1], b0[1], b1[1])})
    nodes_by_x: dict[Fraction, Fraction] = {}
    for alpha in l_alphas:
        x = max(cut(a, alpha)[0], cut(b, alpha)[0])
        if x in nodes_by_x and nodes_by_x[x] != alpha:
            raise ValueError("Inconsistent left membership knots")
        nodes_by_x[x] = alpha
    for alpha in r_alphas:
        x = max(cut(a, alpha)[1], cut(b, alpha)[1])
        if x in nodes_by_x and nodes_by_x[x] != alpha:
            raise ValueError("Inconsistent right membership knots")
        nodes_by_x[x] = alpha
    return PiecewiseLinear(tuple(sorted(nodes_by_x.items())))


def l1_exact(a: PiecewiseLinear, b: PiecewiseLinear) -> Fraction:
    """Exact integral |a-b| for continuous, finitely piecewise-affine curves.

    Split at every knot and every zero of the difference; use trapezoids.
    """
    if not isinstance(a, PiecewiseLinear) or not isinstance(b, PiecewiseLinear):
        raise TypeError("Expected piecewise-linear membership functions")
    knots = sorted({x for x, _ in (*a.nodes, *b.nodes)})
    total = Fraction(0)
    for x0, x1 in zip(knots, knots[1:]):
        d0, d1 = a.at(x0) - b.at(x0), a.at(x1) - b.at(x1)
        width = x1 - x0
        if d0 * d1 < 0:
            # Zero divides into two exact triangles.
            abs0, abs1 = abs(d0), abs(d1)
            total += width * (abs0 * abs0 + abs1 * abs1) / (2 * (abs0 + abs1))
        else:
            total += width * (abs(d0) + abs(d1)) / 2
    return total


@dataclass(frozen=True)
class Comparison:
    """Pairwise result: positive score favors second; negative favors first."""
    distance_first: Fraction
    distance_second: Fraction
    score: Fraction
    max_membership: PiecewiseLinear

    @property
    def relation(self) -> str:
        return "second" if self.score > 0 else "first" if self.score < 0 else "tie"


def compare(a: Triangular, b: Triangular) -> Comparison:
    d = extension_max_nodes(a, b)
    da = l1_exact(triangle_nodes(a), d)
    db = l1_exact(triangle_nodes(b), d)
    return Comparison(da, db, da - db, d)


SOURCE_M = Triangular(2, 5, 12)
SOURCE_N = Triangular(2, 4, 10)


def source_result() -> Comparison:
    """Independent completion of the handwritten page-3 example."""
    return compare(SOURCE_M, SOURCE_N)


if __name__ == "__main__":
    for a, b in ((Triangular(0, 2, 5), Triangular(2, 3, 4)),
                 (SOURCE_M, SOURCE_N)):
        result = compare(a, b)
        print(f"M={a}, N={b}")
        print(f"d(M,D)={result.distance_first}, d(N,D)={result.distance_second}, "
              f"r={result.score}; favored: {result.relation}")
        print("extension knots:", result.max_membership.nodes)
