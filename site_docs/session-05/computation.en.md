# Session 05 — Computational Notes (Optional)

The fractional example (lecture pages 1–3) is solved numerically by applying the **Charnes–Cooper LP transformation** and SciPy/HiGHS. The fuzzy-number example (pages 4–7) evaluates the *membership function*; it does not solve a fuzzy-optimization problem.

Run, from the repository root after `python -m pip install -e ".[dev]"`:

```bash
python examples/session_05/01_fractional_charnes_cooper.py
python examples/session_05/02_triangular_fuzzy.py
```

The independently verified fractional optimum is

$$x^*=(0,50/3),\quad (y_1^*,y_2^*,t^*)=(0,5/26,3/260),\quad f^*=103/26.$$

The membership checks include $\mu(1.2)=0.05$ (from the lecture) and $\mu(6)=0.5$ (independent illustration). These calculations are optional; the cumulative exam review contains only the **formulation**.
