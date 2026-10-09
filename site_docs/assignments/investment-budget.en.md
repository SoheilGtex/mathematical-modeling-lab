# Assignment 01 — Municipal Investment Budgeting

> **Source and scope:** Assignment 01, *Investment Budgeting*, student-supplied two-page Persian handout. The investment requirements, rates, timing and 20-year interest-payment horizon below come from the assignment. The mathematical solution, optimal plan and independent verification are our worked answer, not an answer supplied in the handout.

## 1. Problem data and interpretation

A municipality must fund a public project over four years. All project expenses must be covered **at the beginning of each year**. It can raise money by selling long-term interest-bearing securities, and it can invest any unneeded proceeds in one-year deposits that mature at the beginning of the next year.

| Year $i$ | Project spending (million USD) | Long-term coupon rate | One-year deposit return |
| --- | ---: | ---: | ---: |
| 1 | 2 | 7% | 6% |
| 2 | 4 | 6% | 5.5% |
| 3 | 8 | 6.5% | 4.5% |
| 4 | 5 | 7.5% | — |

The handout uses the word *shares*, although it also specifies interest and maturity. We consequently treat the instrument as an **interest-bearing long-term security (bond-like debt)** rather than ordinary equity. All issues share the same maturity timing. The question describes **20 years of interest payments** beginning one year after project completion. We minimize **nominal coupon expense**, without discounting future payments, since no discount rate is provided. Deposit interest is already reflected in the annual cash-flow equations. Principal redemption is not an interest expense and is not part of the objective.

This timing/nominal-cost interpretation should be stated explicitly when presenting the model. It does not add a terminal cash-reserve requirement or a separate year-four deposit that the handout never specifies.

## 2. Decision variables

For $i=1,2,3,4$, define

$$x_i=\text{amount raised by selling long-term securities at the start of year }i.$$

For $i=1,2,3$, define

$$s_i=\text{amount deposited after funding year }i\text{, available at the start of year }i+1.$$

All seven variables are **nonnegative**, and every dollar amount is measured in **millions of USD**. There is no $s_4$: the four-year project ends after funding year four.

## 3. Cash-flow balance by year

A deposit of $s_i$ earns the year-$i$ short-term return, so $(1+r_i)s_i$ becomes available at the beginning of year $i+1$.

**Year 1.** Sell enough securities to pay the first $2$ million and make any new deposit:

$$\boxed{x_1-s_1=2.}$$

**Year 2.** The first deposit returns with $6\%$ interest. After paying $4$ million, any surplus is deposited again:

$$\boxed{x_2+1.06s_1-s_2=4.}$$

**Year 3.** The second deposit returns with $5.5\%$ interest:

$$\boxed{x_3+1.055s_2-s_3=8.}$$

**Year 4.** The third deposit returns with $4.5\%$ interest and funds the final $5$ million:

$$\boxed{x_4+1.045s_3=5.}$$

Each balance is an **equality**: any cash not spent on that year's project is recorded as a deposit, rather than disappearing.

## 4. Objective and complete LP

The yearly coupon cost of the issued securities is

$$C=0.07x_1+0.06x_2+0.065x_3+0.075x_4.$$

As all issues generate 20 such payments, their total **nominal** interest is $Z=20C$. Minimizing $Z$ is equivalent to minimizing $C$.

$$
\boxed{\begin{aligned}
\min\quad Z={}&20(0.07x_1+0.06x_2+0.065x_3+0.075x_4)\\
\text{s.t.}\quad&x_1-s_1=2,\\
&x_2+1.06s_1-s_2=4,\\
&x_3+1.055s_2-s_3=8,\\
&x_4+1.045s_3=5,\\
&x_i\ge0\quad(i=1,\ldots,4),\\
&s_i\ge0\quad(i=1,2,3).
\end{aligned}}
$$

**Important units:** $C$ is in million USD **per interest-payment year**; $Z$ is in million USD **over 20 payments**, not a present value.

## 5. Paper-and-pencil global optimality proof

