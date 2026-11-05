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

## Session 04

### Three products on four machines

In the [full machine-allocation problem](session-04/machines.md), $x_{ij}\ge0$ is the **number of units of product $i$ made on machine $j$**, for $i=1,2,3$ and $j=1,2,3,4$.

Unit production costs (in USD), machine time (hours per unit), minimum product requirements and maximum machine hours come from the lecture:

$$
C=\begin{pmatrix}4&4&5&7\\6&7&5&6\\12&10&8&11\end{pmatrix},\quad
T=\begin{pmatrix}.30&.25&.20&.20\\.20&.30&.20&.25\\.80&.60&.60&.50\end{pmatrix},
$$

$$d=(3000,6000,4000),\qquad H=(1500,1200,1500,2000).$$

$$
\boxed{\begin{aligned}
\min\ &Z=\sum_{i=1}^3\sum_{j=1}^4 c_{ij}x_{ij}\\
\mathrm{s.t.}\ &\sum_{i=1}^3t_{ij}x_{ij}\le H_j &&j=1,\ldots,4\\
&\sum_{j=1}^4x_{ij}\ge d_i &&i=1,2,3\\
&x_{ij}\ge0 &&\forall i,j.
\end{aligned}}
$$

**Remember:** four $\le$ hour limits and three $\ge$ production minimums; there are **12** nonnegative decision variables. Costs are USD, not toman.

### Light/heavy crude oil procurement

In the [full crude-oil example](session-04/crude.md), let $x_1,x_2\ge0$ be the **amounts of light/heavy raw crude purchased** (before processing losses). Prices are $20 and $15 per unit; recovery is $95\%$ and $92\%$. The products are **diesel, kerosene and jet fuel**, and the output requirements are $1{,}000{,}000$, $500{,}000$, $300{,}000$:

$$
\boxed{\begin{aligned}
\min\quad&Z=20x_1+15x_2\\
\mathrm{s.t.}\quad&0.40(0.95)x_1+0.32(0.92)x_2\ge1{,}000{,}000\\
&0.20(0.95)x_1+0.40(0.92)x_2\ge500{,}000\\
&0.35(0.95)x_1+0.20(0.92)x_2\ge300{,}000\\
&x_1,x_2\ge0.
\end{aligned}}
$$

Apply the recovery factor **before** each product's yield; all requirements are lower bounds ($\ge$).

### Maximum revenue-to-cost ratio (fractional objective)

In the [full fractional model](session-04/ratio.md), $x_1,x_2\ge0$ denote quantities of products $A,B$. Sale prices $(80,40)$, variable costs $(40,20)$ and fixed cost $200$ are measured in **thousand toman**. Products use $(2,3)$ hours and $(3,2)$ kg of raw materials per unit, respectively.

$$
\boxed{\begin{aligned}
\max\quad&Z=\frac{80x_1+40x_2}{40x_1+20x_2+200}\\
\mathrm{s.t.}\quad&2x_1+3x_2\le120\\
&3x_1+2x_2\le150\\
&x_1,x_2\ge0.
\end{aligned}}
$$

**Do not replace the ratio with profit.** This is a **linear-fractional**, not an ordinary linear, objective. The denominator is positive because fixed cost is $200>0$.

## Session 05

### Linear-fractional objective and Charnes–Cooper model

The [fractional-programming lecture example](session-05/fractional.md) is

$$\boxed{\begin{aligned}
\max\quad &\frac{10x_1+20x_2+10}{3x_1+4x_2+20}\\
\mathrm{s.t.}\quad &x_1+3x_2\le50,\\
&3x_1+2x_2\le80,\\
&x_1,x_2\ge0.
\end{aligned}}$$

The denominator is **strictly positive** ($\ge20$). Let $t=1/(3x_1+4x_2+20)$ and $y_i=tx_i$ ($x_i=y_i/t$). Multiply **both** resource constraints by $t$ and normalize the denominator:

$$\boxed{\begin{aligned}
\max\quad&10y_1+20y_2+10t\\
\mathrm{s.t.}\quad&y_1+3y_2\le50t,\\
&3y_1+2y_2\le80t,\\
&3y_1+4y_2+20t=1,\\
&y_1,y_2,t\ge0.
\end{aligned}}$$

**Remember:** in general $t>0$ is needed to invert the transformation; for this model, $t=0$ is impossible because the first scaled constraint and $y\ge0$ contradict the normalizing equality. Do not drop the constant $10$ in the numerator or $20$ in the denominator.

### Triangular fuzzy membership as a mathematical model

From the [fuzzy-number lecture](session-05/fuzzy.md), a crisp characteristic function has values only $0$ or $1$, while fuzzy membership satisfies $\mu_{\widetilde A}(x)\in[0,1]$. For the triangular fuzzy number $\widetilde M=(1,5,7)$:

$$\boxed{\mu_{\widetilde M}(x)=\begin{cases}
0,&x\le1,\\
(x-1)/4,&1<x\le5,\\
(7-x)/2,&5<x<7,\\
0,&x\ge7.
\end{cases}}$$

**Modeling point:** derive the two straight-line equations from $(1,0)$, $(5,1)$ and $(7,0)$. This is a **membership-function model**, not a fuzzy optimization problem; no numerical optimizer is included in the exam review.

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

## Assignment 02

### Python solution to the existing transportation problem

Assignment 02 was **only the Python implementation** of the existing [Session 03 transportation model](session-03/transportation.md). No second transport dataset or different mathematical formulation was assigned. The [existing Python code](assignments/transportation-python.md) solves that lecture example; the model is already included under Session 03 in this cumulative review. There is no need to repeat its constraints here.

## Assignment 03

### Triangular fuzzy memberships and the maximum operator

The full [fuzzy-number assignment solution](assignments/fuzzy-numbers-max.md) uses $\widetilde A=(1,3,7)$ and $\widetilde B=(3,5,6)$. Model the membership functions with the triangular definition, then use **Zadeh's extension-principle constraint**:

$$\mu_{\max(\widetilde A,\widetilde B)}(z)=
\sup_{\substack{x,y\in\mathbb R\\\max(x,y)=z}}
\min\bigl(\mu_{\widetilde A}(x),\mu_{\widetilde B}(y)\bigr).$$

The constraint $\max(x,y)=z$ requires $x\le z$, $y\le z$, and **at least one equality**. Identify the triangle vertices and sketch both membership functions and their maximum; all detailed interval calculations and proofs are on the full assignment page. This is a fuzzy-membership modeling exercise, **not** an extra linear-programming objective.

## Modeling-only checklist

- [ ] Define every decision variable, its meaning, units and domain.
- [ ] State whether the objective is minimized or maximized.
- [ ] Translate each resource limit, minimum requirement and balance into a constraint.
- [ ] Check inequality directions, conversions, indices and boundary conditions.
- [ ] Present the complete mathematical model; no numerical optimum is required.
