"""Geometry and headless rendering tests for 2-variable linear programs."""

import subprocess
import sys

import numpy as np
import pytest

from modeling_lab.problems import boat_production_problem, diet_problem
from modeling_lab.visualization import (
    feasible_integer_points,
    feasible_polygon,
    plot_linear_program_2d,
)


def test_boat_feasible_polygon_vertices_and_inequalities() -> None:
    model = boat_production_problem()
    polygon = feasible_polygon(model, x_max=22, y_max=37)
    assert len(polygon) >= 3
    for expected in ((0, 0), (15, 0), (0, 20)):
        assert any(np.allclose(vertex, expected, atol=1e-8) for vertex in polygon)
    for row, bound in zip(model.a_ub, model.b_ub, strict=True):
        assert np.all(polygon @ np.asarray(row) <= bound + 1e-7)


def test_integer_lattice_points_are_feasible() -> None:
    model = boat_production_problem()
    points = feasible_integer_points(model, x_max=22, y_max=37)
    assert any(np.array_equal(point, (0, 20)) for point in points)
    assert any(np.array_equal(point, (15, 0)) for point in points)
    assert not any(np.array_equal(point, (15, 1)) for point in points)
    for row, bound in zip(model.a_ub, model.b_ub, strict=True):
        assert np.all(points @ np.asarray(row) <= bound + 1e-7)


def test_plot_is_valid_png_in_headless_mode(tmp_path) -> None:
    filename = tmp_path / "nested" / "boats.png"
    result = plot_linear_program_2d(
        boat_production_problem(), filename, show_integer_points=True
    )
    assert result == filename
    assert filename.read_bytes().startswith(b"\x89PNG\r\n\x1a\n")
    assert filename.stat().st_size > 10_000


def test_plot_does_not_support_three_variable_models(tmp_path) -> None:
    with pytest.raises(ValueError, match="two decision variables"):
        plot_linear_program_2d(diet_problem(), tmp_path / "diet.png")


def test_integer_enumeration_limit_is_explicit() -> None:
    with pytest.raises(ValueError, match="too large"):
        feasible_integer_points(boat_production_problem(), x_max=500, y_max=500)


def test_cli_generates_png_and_preserves_json(tmp_path) -> None:
    output = tmp_path / "boats.png"
    result = subprocess.run(
        [sys.executable, "-m", "modeling_lab", "boats", "--integer",
         "--plot", str(output), "--json"],
        capture_output=True, text=True, check=True,
    )
    import json
    data = json.loads(result.stdout)
    assert data["objective_value"] == pytest.approx(1600)
    assert data["plot_path"] == str(output)
    assert output.exists()
