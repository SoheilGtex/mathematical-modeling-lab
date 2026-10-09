# Session 02 — Computational notes

**Source-derived data vs additions:** The single handwritten page has a general symbolic transportation model and a TV model with 60,000 person-hours of labor (confirmed by the student after an ambiguous transcription). Numeric solver solutions, integer extensions, and the 2×2 transportation demo are independent educational additions.

## Mathematical models

- Transportation: $\min\sum_{i,j} c_{ij} x_{ij}$, subject to source $\sum_j x_{ij}\le a_i$, destination $\sum_i x_{ij}=b_j$, $x_{ij}\ge0$.
- Television production: $\max 60x_1+30x_2$, subject to $20x_1+15x_2\le H$, $0\le x_1\le2000$, $0\le x_2\le4000$.

Our `LinearProgram` implementation supports only `A_ub @ x <= b_ub` natively. Each transportation demand equality is therefore represented with **both** $\sum_i x_{ij}\le b_j$ and $-\sum_i x_{ij}\le-b_j$. The two constraints enforce equality; no demand relaxation is intended.

## Commands

```bash
python -m modeling_lab transport-demo --verify
python -m modeling_lab televisions --verify                      # 60000 (corrected capacity)
python -m modeling_lab televisions --integer --verify             # integer extension
python -m modeling_lab televisions --plot plots/tv_continuous.png  # LP visualization
python -m modeling_lab televisions --labor-hours 65000 --verify  # optional what-if scenario
python examples/session_02/01_transportation.py
python examples/session_02/02_television_production.py
```

**Warning:** `--integer --plot` for televisions attempts to plot millions of integer lattice points; the generic visualization currently rejects this rather than misleadingly sampling. Use `--integer` to solve and `--plot` without `--integer` to visualize the continuous region, or inspect the integer optimum numerically.

## Numerical reference (computed, not from the notes)

| Model | Optimal continuous variables | Continuous objective | Integer extension |
| --- | --- | ---: | --- |
| TV, H=60000 | (2000, 4000/3) | $160000 | (2000, 1333), $159990 |
| Transport 2×2 invented demo | (10, 0, 2, 18) | 46 cost units | no integer requirement in source |

## Future refinement

The correction to 60,000 person-hours was supplied by the student. The original handwriting was transcribed ambiguously; the outdated 40,000 / 90,000 alternatives were removed from the official worked example. They are not treated as class data.
