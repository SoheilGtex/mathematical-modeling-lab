# Maximum Revenue-to-Cost Ratio — Full Written Solution

> **Source:** Session 04 handwritten page 4. Prices and costs are in **thousand toman**, resource use in hours and kilograms. The source explicitly asks to maximize **revenue / total cost**, not revenue minus cost. The proof and numerical answer below are independent calculations.

## 1. Problem statement and data

A small factory makes products $A$ and $B$. Decide how many units of each to produce to obtain the greatest ratio of sales revenue to production expense.

| Parameter (per unit) | A | B |
| --- | ---: | ---: |
| Selling price (thousand toman) | 80 | 40 |
| Variable production cost (thousand toman) | 40 | 20 |
| Production time (hours) | 2 | 3 |
| Raw material (kg) | 3 | 2 |

Available time is **120 hours**, material is **150 kg** and fixed operating expense is **200 thousand toman**.

## 2. Decision variables and complete model

Let $x_1\ge0$ be the quantity of $A$ and $x_2\ge0$ the quantity of $B$. Both variables are continuous in the note (no integer condition is stated). Revenue and cost are:

$$R=80x_1+40x_2,\qquad C=40x_1+20x_2+200.$$

The **linear-fractional program** is

$$
\boxed{\begin{aligned}
\max\quad&Z=\frac{80x_1+40x_2}{40x_1+20x_2+200}\\
\mathrm{s.t.}\quad&2x_1+3x_2\le120 &&\text{hours}\\
&3x_1+2x_2\le150 &&\text{kg material}\\
&x_1,x_2\ge0.
\end{aligned}}
$$

Because fixed expense $200>0$, the denominator is strictly positive on the feasible domain. **Do not replace this ratio with profit $R-C$**: the two objectives are conceptually different, even if they happen to share an optimizer for some specially structured numerical data.

## 3. Exact transformation for this instance

Observe that revenue is twice the **variable** cost: if $V=40x_1+20x_2$, then $R=2V$ and $C=V+200$. Hence

$$Z=\frac{2V}{V+200},\qquad\frac{dZ}{dV}=\frac{400}{(V+200)^2}>0.$$

Thus, **for this example only**, maximizing the fractional objective is equivalent to maximizing $V=40x_1+20x_2$ over the same feasible set. This is not a general rule for fractional programming.

## 4. Feasible optimum and global proof

For $x_2\ge0$,

$$V=40x_1+20x_2\le\frac{40}{3}(3x_1+2x_2)\le\frac{40}{3}(150)=2000.$$

The plan $x_1=50$, $x_2=0$ reaches $V=2000$: time used $2(50)=100\le120$, material used $3(50)=150$. Therefore it maximizes $V$ and hence the ratio. Its revenue is $4000$ thousand toman; its total cost is $2200$ thousand toman:

$$\boxed{x_1^*=50,\quad x_2^*=0,\quad Z_{\max}=\frac{4000}{2200}=\frac{20}{11}\approx1.81818.}$$

The objective is **dimensionless**, because both numerator and denominator use the same monetary unit.

## 5. Exam focus

Explain the distinction between $R$, $C$ and the ratio $R/C$; include the fixed cost **inside the denominator**. Write both resource constraints and nonnegativity. No numerical optimization or transformation is required in the modeling-only exam review.
