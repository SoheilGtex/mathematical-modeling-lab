### Three products on four machines

In the [full machine-allocation problem](session-04/machines.md), $x_{ij}\ge0$ is the **number of units of product $i$ made on machine $j$**, for $i=1,2,3$ and $j=1,2,3,4$.

Unit production costs (in USD), machine time (hours per unit), minimum product requirements and maximum machine hours come from the lecture:

$$
C=\begin{pmatrix}4&4&5&7\\6&7&5&6\\12&10&8&11\end{pmatrix},\quad
T=\begin{pmatrix}.30&.25&.20&.20\\.20&.30&.20&.25\\.80&.60&.60&.50\end{pmatrix},
$$

$$d=(3000,6000,4000),\qquad H=(1500,1200,1500,2000).$$

$$
\boxed{\begin{aligned}
\min\ &Z=\sum_{i=1}^3\sum_{j=1}^4 c_{ij}x_{ij}\\
\mathrm{s.t.}\ &\sum_{i=1}^3t_{ij}x_{ij}\le H_j &&j=1,\ldots,4\\
&\sum_{j=1}^4x_{ij}\ge d_i &&i=1,2,3\\
&x_{ij}\ge0 &&\forall i,j.
\end{aligned}}
$$

**Remember:** four $\le$ hour limits and three $\ge$ production minimums; there are **12** nonnegative decision variables. Costs are USD, not toman.

### Light/heavy crude oil procurement

In the [full crude-oil example](session-04/crude.md), let $x_1,x_2\ge0$ be the **amounts of light/heavy raw crude purchased** (before processing losses). Prices are $20 and $15 per unit; recovery is $95\%$ and $92\%$. The products are **diesel, kerosene and jet fuel**, and the output requirements are $1{,}000{,}000$, $500{,}000$, $300{,}000$:

$$
\boxed{\begin{aligned}
\min\quad&Z=20x_1+15x_2\\
\mathrm{s.t.}\quad&0.40(0.95)x_1+0.32(0.92)x_2\ge1{,}000{,}000\\
&0.20(0.95)x_1+0.40(0.92)x_2\ge500{,}000\\
&0.35(0.95)x_1+0.20(0.92)x_2\ge300{,}000\\
&x_1,x_2\ge0.
\end{aligned}}
$$

Apply the recovery factor **before** each product's yield; all requirements are lower bounds ($\ge$).

### Maximum revenue-to-cost ratio (fractional objective)

In the [full fractional model](session-04/ratio.md), $x_1,x_2\ge0$ denote quantities of products $A,B$. Sale prices $(80,40)$, variable costs $(40,20)$ and fixed cost $200$ are measured in **thousand toman**. Products use $(2,3)$ hours and $(3,2)$ kg of raw materials per unit, respectively.

$$
\boxed{\begin{aligned}
\max\quad&Z=\frac{80x_1+40x_2}{40x_1+20x_2+200}\\
\mathrm{s.t.}\quad&2x_1+3x_2\le120\\
&3x_1+2x_2\le150\\
&x_1,x_2\ge0.
\end{aligned}}
$$

**Do not replace the ratio with profit.** This is a **linear-fractional**, not an ordinary linear, objective. The denominator is positive because fixed cost is $200>0$.
