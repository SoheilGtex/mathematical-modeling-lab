"""Regression tests: 4-page Session 03 note, both worked continuous LPs."""
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys

import pytest

from modeling_lab.linear import solve
from modeling_lab.session03 import (
    TRANSPORT_COSTS, TRANSPORT_DEMAND, TRANSPORT_SUPPLY, MONTHLY_DEMAND,
    lecture_transportation_problem, production_inventory_problem,
)
from modeling_lab.verification import verify_solution


def test_transport_source_table_is_not_invented_session02_demo():
    assert TRANSPORT_COSTS == ((80, 5, 12, 15), (1, 9, 4, 5), (12, 8, 6, 4))
    assert TRANSPORT_SUPPLY == (150, 300, 200)
    assert TRANSPORT_DEMAND == (150, 200, 100, 200)
    assert sum(TRANSPORT_SUPPLY) == sum(TRANSPORT_DEMAND) == 650
    model = lecture_transportation_problem()
    assert len(model.variables) == 12
    assert len(model.a_ub) == 3 + 2 * 4
    assert model.objective[0] == 80
    assert model.objective_unit == "toman"
    assert not model.maximize


def test_transport_optimal_plan_saturates_every_origin_and_destination():
    model = lecture_transportation_problem()
    solution = solve(model)
    expected = {
        "x1_2": 150, "x2_1": 150, "x2_2": 50, "x2_3": 100,
        "x3_4": 200,
    }
    for name, value in solution.variable_values.items():
        assert value == pytest.approx(expected.get(name, 0), abs=1e-7)
    for i, supply in enumerate(TRANSPORT_SUPPLY, 1):
        assert sum(solution.variable_values[f"x{i}_{j}"] for j in range(1, 5)) == pytest.approx(supply)
    for j, demand in enumerate(TRANSPORT_DEMAND, 1):
        assert sum(solution.variable_values[f"x{i}_{j}"] for i in range(1, 4)) == pytest.approx(demand)
    assert solution.objective_value == pytest.approx(2550)
    evidence = verify_solution(model, solution)
    assert evidence.candidate_valid and evidence.independent_optimality_verified


def test_transport_handwritten_potential_certificate():
    u, v = (0, 4, 3), (-3, 5, 0, 1)
    assert all(u[i] + v[j] <= TRANSPORT_COSTS[i][j]
               for i in range(3) for j in range(4))
    bound = sum(u[i] * TRANSPORT_SUPPLY[i] for i in range(3)) + sum(
        v[j] * TRANSPORT_DEMAND[j] for j in range(4))
    assert bound == 2550


def test_production_source_data_and_boundaries():
    assert MONTHLY_DEMAND == (1200, 2100, 2400, 3000, 4000)
    model = production_inventory_problem()
    assert len(model.variables) == 14
    assert model.variables[:5] == ("x1", "x2", "x3", "x4", "x5")
    assert model.variables[5:10] == ("y1", "y2", "y3", "y4", "y5")
    assert model.variables[10:] == ("s1", "s2", "s3", "s4")
    assert "s5" not in model.variables
    assert len(model.a_ub) == 10  # five exact balances, each as two inequalities
    assert model.bounds[0] == (0.0, 2000.0)
    assert model.bounds[5] == (0.0, 600.0)
    assert model.bounds[-1] == (0.0, None)


def test_production_solution_inventory_trajectory_and_optimality():
    model = production_inventory_problem()
    solution = solve(model)
    assert solution.objective_value == pytest.approx(152300)
    assert all(solution.variable_values[f"x{i}"] == pytest.approx(2000) for i in range(1, 6))
    assert [solution.variable_values[f"y{i}"] for i in range(1, 6)] == pytest.approx(
        [300, 600, 600, 600, 600])
    stock = [0] + [solution.variable_values[f"s{i}"] for i in range(1, 5)] + [0]
    assert stock == pytest.approx([0, 1100, 1600, 1800, 1400, 0])
    for i, demand in enumerate(MONTHLY_DEMAND, 1):
        assert solution.variable_values[f"x{i}"] + solution.variable_values[f"y{i}"] + stock[i-1] - stock[i] == pytest.approx(demand)
    verified = verify_solution(model, solution)
    assert verified.candidate_valid and verified.independent_optimality_verified
    assert verified.lp_primal_dual_gap == pytest.approx(0, abs=1e-7)


def test_production_exact_hand_lower_bound_certificate():
    p = (15, 17, 19, 21, 23)
    dual_bound = sum(pi * di for pi, di in zip(p, MONTHLY_DEMAND, strict=True))
    dual_bound += sum((10-pi)*2000 for pi in p)
    dual_bound += sum((15-pi)*600 for pi in p[1:])
    assert dual_bound == 152300
    assert dual_bound == 10 * 10000 + 15 * 2700 + 2 * (1100+1600+1800+1400)


@pytest.mark.parametrize("bad", [(), (1,2,3,4), (1,2,3,4,5,6), (1,2,3,-4,5), (1,2,3,float('nan'),5), (1,2,3,float('inf'),5)])
def test_production_bad_demands_rejected(bad):
    with pytest.raises(ValueError, match="demands"):
        production_inventory_problem(demands=bad)


@pytest.mark.parametrize("command,expected_value", [("transport-lecture", 2550), ("production-plan", 152300)])
def test_session03_cli_json_and_lp_verification(command, expected_value):
    root = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        [sys.executable, "-m", "modeling_lab", command, "--verify", "--json"],
        cwd=root, text=True, capture_output=True, check=True,
    )
    data = json.loads(result.stdout)
    assert data["objective_value"] == pytest.approx(expected_value)
    assert data["verification"]["candidate_valid"]
    assert data["verification"]["independent_optimality_verified"]


def test_site_and_cumulative_exam_review_refer_to_session03():
    root = Path(__file__).resolve().parents[1]
    for lang in ("en", "fa"):
        exam = (root / f"site_docs/exam.{lang}.md").read_text("utf-8")
        assert "session-03/transportation.md" in exam
        assert "session-03/production.md" in exam
    one_file = (root / "EXAM_NIGHT.md").read_text("utf-8")
    assert "## Session 03" in one_file
    assert "sessions/session_03/" in one_file
