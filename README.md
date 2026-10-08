# Mathematical Modeling Lab

Reproducible mathematical-modeling examples from an introductory university
course, written in **Python**. Each example goes beyond a mathematical
formulation: it includes a numerical solve, explicit assumptions, feasibility
checks, and automated tests.

The project starts with two examples from **session 01** of *Introductory
Mathematical Modeling*, Kharazmi University (Fall 1405 / 2026).

> The handwritten course notes only formulate the two mathematical models;
> the Python implementations, optimizers, computed solutions and integer-model
> comparisons here are independent extensions. These are pedagogical models;
> their numbers should not be interpreted as real-world nutritional or
> production data.

## Examples

| Session | Problem | Type | Result (continuous formulation) |
| --- | --- | --- | --- |
| 01 | [Minimum-cost diet](docs/session_01.md#example-1--minimum-cost-diet) | Linear program, minimization | 210 toman/day; cheese=0, milk=1, eggs=4 |
| 01 | [Boat production](docs/session_01.md#example-2--production-planning-two-boat-types) | Linear program, maximization | 1600 thousand toman; regular=0, competition=20 |

See [session 01 notes](docs/session_01.md) for original coefficients,
constraints, dimensional units, assumptions, and solved interpretations.

## Quick start (macOS/Linux)

Python 3.11+ is required.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"

python -m modeling_lab diet
python -m modeling_lab boats
python -m modeling_lab boats --integer
python -m modeling_lab diet --integer --json
pytest -q
```

Or run the individual examples:

```bash
python examples/session_01/01_diet.py
python examples/session_01/02_boat_production.py
```

**Why SciPy?** For now, both examples are linear programs.
`scipy.optimize.linprog` uses the HiGHS solver for continuous linear programs;
`scipy.optimize.milp` adds an integer-variable option without requiring a
separate external solver installation. For future nonlinear problems,
`scipy.optimize.minimize` or modeling frameworks such as Pyomo may be better.

## Visualization (session 01)

Install plotting dependencies (the `dev` extra also includes Matplotlib):

```bash
python -m pip install -e ".[dev]"
python -m modeling_lab boats --integer --plot plots/boats.png
```

The generated PNG contains all three constraint lines, the feasible polygon,
objective isoprofit lines, the continuous optimum, and the feasible integer
lattice points plus the integer optimum. **The continuous and integer optima
coincide at (x, y) = (0, 20)** with profit 1600 thousand toman; there is no
integrality gap in this example. The machine-time constraint is binding at the
optimum; the aluminum and labor constraints are redundant over the feasible
triangle. Constraint curves may lie outside the feasible polygon.

Figures are constructed from the coefficient matrices in `problems.py`; no
hand-drawn coordinates or fabricated optimum values are used. Generated files
under `plots/` are ignored by Git; intentionally publish selected figures under
`docs/assets/` if desired. Current 2D plots require two nonnegative variables.

The diet problem has three variables and cannot be plotted by this 2D routine.

## Sensitivity analysis (session 01)

One-at-a-time parameter sweeps re-solve the model for each scenario. Results
include physical-unit parameters, changed optimal decisions, objective values,
scenario statuses and optional PNGs. Local **shadow prices are reported for
continuous LP RHS parameters only**, never as MILP shadow prices.

```bash
python -m modeling_lab boats --list-parameters
python -m modeling_lab boats --sensitivity machine_minutes \
  --values 240 300 360 400 --sensitivity-plot plots/machine_lp.png
python -m modeling_lab boats --integer --sensitivity machine_minutes \
  --values 300 310 315 400 --sensitivity-plot plots/machine_milp.png
python -m modeling_lab diet --sensitivity vitamin_A_requirement \
  --values 10 12 14 --json
```

Read the [sensitivity analysis notes](docs/sensitivity_analysis.md) for sign
conventions, sample results, interpretation and limitations. This feature is
an independent extension beyond the original handwritten class notes.

## Repository structure

```text
src/modeling_lab/
  linear.py            # validated model + linprog/milp adapter
  visualization.py     # coefficient-driven feasible-region plots
  sensitivity.py       # RHS/coefficients scenarios and local LP duals
  problems.py          # class problem data (single source of truth)
  __main__.py          # CLI and JSON output
examples/session_01/
  01_diet.py
  02_boat_production.py
docs/
  session_01.md        # formulation, assumptions, interpretation
  example_template.md  # checklist for new class examples
  sensitivity_analysis.md # sensitivity mathematics and examples
tests/
  test_session_01.py   # regression and feasibility tests
  test_visualization.py # plot geometry, PNG and CLI tests
  test_sensitivity.py   # parametric re-solves and dual sign tests
.github/workflows/
  ci.yml               # automated tests on pushes and PRs
```

## Engineering principles

- Preserve the source formulation; separate any additional assumptions.
- Validate units (e.g. 5 machine-hours = 300 machine-minutes).
- Check feasibility, solver status, integer domains, and objective units.
- Keep model data separate from solver code and exposition.
- Test known optima and numerical constraints.
- Avoid posting scanned copyrighted classroom notes without permission.

## Creating your GitHub repository

Once the project folder is on your computer, run:

```bash
git init
git add .
git commit -m "Initial modeling lab: session 01"
# Install/authenticate the GitHub CLI if needed: https://cli.github.com/
gh auth login
gh repo create mathematical-modeling-lab --public --source=. --remote=origin --push
```

If you already have a repository, connect its remote instead of calling
`gh repo create` a second time. Choose an appropriate license before making
third-party reuse permissions explicit.
