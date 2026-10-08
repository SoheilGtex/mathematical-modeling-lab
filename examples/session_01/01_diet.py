"""Class example 1: cost-minimizing diet with vitamin minimums."""

from modeling_lab import solve
from modeling_lab.problems import diet_problem


def main() -> None:
    problem = diet_problem()
    result = solve(problem)
    print("Diet LP (as written in the class notes)")
    print(f"Minimum cost: {result.objective_value:.2f} toman/day")
    for var, amount in result.variable_values.items():
        print(f"  {var}: {amount:.4f}")
    print("Vitamin A:", result.variable_values["p"] + 4 * result.variable_values["s"] + 2 * result.variable_values["t"])
    print("Vitamin B:", result.variable_values["p"] + 2 * result.variable_values["s"] + 3 * result.variable_values["t"])

    whole_eggs = solve(problem, integer_variables=("t",))
    print(f"Extension (whole eggs): {whole_eggs.objective_value:.2f} toman/day")


if __name__ == "__main__":
    main()
