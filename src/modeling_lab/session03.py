"""Session 03 models transcribed from the four-page handwritten PDF.

The numerical 3x4 transportation instance is *lecture data*, unlike the
invented 2x2 demonstration provided in Session 02. Unit shipping costs are in toman according to the text above the table.

The production-planning instance contains five months, capacities for regular
and overtime production, and inventory carryover with zero initial and final
inventory. Both numerical optima are independent educational computations.
"""

from __future__ import annotations

from collections.abc import Sequence
import math

from .linear import LinearProgram
from .session02 import transportation_problem

ORIGINS = ("Tabriz", "Yazd", "Kerman")
DESTINATIONS = ("Tehran", "Mashhad", "Isfahan", "Shiraz")
TRANSPORT_COSTS = (
    (80.0, 5.0, 12.0, 15.0),
    (1.0, 9.0, 4.0, 5.0),
    (12.0, 8.0, 6.0, 4.0),
)
TRANSPORT_SUPPLY = (150.0, 300.0, 200.0)
TRANSPORT_DEMAND = (150.0, 200.0, 100.0, 200.0)

MONTHLY_DEMAND = (1200.0, 2100.0, 2400.0, 3000.0, 4000.0)
REGULAR_CAPACITY = 2000.0
OVERTIME_CAPACITY = 600.0
REGULAR_UNIT_COST = 10.0
OVERTIME_UNIT_COST = 15.0
INVENTORY_UNIT_COST = 2.0


def lecture_transportation_problem() -> LinearProgram:
    """3-source/4-destination *numerical* transportation model from Session 03."""
    original = transportation_problem(
        costs=TRANSPORT_COSTS,
        supplies=TRANSPORT_SUPPLY,
        demands=TRANSPORT_DEMAND,
    )
    # Reuse the already-tested arbitrary-dimensional transportation builder.
    return LinearProgram(
        name="Session 03 — Lecture transportation (3 origins, 4 destinations)",
        variables=original.variables,
        objective=original.objective,
        maximize=False,
        a_ub=original.a_ub,
        b_ub=original.b_ub,
        constraint_names=original.constraint_names,
        bounds=original.bounds,
        objective_unit="toman",
    )


def production_inventory_problem(
    *, demands: Sequence[float] = MONTHLY_DEMAND,
) -> LinearProgram:
    """Minimum five-month regular/overtime production and inventory cost.

    Variable order: x1..x5 (regular), y1..y5 (overtime), s1..s4 (stock).
    s0=s5=0 are fixed parameters, not decision variables. Each conservation
    equality is encoded as both <= and >= since LinearProgram stores <= only.
    """
    d = tuple(float(v) for v in demands)
    if len(d) != 5 or any(not math.isfinite(v) or v < 0 for v in d):
        raise ValueError("demands must contain five finite nonnegative values")
    variables = tuple(
        [*(f"x{i}" for i in range(1, 6)),
         *(f"y{i}" for i in range(1, 6)),
         *(f"s{i}" for i in range(1, 5))]
    )
    objective = tuple([10.0] * 5 + [15.0] * 5 + [2.0] * 4)
    bounds = tuple(
        [(0.0, REGULAR_CAPACITY)] * 5
        + [(0.0, OVERTIME_CAPACITY)] * 5
        + [(0.0, None)] * 4
    )
    rows: list[tuple[float, ...]] = []
    rhs: list[float] = []
    names: list[str] = []
    for month in range(5):
        row = [0.0] * 14
        row[month] = 1.0
        row[5 + month] = 1.0
        if month:
            row[10 + month - 1] = 1.0
        if month < 4:
            row[10 + month] = -1.0
        rows.extend((tuple(row), tuple(-v for v in row)))
        rhs.extend((d[month], -d[month]))
        names.extend((f"month_{month+1}_balance_max", f"month_{month+1}_balance_min"))
    return LinearProgram(
        name="Session 03 — Five-month production and inventory",
        variables=variables,
        objective=objective,
        maximize=False,
        a_ub=tuple(rows),
        b_ub=tuple(rhs),
        constraint_names=tuple(names),
        bounds=bounds,
        objective_unit="toman / five-month horizon",
    )
