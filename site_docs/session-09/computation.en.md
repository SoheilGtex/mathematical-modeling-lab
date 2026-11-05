# Session 09 — Reproduce the corrected worked example

The handwritten example is $M=(2,5,12)$ and $N=(2,4,10)$. The [mathematical audit](source-example.md) explains why the left and right slopes of $N$ must be $1/2$ and $-1/6$, respectively.

The optional program [`examples/session_09/01_kerre_source_example.py`](https://github.com/SoheilGtex/mathematical-modeling-lab/blob/main/examples/session_09/01_kerre_source_example.py) uses the exact implementation [`fuzzy_comparison.py`](https://github.com/SoheilGtex/mathematical-modeling-lab/blob/main/src/modeling_lab/fuzzy_comparison.py).

```bash
python examples/session_09/01_kerre_source_example.py
python -m pytest tests/test_session_08_09.py -q
```

Expected output, with exact fractions:

```text
Distance M to maximum: 0
Distance N to maximum: 17/9
Pairwise score: -17/9
Preferred triangle: first
```

The source's **two triangles** are exactly preserved; only the inconsistent membership denominators are replaced using the formal triangular definition. Every numerical score and integral evaluation is a new derivation.

## Why exact arithmetic matters here

The turning point $14/3$ is not a terminating decimal. Approximating it to $4.67$ before integration introduces small errors and can hide a sign change. The implementation uses Python's `fractions.Fraction` for endpoints and breakpoints and computes each linear segment's area exactly. These checks complement the written proof; they do not replace it.
