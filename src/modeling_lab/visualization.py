"""Headless 2D linear-program plots generated from the model coefficients.

Scope: two nonnegative decision variables, linear <= inequalities and optional
finite upper bounds. The feasible region is clipped to the displayed viewport;
this is a visualization, not a substitute for solving or proving boundedness.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure

from .linear import LinearProgram, solve


_DEF_TOL = 1e-9


def _validate_plot_model(model: LinearProgram) -> None:
    if len(model.variables) != 2:
        raise ValueError("2D visualization requires exactly two decision variables")
    for lo, hi in model.bounds:
        if lo is None or not np.isclose(lo, 0.0, atol=_DEF_TOL):
            raise ValueError("2D visualization currently requires zero lower bounds")
        if hi is not None and (not np.isfinite(hi) or hi < 0):
            raise ValueError("Upper bounds must be finite and nonnegative")
    values = [*model.objective, *model.b_ub]
    values.extend(v for row in model.a_ub for v in row)
    if not np.all(np.isfinite(np.asarray(values, dtype=float))):
        raise ValueError("2D visualization requires finite objective and constraint coefficients")


def _clip_to_half_plane(polygon: np.ndarray, a: np.ndarray, b: float) -> np.ndarray:
    """Sutherland–Hodgman intersection with a @ point <= b."""
    if len(polygon) == 0:
        return polygon
    result: list[np.ndarray] = []
    previous = polygon[-1]
    prev_distance = float(a @ previous - b)
    for current in polygon:
        current_distance = float(a @ current - b)
        prev_inside = prev_distance <= _DEF_TOL
        cur_inside = current_distance <= _DEF_TOL
        if prev_inside != cur_inside:
            denominator = prev_distance - current_distance
            if abs(denominator) > 1e-15:
                fraction = np.clip(prev_distance / denominator, 0.0, 1.0)
                result.append(previous + fraction * (current - previous))
        if cur_inside:
            result.append(current)
        previous, prev_distance = current, current_distance
    return np.asarray(result, dtype=float).reshape(-1, 2)


def feasible_polygon(
    model: LinearProgram, *, x_max: float, y_max: float
) -> np.ndarray:
    """Feasible polygon inside [0, x_max] x [0, y_max], counterclockwise.

    A blank (0, 2) array indicates no feasible *area* or no feasible points in
    the viewport. A degenerate feasible segment can have repeated vertices.
    """
    _validate_plot_model(model)
    if not np.isfinite(x_max) or not np.isfinite(y_max) or x_max <= 0 or y_max <= 0:
        raise ValueError("Plot limits must be positive finite numbers")

    polygon = np.asarray(
        [[0.0, 0.0], [x_max, 0.0], [x_max, y_max], [0.0, y_max]],
        dtype=float,
    )
    for row, bound in zip(model.a_ub, model.b_ub, strict=True):
        polygon = _clip_to_half_plane(polygon, np.asarray(row, dtype=float), bound)
    for axis, (_, upper) in enumerate(model.bounds):
        if upper is not None:
            normal = np.eye(2, dtype=float)[axis]
            polygon = _clip_to_half_plane(polygon, normal, upper)
    return polygon


def feasible_integer_points(
    model: LinearProgram, *, x_max: float, y_max: float, max_candidates: int = 50_000
) -> np.ndarray:
    """Enumerate integer lattice points feasible for a nonnegative 2D LP.

    Raises rather than silently sampling or pretending to show all points.
    """
    _validate_plot_model(model)
    if not np.isfinite(x_max) or not np.isfinite(y_max) or x_max <= 0 or y_max <= 0:
        raise ValueError("Plot limits must be positive finite numbers")
    nx, ny = int(np.floor(x_max)) + 1, int(np.floor(y_max)) + 1
    if nx * ny > max_candidates:
        raise ValueError("Integer grid too large; set tighter plot limits")
    xx, yy = np.meshgrid(np.arange(nx), np.arange(ny), indexing="xy")
    points = np.column_stack([xx.ravel(), yy.ravel()]).astype(float)
    for row, bound in zip(model.a_ub, model.b_ub, strict=True):
        a = np.asarray(row, dtype=float)
        points = points[(points @ a) <= bound + _DEF_TOL]
    for axis, (_, upper) in enumerate(model.bounds):
        if upper is not None:
            points = points[points[:, axis] <= upper + _DEF_TOL]
    return points


def _auto_limits(model: LinearProgram, point: np.ndarray) -> tuple[float, float]:
    """Include positive constraint intercepts and the continuous solution."""
    ends: list[float] = []
    for axis in range(2):
        intercepts = [
            bound / row[axis]
            for row, bound in zip(model.a_ub, model.b_ub, strict=True)
            if row[axis] > 0 and bound > 0
        ]
        # A far-away redundant constraint should not shrink the feasible
        # polygon into a corner of the image. The median of axis intercepts
        # gives a practical default; callers may override both limits.
        typical_intercept = float(np.median(intercepts)) if intercepts else 0.0
        candidates = [1.0, 1.25 * max(0.0, float(point[axis])),
                      1.1 * typical_intercept]
        if model.bounds[axis][1] is not None:
            candidates.append(1.1 * model.bounds[axis][1])
        ends.append(max(candidates))
    return ends[0], ends[1]


def plot_linear_program_2d(
    model: LinearProgram,
    output_path: str | Path,
    *,
    show_integer_points: bool = False,
    x_max: float | None = None,
    y_max: float | None = None,
) -> Path:
    """Render constraint lines, feasible set, objective contours, and optima.

    The source LP stays continuous. `show_integer_points=True` additionally
    solves the all-integer extension and draws all feasible lattice points.
    This function deliberately uses the Agg canvas for headless CI execution.
    """
    _validate_plot_model(model)
    continuous = solve(model)
    optimum = np.asarray([continuous.variable_values[name] for name in model.variables])
    default_x, default_y = _auto_limits(model, optimum)
    x_limit = default_x if x_max is None else float(x_max)
    y_limit = default_y if y_max is None else float(y_max)
    if not np.isfinite(x_limit) or not np.isfinite(y_limit) or min(x_limit, y_limit) <= 0:
        raise ValueError("Plot limits must be positive finite numbers")
    if np.any(optimum > np.array([x_limit, y_limit]) + _DEF_TOL):
        raise ValueError("Plot limits would hide the continuous optimum")

    polygon = feasible_polygon(model, x_max=x_limit, y_max=y_limit)
    if len(polygon) == 0:
        raise ValueError("No feasible points in plotting viewport")

    fig = Figure(figsize=(9.5, 7), layout="constrained")
    FigureCanvasAgg(fig)
    ax = fig.subplots()
    ax.set_xlim(0.0, x_limit)
    ax.set_ylim(0.0, y_limit)
    ax.grid(True, alpha=0.20)
    ax.set_axisbelow(True)
    ax.set_xlabel(model.variables[0])
    ax.set_ylabel(model.variables[1])
    ax.set_title(f"{model.name} — feasible set and optimum")

    if len(polygon) >= 3:
        ax.fill(polygon[:, 0], polygon[:, 1], alpha=0.20, label="Feasible region")

    line_x = np.linspace(0.0, x_limit, 450)
    for row, bound, name in zip(
        model.a_ub, model.b_ub, model.constraint_names, strict=True
    ):
        a0, a1 = row
        if abs(a1) > _DEF_TOL:
            line_y = (bound - a0 * line_x) / a1
            ax.plot(line_x, line_y, linewidth=1.5, label=f"Constraint: {name}")
        elif abs(a0) > _DEF_TOL:
            ax.axvline(bound / a0, linewidth=1.5, label=f"Constraint: {name}")
        # A zero-coefficient constraint is either redundant or infeasible,
        # but does not define a line in the x/y plane.

    coefficients = np.asarray(model.objective, dtype=float)
    if np.linalg.norm(coefficients) > _DEF_TOL and len(polygon) > 0:
        values = polygon @ coefficients
        levels = np.linspace(float(np.min(values)), float(np.max(values)), 5)
        levels = np.unique(np.r_[levels, continuous.objective_value])
        if len(levels) >= 2 and levels[-1] - levels[0] > _DEF_TOL:
            gx, gy = np.meshgrid(
                np.linspace(0.0, x_limit, 180),
                np.linspace(0.0, y_limit, 180),
            )
            z = coefficients[0] * gx + coefficients[1] * gy
            contours = ax.contour(gx, gy, z, levels=levels, linewidths=0.8,
                                  linestyles="dashed", alpha=0.55)
            ax.clabel(contours, inline=True, fmt="%g", fontsize=8)

    if show_integer_points:
        points = feasible_integer_points(model, x_max=x_limit, y_max=y_limit)
        if len(points):
            ax.scatter(points[:, 0], points[:, 1], s=13, alpha=0.38,
                       marker="o", label="Feasible integer points")
        integer_solution = solve(model, integer_variables=model.variables)
        integer_point = np.asarray(
            [integer_solution.variable_values[name] for name in model.variables]
        )
        if np.any(integer_point > np.array([x_limit, y_limit]) + _DEF_TOL):
            raise ValueError("Plot limits would hide the integer optimum")
    else:
        integer_point = None

    ax.scatter([optimum[0]], [optimum[1]], marker="*", s=330,
               facecolor="gold", edgecolor="black", linewidth=0.8,
               zorder=6, label=f"LP optimum: z={continuous.objective_value:g}")
    if integer_point is not None:
        ax.scatter([integer_point[0]], [integer_point[1]], marker="x", s=105,
                   color="black", linewidth=2, zorder=7,
                   label=f"Integer optimum: z={integer_solution.objective_value:g}")
        if np.allclose(optimum, integer_point, atol=1e-7):
            ax.annotate("LP = integer optimum", xy=optimum,
                        xytext=(13, 14), textcoords="offset points", fontsize=9)

    ax.legend(loc="upper right", fontsize=8)
    target = Path(output_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(target, dpi=170)
    return target
