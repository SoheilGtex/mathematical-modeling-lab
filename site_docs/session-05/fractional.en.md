# Linear-Fractional Programming — Charnes–Cooper

> **Lecture source:** Session 05 handwritten pages 1–3. The general transformation and the example data appear in the lecture. The completed transformed model, numerical optimum and proof are independent educational calculations.

## 1. Why the fractional objective is not an LP

For $x\in\mathbb R^n$, a **linear-fractional program** has an objective of the form

$$\max\ f(x)=\frac{c^\top x+c_0}{d^\top x+d_0}$$

with a feasible domain $Ax\le b$, $x\ge0$, and **$d^\top x+d_0>0$ everywhere on that domain**. Both numerator and denominator are affine; the *ratio* is not generally linear. The positivity condition is essential; if the denominator can be zero or change sign, the transformation below cannot simply be applied to the entire feasible set.

## 2. Charnes–Cooper substitution

Introduce a scalar $t$ and a vector $y$:

$$t=\frac1{d^\top x+d_0},\qquad y=tx=\frac{x}{d^\top x+d_0}.$$

Because the denominator is positive, $t>0$ and $x=y/t$. Multiplication by $t$ produces the **linear equality**

$$\boxed{d^\top y+d_0t=1}.$$

Each original row $a_i^\top x\le b_i$ becomes $a_i^\top y\le b_it$. The transformed linear program is

$$\boxed{\begin{aligned}
\max_{y,t}\quad &c^\top y+c_0t\\
\mathrm{s.t.}\quad &Ay\le bt,\\
&d^\top y+d_0t=1,\\
&y\ge0,\quad t>0.
\end{aligned}}$$

The strict inequality $t>0$ follows from the substitution. In applications an LP solver typically uses $t\ge0$; **equivalence then also requires excluding or proving impossible solutions with $t=0$**. This proof is supplied for the bounded numerical example below.

## 3. Example transcribed from the lecture

The lecture gives

$$\boxed{\begin{aligned}
\max\quad &\frac{10x_1+20x_2+10}{3x_1+4x_2+20}\\
\mathrm{s.t.}\quad &x_1+3x_2\le50,\\
&3x_1+2x_2\le80,\\
&x_1,x_2\ge0.
\end{aligned}}$$

The denominator is at least $20$ for $x_1,x_2\ge0$, so it is positive. Set

$$t=\frac1{3x_1+4x_2+20},\qquad y_i=tx_i\quad(i=1,2).$$

**Step-by-step transformation:**

$$x_1+3x_2\le50\quad\Longleftrightarrow\quad y_1+3y_2\le50t,$$

$$3x_1+2x_2\le80\quad\Longleftrightarrow\quad3y_1+2y_2\le80t,$$

$$3x_1+4x_2+20=\frac1t\quad\Longleftrightarrow\quad3y_1+4y_2+20t=1.$$

Therefore the **complete equivalent LP** is

$$\boxed{\begin{aligned}
\max\quad &10y_1+20y_2+10t\\
\mathrm{s.t.}\quad&y_1+3y_2\le50t,\\
&3y_1+2y_2\le80t,\\
&3y_1+4y_2+20t=1,\\
&y_1,y_2,t\ge0.
\end{aligned}}$$

For this example the $t\ge0$ formulation is exact: if $t=0$, the first resource inequality and $y\ge0$ force $y_1=y_2=0$, contradicting the equality $3y_1+4y_2=1$. Hence **all** feasible transformed points have $t>0$.

## 4. Independent exact optimum (not supplied by the note)

A feasible plan is $x_1=0$, $x_2=50/3$. The first resource constraint is tight and the second is satisfied:

$$x_1+3x_2=50,\qquad3x_1+2x_2=\frac{100}{3}\le80.$$

The objective value is

$$\boxed{f^*=\frac{10+20(50/3)}{20+4(50/3)}=\frac{103}{26}\approx3.961538.}$$

Its transformed coordinates are

$$\boxed{y_1=0,\quad y_2=\frac5{26},\quad t=\frac3{260}.}$$

**Global certificate.** For every feasible nonnegative $x$,

$$f(x)\le\frac{103}{26}\ \Longleftrightarrow\ 108x_2-49x_1\le1800.$$

But $x_1+3x_2\le50$ implies $108x_2\le1800-36x_1$, hence

$$108x_2-49x_1\le1800-85x_1\le1800.$$

This proves the global optimum without depending on numerical solver output. The original note stops at explaining the transformation; **this optimum and certificate are supplemental**.

## 5. Modeling-only exam focus

Identify numerator and denominator, establish positivity, introduce $y=tx$ and $t=1/(d^\top x+d_0)$, write the normalizing equality and scale **every constraint** correctly. Recover $x=y/t$ when $t>0$. The numerical maximizer and certificate belong to the full notes, not the modeling-only exam review.
