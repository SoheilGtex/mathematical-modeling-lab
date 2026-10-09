# Session 01 — Parametric sensitivity analysis

This is an **independent Python extension**, not material quoted from the
handwritten session notes. The notes provide the baseline formulations only.

## What is computed

For each selected parameter value \(\theta\), the software constructs a new
LP or MILP by changing **one coefficient or one right-hand side at a time**,
then re-solves it with SciPy/HiGHS. Model coefficients other than the selected
parameter remain fixed. Scenario outcomes can be optimal, infeasible, unbounded,
or solver-error; failed solves are reported, not substituted with fabricated
objective values.

- A **RHS** parameter alters the available resource or minimum requirement.
- An **objective** parameter alters one unit price/profit coefficient.
- **LP** scenarios solve the continuous formulation from the original notes.
- **MILP** scenarios use an explicitly added integrality assumption.

### Shadow price: definition and limits

For continuous LPs only, the local marginal value for a physical RHS parameter
\(\theta\) is

\[
  \pi = \left.\frac{\partial z^*(\theta)}{\partial\theta}\right|_{\theta_0}.
\]

SciPy reports `linprog(...).ineqlin.marginals` for the solver's **minimization**
objective and internally transformed `A_ub @ x <= b_ub` constraints. The code
reverses the objective sign for maximization and adjusts the physical RHS sign
for originally `>=` vitamin requirements.

Shadow prices depend on the local optimal basis and should not be extrapolated
across arbitrary parameter changes. At a degenerate breakpoint a derivative
may be non-unique. **MILPs do not receive these LP shadow prices**; instead,
we show independently re-optimized integer solutions and their finite changes.

## Commands

```bash
# Discover supported physical-unit parameters
python -m modeling_lab boats --list-parameters
python -m modeling_lab diet --list-parameters

# LP machine capacity in minutes; print values, solutions and local marginal
python -m modeling_lab boats --sensitivity machine_minutes \
  --values 240 300 360 400 --sensitivity-plot plots/machine_lp.png

# Integer production counts: no continuous-LP shadow-price claim
python -m modeling_lab boats --integer --sensitivity machine_minutes \
  --values 300 310 315 400 --sensitivity-plot plots/machine_milp.png

# Daily minimum vitamin A in original positive units (not negative b_ub)
python -m modeling_lab diet --sensitivity vitamin_A_requirement \
  --values 10 12 14 --json

# Change unit profit rather than RHS
python -m modeling_lab boats --sensitivity competition_profit \
  --values 20 37.5 80
```

`--values` accepts between 1 and 200 finite numbers. `--json` includes scenario
statuses and numeric results. Generated PNGs are ignored under `plots/`.
Sensitivity plots show the **sampled scenarios**, not a certified analytic
response curve. For integer models the points are not connected, to avoid
suggesting a continuous profit function.

## Session 01: boat production

At the original data, the **continuous** solution is \((x,y)=(0,20)\), profit
\(1600\) thousand toman. The active constraint is the machine-time bound
\(20x+15y\le 300\). Nonbinding aluminum and labor constraints have zero local
shadow prices. The continuous machine-time shadow price is:

\[
  \pi_{machine}=\frac{80}{15}\approx 5.333333
  \quad \text{thousand toman per minute}.
\]

This says one more minute is worth about 5.333 thousand toman *locally* in the
continuous LP. It does **not** say that every additional minute of machine
capacity yields exactly that profit in an integer production plan.

| Machine minutes | LP optimal profit (thousand toman) | LP boats \((x,y)\) |
| ---: | ---: | --- |
| 240 | 1280 | (0,16) |
| 300 | 1600 | (0,20) |
| 360 | 1920 | (0,24) |
| 400 | 2133.333... | (0,26.666...) |

With integer production counts, profit stays at 1600 at 310 minutes and jumps
to 1680 at 315 minutes; it is 2080 at 400 minutes. This is the **re-solved**
MILP, not a derivative calculation.

## Session 01: diet

For the physical requirements \(A\ge12, B\ge14\), the code stores the same
inequalities internally as \(-A\le-12, -B\le-14\). A request to increase
`vitamin_A_requirement` from 12 to 13 correctly changes \(-12\) to \(-13\).
The continuous LP local cost marginals are:

- Vitamin A requirement: **8.75 toman per additional A unit/day**.
- Vitamin B requirement: **7.5 toman per additional B unit/day**.

These are local optimum derivatives (not changes in the market price of foods).
Diet integers are an explicit **whole-egg** extension only.

## Scope and limitations

- One parameter varies per sweep; no simultaneous-parameter interaction.
- No solver-provided allowable sensitivity intervals are claimed.
- Solver tolerances apply; marginal estimates can be unstable in degenerate
  or ill-conditioned models.
- Nonoptimal cases have no reported objective or variable values.
- The baseline mathematical models are sourced from the lesson; the sensitivity
  calculations and all integers/visualizations are supplementary work.
