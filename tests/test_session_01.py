"""Reproducibility checks for class examples and their modeling assumptions."""

import pytest

from modeling_lab import LinearProgram, OptimizationError, solve
from modeling_lab.problems import boat_production_problem, diet_problem


def test_diet_solution_and_vitamins() -> None:
    result = solve(diet_problem())
    p, s, t = (result.variable_values[name] for name in ("p", "s", "t"))
    assert result.objective_value == pytest.approx(210.0)
    assert p == pytest.approx(0.0)
    assert s == pytest.approx(1.0)
    assert t == pytest.approx(4.0)
    assert p + 4 * s + 2 * t >= 12 - 1e-7
    assert p + 2 * s + 3 * t >= 14 - 1e-7


def test_diet_whole_eggs_extension() -> None:
    result = solve(diet_problem(), integer_variables=["t"])
    assert result.objective_value == pytest.approx(210.0)
    assert result.variable_values["t"] == pytest.approx(4.0)


def test_boat_solution_and_constraints() -> None:
    result = solve(boat_production_problem())
    x, y = result.variable_values["x"], result.variable_values["y"]
    assert result.objective_value == pytest.approx(1600.0)
    assert x == pytest.approx(0)
    assert y == pytest.approx(20)
    assert 50 * x + 30 * y <= 1000 + 1e-7
    assert 20 * x + 15 * y <= 300 + 1e-7
    assert 3 * x + 5 * y <= 200 + 1e-7


def test_boat_integer_extension() -> None:
    result = solve(boat_production_problem(), integer_variables=["x", "y"])
    assert result.variable_values["x"] == pytest.approx(0.0)
    assert result.variable_values["y"] == pytest.approx(20.0)
    assert result.objective_value == pytest.approx(1600.0)


def test_invalid_integer_variable_is_rejected() -> None:
    with pytest.raises(ValueError, match="Unknown integer"):
        solve(diet_problem(), integer_variables=["unknown"])


def test_infeasible_problem_is_reported() -> None:
    model = LinearProgram(
        name="impossible", variables=("x",), objective=(1.0,), maximize=False,
        a_ub=((1.0,),), b_ub=(-1.0,), constraint_names=("x_le_negative_1",),
        bounds=((0.0, None),), objective_unit="units",
    )
    with pytest.raises(OptimizationError, match="solver status"):
        solve(model)
