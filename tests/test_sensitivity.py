"""Parametric re-solves, dual sign conventions, failure modes and CLI tests."""

import json
import subprocess
import sys

import pytest

from modeling_lab.problems import boat_production_problem, diet_problem
from modeling_lab.sensitivity import (
    parameter_value, perturbed_model, save_sensitivity_plot,
    session01_parameters, sweep_parameter,
)


def _parameter(problem: str, key: str):
    return session01_parameters(problem)[key]


def test_boat_machine_lp_marginal_and_objectives():
    model = boat_production_problem()
    report = sweep_parameter(model, _parameter("boats", "machine_minutes"),
                             [240, 300, 360, 400])
    assert report.baseline_parameter_value == 300
    assert report.shadow_price == pytest.approx(80 / 15)
    assert [point.objective_value for point in report.scenarios] == pytest.approx(
        [1280, 1600, 1920, 80 * 400 / 15]
    )
    assert report.scenarios[-1].variable_values["y"] == pytest.approx(400 / 15)
    assert model.b_ub == (1000, 300, 200)  # Baseline must remain immutable.


def test_nonbinding_boat_resources_have_zero_shadow_price():
    model = boat_production_problem()
    for parameter in ("aluminum_kg", "labor_hours"):
        report = sweep_parameter(model, _parameter("boats", parameter),
                                 [parameter_value(model, _parameter("boats", parameter))])
        assert report.shadow_price == pytest.approx(0.0, abs=1e-9)


def test_diet_requirement_uses_original_positive_units():
    model = diet_problem()
    a = _parameter("diet", "vitamin_A_requirement")
    b = _parameter("diet", "vitamin_B_requirement")
    assert parameter_value(model, a) == 12
    assert perturbed_model(model, a, 15).b_ub[0] == -15
    report_a = sweep_parameter(model, a, [12, 12.01])
    report_b = sweep_parameter(model, b, [14, 14.01])
    assert report_a.shadow_price == pytest.approx(8.75)
    assert report_b.shadow_price == pytest.approx(7.5)
    assert report_a.scenarios[1].objective_value - 210 == pytest.approx(.0875)
    assert report_b.scenarios[1].objective_value - 210 == pytest.approx(.075)


def test_integer_model_is_reoptimized_but_has_no_shadow_price():
    model = boat_production_problem()
    report = sweep_parameter(model, _parameter("boats", "machine_minutes"),
                             [300, 310, 315, 400], integer_variables=("x", "y"))
    assert report.shadow_price is None
    assert [row.objective_value for row in report.scenarios] == [1600, 1600, 1680, 2080]
    assert report.scenarios[1].variable_values["y"] == 20


def test_objective_coefficient_switches_optimal_product():
    model = boat_production_problem()
    report = sweep_parameter(model, _parameter("boats", "competition_profit"),
                             [20, 80])
    assert report.shadow_price is None
    assert report.scenarios[0].variable_values == pytest.approx({"x": 15, "y": 0})
    assert report.scenarios[0].objective_value == pytest.approx(750)
    assert report.scenarios[1].variable_values == pytest.approx({"x": 0, "y": 20})
    assert report.scenarios[1].objective_value == pytest.approx(1600)


def test_infeasible_scenario_is_recorded_without_stopping_other_cases():
    model = boat_production_problem()
    report = sweep_parameter(model, _parameter("boats", "machine_minutes"),
                             [-1, 300])
    assert report.scenarios[0].status == "infeasible"
    assert report.scenarios[0].objective_value is None
    assert report.scenarios[1].status == "optimal"
    assert report.scenarios[1].objective_value == pytest.approx(1600)


@pytest.mark.parametrize("values", [[], [float("nan")], [float("inf")], list(range(201))])
def test_rejects_invalid_or_excessively_large_sweeps(values):
    with pytest.raises(ValueError):
        sweep_parameter(boat_production_problem(),
                        _parameter("boats", "machine_minutes"), values)


def test_invalid_parameter_target_is_rejected():
    from modeling_lab.sensitivity import Parameter
    with pytest.raises(ValueError, match="Unknown rhs target"):
        sweep_parameter(boat_production_problem(),
                        Parameter("bad", "rhs", "unknown", "unit"), [1])


def test_plot_png_and_baseline(tmp_path):
    report = sweep_parameter(boat_production_problem(),
                             _parameter("boats", "machine_minutes"), [240, 300, 360])
    path = tmp_path / "nested" / "sensitivity.png"
    assert save_sensitivity_plot(report, path) == path
    assert path.read_bytes().startswith(b"\x89PNG\r\n\x1a\n")
    assert path.stat().st_size > 5000


def test_integer_plot_png(tmp_path):
    report = sweep_parameter(boat_production_problem(),
                             _parameter("boats", "machine_minutes"),
                             [301, 310, 315], integer_variables=["x", "y"])
    path = tmp_path / "integer.png"
    save_sensitivity_plot(report, path)
    assert path.read_bytes().startswith(b"\x89PNG")


def test_cli_json_includes_sensitivity_and_png(tmp_path):
    image = tmp_path / "sweep.png"
    process = subprocess.run([
        sys.executable, "-m", "modeling_lab", "boats",
        "--sensitivity", "machine_minutes", "--values", "300", "315",
        "--sensitivity-plot", str(image), "--json",
    ], capture_output=True, text=True, check=True)
    payload = json.loads(process.stdout)
    assert payload["sensitivity"]["shadow_price"] == pytest.approx(80 / 15)
    assert payload["sensitivity"]["scenarios"][1]["objective_value"] == 1680
    assert payload["sensitivity"]["plot_path"] == str(image)
    assert image.exists()


def test_cli_list_parameters_and_missing_values():
    listed = subprocess.run([
        sys.executable, "-m", "modeling_lab", "diet", "--list-parameters"
    ], capture_output=True, text=True, check=True)
    assert "vitamin_A_requirement" in listed.stdout
    failed = subprocess.run([
        sys.executable, "-m", "modeling_lab", "diet",
        "--sensitivity", "vitamin_A_requirement",
    ], capture_output=True, text=True)
    assert failed.returncode != 0
    assert "--values" in failed.stderr
