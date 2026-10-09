"""Assignment 01 regression: source data, cash flow, exact optimum and bilingual documentation."""
from __future__ import annotations

from pathlib import Path

import pytest

from modeling_lab.assignment01 import (
    ANNUAL_NEEDS, INTEREST_PAYMENT_YEARS, LONG_TERM_RATES,
    SHORT_TERM_RATES, annual_coupon_cost, exact_optimal_plan,
    investment_budget_problem, proof_coefficients,
)
from modeling_lab.linear import solve
from modeling_lab.verification import verify_solution

ROOT = Path(__file__).resolve().parents[1]


def test_handout_coefficients_and_model_dimensions():
    assert ANNUAL_NEEDS == (2, 4, 8, 5)
    assert LONG_TERM_RATES == (0.07, 0.06, 0.065, 0.075)
    assert SHORT_TERM_RATES == (0.06, 0.055, 0.045)
    assert INTEREST_PAYMENT_YEARS == 20
    model = investment_budget_problem()
    assert model.variables == ("x1", "x2", "x3", "x4", "s1", "s2", "s3")
    assert len(model.a_ub) == len(model.b_ub) == 8
    assert model.objective == pytest.approx((1.4, 1.2, 1.3, 1.5, 0, 0, 0))
    assert model.maximize is False


def test_analytical_plan_satisfies_four_exact_balances():
    p = exact_optimal_plan()
    cash_flow = (
        p["x1"] - p["s1"],
        p["x2"] + 1.06 * p["s1"] - p["s2"],
        p["x3"] + 1.055 * p["s2"] - p["s3"],
        p["x4"] + 1.045 * p["s3"],
    )
    assert cash_flow == pytest.approx(ANNUAL_NEEDS, abs=1e-9)
    assert all(value >= 0 for value in p.values())
    assert p["x2"] == pytest.approx(16.11818862105717)
    assert p["s2"] == pytest.approx(12.118188621057168)
    assert p["s3"] == pytest.approx(4.784688995215311)


def test_algebraic_certificate_positive_proves_unique_minimum():
    a, b, c = proof_coefficients()
    assert (a, b, c) == pytest.approx((0.0064, 0.008127962085308055, 0.020576997210821096))
    assert min(a, b, c) > 0
    # Every feasible plan has C = C* + a*s1 + b*x3 + c*x4.
    p = exact_optimal_plan()
    assert annual_coupon_cost(p) == pytest.approx(1.1070913172634302)
    assert 20 * annual_coupon_cost(p) == pytest.approx(22.141826345268605)


def test_lp_matches_exact_optimum_and_independent_verification():
    model = investment_budget_problem()
    sol = solve(model)
    expected = exact_optimal_plan()
    for key, target in expected.items():
        assert sol.variable_values[key] == pytest.approx(target, abs=1e-6)
    assert sol.objective_value == pytest.approx(22.141826345268605, abs=1e-6)
    ev = verify_solution(model, sol)
    assert ev.candidate_valid is True
    assert ev.independent_optimality_verified is True


def test_bilingual_assignments_exist_without_changing_exam_review():
    for lang in ("en", "fa"):
        index = (ROOT / f"site_docs/assignments/index.{lang}.md").read_text(encoding="utf-8")
        solution = (ROOT / f"site_docs/assignments/investment-budget.{lang}.md").read_text(encoding="utf-8")
        assert "investment-budget.md" in index
        assert "1.055" in solution and "1.045" in solution
        assert "22.141826" in solution
        assert "x_1" in solution and "s_3" in solution
    assert (ROOT / "site_docs/exam.en.md").is_file()
    assert (ROOT / "site_docs/exam.fa.md").is_file()
