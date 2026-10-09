"""Session 02 mathematical regression tests with corrected 60,000 labor hours."""

import math
import subprocess
import sys
from pathlib import Path

import pytest

from modeling_lab.linear import solve
from modeling_lab.session02 import (
    TV_LABOR_HOURS,
    television_problem,
    transportation_demo_problem,
    transportation_problem,
)
from modeling_lab.verification import verify_solution


def test_tv_formulation_uses_confirmed_capacity():
    model = television_problem()
    assert model.objective == (60.0, 30.0)
    assert model.a_ub == ((20.0, 15.0),)
    assert model.b_ub == (TV_LABOR_HOURS,) == (60000.0,)
    assert model.bounds == ((0.0, 2000.0), (0.0, 4000.0))


def test_tv_60000_continuous_solution_and_verification():
    model = television_problem()
    sol = solve(model)
    assert sol.variable_values["x1"] == pytest.approx(2000)
    assert sol.variable_values["x2"] == pytest.approx(4000 / 3)
    assert sol.objective_value == pytest.approx(160000)
    report = verify_solution(model, sol)
    assert report.candidate_valid and report.independent_optimality_verified


def test_tv_explicit_65000_what_if_override():
    model = television_problem(labor_hours=65000)
    assert model.b_ub == (65000.0,)
    sol = solve(model)
    assert sol.variable_values == pytest.approx({"x1": 2000, "x2": 5000 / 3})
    assert sol.objective_value == pytest.approx(170000)


def test_tv_60000_integer_solution():
    model = television_problem()
    sol = solve(model, integer_variables=model.variables)
    assert sol.variable_values == pytest.approx({"x1": 2000, "x2": 1333})
    assert sol.objective_value == pytest.approx(159990)
    assert verify_solution(model, sol).candidate_valid


def test_tv_invalid_labor_hours_rejected():
    for hours in (-1.0, math.nan, math.inf):
        with pytest.raises(ValueError, match="labor_hours"):
            television_problem(labor_hours=hours)


def test_transport_dimensions_supply_and_exact_demand():
    model = transportation_demo_problem()
    assert len(model.variables) == 4
    assert len(model.a_ub) == 6  # two capacities; two pairs of demand constraints
    assert model.variables == ("x1_1", "x1_2", "x2_1", "x2_2")
    assert model.objective == (2.0, 5.0, 4.0, 1.0)
    sol = solve(model)
    x = sol.variable_values
    assert x == pytest.approx({"x1_1": 10, "x1_2": 0, "x2_1": 2, "x2_2": 18})
    assert x["x1_1"] + x["x2_1"] == pytest.approx(12)
    assert x["x1_2"] + x["x2_2"] == pytest.approx(18)
    assert sol.objective_value == pytest.approx(46)
    report = verify_solution(model, sol)
    assert report.candidate_valid and report.independent_optimality_verified


def test_transport_arbitrary_3_by_2_instance():
    model = transportation_problem(
        costs=((1, 2), (2, 3), (4, 5)),
        supplies=(5, 5, 10),
        demands=(6, 7),
    )
    sol = solve(model)
    x = sol.variable_values
    assert x["x1_1"] + x["x2_1"] + x["x3_1"] == pytest.approx(6)
    assert x["x1_2"] + x["x2_2"] + x["x3_2"] == pytest.approx(7)
    assert all(value >= -1e-8 for value in x.values())


@pytest.mark.parametrize("costs,supply,demand", [
    (((1, 2),), (5,), (3, 3)),
    (((1, 2),), (7,), (3,)),
    (((1, 2),), (2,), (4, 4)),
])
def test_transport_bad_data_rejected(costs, supply, demand):
    with pytest.raises(ValueError):
        transportation_problem(costs, supply, demand)


def test_transport_cannot_have_negative_supply_or_nonfinite_cost():
    with pytest.raises(ValueError, match="nonnegative"):
        transportation_problem(((2.0,),), (-1.0,), (0.0,))
    with pytest.raises(ValueError, match="finite"):
        transportation_problem(((math.inf,),), (1.0,), (1.0,))


def test_cli_television_capacity_correction_and_transport_label():
    root = Path(__file__).resolve().parents[1]
    commands = [
        (["televisions", "--verify"], "student-confirmed source correction"),
        (["transport-demo", "--verify"], "Illustrative numbers only"),
    ]
    for args, fragment in commands:
        result = subprocess.run(
            [sys.executable, "-m", "modeling_lab", *args],
            cwd=root, capture_output=True, text=True, check=True,
        )
        assert fragment in result.stdout
        assert "Independently verified global optimality: True" in result.stdout


def test_cli_rejects_session01_sensitivity_flag_on_tv():
    root = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        [sys.executable, "-m", "modeling_lab", "televisions", "--list-parameters"],
        cwd=root, capture_output=True, text=True,
    )
    assert result.returncode != 0
    assert "only for session 01" in result.stderr
