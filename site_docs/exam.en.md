# Exam Review — Mathematical Modeling Only

**Instructor clarification:** only mathematical modeling is required for the examination.
This single cumulative review covers **all sessions and assignments**, including future additions.
Practice defining the decision variables, objective, constraints, units and domains.
Numerical optimization and proof of optimality belong to the complete worked solutions, not this revision sheet.
This is an independent study aid, not an official exam syllabus or grading rubric.

## Session 01

### Modeling fundamentals

- **Decision variable:** the quantity we choose; identify its meaning, measurement unit and domain.
- **Objective:** an expression to minimize (cost) or maximize (profit).
- **Constraint:** a limited resource uses $\le$; a required minimum uses $\ge$; an exact balance uses $=$.
- **Domain:** declare nonnegativity and use integrality only if the problem explicitly requires whole units.

### Diet — minimum daily cost

From the [complete diet solution](session-01/diet.md), let $p,s,t$ represent the quantities of cheese, milk and eggs, respectively. Costs are in toman per day; vitamin A and B requirements are minima.

$$
\boxed{\begin{aligned}
\min\quad&Z=100p+50s+40t\\
\mathrm{s.t.}\quad&p+4s+2t\ge12&&\text{(vitamin A)}\\
&p+2s+3t\ge14&&\text{(vitamin B)}\\
&p,s,t\ge0.
\end{aligned}}
$$

**Why these directions?** Daily cost is minimized while each nutrient intake must be **at least** its required amount.

### Boat production — maximum profit

In the [boat model and full solution](session-01/boats.md), $x$ is the number of ordinary boats and $y$ the number of racing boats; profit is measured in **thousand toman**.

$$
\boxed{\begin{aligned}
\max\quad&Z=50x+80y\\
\mathrm{s.t.}\quad&50x+30y\le1000&&\text{(aluminum, kg)}\\
&20x+15y\le300&&\text{(machine, minutes)}\\
&3x+5y\le200&&\text{(labor, hours)}\\
&x,y\ge0.
\end{aligned}}
$$

Convert the available **5 machine-hours to 300 minutes** before writing the machine constraint. The supplied lecture model does not explicitly require integer variables; do not silently add integrality.

## Session 02

### Transportation — symbolic lecture model

From the [complete transportation explanation](session-02/transportation.md), let $x_{ij}$ be the shipment from source $i$ to destination $j$, $a_i$ the available supply, $b_j$ the **exact** destination demand and $c_{ij}$ the unit transport cost ($i=1,\ldots,m$, $j=1,\ldots,n$).

$$
\boxed{\begin{aligned}
\min\quad&Z=\sum_{i=1}^{m}\sum_{j=1}^{n}c_{ij}x_{ij}\\
\mathrm{s.t.}\quad&\sum_{j=1}^{n}x_{ij}\le a_i&&\forall i\\
&\sum_{i=1}^{m}x_{ij}=b_j&&\forall j\\
&x_{ij}\ge0&&\forall i,j.
\end{aligned}}
$$

The source limits are **upper bounds**, and every destination's stated requirement is **exact**. This lecture example has no lecturer-provided numerical cost matrix.

### Television production — profit maximization

For the [television model](session-02/televisions.md), let $x_1$ and $x_2$ be color and black-and-white televisions. Profit is in USD, labor in person-hours.

$$
\boxed{\begin{aligned}
\max\quad&Z=60x_1+30x_2\\
\mathrm{s.t.}\quad&20x_1+15x_2\le60000&&\text{(labor)}\\
&x_1\le2000&&\text{(color TV limit)}\\
&x_2\le4000&&\text{(black-and-white limit)}\\
&x_1,x_2\ge0.
\end{aligned}}
$$

The labor capacity is **60,000 person-hours**, confirmed from the corrected notes. Do not mix profit units with labor units.

## Session 03

### Numerical transportation — the lecture's 3×4 table

In the [complete numerical transportation problem](session-03/transportation.md), $x_{ij}$ is the amount shipped from origin $i$ (Tabriz, Yazd, Kerman) to destination $j$ (Tehran, Mashhad, Isfahan, Shiraz). The shipping costs $c_{ij}$ are **in toman per unit**.

