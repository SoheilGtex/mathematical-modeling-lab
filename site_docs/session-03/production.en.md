# Five-Month Production and Inventory — Full Written Solution

> **Source:** Session 03, handwritten pages 3–4. Numerical demands, capacities and unit costs are from the note. The five-month optimal schedule, numerical answer and rigorous optimality proof are independent worked additions. No inventory is permitted before month 1 or after month 5.

## Problem statement

A factory plans production over five months. It can produce at most **2,000 units per month** in regular time and **600 additional units per month** in overtime. Regular production costs **10 toman/unit**; overtime costs **15 toman/unit**. Any unit held at the end of a month and carried into the next costs **2 toman/unit per month**. Demands for months 1–5 are **1,200, 2,100, 2,400, 3,000 and 4,000 units**, respectively. Meet all demands on time, with no initial stock and no stock remaining after the fifth month, at minimum total cost.

| Month $i$ | 1 | 2 | 3 | 4 | 5 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Demand $d_i$ | 1,200 | 2,100 | 2,400 | 3,000 | 4,000 |
| Regular capacity | 2,000 | 2,000 | 2,000 | 2,000 | 2,000 |
| Overtime capacity | 600 | 600 | 600 | 600 | 600 |

The total demand is $12,700$ units versus a maximum five-month production capacity of $13,000$ units. Aggregate capacity is necessary but does not by itself verify the month-by-month feasibility of a production plan.

## Decision variables and model

For each month $i=1,\ldots,5$:

- $x_i\ge0$: units made in regular time;
- $y_i\ge0$: units made in overtime;
- $s_i\ge0$: units held at the **end** of month $i$.

The boundary conditions are $s_0=s_5=0$, so $s_5$ is **not an independent variable**. There are 5 regular-production variables, 5 overtime variables and 4 inventory variables: **14 decision variables**. The note states 15 structural constraints before variable nonnegativity (5 regular limits, 5 overtime limits, 5 material-balance equalities).

$$
\boxed{\begin{aligned}
\min\quad Z={}&10\sum_{i=1}^{5}x_i+15\sum_{i=1}^{5}y_i+2\sum_{i=1}^{4}s_i\\
\mathrm{s.t.}\quad &0\le x_i\le2000 &&i=1,\ldots,5\\
&0\le y_i\le600 &&i=1,\ldots,5\\
&x_i+y_i+s_{i-1}-s_i=d_i &&i=1,\ldots,5\\
&s_i\ge0 &&i=1,\ldots,4,\\
&s_0=s_5=0.
\end{aligned}}
$$

In particular, the month-by-month material balances are:

$$
\begin{aligned}
x_1+y_1-s_1&=1200,\\
x_2+y_2+s_1-s_2&=2100,\\
x_3+y_3+s_2-s_3&=2400,\\
x_4+y_4+s_3-s_4&=3000,\\
x_5+y_5+s_4&=4000.
\end{aligned}
$$

**Inventory sign convention:** Incoming stock $s_{i-1}$ helps meet this month's demand; outgoing stock $s_i$ is what remains for the next month and is therefore subtracted. Holding cost is incurred only for $s_1,\ldots,s_4$, not for a fictitious $s_5$.

## Optimal production schedule

| Month | Regular $x_i$ | Overtime $y_i$ | Demand $d_i$ | End stock $s_i$ |
| --- | ---: | ---: | ---: | ---: |
| 1 | 2,000 | 300 | 1,200 | 1,100 |
| 2 | 2,000 | 600 | 2,100 | 1,600 |
| 3 | 2,000 | 600 | 2,400 | 1,800 |
| 4 | 2,000 | 600 | 3,000 | 1,400 |
| 5 | 2,000 | 600 | 4,000 | 0 |
| **Total** | **10,000** | **2,700** | **12,700** | — |

For example, month 2 has $2000+600+1100-1600=2100$ and month 5 has $2000+600+1400=4000$. All bounds hold. The monthly material balances verify feasibility independently of the solver.

The total objective cost is

$$
\begin{aligned}
Z&=10(10000)+15(2700)+2(1100+1600+1800+1400)\\
 &=100000+40500+11800=\boxed{152300\text{ toman}}.
\end{aligned}
$$

## Paper-and-pencil global optimality proof

Let $p_i=15+2(i-1)$, so $p=(15,17,19,21,23)$. Multiply each of the five material-balance equalities by the corresponding $p_i$ and add them. Inventory terms telescope:

$$
\sum_{i=1}^5p_id_i=\sum_{i=1}^5p_i(x_i+y_i)+2\sum_{i=1}^4s_i.
$$

Subtract this identity from the objective formula:

$$
Z=\sum_{i=1}^5p_id_i+\sum_{i=1}^5(10-p_i)x_i+\sum_{i=1}^5(15-p_i)y_i.
$$

Every $10-p_i$ is negative; because $x_i\le2000$, one has $(10-p_i)x_i\ge(10-p_i)2000$. For months 2–5, $15-p_i<0$; because $y_i\le600$, one has $(15-p_i)y_i\ge(15-p_i)600$. For month 1, $15-p_1=0$. Therefore **every feasible plan** satisfies

$$
\begin{aligned}
Z&\ge\sum_{i=1}^5p_id_i+\sum_{i=1}^5(10-p_i)2000
 +\sum_{i=2}^5(15-p_i)600\\
 &=254300-90000-12000=\boxed{152300}.
\end{aligned}
$$

The displayed feasible schedule attains this exact lower bound, proving **global optimality without relying on SciPy**. Because all five regular capacities and overtime capacities in months 2–5 must bind for equality, the schedule is also **unique** (balances fix $y_1$ and the four inventories).

## Exam checkpoints

- Write $s_0=s_5=0$ explicitly; there are **14**, not 15, independent decision variables.
- Monthly balances are **equalities**, not supply inequalities.
- Holding cost is paid on the **four month-end stocks**, not on all five months.
- A feasible five-month schedule must satisfy **each** month's demand on time.
- Distinguish the **lecture model** from our computed optimum and proof; the note does not solve the LP numerically.
