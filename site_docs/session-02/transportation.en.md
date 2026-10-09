# Transportation Model — Full Written Solution

> **Source boundary:** The photographed lecture page defines a symbolic transportation model and route graph but supplies no numerical costs, capacities, or demands. The 2 × 2 numerical example in this page is an independent educational illustration, **not lecture data**.

## Problem statement (faithful English rendering)

A transportation company moves goods from $m$ origin warehouses to $n$
destination warehouses. Warehouse $i$ has available supply/capacity $a_i$;
destination $j$ requires $b_j$ units. Shipping one unit from origin $i$
to destination $j$ costs $c_{ij}$. Determine the amounts shipped so that
all destination requirements are fulfilled and the total transport cost is
minimized without exceeding any origin's capacity.

## Decision variables and parameters

- $i=1,\dots,m$ is an origin; $j=1,\dots,n$ is a destination.
- $a_i\ge0$: available quantity at origin $i$ (units of goods).
- $b_j\ge0$: amount required by destination $j$ (same units).
- $c_{ij}$: monetary cost per unit on route $i\to j$.
- $x_{ij}\ge0$: amount sent from origin $i$ to destination $j$.

There are $mn$ decision variables. The arrows in the source diagram represent
possible shipping routes; the handwritten model does not specify route-specific
upper bounds other than source capacities.

## Objective and mathematical formulation

Every route contributes $c_{ij}x_{ij}$ to cost, so:

$$
\boxed{\begin{aligned}
\min_{x}\quad & Z=\sum_{i=1}^{m}\sum_{j=1}^{n}c_{ij}x_{ij}\\
\text{subject to}\quad
&\sum_{j=1}^{n}x_{ij}\le a_i, && i=1,\ldots,m\\
&\sum_{i=1}^{m}x_{ij}=b_j, && j=1,\ldots,n\\
&x_{ij}\ge0, &&i=1,\ldots,m,\quad j=1,\ldots,n.
\end{aligned}}
$$

Why do the directions differ? **Origin stock is a maximum**, so $\le$;
**destination demand must be exactly met** in the source model, so $=$.
Replacing $=$ with $\ge$ is not faithful to the photographed formulation.

## Feasibility check (proof)

Summing destination equalities gives $\sum_{i,j}x_{ij}=\sum_j b_j$.
Summing origin inequalities gives $\sum_{i,j}x_{ij}\le\sum_i a_i$.
Thus a necessary condition is

$$\boxed{\sum_{i=1}^{m}a_i\ge\sum_{j=1}^{n}b_j.}$$

For a complete network where **every origin can ship to every destination**
and there are no extra route restrictions, this is also sufficient for
nonnegative continuous flows. If total supply equals demand, every source
capacity is tight; if supply exceeds demand, some source capacity may remain
unused. This claim must not be transferred to networks with forbidden routes
or additional arc capacities without further checks.

## Supplemental worked numerical example — NOT in the lecture note

To illustrate solving on paper, consider two origins and two destinations:

| Cost per unit | Destination 1 | Destination 2 | Supply |
| --- | ---: | ---: | ---: |
| Origin 1 | 2 | 5 | 10 |
| Origin 2 | 4 | 1 | 20 |
| Demand | 12 | 18 | 30 |

The model is

$$
\begin{aligned}
\min\quad&2x_{11}+5x_{12}+4x_{21}+x_{22}\\
\text{s.t.}\quad&x_{11}+x_{12}\le10,\\
&x_{21}+x_{22}\le20,\\
&x_{11}+x_{21}=12,\\
&x_{12}+x_{22}=18,\\
&x_{ij}\ge0.
\end{aligned}
$$

Because the total supply $10+20=30$ equals total demand $12+18=30$,
both supply inequalities hold with equality in every feasible solution.
Let $t=x_{12}$. Then

$$x_{11}=10-t,\qquad x_{21}=2+t,\qquad x_{22}=18-t.$$

Nonnegativity implies $0\le t\le10$. Substitution into the objective:

$$Z(t)=2(10-t)+5t+4(2+t)+(18-t)=46+6t.$$

As the coefficient of $t$ is positive, the minimum is attained at $t=0$:

$$\boxed{(x_{11},x_{12},x_{21},x_{22})=(10,0,2,18),\quad Z_{\min}=46.}$$

**Why globally optimal?** Every feasible solution has the form above, and
$Z(t)\ge46$ on $[0,10]$. Thus $Z=46$ is a global minimum, not merely a
feasible cost. Destination totals are $10+2=12$ and $0+18=18$; origin totals
are $10$ and $20$.

## Common written-exam pitfalls

1. Defining $x_{ij}$ without explaining the meanings of $i$ and $j$.
2. Using $\ge$ for source capacity instead of $\le$.
3. Using $\le$ for destination demand instead of the source's equality.
4. Forgetting nonnegativity or mixing supply/demand units.
5. Claiming a numerical solution for the lecturer's abstract model without data.
6. Treating an LP solver result as a handwritten optimality proof.