$$
C=(c_{ij})=\begin{pmatrix}
80&5&12&15\\
1&9&4&5\\
12&8&6&4
\end{pmatrix},\quad a=(150,300,200),\quad b=(150,200,100,200).
$$

$$
\boxed{\begin{aligned}
\min\quad&Z=\sum_{i=1}^{3}\sum_{j=1}^{4}c_{ij}x_{ij}\\
\mathrm{s.t.}\quad&\sum_{j=1}^{4}x_{ij}\le a_i&&i=1,2,3\\
&\sum_{i=1}^{3}x_{ij}\ge b_j&&j=1,2,3,4\\
&x_{ij}\ge0&&\forall i,j.
\end{aligned}}
$$

Unlike Session 02's symbolic model, this note writes destination demand as **$\ge$**. Both totals equal $650$, so these constraints hold as equalities in any feasible plan **for this data**. Do not change the original inequality directions when initially modeling the question.

### Five-month production and inventory planning

From the [complete production/inventory formulation](session-03/production.md), $x_i$ denotes regular production, $y_i$ overtime production and $s_i$ the inventory at the **end** of month $i$. The demand vector is $d=(1200,2100,2400,3000,4000)$. Regular capacity is $2000$ units/month, overtime capacity is $600$ units/month. Unit costs: regular production $10$ toman, overtime $15$ toman, inventory holding $2$ toman per unit carried to the next month.

Set $s_0=s_5=0$ as boundary conditions; $s_1,\ldots,s_4$ are decision variables.

$$
\boxed{\begin{aligned}
\min\quad&Z=10\sum_{i=1}^{5}x_i+15\sum_{i=1}^{5}y_i+2\sum_{i=1}^{4}s_i\\
\mathrm{s.t.}\quad&x_i+y_i+s_{i-1}-s_i=d_i&&i=1,\ldots,5\\
&0\le x_i\le2000&&i=1,\ldots,5\\
&0\le y_i\le600&&i=1,\ldots,5\\
&s_i\ge0&&i=1,\ldots,4\\
&s_0=s_5=0.
\end{aligned}}
$$

There are **14 decision variables**: five $x_i$, five $y_i$ and four $s_i$. The monthly balance equations are **equalities**, not capacity inequalities.

## Assignment 01

### Municipal investment budgeting — Assignment 01

See the [complete analytical assignment solution](assignments/investment-budget.md). The municipality needs $2,4,8,5$ **million USD** at the **start** of years 1–4. It issues interest-bearing long-term securities at coupon rates $7\%,6\%,6.5\%,7.5\%$ and can deposit any unspent funds for one year at returns $6\%,5.5\%,4.5\%$ (years 1–3).

- $x_i\ge0$: millions of USD in long-term securities sold at the start of year $i$, for $i=1,2,3,4$.
- $s_i\ge0$: millions of USD deposited after paying for year $i$, available next year with return, for $i=1,2,3$.

Assuming the same **20 nominal yearly coupon payments** for each issue (no discount rate is provided), define the total coupon-cost objective:

$$
\boxed{\begin{aligned}
\min\quad&Z=20(0.07x_1+0.06x_2+0.065x_3+0.075x_4)\\
\mathrm{s.t.}\quad&x_1-s_1=2\\
&x_2+1.06s_1-s_2=4\\
&x_3+1.055s_2-s_3=8\\
&x_4+1.045s_3=5\\
&x_i\ge0\ (i=1,\ldots,4),\quad s_i\ge0\ (i=1,2,3).
\end{aligned}}
$$

**Modeling explanation:** every year's available funds equal its required spending plus the next deposit. The factors $1.06,1.055,1.045$ include the principal **and** one year's deposit interest. This objective counts nominal coupon expense (not principal repayment or discounted present value). The handout calls the issued instruments “shares,” but because it specifies interest and maturity, the model interprets them as **bond-like interest-bearing securities**; state this assumption.

## Modeling-only checklist

- [ ] Define every decision variable, its meaning, units and domain.
- [ ] State whether the objective is minimized or maximized.
- [ ] Translate each resource limit, minimum requirement and balance into a constraint.
- [ ] Check inequality directions, conversions, indices and boundary conditions.
- [ ] Present the complete mathematical model; no numerical optimum is required.
