# Assignments

Course assignments and full solutions are kept separate from lecture notes.
The **modeling components** are included in the single cumulative exam review.
The handouts are paraphrased; their scans are not redistributed.

- **Assignment 01 — Investment budgeting:** [English](../site_docs/assignments/investment-budget.en.md) · [فارسی](../site_docs/assignments/investment-budget.fa.md). Standalone Python: `examples/assignments/01_investment_budget.py`.
- **Assignment 02 — Transportation (Python only):** [English](../site_docs/assignments/transportation-python.en.md) · [فارسی](../site_docs/assignments/transportation-python.fa.md). The assigned work was **only the Python solution of the existing Session 03 transportation model**. No separate new transport problem: the code is already at [`examples/session_03/01_transportation.py`](../examples/session_03/01_transportation.py).
- **Assignment 03 — Triangular fuzzy numbers and max:** [English complete solution](../site_docs/assignments/fuzzy-numbers-max.en.md) · [حل کامل فارسی](../site_docs/assignments/fuzzy-numbers-max.fa.md). Analytical derivations, graphs and extension-principle verification; optional script: `examples/assignments/03_fuzzy_numbers_max.py`.

```bash
python examples/assignments/01_investment_budget.py
python examples/session_03/01_transportation.py
python examples/assignments/03_fuzzy_numbers_max.py
python -m pytest -q tests/test_assignment_03.py
```
