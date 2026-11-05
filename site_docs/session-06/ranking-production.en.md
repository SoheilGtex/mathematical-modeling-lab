# Ranking fuzzy numbers and the two-product model

**Lecture source: pages 2–3.** The lecture defines an order through a ranking function and formulates a production problem with triangular uncertain profits, resource coefficients, and capacities.

## 1. The lecture's ranking order

For an LR trapezoid $\widetilde A=(a^L,a^U,\ell,r)_{LR}$ the given ranking is

$$\boxed{R(\widetilde A)=\frac{a^L+a^U}{2}+\frac{r-\ell}{4}.}$$

Equivalently, $R=c_La^L+c_Ua^U+c_\ell\ell+c_rr$ with $c_L=c_U=1/2$, $c_\ell=-1/4$, $c_r=1/4$.

**Derivation (additional explanation):** at level $\lambda$ the cut midpoint is

$$m_\lambda=\frac{a^L+a^U}{2}+\frac{(1-\lambda)(r-\ell)}2.$$

Integrating over $\lambda\in[0,1]$ gives the boxed formula. For a triangle $\widetilde T=(a,b,c)$,

$$R(\widetilde T)=\frac{a+2b+c}{4}.$$

Define the *ranking-based* relations

$$\widetilde A\le_R\widetilde B\iff R(\widetilde A)\le R(\widetilde B),\qquad
\widetilde A=_R\widetilde B\iff R(\widetilde A)=R(\widetilde B).$$

Two different fuzzy numbers can tie under $R$; this is not equality of membership functions. This ranking is **one chosen modeling convention**, not a universal fuzzy order. In particular, rank-based feasibility is not equivalent to satisfying every alpha-cut constraint.

## 2. Source data and units

A plant produces products A and B. Let $x_1,x_2\ge0$ be their production quantities. The lecture specifies the following **triangular fuzzy coefficients** in the $(\text{left},\text{mode},\text{right})$ convention:

| Quantity | Product A | Product B | Available |
|---|---|---|---|
| Profit per unit | $(35,40,45)$ | $(45,50,55)$ | — |
| Machine time per unit, hours | $(1.5,2,2.5)$ | $(0.75,1,1.2)$ | $(98,100,102)$ |
| Raw material per unit, kg | $(0.25,1,1.5)$ | $(2,2.2,2.5)$ | $(78,80,82)$ |

The notes do not state a currency unit for profit; none is invented here. The fuzzy coefficients should not be interpreted as probability distributions.

## 3. The fuzzy mathematical model (lecture)

$$\boxed{\begin{aligned}
\max\quad &\widetilde Z=(35,40,45)x_1+(45,50,55)x_2,\\
\mathrm{s.t.}\quad &(1.5,2,2.5)x_1+(0.75,1,1.2)x_2\le_R(98,100,102),\\
&(0.25,1,1.5)x_1+(2,2.2,2.5)x_2\le_R(78,80,82),\\
&x_1,x_2\ge0.
\end{aligned}}$$

Here the triangular triples denote fuzzy numbers, the arithmetic is fuzzy addition/scaling, and $\le_R$ is the course-specific ranking comparison. Explicitly stating $\le_R$ eliminates the ambiguity of writing an ordinary $\le$ between fuzzy quantities.

## 4. Ranked linear-programming counterpart (independent derivation)

Applying $R(a,b,c)=(a+2b+c)/4$ and using its additivity and positive homogeneity yields the *crisp* LP:

$$\boxed{\begin{aligned}
\max\quad &40x_1+50x_2,\\
\mathrm{s.t.}\quad &2x_1+0.9875x_2\le100,\\
&0.9375x_1+2.225x_2\le80,\\
&x_1,x_2\ge0.
\end{aligned}}$$

Examples: $R(0.75,1,1.2)=0.9875$ and $R(0.25,1,1.5)=0.9375$. Both resource constraints bind at the ranked optimum (computed separately from the lecture):

$$x_1^*\approx40.71824429,\qquad x_2^*\approx18.79849257,\qquad R(\widetilde Z^*)\approx2568.65440035.$$

This numerical optimum is **not in the handwritten pages**. It solves this *ranking-based* LP only; switching to possibility, necessity, componentwise-cut, or robust constraints would define a different problem.
