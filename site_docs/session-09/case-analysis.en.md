# From LR branches to a rigorous Kerre score

The third source page sketches formulas for a relative comparison score $r(M,N)$, including cases for ordered modes and an intersection $\bar z$. Those expressions are a **case-dependent integration outline** rather than a general formula that can be used without checking the sign of each integrand.

## 1. Start with the extension maximum

For any triangular numbers $M=(a,b,c)$ and $N=(a',b',c')$ with $a<b<c$ and $a'<b'<c'$, the closed $\alpha$-cuts are

$$[M]_\alpha=[a+\alpha(b-a),c-\alpha(c-b)],$$

$$[N]_\alpha=[a'+\alpha(b'-a'),c'-\alpha(c'-b')].$$

For the **extension-principle** maximum $D=\widetilde{\max}(M,N)$,

$$\boxed{[D]_\alpha=
[\max\{L_M(\alpha),L_N(\alpha)\},\quad
 \max\{R_M(\alpha),R_N(\alpha)\}].}$$

The left and right endpoints are each maxima of two affine functions. They can change active branch only at an intersection. Therefore the membership function of $D$ is continuous and piecewise affine; the exact transition points can be determined using elementary linear equations.

**Do not confuse this with** $\max\{\mu_M(z),\mu_N(z)\}$, which is a union of fuzzy sets, not the extension image of the numerical maximum.

## 2. The two integration formulas in the handwritten page

The scan first assumes the modes satisfy $b\le b'$. Set $m(z)=\mu_M(z)$ and $n(z)=\mu_N(z)$. For triangular numbers, the extension maximum has the following branches **under exactly this ordered-mode assumption**:

$$\mu_D(z)=\begin{cases}
\min(m(z),n(z)),&z<b,\\
n(z),&b\le z\le b',\\
\max(m(z),n(z)),&z>b'.
\end{cases}$$

Substituting into $r=d(M,D)-d(N,D)$ yields the first case formula from the scan:

$$\boxed{\begin{aligned}
r(M,N)&=\int_{\min(a,a')}^{b}\big(m(z)-n(z)\big)\,dz\\
&\quad+\int_b^{b'}|m(z)-n(z)|\,dz\\
&\quad+\int_{b'}^{\max(c,c')}\big(n(z)-m(z)\big)\,dz.
\end{aligned}}$$

**Why the signs are correct:** for $z<b$, $D=\min(m,n)$ and the difference of the two absolute deviations simplifies identically to $m-n$. For $z>b'$, $D=\max(m,n)$ and it simplifies to $n-m$. Only the middle region retains the absolute value.

For **strictly ordered modes** $b<b'$, the source next introduces an intersection $\bar z\in[b,b']$ of the descending branch $M_R$ and ascending branch $N_L$. If these active branches intersect once and $M_R\ge N_L$ before that point, the middle integral splits, giving the second handwritten case formula:

$$\boxed{\begin{aligned}
r(M,N)&=\int_{\min(a,a')}^{b}(M_L-N_L)\,dz\\
&\quad+\int_b^{\bar z}(M_R-N_L)\,dz\\
&\quad+\int_{\bar z}^{b'}(N_L-M_R)\,dz\\
&\quad+\int_{b'}^{\max(c,c')}(N_R-M_R)\,dz.
\end{aligned}}$$

Here each branch is **understood as zero outside its own support**. If the supports do not overlap on $[b,b']$, the intersection may be non-unique (both branches can vanish), so the first formula is safer. If instead $b>b'$, swap $M,N$ and change the score sign: $r(M,N)=-r(N,M)$. Thus the case formulas can be used reliably without guessing the sign of the integrands.

## 3. The source's new example is a special dominance case

For $M=(2,5,12)$ and $N=(2,4,10)$:

$$\begin{aligned}
[M]_\alpha&=[2+3\alpha,12-7\alpha],\\
[N]_\alpha&=[2+2\alpha,10-6\alpha].
\end{aligned}$$

For all $0\le\alpha\le1$,

$$2+3\alpha\ge2+2\alpha,\qquad12-7\alpha\ge10-6\alpha$$

because the differences are $\alpha\ge0$ and $2-\alpha\ge1$. Consequently

$$\boxed{[D]_\alpha=[M]_\alpha\text{ for every }\alpha,\quad D=M.}$$

This **does not** assert that $\mu_M(z)\ge\mu_N(z)$ at every point. Indeed, near $z=3$ the $N$ membership is larger. Dominance of both alpha-cut *endpoints* and pointwise dominance of membership functions are different concepts.

## 4. Compute the score and every absolute-value interval

Since $D=M$,

$$r(M,N)=d(M,M)-d(N,M)=-d(M,N).$$

With $z_*=14/3$ from the branch intersection, partition at $2,4,z_*,5,10,12$:

$$\begin{aligned}
d(M,N)&=\int_2^4\left(\frac{z-2}{2}-\frac{z-2}{3}\right)dz\\
&\quad+\int_4^{14/3}\left(\frac{10-z}{6}-\frac{z-2}{3}\right)dz\\
&\quad+\int_{14/3}^5\left(\frac{z-2}{3}-\frac{10-z}{6}\right)dz\\
&\quad+\int_5^{10}\left(\frac{12-z}{7}-\frac{10-z}{6}\right)dz
+\int_{10}^{12}\frac{12-z}{7}\,dz\\
&=\frac13+\frac19+\frac1{36}+\frac{95}{84}+\frac27
=\boxed{\frac{17}{9}}.
\end{aligned}$$

Thus

$$\boxed{d(M,D)=0,\quad d(N,D)=\frac{17}{9},\quad r(M,N)=-\frac{17}{9}<0.}$$

Under the source's convention **$M$ is preferred to $N$** for this pair. The numerical integral, its breakpoints, and the preference conclusion are an **independent completion** of the unfinished handwritten example.

## 5. General integration procedure and failure modes

For a different pair (where neither alpha-cut endpoint dominates), determine $D$ from level intervals, locate **all** knots of $M$, $N$, $D$, plus crossings of the integrand differences, and split the absolute-value integrals. The handwritten ordered-mode **first formula already handles the middle absolute value**; its fully expanded second formula requires the correct middle crossing and branch ranges. Do not transfer the expanded signs to an unrelated ordering.

The exact implementation in [the computation section](computation.md) constructs all piecewise-linear knots and integrates each segment as an exact trapezoid or a pair of triangles.
