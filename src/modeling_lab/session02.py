"""Session 02 models from one handwritten lecture page.

The labor capacity was clarified by the student as 60,000 person-hours.
The initial transcription of the handwritten page had been ambiguous.
This corrected value is the default for the TV model and can be overridden
explicitly for independent what-if analysis.

The transportation example is symbolic in the source (no numeric dataset).
The `transportation_demo_problem` uses independently invented illustrative
numbers, never presented as class data.
"""

from __future__ import annotations

import math
from collections.abc import Sequence

from .linear import LinearProgram

TV_LABOR_HOURS = 60_000.0


def television_problem(*, labor_hours: float = TV_LABOR_HOURS) -> LinearProgram:
    """Maximize television profit, respecting labor and monthly sales limits.

    x1: color televisions; x2: black-and-white televisions. The handwritten
    formulation has nonnegative continuous variables; integrality is an option
    for the solver, not an assumption silently added to this model.
    """
    if not math.isfinite(labor_hours) or labor_hours < 0:
        raise ValueError("labor_hours must be a finite nonnegative number")
    return LinearProgram(
        name=f"Session 02 — Television production ({labor_hours:g} person-hours)",
        variables=("x1", "x2"),
        objective=(60.0, 30.0),
        maximize=True,
        a_ub=((20.0, 15.0),),
        b_ub=(float(labor_hours),),
        constraint_names=("monthly_labor_person_hours",),
        bounds=((0.0, 2000.0), (0.0, 4000.0)),
        objective_unit="dollars/month",
    )


def transportation_problem(
    costs: Sequence[Sequence[float]],
    supplies: Sequence[float],
    demands: Sequence[float],
) -> LinearProgram:
    """Construct a capacitated transportation LP with exact destination demand.

    Source i ships at most supplies[i]; destination j must receive exactly
    demands[j]. Existing LinearProgram supports only <= constraints, so each
    demand equality is represented by two inequalities. Variables x{i}_{j}
    are row-major, 1-indexed, nonnegative *continuous* shipment amounts.
    """
    m, n = len(supplies), len(demands)
    if m == 0 or n == 0 or len(costs) != m or any(len(row) != n for row in costs):
        raise ValueError("costs must be a nonempty m-by-n matrix")
    values = [*supplies, *demands, *(cost for row in costs for cost in row)]
    if any(not math.isfinite(v) for v in values):
        raise ValueError("All transportation parameters must be finite")
    if any(x < 0 for x in supplies) or any(x < 0 for x in demands):
        raise ValueError("Supplies and demands must be nonnegative")
    if sum(supplies) + 1e-9 < sum(demands):
        raise ValueError("Total supply below total demand: infeasible complete network")

    variables = tuple(f"x{i + 1}_{j + 1}" for i in range(m) for j in range(n))
    objective = tuple(float(costs[i][j]) for i in range(m) for j in range(n))
    rows: list[tuple[float, ...]] = []
    rhs: list[float] = []
    names: list[str] = []

    for i in range(m):
        rows.append(tuple(1.0 if k // n == i else 0.0 for k in range(m * n)))
        rhs.append(float(supplies[i]))
        names.append(f"source_{i+1}_capacity")
    for j in range(n):
        row = tuple(1.0 if k % n == j else 0.0 for k in range(m * n))
        rows.extend((row, tuple(-v for v in row)))
        rhs.extend((float(demands[j]), -float(demands[j])))
        names.extend((f"destination_{j+1}_demand_max", f"destination_{j+1}_demand_min"))

    return LinearProgram(
        name=f"Session 02 — Transportation ({m} sources, {n} destinations)",
        variables=variables,
        objective=objective,
        maximize=False,
        a_ub=tuple(rows),
        b_ub=tuple(rhs),
        constraint_names=tuple(names),
        bounds=tuple((0.0, None) for _ in variables),
        objective_unit="cost units",
    )


def transportation_demo_problem() -> LinearProgram:
    """Independent constructed example; no numeric transport data in notes."""
    return transportation_problem(
        costs=((2.0, 5.0), (4.0, 1.0)),
        supplies=(10.0, 20.0),
        demands=(12.0, 18.0),
    )
