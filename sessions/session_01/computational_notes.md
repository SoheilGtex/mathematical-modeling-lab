# Session 01 — Mathematical models, constraints, and optimization

**Course:** Introductory Mathematical Modeling, Kharazmi University (Fall 1405).

This document reformulates the examples from the course notes. The solver and
numerical solutions are **our extensions**: the handwritten notes present
models but do not compute the optima.

## Example 1 — Minimum-cost diet

Choose nonnegative amounts of cheese (`p`), milk (`s`), and eggs (`t`).
The course gives the following quantities and costs:

| Food (one unit) | Vitamin A | Vitamin B | Cost (toman) |
| --- | ---: | ---: | ---: |
| Cheese | 1 | 1 | 100 |
| Milk | 4 | 2 | 50 |
| Eggs | 2 | 3 | 40 |

Daily vitamin minimums: A >= 12, B >= 14.

$$
\begin{aligned}
\min\quad &100p + 50s + 40t \\
\text{s.t.}\quad &p + 4s + 2t\ge12\\
&p + 2s + 3t\ge14\\
&p,s,t\ge0.
\end{aligned}
$$

**Computed continuous solution:** `p = 0, s = 1, t = 4`;
minimum cost `210 toman/day`. Both vitamin requirements are met exactly.

**Assumption audit:** The notes use real-valued nonnegative amounts.
If eggs must be whole units, constrain `t` to integers. This changes the
mathematical model, even though for these specific data the optimum remains
unchanged.

Run: `python -m modeling_lab diet` or
`python -m modeling_lab diet --integer`.

## Example 2 — Production planning (two boat types)

Decision variables: `x` = regular boats; `y` = competition boats.

| Resource / quantity | Regular boat | Competition boat | Capacity |
| --- | ---: | ---: | ---: |
| Aluminum (kg) | 50 | 30 | 1000 |
| Machine time (minutes) | 20 | 15 | 300 (5 hours) |
| Human labor (hours) | 3 | 5 | 200 |
| Profit (1000 toman) | 50 | 80 | — |

$$
\begin{aligned}
\max\quad &50x+80y\\
\text{s.t.}\quad &50x+30y\le1000\\
&20x+15y\le300\\
&3x+5y\le200\\
&x,y\ge0.
\end{aligned}
$$

**Computed continuous solution:** `x = 0, y = 20`, maximum profit
`1600 thousand toman = 1,600,000 toman`. Resources used: 600 kg aluminum,
300 machine minutes, 100 labor hours. Therefore machine time is binding.

**Assumption audit:** The original notes have `x,y >= 0`, not integrality
constraints, despite the quantities representing boats. Our `--integer`
option enforces whole boat counts. Here it yields the same optimum, but
that need not be true for other datasets.

Run: `python -m modeling_lab boats` or
`python -m modeling_lab boats --integer`.

## What to document for every future class example

1. Session number and concise statement of the real-world question.
2. Decision variables, units, parameters, and their source.
3. Mathematical objective and every constraint.
4. Modeling assumptions and any ambiguous details in the notes.
5. Solver choice and optimality status (or infeasible/unbounded status).
6. Values, units, feasibility checks, and practical interpretation.
7. At least one reproducible automated test.

Avoid reproducing or publishing the entire scanned class notes without
permission; use your own explanations and mathematical formulations.
