# Computation — Session 11

The [exact-rational implementation](https://github.com/SoheilGtex/mathematical-modeling-lab/blob/main/src/modeling_lab/hesitant_final.py) checks that fuzzy-triangle and trapezoid coordinates are ordered, and computes the rank defined in the lecture.

```bash
python examples/session_11/01_ranked_hesitant_numbers.py
python -m pytest -q tests/test_session_10_11.py
```

Expected source comparison: \(R_1(A)=4.5\) and \(R_1(B)=3.75\). An explicitly marked hypothetical production scenario has model \(\max 50x_A+40x_B\) subject to \(2x_A+3x_B\le52.5\), but is **not a verified numerical model from the scan**.

For uncertainty or a data-entry mismatch, see [audit and open questions](audit.md).
