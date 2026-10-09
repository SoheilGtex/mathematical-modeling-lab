# Numerical Transportation — Full Written Solution

> **Source:** Session 03, handwritten pages 1–2. The cost table, supplies and demands below **are given in the lecture note**. The optimal shipping plan and proof are independent calculations. The note explicitly states shipping costs are **in toman**.

## Problem statement

Three origins (Tabriz, Yazd, Kerman) ship products to four destinations (Tehran, Mashhad, Isfahan, Shiraz). Each origin has limited stock and each destination has a required quantity. Choose nonnegative shipments to meet every requirement at minimum cost.

| Origin / destination | Tehran | Mashhad | Isfahan | Shiraz | Supply |
| --- | ---: | ---: | ---: | ---: | ---: |
| Tabriz ($i=1$) | 80 | 5 | 12 | 15 | 150 |
| Yazd ($i=2$) | 1 | 9 | 4 | 5 | 300 |
| Kerman ($i=3$) | 12 | 8 | 6 | 4 | 200 |
| **Demand** | **150** | **200** | **100** | **200** | **650** |

Destination indices are $j=1$ for Tehran, $2$ for Mashhad, $3$ for Isfahan, and $4$ for Shiraz. The cost **80** at Tabriz–Tehran is transcribed directly from the handwritten table (not an assumed value of 8).

## Variables and model

Define $x_{ij}\ge0$ as units shipped from origin $i$ to destination $j$, with $c_{ij}$ denoting the corresponding cost per unit. There are $3\times4=12$ decision variables.

$$
\boxed{\begin{aligned}
\min\quad &Z=\sum_{i=1}^{3}\sum_{j=1}^{4}c_{ij}x_{ij}\\
\mathrm{s.t.}\quad&\sum_{j=1}^{4}x_{ij}\le a_i &&i=1,2,3\\
&\sum_{i=1}^{3}x_{ij}\ge b_j &&j=1,2,3,4\\
&x_{ij}\ge0 &&\forall i,j.
\end{aligned}}
$$

The handwritten note writes the destination conditions as **$\ge$** (at least the required demand), unlike the exact-equality model used in Session 02. In this particular example, total supply equals total demand, so **every feasible solution must satisfy both sets of constraints with equality**:

$$\sum_i a_i=150+300+200=650=150+200+100+200=\sum_j b_j.$$

Indeed, $\sum_{ij}x_{ij}\le650$ from supply and $\sum_{ij}x_{ij}\ge650$ from demand. Consequently, all origin supplies and all destination requirements are saturated. Thus the $\ge$ model and its equality version have the same feasible set **for these numbers only**.

The expanded objective, in the origin–destination order above, is

$$
\begin{aligned}
Z={}&80x_{11}+5x_{12}+12x_{13}+15x_{14}\\
 &+x_{21}+9x_{22}+4x_{23}+5x_{24}\\
 &+12x_{31}+8x_{32}+6x_{33}+4x_{34}.
\end{aligned}
$$

## Optimal shipping plan

| Origin / destination | Tehran | Mashhad | Isfahan | Shiraz | Shipped |
| --- | ---: | ---: | ---: | ---: | ---: |
| Tabriz | 0 | 150 | 0 | 0 | 150 |
| Yazd | 150 | 50 | 100 | 0 | 300 |
| Kerman | 0 | 0 | 0 | 200 | 200 |
| **Received** | **150** | **200** | **100** | **200** | **650** |

The row sums equal supplies and column sums equal demands. The cost is

$$
\boxed{Z=150(5)+150(1)+50(9)+100(4)+200(4)=2550.}
$$

## Paper-and-pencil global optimality proof

A feasible shipping plan alone does not establish optimality. For a balanced transportation LP, choose origin potentials $u_i$ and destination potentials $v_j$ satisfying $u_i+v_j\le c_{ij}$. Then every feasible plan obeys

$$
\sum_{ij}c_{ij}x_{ij}\ge\sum_i u_i a_i+\sum_j v_j b_j.
$$

Take

$$\boxed{(u_1,u_2,u_3)=(0,4,3),\qquad(v_1,v_2,v_3,v_4)=(-3,5,0,1).}$$

The twelve potential sums are

$$
(u_i+v_j)=\begin{pmatrix}-3&5&0&1\\1&9&4&5\\0&8&3&4\end{pmatrix}
\le\begin{pmatrix}80&5&12&15\\1&9&4&5\\12&8&6&4\end{pmatrix}=(c_{ij}).
$$

Hence, for any feasible plan,

$$
Z\ge150(0)+300(4)+200(3)+150(-3)+200(5)+100(0)+200(1)=\boxed{2550}.
$$

Our feasible plan costs exactly 2550, so it is a **global minimum**. This certificate can be checked without running Python.

## Exam checkpoints

1. Explain the meaning of $x_{ij}$ and the units of every parameter.
2. Keep the source's $\ge$ demand constraints; justify why they are equalities in this balanced example.
3. Check the four destination totals and three origin totals.
4. Calculate the total cost, and prove it cannot be improved using the potential certificate.
5. **Do not confuse** this numerical Session 03 instance with the independently invented 2×2 demonstration in Session 02.
