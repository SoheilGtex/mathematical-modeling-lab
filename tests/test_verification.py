"""Independent primal computations, LP dual certificates and MILP scope."""

from dataclasses import replace
import json
import subprocess
import sys

import pytest

from modeling_lab.linear import LinearProgram, solve
from modeling_lab.problems import boat_production_problem, diet_problem
from modeling_lab.verification import verify_solution


@pytest.mark.parametrize("factory", [diet_problem, boat_production_problem])
def test_lp_primal_dual_certificate(factory):
    model = factory()
    report = verify_solution(model, solve(model))
    assert report.candidate_valid
    assert report.independent_optimality_verified
    assert report.evidence == "lp_primal_dual"
    assert report.lp_primal_dual_gap == pytest.approx(0., abs=1e-7)
    assert report.lp_dual_stationarity_residual == pytest.approx(0., abs=1e-7)
    assert report.max_inequality_violation == pytest.approx(0.)
    assert report.max_bound_violation == pytest.approx(0.)
    assert report.lp_dual_multipliers is not None


def test_diet_dual_is_valid_even_with_negative_transformed_rhs():
    model = diet_problem()
    report = verify_solution(model, solve(model))
    duals = report.lp_dual_multipliers
    assert duals["constraint:vitamin_A_min_12"] == pytest.approx(8.75)
    assert duals["constraint:vitamin_B_min_14"] == pytest.approx(7.5)


def test_modified_constraint_slacks_are_not_trusted():
    model = boat_production_problem()
    result = solve(model)
    # Solution claims zero slacks even for nonbinding resources; recompute.
    tampered = replace(result, constraint_slacks={key: 0. for key in result.constraint_slacks})
    report = verify_solution(model, tampered)
    assert report.candidate_valid
    assert report.independent_optimality_verified


def test_infeasible_inequality_rejected_independently():
    model = boat_production_problem()
    baseline = solve(model)
    forged = replace(baseline, variable_values={"x": 0., "y": 21.},
                     objective_value=1680.)
    report = verify_solution(model, forged)
    assert not report.primal_feasible
    assert report.max_inequality_violation == pytest.approx(15.)
    assert not report.independent_optimality_verified


def test_bound_violation_rejected():
    model = boat_production_problem()
    baseline = solve(model)
    forged = replace(baseline, variable_values={"x": -1., "y": 20.},
                     objective_value=1550.)
    report = verify_solution(model, forged)
    assert not report.primal_feasible
    assert report.max_bound_violation == pytest.approx(1.)


def test_objective_mismatch_rejected():
    model = diet_problem()
    forged = replace(solve(model), objective_value=42.)
    report = verify_solution(model, forged)
    assert report.primal_feasible
    assert not report.objective_consistent
    assert report.objective_absolute_error == pytest.approx(168.)
    assert not report.independent_optimality_verified


def test_lp_feasible_but_suboptimal_cannot_get_certificate():
    model = boat_production_problem()
    baseline = solve(model)
    candidate = replace(baseline, variable_values={"x": 0., "y": 0.},
                        objective_value=0.)
    report = verify_solution(model, candidate)
    assert report.candidate_valid
    assert report.lp_primal_dual_gap > 1000
    assert not report.independent_optimality_verified
    assert report.evidence == "none"


def test_integrality_violation_detected():
    model = boat_production_problem()
    baseline = solve(model, integer_variables=("x", "y"))
    candidate = replace(baseline, variable_values={"x": 0., "y": 19.5},
                        objective_value=1560.)
    report = verify_solution(model, candidate)
    assert report.primal_feasible
    assert not report.integrality_satisfied
    assert report.max_integrality_violation == pytest.approx(.5)
    assert not report.candidate_valid


def test_milp_reports_solver_bound_but_never_independent_certification():
    model = boat_production_problem()
    result = solve(model, integer_variables=("x", "y"))
    report = verify_solution(model, result)
    assert report.candidate_valid
    assert report.evidence == "milp_solver_bound"
    assert report.milp_solver_objective_bound == pytest.approx(1600)
    assert report.milp_solver_relative_gap == pytest.approx(0)
    assert report.milp_bound_consistent is True
    assert not report.independent_optimality_verified
    assert "not independently" in " ".join(report.notes)


def test_solver_milp_inconsistent_bound_is_flagged():
    model = boat_production_problem()
    result = solve(model, integer_variables=("x", "y"))
    tampered = replace(result, solver_objective_bound=1500.)
    report = verify_solution(model, tampered)
    assert report.candidate_valid
    assert report.milp_bound_consistent is False
    assert report.evidence == "none"


def test_whole_eggs_extension_only_requires_integrality_for_t():
    model = diet_problem()
    result = solve(model, integer_variables=("t",))
    report = verify_solution(model, result)
    assert report.candidate_valid
    assert not report.independent_optimality_verified


def test_mismatched_names_and_bad_tolerance_rejected():
    model = diet_problem()
    result = solve(model)
    with pytest.raises(ValueError, match="names"):
        verify_solution(model, replace(result, variable_values={"p": 0.}))
    with pytest.raises(ValueError, match="Tolerances"):
        verify_solution(model, result, atol=-1.)
    with pytest.raises(ValueError, match="model name"):
        verify_solution(model, replace(result, model_name="other"))


def test_nonfinite_candidate_is_never_valid():
    model = diet_problem()
    result = solve(model)
    forged = replace(result, variable_values={"p": float("nan"), "s": 1., "t": 4.})
    report = verify_solution(model, forged)
    assert not report.candidate_valid
    assert not report.independent_optimality_verified


def test_unconstrained_zero_objective_lp_has_trivial_certificate():
    model = LinearProgram(
        name="zero", variables=("x",), objective=(0.,), maximize=False,
        a_ub=(), b_ub=(), constraint_names=(), bounds=((None, None),),
        objective_unit="units",
    )
    result = solve(model)
    report = verify_solution(model, result)
    assert report.candidate_valid
    assert report.independent_optimality_verified
    assert report.lp_dual_multipliers == {}


@pytest.mark.parametrize("argument,integer", [("diet", False), ("boats", True)])
def test_cli_verification_json(argument, integer):
    cmd = [sys.executable, "-m", "modeling_lab", argument, "--verify", "--json"]
    if integer:
        cmd.append("--integer")
    proc = subprocess.run(cmd, capture_output=True, text=True, check=True)
    payload = json.loads(proc.stdout)
    report = payload["verification"]
    assert report["candidate_valid"] is True
    if integer:
        assert report["independent_optimality_verified"] is False
        assert report["evidence"] == "milp_solver_bound"
    else:
        assert report["independent_optimality_verified"] is True
        assert report["evidence"] == "lp_primal_dual"
