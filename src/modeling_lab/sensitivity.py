"""One-at-a-time parametric sensitivity for session 01 linear models.

The same immutable LinearProgram is used for the baseline and every scenario.
Reported dual marginal is a *local* continuous-LP derivative in the units of
its user-facing parameter (not an integer-program shadow price).
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from math import isfinite
from pathlib import Path
from typing import Iterable, Literal

import numpy as np
from scipy.optimize import linprog

from .linear import LinearProgram, OptimizationError, Solution, solve


@dataclass(frozen=True)
class Parameter:
    key: str
    kind: Literal["rhs", "objective"]
    target: str
    unit: str
    # Physical RHS = model b_ub * rhs_scale.  Use -1 for original >= rows.
    rhs_scale: float = 1.0


@dataclass(frozen=True)
class Scenario:
    parameter_value: float
    status: Literal["optimal", "infeasible", "unbounded", "solver_error"]
    objective_value: float | None
    variable_values: dict[str, float] | None
    message: str | None = None


@dataclass(frozen=True)
class SensitivityReport:
    parameter: Parameter
    baseline_parameter_value: float
    baseline_solution: Solution
    scenarios: tuple[Scenario, ...]
    # None for integer models and for objective-coefficient perturbations.
    shadow_price: float | None
    integer_variables: frozenset[str]


def session01_parameters(problem: str) -> dict[str, Parameter]:
    """Explicit source-unit metadata for the two examples, not guessed signs."""
    if problem == "boats":
        definitions = (
            Parameter("aluminum_kg", "rhs", "aluminum_kg", "kg"),
            Parameter("machine_minutes", "rhs", "machine_minutes", "minutes"),
            Parameter("labor_hours", "rhs", "labor_hours", "hours"),
            Parameter("regular_profit", "objective", "x", "thousand toman/boat"),
            Parameter("competition_profit", "objective", "y", "thousand toman/boat"),
        )
    elif problem == "diet":
        definitions = (
            Parameter("vitamin_A_requirement", "rhs", "vitamin_A_min_12", "units/day", -1.0),
            Parameter("vitamin_B_requirement", "rhs", "vitamin_B_min_14", "units/day", -1.0),
            Parameter("cheese_price", "objective", "p", "toman/unit"),
            Parameter("milk_price", "objective", "s", "toman/unit"),
            Parameter("egg_price", "objective", "t", "toman/unit"),
        )
    else:
        raise ValueError(f"Unknown problem: {problem}")
    return {parameter.key: parameter for parameter in definitions}


def _index(model: LinearProgram, parameter: Parameter) -> int:
    names = model.constraint_names if parameter.kind == "rhs" else model.variables
    if parameter.target not in names:
        raise ValueError(f"Unknown {parameter.kind} target: {parameter.target}")
    if parameter.kind == "rhs" and parameter.rhs_scale not in (-1.0, 1.0):
        raise ValueError("RHS scale must be +1 or -1")
    return names.index(parameter.target)


def parameter_value(model: LinearProgram, parameter: Parameter) -> float:
    index = _index(model, parameter)
    if parameter.kind == "rhs":
        return float(model.b_ub[index] * parameter.rhs_scale)
    return float(model.objective[index])


def perturbed_model(model: LinearProgram, parameter: Parameter, value: float) -> LinearProgram:
    if not isfinite(value):
        raise ValueError("Sensitivity parameter must be finite")
    index = _index(model, parameter)
    if parameter.kind == "rhs":
        rhs = list(model.b_ub)
        rhs[index] = value / parameter.rhs_scale
        return replace(model, b_ub=tuple(rhs))
    objective = list(model.objective)
    objective[index] = value
    return replace(model, objective=tuple(objective))


def _continuous_shadow_price(model: LinearProgram, parameter: Parameter) -> float:
    """d(original optimum) / d(physical RHS), locally at the LP baseline.

    SciPy ineqlin.marginals differentiates *minimization* optimum with respect
    to internal <= RHS. Maximization requires negating; original >= constraints
    require the additional coordinate change RHS_internal = -RHS_physical.
    """
    index = _index(model, parameter)
    if parameter.kind != "rhs":
        raise ValueError("Shadow prices are available for RHS parameters only")
    objective = np.asarray(model.objective, dtype=float)
    internal_cost = -objective if model.maximize else objective
    result = linprog(
        c=internal_cost,
        A_ub=np.asarray(model.a_ub, dtype=float).reshape(-1, len(model.variables))
        if model.a_ub else None,
        b_ub=np.asarray(model.b_ub, dtype=float) if model.a_ub else None,
        bounds=model.bounds,
        method="highs",
    )
    if not result.success or result.x is None:
        raise OptimizationError(f"Dual marginal unavailable: {result.message}")
    marginal = float(result.ineqlin.marginals[index])
    return (-1.0 if model.maximize else 1.0) * marginal / parameter.rhs_scale


def sweep_parameter(
    model: LinearProgram,
    parameter: Parameter,
    values: Iterable[float],
    *,
    integer_variables: Iterable[str] = (),
) -> SensitivityReport:
    """Re-optimize independently for each value; record nonoptimal outcomes.

    The baseline input model is never mutated. No LP shadow-price statement is
    made for a MIP, where finite differences need not equal a marginal value.
    """
    values = tuple(float(v) for v in values)
    if not values or len(values) > 200:
        raise ValueError("Provide between 1 and 200 sensitivity values")
    if any(not isfinite(v) for v in values):
        raise ValueError("Sensitivity values must be finite")
    _index(model, parameter)  # Validate target before invoking any solver.
    integer_set = frozenset(integer_variables)
    baseline_solution = solve(model, integer_variables=integer_set)
    scenarios: list[Scenario] = []
    for value in values:
        scenario_model = perturbed_model(model, parameter, value)
        try:
            solution = solve(scenario_model, integer_variables=integer_set)
        except OptimizationError as exc:
            status: Literal["optimal", "infeasible", "unbounded", "solver_error"] = (
                "infeasible" if exc.status == 2 else
                "unbounded" if exc.status == 3 else "solver_error"
            )
            scenarios.append(Scenario(value, status, None, None, str(exc)))
        else:
            scenarios.append(Scenario(
                value, "optimal", solution.objective_value,
                solution.variable_values.copy(),
            ))
    shadow_price = (
        _continuous_shadow_price(model, parameter)
        if not integer_set and parameter.kind == "rhs" else None
    )
    return SensitivityReport(
        parameter=parameter,
        baseline_parameter_value=parameter_value(model, parameter),
        baseline_solution=baseline_solution,
        scenarios=tuple(scenarios),
        shadow_price=shadow_price,
        integer_variables=integer_set,
    )


def save_sensitivity_plot(report: SensitivityReport, path: str | Path) -> Path:
    """Save objective-vs-parameter plot, with gaps for nonoptimal scenarios."""
    from matplotlib.backends.backend_agg import FigureCanvasAgg
    from matplotlib.figure import Figure

    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    # Sorting is for line continuity only; report records user-supplied order.
    ordered = sorted(report.scenarios, key=lambda row: row.parameter_value)
    x = [scenario.parameter_value for scenario in ordered]
    y = [scenario.objective_value if scenario.status == "optimal" else float("nan")
         for scenario in ordered]
    fig = Figure(figsize=(8, 5), constrained_layout=True)
    FigureCanvasAgg(fig)
    ax = fig.subplots()
    label = "MILP (re-solved)" if report.integer_variables else "LP (re-solved)"
    if report.integer_variables:
        # Connecting MIP samples would falsely suggest a continuous response.
        ax.scatter(x, y, label=label)
    else:
        ax.plot(x, y, marker="o", linestyle="--", label=f"{label}; samples only")
    ax.scatter([report.baseline_parameter_value],
               [report.baseline_solution.objective_value], marker="*", s=110,
               label="Baseline")
    ax.axvline(report.baseline_parameter_value, linestyle="--", linewidth=1,
               alpha=.55)
    ax.set_title(f"Sensitivity: {report.parameter.key}")
    ax.set_xlabel(f"{report.parameter.key} ({report.parameter.unit})")
    ax.set_ylabel(f"Optimal objective ({report.baseline_solution.objective_unit})")
    ax.grid(alpha=.25)
    ax.legend()
    fig.savefig(destination, dpi=160)
    return destination
