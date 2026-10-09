"""Run Assignment 01's LP and compare it with the independent hand solution."""
from modeling_lab.assignment01 import (
    annual_coupon_cost, exact_optimal_plan, investment_budget_problem,
)
from modeling_lab.linear import solve
from modeling_lab.verification import verify_solution


def main() -> None:
    model = investment_budget_problem()
    result = solve(model)
    hand_plan = exact_optimal_plan()
    print("Assignment 01 — Four-year municipal investment budgeting")
    print("All amounts: millions of USD")
    print("Variable       LP optimum       Analytic optimum")
    for name in model.variables:
        print(f"{name:<10} {result.variable_values[name]:>13.8f} {hand_plan[name]:>21.8f}")
    print(f"Annual nominal interest: {annual_coupon_cost(hand_plan):.9f}")
    print(f"20-year nominal interest: {result.objective_value:.9f}")
    evidence = verify_solution(model, result)
    print(f"Candidate feasible: {evidence.candidate_valid}")
    print(f"Independent optimality verified: {evidence.independent_optimality_verified}")


if __name__ == "__main__":
    main()
