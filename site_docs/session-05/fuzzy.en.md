# Fuzzy Sets and Triangular Fuzzy Numbers

> **Lecture source:** Session 05 handwritten pages 4–7. This is an introduction to **fuzzy membership**, not yet a fuzzy linear-programming or fuzzy-optimization example.

## 1. Crisp versus fuzzy membership

For an ordinary (*crisp*) set $B$, each element either belongs or does not belong. Its characteristic function takes only two values:

$$\mathbf1_B(x)=\begin{cases}1,&x\in B,\\0,&x\notin B.\end{cases}$$

For a **fuzzy set** $\widetilde A$ on a universe $X$, the membership function

$$\boxed{\mu_{\widetilde A}:X\longrightarrow[0,1]}$$

assigns to each $x$ a **degree of membership**. One representation is

$$\widetilde A=\{(x,\mu_{\widetilde A}(x)):x\in X\}.$$

A membership grade, such as $0.6$, is **not automatically a probability**: it describes the degree to which an element fits a concept, not the chance of a random event. Ordinary sets are the special case with grades $0$ or $1$ only.

## 2. Triangular fuzzy number in the lecture

The drawn triangle has points $(1,0)$, $(5,1)$ and $(7,0)$, so we write

$$\widetilde M=(a,b,c)=(1,5,7).$$

Its membership function is **piecewise linear**:

$$\boxed{\mu_{\widetilde M}(x)=\begin{cases}
0,&x\le1,\\
\dfrac{x-1}{4},&1<x\le5,\\
\dfrac{7-x}{2},&5<x<7,\\
0,&x\ge7.
\end{cases}}$$

The left segment rises from $(1,0)$ to $(5,1)$ with slope $1/4$; the right segment decreases from $(5,1)$ to $(7,0)$ with slope $-1/2$.


At the peak, $\mu_{\widetilde M}(5)=1$. The membership vanishes at and outside the endpoints; the positive-membership support is $(1,7)$ (its closure is $[1,7]$).

## 3. Worked membership calculations

The handwritten calculation evaluates $x=1.2$:

$$\mu_{\widetilde M}(1.2)=\frac{1.2-1}{4}=\boxed{0.05}.$$

For illustration, at $x=6$ the descending branch gives

$$\mu_{\widetilde M}(6)=\frac{7-6}{2}=\boxed{0.5}.$$

These are membership **grades**, not probabilities.

## 4. Exam/modeling focus

A fuzzy number is modeled by its membership function. Identify the three vertices $(a,0)$, $(b,1)$, $(c,0)$; derive the line equation on each interval; write $0$ outside the interval. Do not confuse this definition with the linear-fractional model from pages 1–3. The provided note does **not** contain a numerical fuzzy-optimization problem.
