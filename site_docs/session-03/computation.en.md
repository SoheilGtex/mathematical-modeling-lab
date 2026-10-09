# Session 03 — Computational Notes

Both problems are solved as **continuous linear programs**; Python provides an independent numerical check of the written work, not a substitute for the hand proofs. The numerical inputs below are **from Session 03's scanned note**.

```bash
python -m modeling_lab transport-lecture --verify
python -m modeling_lab production-plan --verify
```

The first model has 12 variables (3 origins × 4 destinations). Its source uses destination demand inequalities $\ge$; since the numerical total demand equals total supply, the implemented equality formulation is equivalent **for this data**. The older `transport-demo` command instead refers to independently invented Session 02 numbers; do not confuse the two.

The second model has 14 variables: 5 regular-production counts, 5 overtime-production counts and 4 carried-inventory amounts. The boundary inventories $s_0=s_5=0$ are fixed values. The common LP solver represents the five monthly **equalities** as ten inequalities; this does not change the original mathematical constraints.

| Lecture example | Minimum objective | Unit |
| --- | ---: | --- |
| Transportation (3×4) | 2,550 | toman |
| Production/inventory (five months) | 152,300 | toman |

For complete proofs see [numerical transportation](transportation.md) and [production and inventory](production.md).
