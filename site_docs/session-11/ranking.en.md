# Ranking a hesitant trapezoidal fuzzy number

## Ranking rule recorded in the lecture

Suppose a hesitant fuzzy number consists of \(p\) trapezoidal fuzzy numbers

$$\mathcal H=\{(a_j,b_j,c_j,d_j):j=1,\ldots,p\}.$$

The handwritten ranking rule is

$$\boxed{R_1(\mathcal H)=\frac1{4p}\sum_{j=1}^{p}(a_j+b_j+c_j+d_j).}$$

This is the **arithmetic mean of all four vertices for every trapezoid**. For \(p=1\), it reduces to \((a+b+c+d)/4\). The course orders two hesitant numbers using this specified scalar: \(A\succ_R B\) if \(R_1(A)>R_1(B)\).

**Interpretation:** it is one ranking convention, not a universal order on fuzzy sets. Different hesitant numbers may share the same score, and the score discards membership-shape detail.

## Fully reconstructed example on page 4

$$\begin{aligned}
\mathcal A&=\{(1,3,5,9),(2,4,5,7)\},\\
\mathcal B&=\{(-1,2,3,8),(2,3,4,9)\}.
\end{aligned}$$

Calculate each trapezoid's score first:

| Estimate | Sum of vertices | Four-point mean |
|---|---:|---:|
| \(A_1\) | 18 | 4.5 |
| \(A_2\) | 18 | 4.5 |
| \(B_1\) | 12 | 3 |
| \(B_2\) | 18 | 4.5 |

Therefore

$$R_1(\mathcal A)=\frac{18+18}{8}=\boxed{4.5},\qquad
R_1(\mathcal B)=\frac{12+18}{8}=\boxed{3.75}.$$

Since \(4.5>3.75\), the course criterion ranks \(\mathcal A\) above \(\mathcal B\). Both values match the scan.

## Caution for triangular components

A triangle \((\ell,m,u)\) has **three** given coordinates. It can be embedded as the degenerate trapezoid \((\ell,m,m,u)\), leading to \((\ell+2m+u)/4\). This is a **declared modeling choice**, not the same as the ordinary mean \((\ell+m+u)/3\). Do not use the four-vertex formula on a three-coordinate tuple without explaining the conversion.
