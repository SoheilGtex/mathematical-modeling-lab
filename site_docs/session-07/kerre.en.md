# Kerre-style comparison by membership-function distance

**Lecture source: pages 5–6.** The notes introduce an $L^1$ distance between fuzzy numbers and compare two fuzzy quantities by measuring how close each is to their extension-principle maximum.

## 1. The distance from the notes

For integrable membership functions,

$$\boxed{d(\widetilde A,\widetilde B)=
\int_{-\infty}^{\infty}|\mu_{\widetilde A}(x)-\mu_{\widetilde B}(x)|\,dx.}$$

This is the area between membership-function graphs. It is zero when the two membership functions agree almost everywhere. With continuous triangular numbers this also implies equality of the functions themselves.

## 2. The comparison rule

Set $\widetilde D=\widetilde{\max}(\widetilde M,\widetilde N)$ **using the extension principle**, not pointwise max of memberships. The notes use the inequality

$$\boxed{\widetilde M\preceq_K\widetilde N\quad\Longleftrightarrow\quad
 d(\widetilde N,\widetilde D)\le d(\widetilde M,\widetilde D).}$$

On the final page they write the associated *pair-dependent* score

$$\boxed{r(\widetilde M,\widetilde N)=d(\widetilde M,\widetilde D)-d(\widetilde N,\widetilde D).}$$

A positive score favors $\widetilde N$, a negative score favors $\widetilde M$, and zero means a tie **under this comparison**. It does not mean the numbers are identical, and this pairwise comparison should not be assumed to provide a universal scalar utility or total order without further proof.

## 3. Complete computation for the example (independent)

For $M=(0,2,5)$, $N=(2,3,4)$, the previous page derived

$$\mu_D(z)=\begin{cases}
z-2,&2<z\le3,\\
4-z,&3<z\le3.5,\\
(5-z)/3,&3.5<z<5,\\
0,&\text{otherwise}.
\end{cases}$$

To integrate $|\mu_M-\mu_D|$, split at their intersection $z=11/4=2.75$, as well as at $2,3,3.5$:

$$\begin{aligned}
d(M,D)&=\int_0^2\frac z2\,dz
+\int_2^{11/4}\left(\frac{5-z}3-(z-2)\right)dz\\
&\quad+\int_{11/4}^3\left((z-2)-\frac{5-z}3\right)dz
+\int_3^{7/2}\left((4-z)-\frac{5-z}3\right)dz\\
&=\boxed{\frac32}.
\end{aligned}$$

For $N$, the differences start only at $z=7/2$:

$$\begin{aligned}
d(N,D)&=\int_{7/2}^{4}\left(\frac{5-z}3-(4-z)\right)dz
+\int_4^{5}\frac{5-z}3\,dz\\
&=\boxed{\frac14}.
\end{aligned}$$

Hence $r(M,N)=3/2-1/4=\boxed{5/4}>0$, and **$M\preceq_K N$** under the lecture's comparison.

## 4. Keep the two ranking methods separate

- **Session 06:** $R(A)$ is a linear scalar rank of each individual LR fuzzy number.
- **Session 07:** $r(M,N)$ is formed from distances to the **pairwise extension-principle max**.

They are different definitions. A result established for $R$ does not automatically hold for Kerre's distance comparison. The evaluated integrals and $5/4$ score are independently derived additions; the source states the method but not these values.
