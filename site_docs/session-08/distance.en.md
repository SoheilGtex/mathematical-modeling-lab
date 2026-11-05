# Kerre comparison: exact areas and decision

The source's second page introduces the distance-based Kerre-style comparison. It refers back to the fuzzy maximum from the previous page.

## 1. Definition and sign convention

For continuous compactly supported membership functions, define

$$d(A,B)=\int_{-\infty}^{\infty}|\mu_A(z)-\mu_B(z)|\,dz.$$

With $D=\widetilde{\max}(M,N)$ from the **extension principle**, define

$$\boxed{r(M,N)=d(M,D)-d(N,D).}$$

Under the convention written in the notes, $r(M,N)>0$ means $N$ is favored in the pairwise comparison; $r(M,N)<0$ favors $M$. Equal distances yield a comparison tie, **not necessarily equal fuzzy numbers**.

## 2. Use the derived membership of $D$

From the [previous derivation](extension-recap.md):

$$\mu_D(z)=\begin{cases}z-2,&2<z\le3,\\4-z,&3<z\le7/2,\\(5-z)/3,&7/2<z<5,\\0,&\text{otherwise}.\end{cases}$$

The integrand for $d(M,D)$ changes sign at $z=11/4$: for $2\le z\le3$, solve $(5-z)/3=z-2$. Other breakpoints arise at $0,2,3,7/2,5$. A correct integral cannot omit the absolute value or its sign-change points.

$$\begin{aligned}
d(M,D)&=\int_0^2\frac z2\,dz
+\int_2^{11/4}\left(\frac{5-z}{3}-(z-2)\right)dz\\
&\quad+\int_{11/4}^3\left((z-2)-\frac{5-z}{3}\right)dz
+\int_3^{7/2}\left((4-z)-\frac{5-z}{3}\right)dz\\
&=\boxed{\frac32}.
\end{aligned}$$

For $N$, $D$ and $N$ coincide up to $7/2$; the remaining difference is

$$\begin{aligned}
d(N,D)&=\int_{7/2}^4\left(\frac{5-z}3-(4-z)\right)dz
+\int_4^5\frac{5-z}3\,dz\\
&=\boxed{\frac14}.
\end{aligned}$$

Consequently

$$\boxed{r(M,N)=\frac32-\frac14=\frac54>0,\quad M\preceq_K N.}$$

## 3. How to reconstruct a new comparison

1. Write the two membership functions with **correct supports and modes**.
2. Derive $[D]_\alpha$ and invert it; never use pointwise membership maxima as a substitute.
3. Collect all supports, modes, maximum-function breakpoints, and intersections of the relevant affine branches.
4. Split each absolute-value integral at all breakpoints; identify the sign on each subinterval.
5. Evaluate $d(M,D)$ and $d(N,D)$ separately and only then determine the sign of $r$.

The numerical areas above are independently evaluated; the scan gives the comparison concept and graphical procedure but does not list these evaluated fractions.
