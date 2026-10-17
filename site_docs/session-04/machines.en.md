# Three Products on Four Machines — Full Worked Solution

> **Source:** Session 04 handwritten pages 1–2. Cost, demand, processing-time and capacity data are from the lecture. The numerical solution and exact optimality certificate below are independent additions. Costs are in **US dollars**, processing times in **hours**.

## 1. Problem and tables

A production manager must make at least 3,000 units of product 1, 6,000 of product 2, and 4,000 of product 3. Each can be made on any of four machines. Find the least-cost allocation while respecting the operating time of every machine.

**Cost per produced unit (USD):**

| Product / machine | 1 | 2 | 3 | 4 | Minimum demand |
| --- | ---: | ---: | ---: | ---: | ---: |
| Product 1 | 4 | 4 | 5 | 7 | 3,000 |
| Product 2 | 6 | 7 | 5 | 6 | 6,000 |
| Product 3 | 12 | 10 | 8 | 11 | 4,000 |

**Processing hours per unit:**

| Product / machine | 1 | 2 | 3 | 4 |
| --- | ---: | ---: | ---: | ---: |
| Product 1 | 0.30 | 0.25 | 0.20 | 0.20 |
| Product 2 | 0.20 | 0.30 | 0.20 | 0.25 |
| Product 3 | 0.80 | 0.60 | 0.60 | 0.50 |
| **Available machine hours** | **1,500** | **1,200** | **1,500** | **2,000** |

## 2. Decision variables and complete LP

Let $x_{ij}\ge0$ be the **number of units of product $i$ made on machine $j$**, where $i=1,2,3$ and $j=1,2,3,4$. There are $12$ variables. Let $c_{ij}$ be the cost table, $t_{ij}$ the processing-time table, $d=(3000,6000,4000)$ and $H=(1500,1200,1500,2000)$.

$$
\boxed{\begin{aligned}
\min\quad &Z=\sum_{i=1}^3\sum_{j=1}^4 c_{ij}x_{ij}\\
\mathrm{s.t.}\quad &\sum_{i=1}^3t_{ij}x_{ij}\le H_j &&j=1,\ldots,4\\
&\sum_{j=1}^4x_{ij}\ge d_i &&i=1,2,3\\
&x_{ij}\ge0 &&\forall i,j.
\end{aligned}}
$$

**Expanded objective:**

$$
\begin{aligned}
Z={}&4x_{11}+4x_{12}+5x_{13}+7x_{14}\\
&+6x_{21}+7x_{22}+5x_{23}+6x_{24}\\
&+12x_{31}+10x_{32}+8x_{33}+11x_{34}.
\end{aligned}
$$

The four machine limits are:

$$
\begin{aligned}
0.30x_{11}+0.20x_{21}+0.80x_{31}&\le1500,\\
0.25x_{12}+0.30x_{22}+0.60x_{32}&\le1200,\\
0.20x_{13}+0.20x_{23}+0.60x_{33}&\le1500,\\
0.20x_{14}+0.25x_{24}+0.50x_{34}&\le2000.
\end{aligned}
$$

The three product minimums are $\sum_jx_{1j}\ge3000$, $\sum_jx_{2j}\ge6000$, $\sum_jx_{3j}\ge4000$.

**Common mistake:** production minima use $\ge$, while finite machine-hour availability uses $\le$. Product quantities have units of **pieces**; the machine constraints convert pieces into **hours**.

## 3. Independently computed optimum

A minimum-cost plan is:

| Product / machine | 1 | 2 | 3 | 4 | Total |
| --- | ---: | ---: | ---: | ---: | ---: |
| Product 1 | 3,000 | 0 | 0 | 0 | 3,000 |
| Product 2 | 3,000 | 0 | 1,500 | 1,500 | 6,000 |
| Product 3 | 0 | 2,000 | 2,000 | 0 | 4,000 |
| **Hours used** | **1,500** | **1,200** | **1,500** | **375** | — |

The allocation meets each demand exactly and satisfies every machine-hour bound. Its cost is:

$$
Z=3000(4)+3000(6)+1500(5)+1500(6)+2000(10)+2000(8)=\boxed{82,500\text{ USD}}.
$$

## 4. Rigorous optimality certificate

Let $p=(4,6,11)$ for the three minimum quantities, and $q=(0,5/3,5,0)$ for the machine-hour upper bounds. Direct inspection of all 12 entries shows:

$$p_i-q_jt_{ij}\le c_{ij},\qquad p_i,q_j\ge0.$$

For any feasible $x$, multiply by $x_{ij}\ge0$ and sum. Since $\sum_jx_{ij}\ge d_i$ and $\sum_it_{ij}x_{ij}\le H_j$,

$$
\begin{aligned}
Z&\ge\sum_i p_i\sum_jx_{ij}-\sum_j q_j\sum_it_{ij}x_{ij}\\
&\ge\sum_ip_id_i-\sum_jq_jH_j\\
&=4(3000)+6(6000)+11(4000)-(5/3)(1200)-5(1500)\\
&=\boxed{82,500}.
\end{aligned}
$$

A feasible plan attains this lower bound, proving global optimality without relying solely on solver output.

## 5. Exam focus

State $x_{ij}$, the cost objective, four time-capacity inequalities, three minimum-production inequalities and nonnegativity. The cost table is in dollars. The numerical schedule and the certificate belong to the **full solution**, not to the modeling-only exam review.