Instead of merely trusting an optimizer, eliminate variables using the four balances. From the last two years,

$$s_3=\frac{5-x_4}{1.045},\qquad
s_2=\frac{8+s_3-x_3}{1.055}.$$

From the first two years,

$$x_1=2+s_1,\qquad x_2=4+s_2-1.06s_1.$$

Substitute these identities in the **annual** objective $C$ and collect terms:

$$
\begin{aligned}
C={}&\underbrace{0.07(2)+0.06\left(4+\frac{8+5/1.045}{1.055}\right)}_{C_*}\\
&+\underbrace{(0.07-1.06\times0.06)}_{0.0064}s_1\\
&+\underbrace{\left(0.065-\frac{0.06}{1.055}\right)}_{\approx0.0081279621}x_3\\
&+\underbrace{\left(0.075-\frac{0.06}{1.055\times1.045}\right)}_{\approx0.0205769972}x_4.
\end{aligned}
$$

Every coefficient after $C_*$ is **strictly positive**, and $s_1,x_3,x_4\ge0$. Therefore, **every feasible plan** obeys $C\ge C_*$, with equality **only if**

$$\boxed{s_1=x_3=x_4=0.}$$

The balances then uniquely determine the remaining variables:

$$
\boxed{\begin{aligned}
s_3^*&=\frac5{1.045}\approx4.784689,\\
s_2^*&=\frac{8+5/1.045}{1.055}\approx12.118189,\\
x_1^*&=2,\qquad x_2^*=4+s_2^*\approx16.118189.
\end{aligned}}
$$

All entries are nonnegative, so this plan is feasible and achieves the proven lower bound. Hence it is the **unique global optimum**; the proof does not depend on Python or a solver.

## 6. Optimal annual financing schedule

All amounts below are **millions of USD** and rounded for display.

| Year | New security proceeds $x_i$ | Deposit maturity with return | Project spending | New deposit $s_i$ |
| --- | ---: | ---: | ---: | ---: |
| 1 | 2.000000 | 0 | 2 | 0 |
| 2 | 16.118189 | 0 | 4 | 12.118189 |
| 3 | 0 | 12.784689 | 8 | 4.784689 |
| 4 | 0 | 5.000000 | 5 | 0 |

Checking all four balances using the **exact expressions** above (before rounding):

$$
\begin{aligned}
x_1-s_1&=2,\\
x_2+1.06s_1-s_2&=4,\\
x_3+1.055s_2-s_3&=8,\\
x_4+1.045s_3&=5.
\end{aligned}
$$

The minimum annual coupon expense and 20-year nominal total are

$$
\boxed{\begin{aligned}
C_{\min}&=0.07(2)+0.06(16.118188621\ldots)\\
&\approx1.107091317\text{ million USD/year},\\
Z_{\min}&=20C_{\min}\approx22.141826345\text{ million USD}.
\end{aligned}}
$$

Total security proceeds issued: $2+16.118188621\ldots=18.118188621\ldots$ million USD. This is less than the project's $19$ million USD of spending because **short-term deposit interest supplies the difference**. It is not an indication that any year's spending is missing.

## 7. Practical exam checklist

1. Label amounts in **millions of dollars**, distinguish securities sold from one-year deposits, and define the indices.
2. Explain the one-year deposit return factors $1.06$, $1.055$ and $1.045$.
3. Write all **four** cash-flow equalities; do not subtract deposit interest a second time in the coupon-cost objective.
4. Distinguish a coupon's **20 nominal payments** from the issue principal or the net-present-value calculation (no discount rate given).
5. A feasible schedule is not automatically optimal: show the positive-coefficient lower-bound identity.
6. Keep this **assignment** separate from the three lecture sessions and their single cumulative exam-review page.

### Computational check (optional)

From the project root with the environment activated:

```bash
python examples/assignments/01_investment_budget.py
python -m pytest -q tests/test_assignment_01.py
```

The code checks the solver result against the independent symbolic construction and a primal–dual LP verification. **The written solution above is sufficient without executing code.**
