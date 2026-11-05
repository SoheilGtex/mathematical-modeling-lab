### LR triangular comparison: correcting the model before solving it

- The new source example is $M=(2,5,12)$ and $N=(2,4,10)$, using **(support left, mode, support right)** rather than four-parameter LR core/spread tuples.
- Write the correct branches $M_L(z)=(z-2)/3$ for $2\le z\le5$, $M_R(z)=(12-z)/7$ for $5\le z\le12$, $N_L(z)=(z-2)/2$ for $2\le z\le4$, and $N_R(z)=(10-z)/6$ for $4\le z\le10$. The handwritten denominators of $N$ are inconsistent with its stated endpoints; the corrected branches here are an explicit mathematical repair.
- Formulate $[D]_\alpha=[\max(L_M,L_N),\max(R_M,R_N)]$ and the Kerre score $r(M,N)=d(M,D)-d(N,D)$. Distinguish model specification from computing the score.
- [Corrected membership model](session-09/source-example.md) and [general case analysis](session-09/case-analysis.md). The evaluated value $-17/9$ is an independent extension.
