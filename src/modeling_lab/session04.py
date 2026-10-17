"""Session 04: three models transcribed from a four-page handwritten note.

Pages 1–2: three products assigned to four machines (LP).
Page 3: blending two crude-oil inputs (LP).
Page 4: revenue-to-total-cost ratio for products A and B (fractional LP).
Numerical optima are independently computed teaching extensions.
"""
from __future__ import annotations

from dataclasses import dataclass

from scipy.optimize import linprog

from .linear import LinearProgram

# Rows: products 1, 2, 3; columns: machines 1, 2, 3, 4.
MACHINE_UNIT_COSTS = (
    (4.0, 4.0, 5.0, 7.0),
    (6.0, 7.0, 5.0, 6.0),
    (12.0, 10.0, 8.0, 11.0),
)
MACHINE_HOURS_PER_UNIT = (
    (0.30, 0.25, 0.20, 0.20),
    (0.20, 0.30, 0.20, 0.25),
    (0.80, 0.60, 0.60, 0.50),
)
PRODUCT_MINIMUMS = (3000.0, 6000.0, 4000.0)
MACHINE_HOUR_CAPACITIES = (1500.0, 1200.0, 1500.0, 2000.0)

# Oil input recovery fractions: light 0.95, heavy 0.92.
CRUDE_PRICES = (20.0, 15.0)  # dollars per unit of raw crude
CRUDE_RECOVERY = (0.95, 0.92)
# Rows: diesel, kerosene, jet fuel; columns: light, heavy crude.
CRUDE_PRODUCT_FRACTIONS = ((0.40, 0.32), (0.20, 0.40), (0.35, 0.20))
REFINED_PRODUCT_MINIMUMS = (1_000_000.0, 500_000.0, 300_000.0)

# Thousand toman; table quantities A,B and fixed operating cost.
SALES_PRICES = (80.0, 40.0)
VARIABLE_COSTS = (40.0, 20.0)
FIXED_OPERATING_COST = 200.0
PRODUCTION_HOURS = (2.0, 3.0)
RAW_MATERIAL = (3.0, 2.0)
AVAILABLE_HOURS = 120.0
AVAILABLE_MATERIAL = 150.0


def machine_allocation_problem() -> LinearProgram:
    """12 nonnegative production quantities, four hour caps, three minima."""
    variables = tuple(f"x{i}_{j}" for i in range(1, 4) for j in range(1, 5))
    rows: list[tuple[float, ...]] = []
    rhs: list[float] = []
    names: list[str] = []
    for j in range(4):
        rows.append(tuple(MACHINE_HOURS_PER_UNIT[i][j] if k % 4 == j else 0.0
                          for k in range(12) for i in (k // 4,)))
        rhs.append(MACHINE_HOUR_CAPACITIES[j])
        names.append(f"machine_{j + 1}_hours")
    for i in range(3):
        rows.append(tuple(-1.0 if k // 4 == i else 0.0 for k in range(12)))
        rhs.append(-PRODUCT_MINIMUMS[i])
        names.append(f"product_{i + 1}_minimum")
    return LinearProgram(
        name="Session 04 — Three products on four machines",
        variables=variables,
        objective=tuple(c for row in MACHINE_UNIT_COSTS for c in row),
        maximize=False,
        a_ub=tuple(rows), b_ub=tuple(rhs), constraint_names=tuple(names),
        bounds=((0.0, None),) * 12, objective_unit="USD",
    )


def crude_oil_problem() -> LinearProgram:
    """Crude amounts before yield/recovery, not post-processing output."""
    rows = tuple(tuple(-CRUDE_PRODUCT_FRACTIONS[k][i] * CRUDE_RECOVERY[i]
                       for i in range(2)) for k in range(3))
    return LinearProgram(
        name="Session 04 — Light/heavy crude procurement",
        variables=("x_light", "x_heavy"), objective=CRUDE_PRICES,
        maximize=False, a_ub=rows,
        b_ub=tuple(-v for v in REFINED_PRODUCT_MINIMUMS),
        constraint_names=("diesel_min", "kerosene_min", "jet_fuel_min"),
        bounds=((0.0, None), (0.0, None)), objective_unit="USD",
    )


@dataclass(frozen=True)
class FractionalSolution:
    product_a: float
    product_b: float
    revenue: float
    total_cost: float
    revenue_cost_ratio: float
    variable_cost: float


def product_revenue_cost_ratio(a: float, b: float) -> float:
    """Return the *ratio* for a feasible nonnegative choice, not profit."""
    if min(a, b) < 0 or 2*a + 3*b > AVAILABLE_HOURS + 1e-9 or 3*a + 2*b > AVAILABLE_MATERIAL + 1e-9:
        raise ValueError("production plan violates a domain or resource constraint")
    return (SALES_PRICES[0]*a + SALES_PRICES[1]*b) / (VARIABLE_COSTS[0]*a + VARIABLE_COSTS[1]*b + FIXED_OPERATING_COST)


def fractional_production_solution() -> FractionalSolution:
    """Solve this special fractional problem by a mathematically exact reduction.

    Revenue equals 2 * variable_cost, so for fixed cost F>0 the objective
    2V/(V+F) strictly increases with V. A standard 2-variable LP therefore
    maximizes V; this is NOT a generic fractional-programming solver.
    """
    result = linprog(
        c=[-VARIABLE_COSTS[0], -VARIABLE_COSTS[1]],
        A_ub=[PRODUCTION_HOURS, RAW_MATERIAL],
        b_ub=[AVAILABLE_HOURS, AVAILABLE_MATERIAL],
        bounds=[(0, None), (0, None)], method="highs",
    )
    if not result.success or result.x is None:
        raise RuntimeError(f"Fractional-production reduction failed: {result.message}")
    a, b = map(float, result.x)
    revenue = SALES_PRICES[0]*a + SALES_PRICES[1]*b
    variable_cost = VARIABLE_COSTS[0]*a + VARIABLE_COSTS[1]*b
    total_cost = variable_cost + FIXED_OPERATING_COST
    return FractionalSolution(a, b, revenue, total_cost, revenue/total_cost, variable_cost)
