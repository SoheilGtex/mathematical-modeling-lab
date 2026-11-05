# LR numbers and arithmetic

**Lecture source: pages 1–2.** The lecture derives the straight-line membership functions of a trapezoid and then gives arithmetic rules for triangular and LR fuzzy numbers.

## 1. The four-parameter LR trapezoid

Let

$$\widetilde A=(a^L,a^U,\ell,r)_{LR},\qquad a^L\le a^U,\quad\ell,r\ge0.$$

The support endpoints are $a^L-\ell$ and $a^U+r$, and the core is $[a^L,a^U]$. The source writes the spreads as $\alpha$ and $\beta$; here $\ell,r$ avoid confusion with cut levels.

The left line joins $(a^L-\ell,0)$ to $(a^L,1)$, hence its slope is $1/\ell$. The right line joins $(a^U,1)$ to $(a^U+r,0)$, hence its slope is $-1/r$. Therefore, for positive spreads,

$$\mu_{\widetilde A}(x)=\begin{cases}
0,&x<a^L-\ell,\\
1-\dfrac{a^L-x}{\ell},&a^L-\ell\le x<a^L,\\
1,&a^L\le x\le a^U,\\
1-\dfrac{x-a^U}{r},&a^U<x\le a^U+r,\\
0,&x>a^U+r.
\end{cases}$$

A zero spread is a vertical shoulder; in that case omit the corresponding sloping segment rather than divide by zero.

The closed $\lambda$-cut is

$$[\widetilde A]_{\lambda}=
[a^L-(1-\lambda)\ell,\ a^U+(1-\lambda)r],\qquad 0\le\lambda\le1.$$

## 2. Addition

For two LR trapezoids with this *same linear shape* (or their alpha-cut representation),

$$\boxed{(a^L,a^U,\ell,r)_{LR}+(b^L,b^U,s,t)_{LR}
=(a^L+b^L,\ a^U+b^U,\ell+s,\ r+t)_{LR}.}$$

This follows by adding the two endpoints of every level interval, not by multiplying membership values. For triangular numbers $(m,\ell,r)_{LR}$, the center and both spreads add componentwise.

## 3. Negation and scalar multiplication

Reflection reverses the core and interchanges left and right spreads:

$$\boxed{-\widetilde A=(-a^U,-a^L,r,\ell)_{LR}.}$$

For $c\ge0$ and $c<0$, respectively,

$$c\widetilde A=\begin{cases}
(ca^L,ca^U,c\ell,cr)_{LR},&c\ge0,\\
(ca^U,ca^L,-cr,-c\ell)_{LR},&c<0.
\end{cases}$$

For a conventional triangular triple $(a,b,c)$, multiplication by a **negative** scalar $t$ produces $(tc,tb,ta)$; the endpoints must be reordered. At $t=0$ the result is the crisp singleton at zero.

**Example (independent check).** Let $\widetilde A=(2,0.8,0.4)_{LR}$ be the lecture triangle in center/spread notation. Then

$$-\widetilde A=(-2,0.4,0.8)_{LR},\qquad
[2\widetilde A]_{1/2}=[3.2,4.4].$$

## 4. When these rules are valid

All displayed LR formulas refer to triangular/trapezoidal **linear** left and right shapes. Arbitrary fuzzy-number multiplication need not remain triangular or trapezoidal. In the fuzzy production models, $x_i\ge0$ ensures that multiplying a fuzzy coefficient by a decision variable uses the positive-scalar rule.
