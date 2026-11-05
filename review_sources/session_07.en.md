### LR fuzzy LP, extension-principle maximum and Kerre comparison

- Interpret $(a^L,a^U,\ell,r)_{LR}$ as **core and spreads**, not as four trapezoid vertices.
- Formulate the [page 4 fuzzy LP](session-07/lr-model.md) with $x_1,x_2\ge0$ and an explicitly specified ranking-based order:

$$\begin{aligned}
\max\ \widetilde Z&=(2,3,1,1)_{LR}x_1+(3,4,1,2)_{LR}x_2,\\
(1,2,1,1)_{LR}x_1+(2,3,1,2)_{LR}x_2&\le_R(5,6,2,2)_{LR},\\
(2,3,1,3)_{LR}x_1+(1,2,1,1)_{LR}x_2&\le_R(4,6,2,1)_{LR}.
\end{aligned}$$

- For [the extension principle](session-07/extension-max.md), model $D=\max(M,N)$ by $\mu_D(z)=\sup_{\max(x,y)=z}\min(\mu_M(x),\mu_N(y))$; do **not** replace this with pointwise max of membership functions. For $M=(0,2,5)$, $N=(2,3,4)$, the key breakpoints are $2,3,3.5,5$.
- For [Kerre comparison](session-07/kerre.md), state $d(A,B)=\int|\mu_A-\mu_B|$ and the pairwise rule comparing $d(N,D)$ with $d(M,D)$, where $D$ is the **extension maximum**.

These are formulation/definition tasks. Numerical LP results and evaluated distance integrals are separately marked as extensions.
