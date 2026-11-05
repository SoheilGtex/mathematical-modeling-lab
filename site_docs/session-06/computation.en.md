# Session 06 — Optional Python verification

These computations support the mathematical modeling pages; they are **not** part of the handwritten lecture's worked numerical results.

From the repository root:

```bash
python examples/session_06/01_membership_and_arithmetic.py
python examples/session_06/02_ranked_production.py
python -m pytest tests/test_session_06_07.py -q
```

The reusable implementation is [`src/modeling_lab/fuzzy_sessions.py`](https://github.com/SoheilGtex/mathematical-modeling-lab/blob/main/src/modeling_lab/fuzzy_sessions.py). The first example checks support, membership, level intervals, negation and LR arithmetic. The second builds the course's **rank-based** deterministic counterpart with SciPy/HiGHS and verifies its binding constraints.

The expected production result is $x_1\approx40.71824429$, $x_2\approx18.79849257$, objective rank $\approx2568.65440035$. These numbers are independent calculations, not data claimed to appear in the scan.

See the mathematical definitions in [foundations](foundations.md), [LR arithmetic](arithmetic.md), and [the production model](ranking-production.md).
