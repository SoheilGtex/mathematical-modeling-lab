### Linear-fractional objective and Charnes–Cooper model

The [fractional-programming lecture example](session-05/fractional.md) is

$$\boxed{\begin{aligned}
\max\quad &\frac{10x_1+20x_2+10}{3x_1+4x_2+20}\\
\mathrm{s.t.}\quad &x_1+3x_2\le50,\\
&3x_1+2x_2\le80,\\
&x_1,x_2\ge0.
\end{aligned}}$$

The denominator is **strictly positive** ($\ge20$). Let $t=1/(3x_1+4x_2+20)$ and $y_i=tx_i$ ($x_i=y_i/t$). Multiply **both** resource constraints by $t$ and normalize the denominator:

$$\boxed{\begin{aligned}
\max\quad&10y_1+20y_2+10t\\
\mathrm{s.t.}\quad&y_1+3y_2\le50t,\\
&3y_1+2y_2\le80t,\\
&3y_1+4y_2+20t=1,\\
&y_1,y_2,t\ge0.
\end{aligned}}$$

**Remember:** in general $t>0$ is needed to invert the transformation; for this model, $t=0$ is impossible because the first scaled constraint and $y\ge0$ contradict the normalizing equality. Do not drop the constant $10$ in the numerator or $20$ in the denominator.

### Triangular fuzzy membership as a mathematical model

From the [fuzzy-number lecture](session-05/fuzzy.md), a crisp characteristic function has values only $0$ or $1$, while fuzzy membership satisfies $\mu_{\widetilde A}(x)\in[0,1]$. For the triangular fuzzy number $\widetilde M=(1,5,7)$:

$$\boxed{\mu_{\widetilde M}(x)=\begin{cases}
0,&x\le1,\\
(x-1)/4,&1<x\le5,\\
(7-x)/2,&5<x<7,\\
0,&x\ge7.
\end{cases}}$$

**Modeling point:** derive the two straight-line equations from $(1,0)$, $(5,1)$ and $(7,0)$. This is a **membership-function model**, not a fuzzy optimization problem; no numerical optimizer is included in the exam review.
