# Television Production — Full Written Solution

> **Confirmed correction:** Monthly labor capacity is **60,000 person-hours**, as clarified by the student after ambiguous handwriting. Numerical solutions, optimality proofs and the integer variant are independent additions; the lecture note gives the model.

## Problem statement

A manufacturer produces color and black-and-white television sets. The maximum monthly sales are **2,000 color sets** and **4,000 black-and-white sets**. One color TV uses **20 person-hours** of labor, and one black-and-white TV uses **15 person-hours**. A total of **60,000 person-hours** is available each month. Profit per set is **$60** for color and **$30** for black-and-white. Formulate a model to maximize monthly profit, then solve it.

## Step 1 — Decision variables and assumptions

- $x_1$: color televisions produced and sold in one month.
- $x_2$: black-and-white televisions produced and sold in one month.

Assume all produced sets are sold (up to the stated sales limits), and unit labor and unit profit remain constant. The photographed formulation only specifies $x_1,x_2\ge0$; **integrality is a separate modeling extension**.

## Step 2 — Objective function

$$\boxed{\max Z=60x_1+30x_2 \quad\text{(dollars/month)}}$$

## Step 3 — Constraints and mathematical model

Labor, sales, and nonnegativity give:

$$
\boxed{\begin{aligned}
\max\quad&Z=60x_1+30x_2\\
\text{s.t.}\quad&20x_1+15x_2\le60\,000\\
&x_1\le2000\\
&x_2\le4000\\
&x_1,x_2\ge0.
\end{aligned}}
$$

## Step 4 — Hand calculation and rigorous optimality proof

Profit per labor-hour is $60/20=3$ for color TVs and $30/15=2$ for black-and-white TVs. This suggests prioritizing color production, but a proof is required.

For every feasible $(x_1,x_2)$:

$$
\begin{aligned}
Z&=60x_1+30x_2\\
 &=2(20x_1+15x_2)+20x_1\\
 &\le 2(60\,000)+20(2000)\\
 &=160\,000.
\end{aligned}
$$

To achieve equality, choose $x_1=2000$ and use all available labor:

$$
20(2000)+15x_2=60\,000
\quad\Longrightarrow\quad
x_2=\frac{20\,000}{15}=\frac{4000}{3}.
$$

Feasibility check:

$$
20(2000)+15\left(\frac{4000}{3}\right)=60\,000,
\qquad 0\le2000\le2000,
\qquad 0\le\frac{4000}{3}\le4000.
$$

The feasible point reaches the global upper bound, so it is globally optimal:

$$\boxed{x_1^*=2000,\quad x_2^*=\frac{4000}{3}\approx1333.333,\quad Z_{\max}=\$160\,000.}$$

**Binding constraints:** labor capacity and the color sales ceiling. The black-and-white sales ceiling has slack $4000-4000/3=8000/3$ units. Equality in the upper bound requires $x_1=2000$ and full use of labor, so the LP optimum is unique.

## Step 5 — Optional integer extension (not specified in the photographed formulation)

If sets must be indivisible, require $x_1,x_2\in\mathbb Z_{\ge0}$. A feasible choice is

$$x_1=2000,\qquad x_2=1333.$$

It uses $20(2000)+15(1333)=59\,995$ person-hours and yields

$$Z=60(2000)+30(1333)=\$159\,990.$$

**Global integer optimality proof:** For integer $x_1,x_2$, $Z=30(2x_1+x_2)$ is a multiple of $30$. The continuous relaxation proves $Z\le160\,000$, so every integer solution has

$$Z\le 30\left\lfloor\frac{160\,000}{30}\right\rfloor=159\,990.$$

Our feasible integer solution reaches this upper bound:

$$\boxed{(x_1,x_2)=(2000,1333),\quad Z_{\max}^{\mathrm{integer}}=\$159\,990.}$$

## Common exam mistakes

- Mixing up $20$ and $15$ person-hours, or $60$ and $30$ dollars.
- Writing $\ge$ for maximum sales/labor capacities.
- Omitting units or nonnegativity restrictions.
- Treating integer requirements as explicitly written in the original note.
- Giving a feasible point without proving that it attains an upper bound.
