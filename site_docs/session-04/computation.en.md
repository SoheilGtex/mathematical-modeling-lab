# Session 04 — Computational Notes (Optional)

The three models are independent teaching examples taken from the four-page handwritten lecture note. The code below is supplementary; **neither software nor a numerical optimum is required for the modeling-only exam review**.

```bash
python examples/session_04/01_machine_allocation.py
python examples/session_04/02_crude_oil.py
python examples/session_04/03_revenue_cost_ratio.py
```

Install the project and its dependencies first: `python -m pip install -e ".[dev]"` in an activated virtual environment. The first two examples are continuous **linear programs**, solved using the shared SciPy HiGHS helper. The third is **linear-fractional**. For its particular coefficients, revenue is exactly twice variable cost; therefore maximizing its ratio is equivalent to maximizing variable cost, a two-variable LP. This reduction is **not** valid for arbitrary fractional programs.

| Lecture model | Independently computed optimum | Units |
| --- | ---: | --- |
| 3 products / 4 machines | 82,500 | USD, total production cost |
| 2 crude oils / 3 refinery products | 50,951,086.96 | USD, crude purchase cost |
| 2 products / revenue-to-cost ratio | 20/11 ≈ 1.81818 | dimensionless |

For exact lower-bound certificates and full explanations, see [machines](machines.md), [crude](crude.md) and [fractional ratio](ratio.md). No Julia code is introduced or modified by this Session 04 update.
