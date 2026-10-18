# Assignment 03 — Triangular fuzzy numbers and their maximum

> **Due date in the handout:** Sunday, October 25, 2026.

> **Source:** One-page submitted course assignment on triangular fuzzy numbers. The data and tasks below are paraphrased from the handout. All derivations, exact breakpoint computation, verification code and figures are independent worked additions. The original PDF is not redistributed.

The handout asks for (1) **piecewise membership functions** of two triangular fuzzy numbers and their graphs on the same coordinate axes, and (2) the **membership function of their maximum** using Zadeh's extension principle, including a justification for the supremum, the intervals and breakpoint(s), and the final graph.

$$\widetilde A=(1,3,7),\qquad \widetilde B=(3,5,6).$$

## 1. Triangular memberships

For a triangular fuzzy number $T=(a,b,c)$, with $a<b<c$:

$$
\mu_T(z)=\begin{cases}
0 & z\le a,\\
\dfrac{z-a}{b-a} & a<z\le b,\\
\dfrac{c-z}{c-b} & b<z<c,\\
0 & z\ge c.
\end{cases}
$$

Substituting the data, the **first answer** is

$$
\boxed{\mu_{\widetilde A}(z)=\begin{cases}
0 & z\le1,\\
\dfrac{z-1}{2} & 1<z\le3,\\
\dfrac{7-z}{4} & 3<z<7,\\
0 & z\ge7,
\end{cases}}
$$

$$
\boxed{\mu_{\widetilde B}(z)=\begin{cases}
0 & z\le3,\\
\dfrac{z-3}{2} & 3<z\le5,\\
6-z & 5<z<6,\\
0 & z\ge6.
\end{cases}}
$$

The vertices are $A:(1,0),(3,1),(7,0)$ and $B:(3,0),(5,1),(6,0)$. Between the vertices, each graph is linear.

![Both triangular fuzzy membership functions on the same axes](../assets/assignment03_fuzzy_A_B.png)

## 2. Constraint in Zadeh's extension principle

The exercise defines $Z=\max(X,Y)$ using the **minimum t-norm**:

$$
\boxed{\mu_Z(z)=\sup_{x,y\in\mathbb R\, :\,\max(x,y)=z}
\min\bigl(\mu_{\widetilde A}(x),\mu_{\widetilde B}(y)\bigr).}
$$

The equality $\max(x,y)=z$ means **both $x\le z$ and $y\le z$, with at least one of them equal to $z$**. Equivalently:

$$\{(x,y):\max(x,y)=z\}=
\{(z,y):y\le z\}\cup\{(x,z):x\le z\}.$$

This is a **maximum of uncertain fuzzy quantities**, not the pointwise maximum of their membership functions. In particular, $\mu_Z(z)\ne\max(\mu_{\widetilde A}(z),\mu_{\widetilde B}(z))$ in general; for example at $z=3$, the latter is $1$, but $\mu_Z(3)=0$.

## 3. Evaluate the supremum rigorously

Define the best attainable membership **at or below $z$**:

$$M_A(z)=\sup_{x\le z}\mu_{\widetilde A}(x),\qquad
M_B(z)=\sup_{y\le z}\mu_{\widetilde B}(y).$$

For triangular numbers, these can be evaluated exactly:

$$M_A(z)=\begin{cases}0&z<1,\\(z-1)/2&1\le z<3,\\1&z\ge3,\end{cases}
\quad M_B(z)=\begin{cases}0&z<3,\\(z-3)/2&3\le z<5,\\1&z\ge5.\end{cases}$$

Because the supremum over the union of the two sets above is the larger of their individual suprema, and the membership functions are nonnegative,

$$
\boxed{\mu_Z(z)=\max\left\{
\min\bigl(\mu_A(z),M_B(z)\bigr),
\min\bigl(\mu_B(z),M_A(z)\bigr)
\right\}.}
$$

Here the suprema are **attained** whenever positive, because each triangle is continuous with compact support; the zero case is immediate. This identity now resolves the originally two-variable optimization exactly.

## 4. Evaluate the relevant intervals

**For $z<3$:** It is impossible for both inputs to have positive membership while $\max(x,y)=z$, because every point with positive $\mu_B(y)$ has $y>3$. Thus $\mu_Z(z)=0$.

**For $3\le z\le5$:** $M_A(z)=1$ (take $x=3$); consequently the branch $y=z$ gives $\mu_B(z)=(z-3)/2$. The competing $x=z$ branch cannot exceed that value because $M_B(z)=\mu_B(z)$. Therefore:

$$\boxed{\mu_Z(z)=\frac{z-3}{2}\quad (3\le z\le5).}$$

**For $5<z<6$:** Both prefix suprema equal one ($M_A=M_B=1$), so the choice is between

$$\mu_A(z)=\frac{7-z}{4},\qquad \mu_B(z)=6-z.$$

They are equal at

$$\frac{7-z}{4}=6-z\quad\Longleftrightarrow\quad 7-z=24-4z
\quad\Longleftrightarrow\quad\boxed{z=\frac{17}{3}}.$$

For $5<z<17/3$, $6-z$ is larger; for $17/3<z<6$, $(7-z)/4$ is larger.

**For $6\le z\le7$:** $\mu_B(z)=0$, and $\mu_A(z)=(7-z)/4$, so that is the maximum. For $z>7$ both terms vanish.

## 5. Final piecewise membership and plot

Combining all intervals gives the **second answer**:

$$
\boxed{\mu_{\max(\widetilde A,\widetilde B)}(z)=
\begin{cases}
0 & z<3,\\
\dfrac{z-3}{2} & 3\le z\le5,\\
6-z & 5<z\le\dfrac{17}{3},\\
\dfrac{7-z}{4} & \dfrac{17}{3}<z\le7,\\
0 & z>7.
\end{cases}}
$$

The key graph points are $(3,0)$, $(5,1)$, $(17/3,1/3)$ and $(7,0)$. Note the output remains **normal** ($\mu_Z(5)=1$), has support from $3$ to $7$, and is **not triangular**: its falling side changes slope at $17/3$.

![Membership function of max(A,B), with its exact breakpoint](../assets/assignment03_fuzzy_max.png)

## 6. Independent verification using alpha-cuts

For $0\le\alpha\le1$, the two $\alpha$-cuts are

$$\widetilde A_\alpha=[1+2\alpha,7-4\alpha],\qquad
\widetilde B_\alpha=[3+2\alpha,6-\alpha].$$

By monotonicity of $\max$ and the extension principle,

$$
Z_\alpha=[\max(1+2\alpha,3+2\alpha),\max(7-4\alpha,6-\alpha)]
=[3+2\alpha,\max(7-4\alpha,6-\alpha)].
$$

The upper endpoints change order exactly when

$$7-4\alpha=6-\alpha\quad\Longleftrightarrow\quad\alpha=\frac13,$$

which corresponds to $z=7-4/3=17/3$. This independently reproduces the piecewise function and confirms that the breakpoint is genuine.

## 7. Optional Python computation

Run the [reproducible Python example](https://github.com/SoheilGtex/mathematical-modeling-lab/blob/main/examples/assignments/03_fuzzy_numbers_max.py) from the project root:

```bash
python examples/assignments/03_fuzzy_numbers_max.py
python -m pytest -q tests/test_assignment_03.py
```

The script checks the exact extension-principle formula against the piecewise expression at representative points, prints the alpha-cuts and recreates both charts in `plots/`. Python is an optional check; the analytical argument above is a complete paper-and-pencil solution.
