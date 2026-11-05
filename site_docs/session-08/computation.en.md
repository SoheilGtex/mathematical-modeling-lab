# Session 08 — Exact computational check (optional)

The mathematical work on the [extension maximum](extension-recap.md) and [Kerre distance](distance.md) is complete without software. This page verifies each result with **exact rational arithmetic** instead of approximate numerical quadrature.

The implementation is in [`src/modeling_lab/fuzzy_comparison.py`](https://github.com/SoheilGtex/mathematical-modeling-lab/blob/main/src/modeling_lab/fuzzy_comparison.py), and the executable example is [`examples/session_08/01_maximum_geometry.py`](https://github.com/SoheilGtex/mathematical-modeling-lab/blob/main/examples/session_08/01_maximum_geometry.py).

From the repository root, with the project's Python environment activated:

```bash
python examples/session_08/01_maximum_geometry.py
python -m pytest tests/test_session_08_09.py -q
```

Expected exact quantities:

| Quantity | Value |
| --- | ---: |
| Extension maximum knots $(z,\mu_D(z))$ | $(2,0),(3,1),(7/2,1/2),(5,0)$ |
| $d(M,D)$ | $3/2$ |
| $d(N,D)$ | $1/4$ |
| $r(M,N)$ | $5/4$ |

The program forms alpha-cut endpoint maxima, inverts the resulting piecewise-linear graph, and integrates absolute differences by splitting at intersections. **No comparison is inferred from pointwise maximum of memberships.** This code is supplemental and not required for a modeling-only written exam.
