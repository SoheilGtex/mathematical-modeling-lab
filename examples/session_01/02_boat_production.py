"""Class example 2: profit-maximizing boat production."""

from modeling_lab import solve
from modeling_lab.problems import boat_production_problem


def main() -> None:
    problem = boat_production_problem()
    continuous = solve(problem)
    whole_boats = solve(problem, integer_variables=("x", "y"))
    print("Boat LP (as written in the notes)")
    print(f"Maximum profit: {continuous.objective_value:.2f} thousand toman")
    print("  Regular boats:", continuous.variable_values["x"])
    print("  Competition boats:", continuous.variable_values["y"])
    print("Constraint slack:", continuous.constraint_slacks)
    print("Extension: integer boats")
    print("  Production:", whole_boats.variable_values)
    print(f"  Profit: {whole_boats.objective_value:.2f} thousand toman")


if __name__ == "__main__":
    main()
