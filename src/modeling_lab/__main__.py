"""Execute the class examples from the command line."""

import argparse
import json
from pathlib import Path
from dataclasses import asdict

from .linear import Solution, solve
from .problems import boat_production_problem, diet_problem
from .session02 import television_problem, transportation_demo_problem, TV_LABOR_HOURS
from .verification import verify_solution
from .sensitivity import (
    save_sensitivity_plot, session01_parameters, sweep_parameter,
)


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
    parser.add_argument("problem", choices=["diet", "boats", "televisions", "transport-demo"])
    parser.add_argument(
        "--integer", action="store_true",
        help="Extension: impose integer counts (including television/transport flows)",
    )
    parser.add_argument("--json", action="store_true", help="Machine-readable output")
    parser.add_argument(
        "--labor-hours", type=float, default=None, metavar="HOURS",
        help="Televisions only: monthly person-hours (default: 60000, confirmed correction)",
    )
    parser.add_argument("--verify", action="store_true", help="Independent feasibility and LP optimality checks")
    parser.add_argument(
        "--plot", type=Path, metavar="PNG_PATH",
        help="Render a two-variable LP (with integer overlay if --integer is set)",
    )
    parser.add_argument(
        "--list-parameters", action="store_true",
        help="List physical-unit sensitivity parameters for this example",
    )
    parser.add_argument(
        "--sensitivity", metavar="PARAMETER",
        help="Re-solve across selected RHS values or objective coefficients",
    )
    parser.add_argument(
        "--values", type=float, nargs="+", metavar="NUMBER",
        help="Physical parameter values to sweep (1 to 200)",
    )
    parser.add_argument(
        "--sensitivity-plot", type=Path, metavar="PNG_PATH",
        help="Save objective-versus-parameter plot for a sensitivity sweep",
    )
    args = parser.parse_args()
    if args.labor_hours is not None and args.problem != "televisions":
        parser.error("--labor-hours applies only to televisions")
    parameters = session01_parameters(args.problem) if args.problem in {"diet", "boats"} else {}
    if args.list_parameters and not parameters:
        parser.error("Sensitivity parameter listing is currently available only for session 01")
    if args.sensitivity is not None and not parameters:
        parser.error("Sensitivity sweeps are currently available only for session 01")
    if args.list_parameters:
        for key, parameter in parameters.items():
            print(f"{key}: {parameter.kind}, {parameter.unit}")
        return
    if args.sensitivity is None and (args.values is not None or args.sensitivity_plot):
        parser.error("--values and --sensitivity-plot require --sensitivity")
    if args.sensitivity is not None:
        if args.sensitivity not in parameters:
            parser.error(
                f"Unknown parameter {args.sensitivity!r}; "
                f"choices: {', '.join(parameters)}"
            )
        if not args.values:
            parser.error("--sensitivity requires --values (one or more numbers)")
    if args.problem == "diet":
        model = diet_problem()
    elif args.problem == "boats":
        model = boat_production_problem()
    elif args.problem == "televisions":
        model = television_problem(labor_hours=(
            TV_LABOR_HOURS if args.labor_hours is None else args.labor_hours
        ))
    else:
        model = transportation_demo_problem()
    integer_variables = (
        ("t",) if args.problem == "diet" else model.variables
    ) if args.integer else ()
    result = solve(model, integer_variables=integer_variables)
    if args.problem == "televisions" and not args.json:
        print(
            "Television labor capacity: " + f"{model.b_ub[0]:g} person-hours "
            "(student-confirmed source correction: 60000)."
        )
    if args.problem == "transport-demo" and not args.json:
        print("Illustrative numbers only: the session notes give no numeric transport instance.")
    verification = verify_solution(model, result) if args.verify else None
    if args.sensitivity:
        report = sweep_parameter(
            model, parameters[args.sensitivity], args.values,
            integer_variables=integer_variables,
        )
        sensitivity_plot_path = (
            save_sensitivity_plot(report, args.sensitivity_plot)
            if args.sensitivity_plot else None
        )
    else:
        report = None
        sensitivity_plot_path = None
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
        if verification is not None:
            payload["verification"] = {**asdict(verification), "candidate_valid": verification.candidate_valid}
        if generated_plot is not None:
            payload["plot_path"] = str(generated_plot)
        if report is not None:
            payload["sensitivity"] = {
                "parameter": report.parameter.key,
                "kind": report.parameter.kind,
                "unit": report.parameter.unit,
                "baseline_parameter_value": report.baseline_parameter_value,
                "shadow_price": report.shadow_price,
                "shadow_price_is_local_lp_only": report.shadow_price is not None,
                "scenarios": [
                    {
                        "parameter_value": scenario.parameter_value,
                        "status": scenario.status,
                        "objective_value": scenario.objective_value,
                        "variables": scenario.variable_values,
                        "message": scenario.message,
                    } for scenario in report.scenarios
                ],
            }
            if sensitivity_plot_path is not None:
                payload["sensitivity"]["plot_path"] = str(sensitivity_plot_path)
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(format_solution(result))
        if verification is not None:
            print(f"Verification: candidate_valid={verification.candidate_valid}")
            print(f"Independently verified global optimality: {verification.independent_optimality_verified}")
            print(f"Evidence: {verification.evidence}")
            if verification.lp_primal_dual_gap is not None:
                print(f"LP primal-dual gap: {verification.lp_primal_dual_gap:.6g}")
            if verification.milp_solver_objective_bound is not None:
                print(f"Solver-reported MILP bound: {verification.milp_solver_objective_bound:.6g}")
            for note in verification.notes:
                print(f"  Note: {note}")
        if generated_plot is not None:
            print(f"Plot saved to: {generated_plot}")
        if report is not None:
            print(f"\nSensitivity: {report.parameter.key} ({report.parameter.unit})")
            print(f"Baseline parameter: {report.baseline_parameter_value:.6g}")
            if report.integer_variables:
                print("Shadow price: not applicable to integer-program solutions")
            elif report.shadow_price is not None:
                print(
                    f"Local continuous-LP shadow price: {report.shadow_price:.6g} "
                    f"{result.objective_unit} / {report.parameter.unit}"
                )
            for scenario in report.scenarios:
                objective_text = (
                    f"{scenario.objective_value:.6g} {result.objective_unit}"
                    if scenario.objective_value is not None else "N/A"
                )
                values_text = (
                    ", ".join(f"{key}={value:.6g}"
                              for key, value in scenario.variable_values.items())
                    if scenario.variable_values else ""
                )
                print(
                    f"  {scenario.parameter_value:g} -> {scenario.status}: "
                    f"{objective_text} {values_text}"
                )
            if sensitivity_plot_path is not None:
                print(f"Sensitivity plot saved to: {sensitivity_plot_path}")
    # Verification failure must be actionable in scripts and CI, not only a
    # printed diagnostic. MILPs lack an independent global-optimality proof;
    # their candidate checks are nevertheless enforceable.
    if verification is not None and (
        not verification.candidate_valid
        or (not integer_variables and not verification.independent_optimality_verified)
    ):
        raise SystemExit(2)


if __name__ == "__main__":
    main()
