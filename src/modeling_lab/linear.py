"""Small, solver-independent representation of linear optimization models.

Continuous problems are solved by SciPy HiGHS (linprog); problems with integer
variables are solved as MILPs by SciPy HiGHS (milp).

All inequality constraints use A_ub @ x <= b_ub. Units are determined by the
problem and must be documented by the caller.
"""

from dataclasses import dataclass
from typing import Iterable

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, linprog, milp


class OptimizationError(RuntimeError):
    """Raised if a solver does not return a certified optimum."""

    def __init__(self, message: str, *, status: int | None = None) -> None:
        super().__init__(message)
        self.status = status


@dataclass(frozen=True)
class LinearProgram:
    name: str
    variables: tuple[str, ...]
    objective: tuple[float, ...]
    maximize: bool
    a_ub: tuple[tuple[float, ...], ...]
    b_ub: tuple[float, ...]
    constraint_names: tuple[str, ...]
    bounds: tuple[tuple[float | None, float | None], ...]
    objective_unit: str

    def __post_init__(self) -> None:
        n = len(self.variables)
        if not n or len(set(self.variables)) != n:
            raise ValueError("Provide a nonempty, unique set of variable names")
        if len(self.objective) != n or len(self.bounds) != n:
            raise ValueError("Objective and variable bounds must match variables")
        if len(self.a_ub) != len(self.b_ub) or len(self.a_ub) != len(self.constraint_names):
            raise ValueError("Each inequality needs a bound and a name")
        if any(len(row) != n for row in self.a_ub):
            raise ValueError("Constraint coefficient count must match variables")
        if len(set(self.constraint_names)) != len(self.constraint_names):
            raise ValueError("Constraint names must be unique")
        for lower, upper in self.bounds:
            if lower is not None and upper is not None and lower > upper:
                raise ValueError("Lower bound cannot exceed upper bound")


@dataclass(frozen=True)
class Solution:
    model_name: str
    objective_value: float
    objective_unit: str
    variable_values: dict[str, float]
    constraint_slacks: dict[str, float]
    integer_variables: frozenset[str]
    solver: str


def solve(model: LinearProgram, *, integer_variables: Iterable[str] = ()) -> Solution:
    """Solve a continuous LP, or an MILP when integer variables are specified.

    Raises OptimizationError for infeasible, unbounded, or interrupted results;
    no potentially-invalid primal values are returned as a successful solve.
    """
    integers = frozenset(integer_variables)
    unknown = integers - set(model.variables)
    if unknown:
        raise ValueError(f"Unknown integer variables: {sorted(unknown)}")

    objective = np.asarray(model.objective, dtype=float)
    c = -objective if model.maximize else objective
    a_ub = np.asarray(model.a_ub, dtype=float).reshape(-1, len(model.variables))
    b_ub = np.asarray(model.b_ub, dtype=float)
    lower = np.array([float("-inf") if lo is None else lo for lo, _ in model.bounds])
    upper = np.array([float("inf") if hi is None else hi for _, hi in model.bounds])

    if integers:
        integrality = np.array([int(name in integers) for name in model.variables])
        constraints = (
            [LinearConstraint(a_ub, -np.inf, b_ub)] if model.a_ub else []
        )
        result = milp(
            c=c,
            integrality=integrality,
            bounds=Bounds(lower, upper),
            constraints=constraints,
            options={"disp": False},
        )
        solver = "scipy.optimize.milp (HiGHS)"
    else:
        result = linprog(
            c=c,
            A_ub=a_ub if model.a_ub else None,
            b_ub=b_ub if model.a_ub else None,
            bounds=list(model.bounds),
            method="highs",
        )
        solver = "scipy.optimize.linprog (HiGHS)"

    if not result.success or result.x is None:
        raise OptimizationError(
            f"{model.name}: solver status={result.status}; {result.message}",
            status=int(result.status),
        )

    x = np.asarray(result.x, dtype=float)
    slack = b_ub - a_ub @ x
    # Validate the result independently to protect downstream interpretation.
    scale = max(1.0, float(np.max(np.abs(b_ub))) if b_ub.size else 1.0)
    tolerance = 1e-6 * scale
    if np.any(slack < -tolerance):
        raise OptimizationError("Solver returned a solution violating an inequality")
    if np.any(x < lower - tolerance) or np.any(x > upper + tolerance):
        raise OptimizationError("Solver returned a solution violating a variable bound")
    for idx, name in enumerate(model.variables):
        if name in integers and abs(x[idx] - round(x[idx])) > 1e-6:
            raise OptimizationError(f"Solver returned a fractional integer variable: {name}")

    return Solution(
        model_name=model.name,
        objective_value=float(objective @ x),
        objective_unit=model.objective_unit,
        variable_values=dict(zip(model.variables, map(float, x), strict=True)),
        constraint_slacks=dict(zip(model.constraint_names, map(float, slack), strict=True)),
        integer_variables=integers,
        solver=solver,
    )
