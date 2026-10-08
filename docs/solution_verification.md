# Solution Verification (Feature 04)

The first-session handwritten notes **formulate** the optimization models but
provide no numerical solutions or optimality proofs. This module is an
**independent software extension**, not a claim about what the instructor taught.

## Usage

```bash
python -m modeling_lab diet --verify
python -m modeling_lab boats --verify --json
python -m modeling_lab boats --integer --verify
python -m pytest -q
```

The `--verify` option is opt-in; existing CLI outputs remain unchanged without
it. JSON adds a `verification` object with the computed checks and evidence.
Verification exits with status code 2 if the primal checks fail or a continuous
LP optimality certificate cannot be established. MILP runs can exit successfully
with valid candidates **without claiming independent global optimality**.

## Primal checks

For an LP specified in **standard project form**

\[
 \operatorname{min/max} c^Tx \quad
 \text{s.t.}\; Ax\le b, \quad \ell\le x\le u,
\]

the verification code computes every residual from `LinearProgram` coefficients,
ignoring the `Solution.constraint_slacks` field. It checks:

- Each original inequality violation \(\max(0,(Ax-b)_i)\).
- Each finite lower and upper bound violation.
- Distance to the nearest integer for designated integer variables.
- Agreement between the independently recomputed \(c^Tx\) and the reported
  objective, plus finite values, names, and objective units.

Inequality and bound tolerances are row-scaled: `atol + rtol * max(1, |b_i|,
|a_i| @ |x|)`. The default tolerances are `atol=1e-7`, `rtol=1e-8`, and
`integer_tolerance=1e-6`. These are **numerical acceptance thresholds**, not
mathematical proofs for arbitrary floating-point data. Raw maximum violations
are reported in each row's native physical units; values across different
units should not be compared as if they shared a scale.

## LP primal-dual certificate

A feasible point is not automatically optimal. For continuous LPs we construct
an explicit dual witness, with all finite variable bounds converted into
additional rows of \(Gx\le h\). Let \(d=c\) for minimization and \(d=-c\) for
maximization; then the equivalent primal is

\[
 \min d^Tx \qquad \text{s.t.}\; Gx\le h
\]

with otherwise unrestricted \(x\). A valid dual vector \(\lambda\) satisfies

\[
 \lambda\ge0, \qquad G^T\lambda=-d.
\]

The weak-duality bound for the minimization primal is \(-h^T\lambda\), so

\[
 \text{primal-dual gap}=d^Tx+h^T\lambda\ge0.
\]

If the primal point is feasible, the dual vector is feasible, and the gap is
zero (to the chosen numerical tolerances), global LP optimality is verified.
The code obtains a *candidate* dual using SciPy HiGHS, then **independently
recomputes** dual feasibility, stationarity and the primal-dual gap. It does
not accept HiGHS's `success` flag alone as proof. Solver and verifier still
share floating-point data and code dependencies; this is not a formally
verified or exact-arithmetic proof.

No KKT differentiability assumptions are required for this linear-duality
certificate.

## MILP limitations and solver bounds

MILP candidates are checked independently for feasibility, objective
consistency and integrality. A MILP solver may additionally report a dual
bound and relative gap. This project translates `scipy.optimize.milp`'s
minimization-side bound into the **original objective direction**:

- **Maximize:** solver bound should be an *upper* bound on best feasible profit.
- **Minimize:** solver bound should be a *lower* bound on best feasible cost.

A consistent solver-reported bound is explicitly tagged as
`milp_solver_bound`. It is **not an independently verified global optimality
certificate**: proving the bound valid would require verifying additional
branch-and-bound/cutting-plane evidence or a separate exact method. The field
`independent_optimality_verified` therefore remains `false` for MILPs.

This distinction also applies to the diet extension where only the egg count
is integral.

## Tests

Tests cover correct LP solutions and dual witnesses for both class models,
forged constraint slacks, violated inequalities/bounds, inconsistent objective,
fractional integer decisions, a feasible but suboptimal LP, inconsistent MILP
bound metadata, finite-value checks, and both CLI JSON paths.
