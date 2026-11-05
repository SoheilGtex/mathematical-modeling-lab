# Two-product production planning with hesitant fuzzy coefficients

## Source statement (pages 4–5)

A factory manufactures products A and B. Management wants to **maximize profit**. Profit per unit, processing time per unit and the available total production time are uncertain. Instead of one precise estimate, two fuzzy estimates are recorded for each coefficient.

Let \(x_A,x_B\) be the nonnegative quantities of products A and B.

The handwritten formulation is a **hesitant-fuzzy mathematical model**:

$$\max\;\widetilde Z=\widetilde P_Ax_A+\widetilde P_Bx_B$$

subject to

$$\widetilde T_Ax_A+\widetilde T_Bx_B\;\preceq\;\widetilde C,
\qquad x_A,x_B\ge0.$$

Here each \(\widetilde P_i,\widetilde T_i,\widetilde C\) is a **family of two fuzzy triangles**, not a single crisp number. The inequality symbol \(\preceq\) needs an explicit comparison rule to become an executable optimization problem. The scan **does not define that rule for this specific model**.

## Transcribed classroom coefficients

The comparatively clear **time requirements** (in hours per product) are:

| Product | First evaluator \((l,m,u)\) | Second evaluator \((l,m,u)\) |
|---|---|---|
| A | \((1,1.5,2)\) | \((2,2.5,3)\) |
| B | \((2,2.5,3)\) | \((3,3.5,4)\) |

The profit estimates clearly include \((40,45,50)\) for A and \((30,35,40),(40,45,50)\) for B. The second A profit tuple and one capacity tuple have a difficult or internally inconsistent last digit in the scan. **They must be treated as unverified**; see [source audit](audit.md). The second capacity is legible as \((40,45,70)\). Do not silently replace the ambiguous entries with assumed numbers.

## Model formulation checklist

1. Define products and nonnegative variables, and state production units.
2. Record which fuzzy tuple belongs to which evaluator and attribute (profit, time or capacity).
3. Keep the hesitant components grouped instead of silently averaging them.
4. Explain the meaning of a fuzzy inequality and which ranking, feasibility or robustness convention is adopted.
5. Only after declaring those choices, derive a deterministic equivalent (if one exists) and solve it.

### Optional complete numerical illustration — **not a source answer**

To show what an **explicit additional assumption** looks like, suppose the unreadable upper values are both **60**, and rank every triangle using the trapezoid embedding \((l,m,m,u)\) with an equal-weight average over the two evaluators. This produces

$$\max\;50x_A+40x_B\quad\text{subject to}\quad
2x_A+3x_B\le52.5,\quad x_A,x_B\ge0.$$

The mathematical consequence of **these extra assumptions** is \(x_A=26.25,x_B=0\) and an objective value of \(1312.5\). The number is not printed in the scan and is **not** a validated solution to an unspecified fuzzy inequality.
