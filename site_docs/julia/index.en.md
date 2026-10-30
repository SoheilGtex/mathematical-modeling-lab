# Julia Learning Materials

These optional Julia tutorials complement the mathematical-modeling course.

The Julia section is maintained separately from the Python implementation and from the **modeling-only exam review** for all course sessions and assignments.

## Available Basics

- [Variables](https://github.com/SoheilGtex/mathematical-modeling-lab/blob/main/Julia/01_Basics/01_variables.jl): variables and production-cost calculations.
- [Control flow](https://github.com/SoheilGtex/mathematical-modeling-lab/blob/main/Julia/01_Basics/04_control_flow.jl): conditions, loops, and branching.
- [Functions](https://github.com/SoheilGtex/mathematical-modeling-lab/blob/main/Julia/01_Basics/05_functions.jl): arguments, return values, and reusable calculations.

## Course Examples

The `03_Course_Examples/` directory contains seven practical examples of mathematical modeling and optimization using Julia, JuMP, and HiGHS.

- [Boat production](https://github.com/SoheilGtex/mathematical-modeling-lab/blob/main/Julia/03_Course_Examples/boat-production.jl): production planning and profit maximization.
- [Diet problem](https://github.com/SoheilGtex/mathematical-modeling-lab/blob/main/Julia/03_Course_Examples/diet.jl): minimum-cost food selection subject to nutritional requirements.
- [Investment](https://github.com/SoheilGtex/mathematical-modeling-lab/blob/main/Julia/03_Course_Examples/investment.jl): investment planning and financial optimization over multiple years.
- [Production and inventory](https://github.com/SoheilGtex/mathematical-modeling-lab/blob/main/Julia/03_Course_Examples/production-and-inventory.jl): production planning, overtime, and inventory management.
- [Scheduling](https://github.com/SoheilGtex/mathematical-modeling-lab/blob/main/Julia/03_Course_Examples/scheduling.jl): production scheduling and machine-capacity allocation.
- [Television production](https://github.com/SoheilGtex/mathematical-modeling-lab/blob/main/Julia/03_Course_Examples/television-production.jl): television production planning and profit maximization.
- [Transportation](https://github.com/SoheilGtex/mathematical-modeling-lab/blob/main/Julia/03_Course_Examples/transportation.jl): transportation planning and minimum-cost distribution.

These examples demonstrate how to define decision variables, objective functions, and constraints, and solve linear optimization models.

## How to Run

Install [Julia](https://julialang.org/downloads/).

### Running the Basics

From the repository root, run:

```bash
julia Julia/01_Basics/01_variables.jl
julia Julia/01_Basics/04_control_flow.jl
julia Julia/01_Basics/05_functions.jl
```

Only Julia itself is required for these introductory examples. **JuMP and HiGHS are not required.**

### Running the Course Examples

The course examples require the following Julia packages:

- [JuMP](https://jump.dev/JuMP.jl/stable/): mathematical optimization modeling.
- [HiGHS](https://highs.dev/): optimization solver.
- [MathOptInterface](https://jump.dev/MathOptInterface.jl/stable/): optimization model and solver-status interface.

Install the required packages in your Julia environment:

```julia
using Pkg
Pkg.add(["JuMP", "HiGHS", "MathOptInterface"])
```

Then, from the repository root, run an example. For instance:

```bash
julia Julia/03_Course_Examples/boat-production.jl
```

Replace `boat-production.jl` with the filename of any other course example you want to run.

## Additional Resources

See the [Julia source README](https://github.com/SoheilGtex/mathematical-modeling-lab/blob/main/Julia/README.md) for more information and the [contributors](https://github.com/SoheilGtex/mathematical-modeling-lab/blob/main/CONTRIBUTORS.md) page for project contributors.