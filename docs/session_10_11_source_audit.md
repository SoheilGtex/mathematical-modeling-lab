# Sessions 10–11: source-by-source audit (10 Aban)

**Input:** five handwritten scanned pages supplied by the student. These pages are not distributed in the repo. **Editorial split:** pages 1–3 Session 10; pages 4–5 Session 11. The page cut is not labeled as a session boundary in the scan.

| Page | Source material | Verification and limitations |
|---|---|---|
| 1 | Definition of HFS, h maps elements to subsets of [0,1]; example X={x1,x2,x3}; five students and crisp tall set | Formalization restricted to finite nonempty subsets. Grades x1={.2,.4,.5}, x2={.3,.4}, x3={.3,.2,.5,.6}. Heights 173,195,181,179,145; threshold >180 selects b,c. |
| 2 | Fuzzy height threshold ramp; hesitant meaning when raters disagree; alternative ramps 140–190 and 150–170 | Exact linear ramps are model reconstructions from drawings, not a claim of a prescribed clinical threshold. |
| 3 | A finite HFS example; hesitant fuzzy-number family; nonempty-intersection condition; trapezoid ranking formula | The mathematical meaning of fuzzy-number intersection is unspecified in handwriting. The finite example is partly hard to read. Rank R1 is exact and checked. |
| 4 | Comparison of two two-component trapezoidal hesitant numbers; two-product factory with fuzzy profit/time/capacity tables | Ranking example: A={(1,3,5,9),(2,4,5,7)}, B={(-1,2,3,8),(2,3,4,9)} -> R(A)=4.5, R(B)=3.75. Possible ambiguity in second A profit and capacity triples. |
| 5 | Production variables, objective and fuzzy capacity inequality | The fuzzy inequality requires a feasibility rule which the scan has not specified. No source optimum is asserted. |

## Critical uncertainties that must remain visible

1. The source sometimes appears to show an upper endpoint **40** following **(50,55,...)**. If so, the tuple fails `left <= mode <= right`. **The reading is not confirmed; do not treat this as an admissible triangle.**
2. The course's ranking `R1` is defined for trapezoidal components with four corners. Its application to triangular coefficients needs an additional mapping, such as `(l,m,m,u)`, which the source does not explicitly state.
3. Aggregating two evaluators with equal weights and ranking a fuzzy constraint as `R(lhs) <= R(rhs)` are additional methodological choices, not automatic mathematical equivalences.
4. The example scenario in the computation page uses **60 as an explicitly assumed missing upper endpoint** and obtains `(profit A,profit B,time A,time B,capacity)=(50,40,2,3,52.5)`. The derived optimum `(26.25,0)` is **independent** and not a transcribed classroom solution.
5. The period boundary—Sessions 01–09 withdrawn midterm, 10+ final—is based on student instruction, **not the PDF**. The site must show the two separate study guides and never merge their contents.

## Editorial standards

- Preserve all source-level definitions and unambiguous numbers.
- Derive math with exact rational arithmetic and validation; keep assumptions separate from source facts.
- Do not silently change the handwritten problem, conflate ordinary fuzzy/HFS/hesitant numbers, or imply uncertain results are source answers.
