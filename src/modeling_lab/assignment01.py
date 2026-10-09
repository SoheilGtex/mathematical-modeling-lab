"""Assignment 01: four-year municipal financing with long-term securities.

The scanned Persian handout calls the securities 'shares' but explicitly gives
coupon interest, a common maturity and a 20-year payment period. Accordingly,
they are treated as interest-bearing long-term securities, not ordinary equity.

All money values are in millions of US dollars, and years 1..4 start at the
beginning of the corresponding project years. Deposits made after funding the
annual project costs mature at the *next* year's beginning.

The nominal coupon-interest objective counts 20 annual payments on every
long-term security; the principal repayment is not part of that objective.
"""
from __future__ import annotations

from .linear import LinearProgram

ANNUAL_NEEDS = (2.0, 4.0, 8.0, 5.0)
LONG_TERM_RATES = (0.07, 0.06, 0.065, 0.075)
SHORT_TERM_RATES = (0.06, 0.055, 0.045)
INTEREST_PAYMENT_YEARS = 20


def investment_budget_problem() -> LinearProgram:
    """Seven nonnegative variables: x1..x4 bond proceeds, s1..s3 deposits.

    Four funding equalities are represented as two <= inequalities apiece,
    as required by the repository's generic LinearProgram abstraction.
    """
    variables = ("x1", "x2", "x3", "x4", "s1", "s2", "s3")
    equalities = (
        (1.0, 0.0, 0.0, 0.0, -1.0, 0.0, 0.0),
        (0.0, 1.0, 0.0, 0.0, 1.06, -1.0, 0.0),
        (0.0, 0.0, 1.0, 0.0, 0.0, 1.055, -1.0),
        (0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.045),
    )
    rows: list[tuple[float, ...]] = []
    rhs: list[float] = []
    names: list[str] = []
    for i, (coefficients, need) in enumerate(zip(equalities, ANNUAL_NEEDS, strict=True), start=1):
        rows.extend((coefficients, tuple(-c for c in coefficients)))
        rhs.extend((need, -need))
        names.extend((f"year_{i}_balance_max", f"year_{i}_balance_min"))
    return LinearProgram(
        name="Assignment 01 — Four-year municipal investment budgeting",
        variables=variables,
        objective=tuple(
            [INTEREST_PAYMENT_YEARS * rate for rate in LONG_TERM_RATES]
            + [0.0, 0.0, 0.0]
        ),
        maximize=False,
        a_ub=tuple(rows),
        b_ub=tuple(rhs),
        constraint_names=tuple(names),
        bounds=((0.0, None),) * len(variables),
        objective_unit="million USD nominal coupon interest over 20 years",
    )


def exact_optimal_plan() -> dict[str, float]:
    """Analytical candidate, independent of the numerical optimizer."""
    s3 = ANNUAL_NEEDS[3] / (1 + SHORT_TERM_RATES[2])
    s2 = (ANNUAL_NEEDS[2] + s3) / (1 + SHORT_TERM_RATES[1])
    return {"x1": 2.0, "x2": 4.0 + s2, "x3": 0.0, "x4": 0.0,
            "s1": 0.0, "s2": s2, "s3": s3}


def annual_coupon_cost(plan: dict[str, float]) -> float:
    """Annual coupon expense in millions of USD (not present value)."""
    return sum(LONG_TERM_RATES[i] * plan[f"x{i + 1}"] for i in range(4))


def proof_coefficients() -> tuple[float, float, float]:
    """Positive coefficients of (s1, x3, x4) in the reduced objective."""
    return (
        LONG_TERM_RATES[0] - (1 + SHORT_TERM_RATES[0]) * LONG_TERM_RATES[1],
        LONG_TERM_RATES[2] - LONG_TERM_RATES[1] / (1 + SHORT_TERM_RATES[1]),
        LONG_TERM_RATES[3] - LONG_TERM_RATES[1] / (
            (1 + SHORT_TERM_RATES[1]) * (1 + SHORT_TERM_RATES[2])
        ),
    )
