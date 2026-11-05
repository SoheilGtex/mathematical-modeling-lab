# Second fuzzy LP: four-parameter LR coefficients

**Lecture source: page 4 (top).** All ordered four-tuples below use the *same* LR meaning:

$$(a^L,a^U,\ell,r)_{LR}=(\text{left core},\text{right core},\text{left spread},\text{right spread}).$$

They are **not** conventional trapezoidal endpoints $(a,b,c,d)$; e.g. $(2,3,1,1)_{LR}$ has support $[1,4]$ and core $[2,3]$.

## 1. The model as written in the lecture

For two nonnegative decision variables, the fuzzy objective and ranked resource constraints are

$$\boxed{\begin{aligned}
\max\quad &\widetilde Z=(2,3,1,1)_{LR}x_1+(3,4,1,2)_{LR}x_2,\\
\mathrm{s.t.}\quad &(1,2,1,1)_{LR}x_1+(2,3,1,2)_{LR}x_2\le_R(5,6,2,2)_{LR},\\
&(2,3,1,3)_{LR}x_1+(1,2,1,1)_{LR}x_2\le_R(4,6,2,1)_{LR},\\
&x_1,x_2\ge0.
\end{aligned}}$$

The variables in the scan are not accompanied by physical units or a detailed business scenario; this page therefore leaves their units unspecified. The ordering sign $\le_R$ makes explicit the ranking notion introduced in Session 06.

## 2. Rank every coefficient

Use the lecture formula

$$R(a^L,a^U,\ell,r)=\frac{a^L+a^U}2+\frac{r-\ell}4.$$

The ranks are:

| Coefficient | Original LR tuple | Rank |
|---|---|---:|
| $x_1$ objective | $(2,3,1,1)$ | $2.5$ |
| $x_2$ objective | $(3,4,1,2)$ | $3.75$ |
| Resource 1, $x_1$ | $(1,2,1,1)$ | $1.5$ |
| Resource 1, $x_2$ | $(2,3,1,2)$ | $2.75$ |
| Resource 1 capacity | $(5,6,2,2)$ | $5.5$ |
| Resource 2, $x_1$ | $(2,3,1,3)$ | $3$ |
| Resource 2, $x_2$ | $(1,2,1,1)$ | $1.5$ |
| Resource 2 capacity | $(4,6,2,1)$ | $4.75$ |

## 3. Deterministic ranked LP (additional derivation)

Since $x_1,x_2\ge0$ and $R$ is additive and positively homogeneous, the ranked counterpart is

$$\boxed{\begin{aligned}
\max\quad &2.5x_1+3.75x_2,\\
\mathrm{s.t.}\quad &1.5x_1+2.75x_2\le5.5,\\
&3x_1+1.5x_2\le4.75,\\
&x_1,x_2\ge0.
\end{aligned}}$$

The independently computed optimal solution is

$$x_1^*=\frac{77}{96}\approx0.8020833333,\qquad
x_2^*=\frac{25}{16}=1.5625,\qquad
R(\widetilde Z^*)=\frac{755}{96}\approx7.8645833333.$$

Substitution gives $1.5x_1+2.75x_2=5.5$ and $3x_1+1.5x_2=4.75$. Both resource constraints bind. The numerical optimum was **not supplied** by the handwritten source.

**Interpretation:** solving this crisp LP only proves optimality under the ranking-defined $\le_R$; it does not impose interval-wise or robust feasibility.
