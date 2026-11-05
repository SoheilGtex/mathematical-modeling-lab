"""Fuzzy modeling for course sessions 06–07.

Source: six-page student lecture scan ('26 Mehr'), pages 1–6.
The models and LR ranking are transcribed from the lecture; linear-programming
solutions, extension-principle derivations, and Kerre distances are independent
computational checks, not solutions stated in the source.

Both triangular representations are intentional:
- Triangular(left, mode, right) uses support/mode endpoints.
- LR(left_core, right_core, left_spread, right_spread) uses core/spreads.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import isfinite

import numpy as np
from scipy.integrate import quad
from scipy.optimize import linprog


@dataclass(frozen=True)
class Triangular:
    left: float
    mode: float
    right: float

    def __post_init__(self) -> None:
        if not all(isfinite(v) for v in (self.left, self.mode, self.right)):
            raise ValueError("Triangle parameters must be finite")
        if not self.left < self.mode < self.right:
            raise ValueError("This implementation requires left < mode < right")

    def membership(self, x: float) -> float:
        if x <= self.left or x >= self.right:
            return 0.0
        if x <= self.mode:
            return (x - self.left) / (self.mode - self.left)
        return (self.right - x) / (self.right - self.mode)

    def alpha_cut(self, level: float) -> tuple[float, float]:
        """Closed alpha-cut for 0 < level <= 1; level=0 is support closure."""
        if not 0.0 <= level <= 1.0:
            raise ValueError("alpha level must be in [0, 1]")
        return (self.left + level * (self.mode - self.left),
                self.right - level * (self.right - self.mode))

    def scaled(self, c: float) -> Triangular:
        if not isfinite(c) or c == 0:
            raise ValueError("Use a separate crisp singleton for a zero multiplier")
        values = (c * self.left, c * self.mode, c * self.right)
        return Triangular(*values) if c > 0 else Triangular(*reversed(values))

    def __add__(self, other: Triangular) -> Triangular:
        if not isinstance(other, Triangular):
            return NotImplemented
        return Triangular(self.left + other.left,
                          self.mode + other.mode,
                          self.right + other.right)

    def lr(self) -> LR:
        return LR(self.mode, self.mode,
                  self.mode - self.left, self.right - self.mode)


@dataclass(frozen=True)
class LR:
    """Trapezoidal LR = (left_core, right_core, left_spread, right_spread)."""
    left_core: float
    right_core: float
    left_spread: float
    right_spread: float

    def __post_init__(self) -> None:
        vals = (self.left_core, self.right_core, self.left_spread, self.right_spread)
        if not all(isfinite(v) for v in vals):
            raise ValueError("All LR parameters must be finite")
        if self.left_core > self.right_core or min(self.left_spread, self.right_spread) < 0:
            raise ValueError("LR requires ordered core and nonnegative spreads")

    def alpha_cut(self, level: float) -> tuple[float, float]:
        if not 0 <= level <= 1:
            raise ValueError("alpha level must be in [0, 1]")
        return (self.left_core - (1 - level) * self.left_spread,
                self.right_core + (1 - level) * self.right_spread)

    def membership(self, x: float) -> float:
        left, right = self.alpha_cut(0)
        if x < left or x > right:
            return 0.0
        if self.left_core <= x <= self.right_core:
            return 1.0
        if x < self.left_core and self.left_spread > 0:
            return (x - left) / self.left_spread
        if x > self.right_core and self.right_spread > 0:
            return (right - x) / self.right_spread
        return 0.0

    def rank(self) -> float:
        """Course-specific ranking: average of alpha-cut midpoints over [0,1]."""
        return ((self.left_core + self.right_core) / 2
                + (self.right_spread - self.left_spread) / 4)

    def __add__(self, other: LR) -> LR:
        if not isinstance(other, LR):
            return NotImplemented
        return LR(self.left_core + other.left_core,
                  self.right_core + other.right_core,
                  self.left_spread + other.left_spread,
                  self.right_spread + other.right_spread)

    def scaled(self, c: float) -> LR:
        if not isfinite(c):
            raise ValueError("Multiplier must be finite")
        if c >= 0:
            return LR(c * self.left_core, c * self.right_core,
                      c * self.left_spread, c * self.right_spread)
        return LR(c * self.right_core, c * self.left_core,
                  -c * self.right_spread, -c * self.left_spread)


def solve_ranked_lp(objective: tuple[LR, LR],
                    rows: tuple[tuple[LR, LR], tuple[LR, LR]],
                    bounds: tuple[LR, LR]) -> tuple[np.ndarray, float]:
    """Maximize rank of a two-variable fuzzy LP subject to ranked constraints.

    Important: these are constraints in the course-defined ranking order,
    not componentwise alpha-cut inequalities, chance constraints or robust LP.
    x_1,x_2 are nonnegative (required for positive scaling of LR coefficients).
    """
    c = np.array([v.rank() for v in objective], dtype=float)
    a = np.array([[v.rank() for v in row] for row in rows], dtype=float)
    b = np.array([v.rank() for v in bounds], dtype=float)
    result = linprog(-c, A_ub=a, b_ub=b, bounds=[(0, None)] * 2, method="highs")
    if not result.success:
        raise RuntimeError(f"Ranked model solver failed: {result.message}")
    return result.x, float(-result.fun)


def production_data() -> tuple[tuple[LR, LR], tuple[tuple[LR, LR], tuple[LR, LR]], tuple[LR, LR]]:
    """Page 3: triangular coefficients (left, mode, right)."""
    t = lambda x, y, z: Triangular(x, y, z).lr()
    return ((t(35, 40, 45), t(45, 50, 55)),
            ((t(1.5, 2, 2.5), t(.75, 1, 1.2)),
             (t(.25, 1, 1.5), t(2, 2.2, 2.5))),
            (t(98, 100, 102), t(78, 80, 82)))


def large_scale_data() -> tuple[tuple[LR, LR], tuple[tuple[LR, LR], tuple[LR, LR]], tuple[LR, LR]]:
    """Page 4: four-tuples (left core, right core, left spread, right spread)."""
    return ((LR(2, 3, 1, 1), LR(3, 4, 1, 2)),
            ((LR(1, 2, 1, 1), LR(2, 3, 1, 2)),
             (LR(2, 3, 1, 3), LR(1, 2, 1, 1))),
            (LR(5, 6, 2, 2), LR(4, 6, 2, 1)))


def max_alpha_cut(a: Triangular, b: Triangular, level: float) -> tuple[float, float]:
    """Exact extension-principle alpha-cut for max(X,Y).

    For fuzzy intervals and continuous max:
    [max(X,Y)]_alpha = [max(left_X,left_Y), max(right_X,right_Y)].
    """
    al, ar = a.alpha_cut(level)
    bl, br = b.alpha_cut(level)
    return max(al, bl), max(ar, br)


def max_extension_membership(a: Triangular, b: Triangular, z: float) -> float:
    """Inversion of nested alpha-cuts via bisection; generic triangular inputs."""
    low0, high0 = max_alpha_cut(a, b, 0.0)
    if z <= low0 or z >= high0:
        # Core can coincide with endpoint for degeneracies excluded by Triangular,
        # but check exact alpha=1 before declaring boundary membership zero.
        l1, r1 = max_alpha_cut(a, b, 1.0)
        return 1.0 if l1 <= z <= r1 else 0.0
    low1, high1 = max_alpha_cut(a, b, 1.0)
    if low1 <= z <= high1:
        return 1.0
    lo, hi = 0.0, 1.0
    for _ in range(55):
        mid = (lo + hi) / 2
        left, right = max_alpha_cut(a, b, mid)
        if left <= z <= right:
            lo = mid
        else:
            hi = mid
    return lo


LECTURE_M = Triangular(0, 2, 5)
LECTURE_N = Triangular(2, 3, 4)


def lecture_max_membership(z: float) -> float:
    """Exact analytic extension maximum for page 4–5 example."""
    if z < 2 or z > 5:
        return 0.0
    if z <= 3:
        return z - 2
    if z <= 3.5:
        return 4 - z
    return (5 - z) / 3


def l1_distance(f, g, knots: tuple[float, ...]) -> float:
    """L1 membership distance using piecewise integration at known breakpoints."""
    if len(knots) < 2 or any(y <= x for x, y in zip(knots, knots[1:])):
        raise ValueError("knots must be strictly increasing")
    return float(sum(quad(lambda x: abs(f(x) - g(x)), a, b,
                          epsabs=2e-11, epsrel=2e-11)[0]
                     for a, b in zip(knots, knots[1:])))


def kerre_lecture_distances() -> tuple[float, float, float]:
    """(d(M,max), d(N,max), d(M,max)-d(N,max)); exact 3/2,1/4,5/4."""
    f = lecture_max_membership
    breaks = (0.0, 2.0, 2.75, 3.0, 3.5, 4.0, 5.0)
    d_m = l1_distance(LECTURE_M.membership, f, breaks)
    d_n = l1_distance(LECTURE_N.membership, f, breaks)
    return d_m, d_n, d_m - d_n


def main() -> None:
    for title, data in (("production (p.3)", production_data()),
                        ("large-scale example (p.4)", large_scale_data())):
        x, value = solve_ranked_lp(*data)
        print(f"{title}: x1={x[0]:.9f}, x2={x[1]:.9f}, R(Z)={value:.9f}")
    dm, dn, score = kerre_lecture_distances()
    print(f"max distances: d(M,max)={dm:.9f}, d(N,max)={dn:.9f}, score={score:.9f}")


if __name__ == "__main__":
    main()
