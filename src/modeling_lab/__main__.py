"""Execute the class examples from the command line."""

import argparse
import json
from pathlib import Path

from .linear import Solution, solve
from .problems import boat_production_problem, diet_problem


def format_solution(solution: Solution) -> str:
    items = [
        f"Model: {solution.model_name}",
        f"Solver: {solution.solver}",
        f"Objective: {solution.objective_value:.6g} {solution.objective_unit}",
        "Variables:",
    ]
    items.extend(f"  {name} = {value:.6g}" for name, value in solution.variable_values.items())
    items.append("Constraint slacks (in original inequality units):")
    items.extend(
        f"  {name}: {value:.6g}" for name, value in solution.constraint_slacks.items()
    )
    return "\n".join(items)


def main() -> None:
    parser = argparse.ArgumentParser(description="Solve mathematical modeling examples")
    parser.add_argument("problem", choices=["diet", "boats"])
    parser.add_argument(
        "--integer", action="store_true",
        help="Extension: diet uses whole eggs; boats use whole counts",
    )
    parser.add_argument("--json", action="store_true", help="Machine-readable output")
    parser.add_argument(
        "--plot", type=Path, metavar="PNG_PATH",
        help="Render a two-variable LP (with integer overlay if --integer is set)",
    )
    args = parser.parse_args()
    model = diet_problem() if args.problem == "diet" else boat_production_problem()
    integer_variables = (
        ("t",) if args.problem == "diet" else ("x", "y")
    ) if args.integer else ()
    result = solve(model, integer_variables=integer_variables)
    if args.plot:
        if len(model.variables) != 2:
            parser.error("--plot requires exactly two variables (try 'boats')")
        from .visualization import plot_linear_program_2d

        generated_plot = plot_linear_program_2d(
            model, args.plot, show_integer_points=args.integer
        )
    else:
        generated_plot = None
    if args.json:
        payload = {
            "model": result.model_name,
            "objective_value": result.objective_value,
            "objective_unit": result.objective_unit,
            "variables": result.variable_values,
            "constraint_slacks": result.constraint_slacks,
            "integer_variables": sorted(result.integer_variables),
            "solver": result.solver,
        }
        if generated_plot is not None:
            payload["plot_path"] = str(generated_plot)
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(format_solution(result))
        if generated_plot is not None:
            print(f"Plot saved to: {generated_plot}")


if __name__ == "__main__":
    main()
