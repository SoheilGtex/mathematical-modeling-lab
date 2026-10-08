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

## Repository structure

```text
src/modeling_lab/
  linear.py            # validated model + linprog/milp adapter
  problems.py          # class problem data (single source of truth)
  __main__.py          # CLI and JSON output
examples/session_01/
  01_diet.py
  02_boat_production.py
docs/
  session_01.md        # formulation, assumptions, interpretation
  example_template.md  # checklist for new class examples
tests/
  test_session_01.py   # regression and feasibility tests
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
