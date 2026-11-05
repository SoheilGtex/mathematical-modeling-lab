# Exact maximum of two triangular fuzzy numbers

The first page of the new scan repeats the example from Session 07. We use it to make **the distinction between a maximum of fuzzy quantities and a maximum of membership grades** completely explicit.

## 1. Source definitions and data

For $M=(0,2,5)$ and $N=(2,3,4)$ (left endpoint, mode, right endpoint), their membership functions are

$$\mu_M(x)=\begin{cases}x/2&0\le x\le2,\\(5-x)/3&2<x\le5,\\0&\text{elsewhere},\end{cases}$$

$$\mu_N(y)=\begin{cases}y-2&2\le y\le3,\\4-y&3<y\le4,\\0&\text{elsewhere}.\end{cases}$$

Zadeh's extension principle defines $D=\widetilde{\max}(M,N)$ as

$$\boxed{\mu_D(z)=\sup_{\max(x,y)=z}\min\{\mu_M(x),\mu_N(y)\}.}$$

Here $\max(x,y)=z$ requires $x\le z$, $y\le z$, and $x=z$ or $y=z$. Taking $\max(\mu_M(z),\mu_N(z))$ would define a **different** operation.

## 2. Derive the level intervals

For $\alpha\in[0,1]$ (at $\alpha=0$, use the closure of the support),

$$[M]_\alpha=[2\alpha,5-3\alpha],\qquad[N]_\alpha=[2+\alpha,4-\alpha].$$

The image of the rectangle $[M]_\alpha\times[N]_\alpha$ under the continuous function $(x,y)\mapsto\max(x,y)$ is the interval

$$\boxed{[D]_\alpha=[2+\alpha,\max(5-3\alpha,4-\alpha)].}$$

The descending endpoints switch when $5-3\alpha=4-\alpha$, so $\alpha=1/2$. This gives

$$[D]_\alpha=\begin{cases}[2+\alpha,5-3\alpha],&0\le\alpha\le1/2,\\{}[2+\alpha,4-\alpha],&1/2\le\alpha\le1.\end{cases}$$

## 3. Invert the intervals to get membership

The left boundary is $z=2+\alpha$, hence $\alpha=z-2$ for $2\le z\le3$. On the right, the active line changes at

$$z=5-3(1/2)=4-(1/2)=\boxed{3.5}.$$

Thus

$$\boxed{\mu_D(z)=\begin{cases}
0,&z\le2,\\
z-2,&2<z\le3,\\
4-z,&3<z\le7/2,\\
(5-z)/3,&7/2<z<5,\\
0,&z\ge5.
\end{cases}}$$

Check $\mu_D(3)=1$, $\mu_D(3.5)=1/2$, $\mu_D(4)=1/3$ and $\mu_D(5)=0$. Note that $\mu_D(2.5)=1/2$ while $\max\{\mu_M(2.5),\mu_N(2.5)\}=5/6$.

This result reproduces the source's case-by-case answer. For other inputs, **recompute the alpha-cut endpoints** rather than reusing these numerical breakpoints.
