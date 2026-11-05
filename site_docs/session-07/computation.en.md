# Session 07 — Optional Python verification

From the repository root, after installing the project's Python dependencies:

```bash
python examples/session_07/01_ranked_lr_lp.py
python examples/session_07/02_extension_kerre.py
python -m pytest tests/test_session_06_07.py -q
```

The first program solves the **rank-defined** four-parameter LR LP on page 4; the expected result is $x_1=77/96$, $x_2=25/16$, $R(Z)=755/96$.

The second program computes the fuzzy maximum by **alpha-cut inversion**, compares it with the independently derived piecewise formula, and numerically integrates Kerre's $L^1$ distances. Expected distances: $d(M,D)=3/2$ and $d(N,D)=1/4$.

These outputs are independent extensions of the source, not quoted solutions. The calculations cannot replace the mathematical justification in [the LR model](lr-model.md), [the extension principle](extension-max.md), and [the comparison rule](kerre.md).
