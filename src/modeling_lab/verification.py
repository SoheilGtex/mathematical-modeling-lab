"""Independent primal checks and LP primal-dual optimality certificates.

The primal checks use model coefficients rather than solver-provided slacks.
For continuous LPs, a dual *candidate* is computed with SciPy HiGHS, but its
feasibility and duality gap are checked separately by matrix arithmetic.
This is independent of trusting the primal solve's "success" flag, though the
candidate is still obtained with the same solver family.

For MILPs, a valid candidate and a solver-reported bound do NOT constitute an
independent proof of global optimality. We record them as separate evidence.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite
from typing import Literal

import numpy as np
from scipy.optimize import linprog

from .linear import LinearProgram, Solution

Evidence = Literal["lp_primal_dual", "milp_solver_bound", "none"]


@dataclass(frozen=True)
class VerificationReport:
    model_name: str
    primal_feasible: bool
    integrality_satisfied: bool
    objective_consistent: bool
    independent_optimality_verified: bool
    evidence: Evidence
    max_inequality_violation: float
    max_bound_violation: float
    max_integrality_violation: float
    objective_absolute_error: float
    lp_primal_dual_gap: float | None
    lp_dual_stationarity_residual: float | None
    # LP dual multipliers are with respect to all modeled <= constraints,
    # including the finite lower and upper variable bounds.
    lp_dual_multipliers: dict[str, float] | None
    milp_solver_objective_bound: float | None
    milp_solver_relative_gap: float | None
    milp_bound_consistent: bool | None
    notes: tuple[str, ...]

    @property
    def candidate_valid(self) -> bool:
        return self.primal_feasible and self.integrality_satisfied and self.objective_consistent


def _dual_system(model: LinearProgram) -> tuple[np.ndarray, np.ndarray, tuple[str, ...]]:
    """Convert all finite bounds to <= inequalities; variables are free in dual."""
    n = len(model.variables)
    rows = [list(row) for row in model.a_ub]
    rhs = list(model.b_ub)
    labels = [f"constraint:{name}" for name in model.constraint_names]
    for j, (lower, upper) in enumerate(model.bounds):
        if lower is not None:
            row = [0.] * n
            row[j] = -1.
            rows.append(row)
            rhs.append(-float(lower))
            labels.append(f"lower:{model.variables[j]}")
        if upper is not None:
            row = [0.] * n
            row[j] = 1.
            rows.append(row)
            rhs.append(float(upper))
            labels.append(f"upper:{model.variables[j]}")
    a = np.asarray(rows, dtype=float).reshape(-1, n)
    return a, np.asarray(rhs, dtype=float), tuple(labels)


def _tolerance(atol: float, rtol: float, *scales: float) -> float:
    return atol + rtol * max(1., *(abs(float(v)) for v in scales))


def verify_solution(
    model: LinearProgram,
    solution: Solution,
    *,
    atol: float = 1e-7,
    rtol: float = 1e-8,
    integer_tolerance: float = 1e-6,
) -> VerificationReport:
    """Validate a candidate and, if continuous, seek a primal-dual LP proof.

    An LP certificate requires dual feasibility plus a sufficiently small
    nonnegative primal-dual gap. MILP optimality is never independently
    certified here; use solver bounds only as *reported* metadata.

    Violations are measured in original constraint units. For general models
    with heterogeneous units, compare each row using its own scaled tolerance.
    """
    if any(not isfinite(v) or v < 0 for v in (atol, rtol, integer_tolerance)):
        raise ValueError("Tolerances must be finite nonnegative numbers")
    if solution.model_name != model.name or solution.objective_unit != model.objective_unit:
        raise ValueError("Solution model name or objective unit does not match")
    if set(solution.variable_values) != set(model.variables):
        raise ValueError("Solution variable names must match model variables exactly")
    if not solution.integer_variables <= set(model.variables):
        raise ValueError("Unknown integer variable in solution")
    if any(not isfinite(float(v)) for v in (*model.objective, *model.b_ub)):
        raise ValueError("Non-finite objective or RHS coefficient in model")
    if any(not isfinite(float(v)) for row in model.a_ub for v in row):
        raise ValueError("Non-finite constraint coefficient in model")
    if any(not isfinite(float(v)) for pair in model.bounds for v in pair if v is not None):
        raise ValueError("Non-finite model bound")

    x = np.asarray([solution.variable_values[name] for name in model.variables], dtype=float)
    finite_candidate = bool(np.isfinite(x).all() and isfinite(solution.objective_value))
    if not finite_candidate:
        return VerificationReport(
            model.name, False, False, False, False, "none",
            float("inf"), float("inf"), float("inf"), float("inf"),
            None, None, None, solution.solver_objective_bound,
            solution.solver_relative_gap, None,
            ("Candidate has a non-finite variable or objective value",),
        )

    a, b, labels = _dual_system(model)
    violations = np.maximum(a @ x - b, 0.)
    inequality_violations = violations[:len(model.a_ub)]
    bound_violations = violations[len(model.a_ub):]
    # The dual system includes original constraints followed by finite bounds.
    row_magnitudes = np.abs(a) @ np.abs(x)
    row_tolerances = np.asarray([
        _tolerance(atol, rtol, b[i], row_magnitudes[i]) for i in range(len(b))
    ])
    primal_feasible = bool(np.all(violations <= row_tolerances))

    integers = [model.variables.index(name) for name in solution.integer_variables]
    integer_error = (
        float(np.max(np.abs(x[integers] - np.rint(x[integers]))))
        if integers else 0.
    )
    integrality_ok = integer_error <= integer_tolerance
    obj = np.asarray(model.objective, dtype=float)
    true_objective = float(obj @ x)
    objective_error = abs(solution.objective_value - true_objective)
    objective_ok = objective_error <= _tolerance(
        atol, rtol, solution.objective_value, true_objective
    )

    gap: float | None = None
    residual: float | None = None
    dual_multipliers: dict[str, float] | None = None
    independent = False
    evidence: Evidence = "none"
    bound_consistent: bool | None = None
    notes: list[str] = []

    if not (primal_feasible and integrality_ok and objective_ok):
        notes.append("Candidate failed at least one primal, integrality or objective check")
    elif solution.integer_variables:
        # HiGHS is trusted to generate this bound: checking its direction is
        # not an independent proof that the value bounds all feasible MILPs.
        bound = solution.solver_objective_bound
        if bound is not None and isfinite(bound):
            margin = _tolerance(atol, rtol, bound, true_objective)
            bound_consistent = bool(
                bound >= true_objective - margin if model.maximize
                else bound <= true_objective + margin
            )
            if bound_consistent:
                evidence = "milp_solver_bound"
            else:
                notes.append("Solver-reported MILP bound contradicts candidate objective")
        notes.append("MILP global optimality is not independently established")
    else:
        # Set c for the universal minimization representation.
        c = -obj if model.maximize else obj
        if not len(b):
            multipliers = np.array([], dtype=float)
            dual_found = bool(np.allclose(c, 0., atol=atol, rtol=rtol))
        else:
            # Minimize h@y, subject to G.T@y=-c, y>=0.
            # A verified y implies dual lower bound -h@y on min c@x.
            dual = linprog(
                c=b, A_eq=a.T, b_eq=-c,
                bounds=[(0., None)] * len(b), method="highs",
            )
            dual_found = bool(dual.success and dual.x is not None)
            multipliers = np.asarray(dual.x, dtype=float) if dual_found else None
        if dual_found and multipliers is not None and np.isfinite(multipliers).all():
            # Re-check the *candidate* y ourselves, independently of HiGHS flags.
            residual = float(np.max(np.abs(a.T @ multipliers + c)))
            gap = float(c @ x + b @ multipliers)
            dual_multipliers = dict(zip(labels, map(float, multipliers), strict=True))
            stationary_tolerance = _tolerance(
                atol, rtol, float(np.max(np.abs(c))),
                float(np.max(np.abs(a.T @ multipliers))) if len(b) else 0.,
            )
            # A dual gap can be slightly negative within floating-point tolerance.
            gap_tolerance = _tolerance(
                atol, rtol, float(c @ x), float(b @ multipliers)
            )
            independent = bool(
                np.all(multipliers >= -atol)
                and residual <= stationary_tolerance
                and -gap_tolerance <= gap <= gap_tolerance
            )
            if independent:
                evidence = "lp_primal_dual"
            else:
                notes.append("LP dual feasibility or duality-gap check failed")
        else:
            notes.append("Could not obtain a finite LP dual certificate")

    return VerificationReport(
        model_name=model.name,
        primal_feasible=primal_feasible,
        integrality_satisfied=integrality_ok,
        objective_consistent=objective_ok,
        independent_optimality_verified=independent,
        evidence=evidence,
        max_inequality_violation=float(np.max(inequality_violations))
        if len(inequality_violations) else 0.,
        max_bound_violation=float(np.max(bound_violations)) if len(bound_violations) else 0.,
        max_integrality_violation=integer_error,
        objective_absolute_error=objective_error,
        lp_primal_dual_gap=gap,
        lp_dual_stationarity_residual=residual,
        lp_dual_multipliers=dual_multipliers,
        milp_solver_objective_bound=solution.solver_objective_bound,
        milp_solver_relative_gap=solution.solver_relative_gap,
        milp_bound_consistent=bound_consistent,
        notes=tuple(notes),
    )
