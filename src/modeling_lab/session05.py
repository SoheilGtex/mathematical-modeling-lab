"""Session 05: fractional programming and triangular fuzzy membership.

The lecture defines the Charnes--Cooper transformation and a triangular fuzzy
number. Numerical optimization and its independent proof are study additions.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import isfinite

from scipy.optimize import linprog

NUMERATOR = (10.0, 20.0, 10.0)  # c1, c2, c0
DENOMINATOR = (3.0, 4.0, 20.0)  # d1, d2, d0
RESOURCE_ROWS = ((1.0, 3.0), (3.0, 2.0))
RESOURCE_LIMITS = (50.0, 80.0)
FUZZY_TRIANGLE = (1.0, 5.0, 7.0)


@dataclass(frozen=True)
class FractionalResult:
    x1: float
    x2: float
    y1: float
    y2: float
    t: float
    value: float


def fractional_objective(x1: float, x2: float) -> float:
    """Evaluate the source ratio on the nonnegative resource-feasible set."""
    if not (isfinite(x1) and isfinite(x2)):
        raise ValueError("Variables must be finite")
    if x1 < 0 or x2 < 0 or x1 + 3*x2 > 50 + 1e-9 or 3*x1 + 2*x2 > 80 + 1e-9:
        raise ValueError("Infeasible original variables")
    return (10*x1 + 20*x2 + 10) / (3*x1 + 4*x2 + 20)


def solve_fractional_example() -> FractionalResult:
    """Solve the lecture example via its Charnes--Cooper equivalent LP.

    With t=1/(3*x1+4*x2+20) and y_i=x_i*t:
        max 10*y1+20*y2+10*t
        s.t. y1+3*y2 <= 50*t; 3*y1+2*y2 <= 80*t
             3*y1+4*y2+20*t = 1; y1,y2,t >= 0.
    The original feasible set is compact; t=0 is infeasible in this LP.
    """
    result = linprog(
        c=[-10., -20., -10.],
        A_ub=[[1., 3., -50.], [3., 2., -80.]],
        b_ub=[0., 0.],
        A_eq=[[3., 4., 20.]],
        b_eq=[1.],
        bounds=[(0., None)]*3,
        method="highs",
    )
    if not result.success or result.x is None:
        raise RuntimeError(f"Fractional transformed LP failed: {result.message}")
    y1, y2, t = map(float, result.x)
    if t <= 0:
        raise RuntimeError("Transformation requires strictly positive t")
    x1, x2 = y1/t, y2/t
    return FractionalResult(x1,x2,y1,y2,t,fractional_objective(x1,x2))


def triangular_membership(x: float, a: float=1., b: float=5., c: float=7.) -> float:
    """Triangular fuzzy membership: support [a,c], peak b, with a<b<c."""
    if not all(map(isfinite,(x,a,b,c))) or not a < b < c:
        raise ValueError("Expected finite x and a < b < c")
    if x <= a or x >= c:
        return 0.
    if x <= b:
        return (x-a)/(b-a)
    return (c-x)/(c-b)
