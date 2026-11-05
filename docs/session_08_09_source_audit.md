# Sessions 08–09 — Source extraction and correctness audit

**Input:** three-page handwritten scan titled «مدلسازی (۳ آبان)», supplied by a course participant. The original scan is not republished. Teaching-meeting split supplied by the participant; first two pages treated as Session 08, third as Session 09. These reconstructed notes are independent student resources, not official approved solutions.

## Source ledger and overlap check

| New scan page | What is actually written | Relation to the previous 26 Mehr scan | Site location |
| --- | --- | --- | --- |
| 1 | A four-component LR fuzzy LP with two variables; extension-principle maximum for `(0,2,5)` and `(2,3,4)`; membership branches and diagram; start of z-case analysis | Near duplication of previous page 4 | `session-08/extension-recap` and Session 07 cross-reference |
| 2 | z-cases, switch at `3.5`; L1 membership distance; Kerre comparison to the extension maximum; introductory generic max shortcut | Near duplication of previous page 5 | `session-08/distance` and Session 07 cross-reference |
| 3 | `r(M,N)=d(M,D)-d(N,D)`; multiple case-specific integral partitions; **new** worked data `M=(2,5,12)` and `N=(2,4,10)` and four membership branches | Expanded material beyond the old page 6, which stopped shortly after the definition of `r` | `session-09/source-example` and `session-09/case-analysis` |

**No false novelty:** Session 08 is labeled as a rigorous *recap*. A new four-component fuzzy LP is **not** invented from these repeats. Session 09 contains the additional handwritten integration outline and the new example; it is explicitly marked as independently completed beyond the source.

## Audit of the handwritten new example

The two triangles in the source are `M=(2,5,12)` and `N=(2,4,10)`. For a triangular membership with endpoints `(a,b,c)`, the slopes are `1/(b-a)` and `-1/(c-b)`.

- `M_L=(z-2)/3` on `[2,5]`, `M_R=(12-z)/7` on `[5,12]`: consistent.
- `N_L`: manuscript visually shows `1+(z-4)/4`; at `z=2` it gives `1/2`, not `0`. **Mathematically consistent repair:** `(z-2)/2` on `[2,4]`.
- `N_R`: manuscript visually shows `1+(z-4)/(-4)`; at `z=10` it gives `-1/2`, not `0`. **Mathematically consistent repair:** `(10-z)/6` on `[4,10]`.
- **The source supplies neither a completed final integral nor a final comparison score.** Those are separately derived in the site.
- Intersection of the curves in their active regions is `M_L=N_R` at `z=14/3`. The inactive pair `M_R` / `N_L` has no overlapping interior for these data.

## Rigorous completion

Alpha cuts: `M_alpha=[2+3 alpha,12-7 alpha]`, `N_alpha=[2+2 alpha,10-6 alpha]`. For all alpha in `[0,1]`, both `M` cut endpoints dominate `N` endpoints, hence under the **extension-principle maximum** `D=max(M,N)=M`. This does **not** say `mu_M>=mu_N` pointwise.

`d(M,N)` is broken at `2,4,14/3,5,10,12` and equals `1/3 + 1/9 + 1/36 + 95/84 + 2/7 = 17/9`. Thus `d(M,D)=0`, `d(N,D)=17/9`, and the lecture-defined Kerre-style score `r(M,N)=-17/9`, favoring `M`. These are independent corrections/computations, not quoted from the lecturer.

## Methodological hazards

1. Do not confuse maximum of membership functions with maximum of fuzzy variables by extension.
2. The handwritten integral cases depend on branch signs and crossings; ordering modes alone does not justify their application to arbitrary triangles.
3. Use the support-closure at alpha 0 and closed intervals for levels greater than 0.
4. In the source both `(a,b,c)` triangular endpoint notation and four-parameter LR notation are used in different contexts; never identify these tuples by position alone.
5. The term "Kerre-style" refers to the specific distance comparison as introduced in the supplied course notes, not a proof of a globally transitive fuzzy-number order.
6. The Python module uses exact rational piecewise integration and compares against the pre-existing bisection implementation in regression tests.

## Reproduction

Run `python -m pytest tests/test_session_08_09.py -q`, `python scripts/check_site_docs.py`, `python scripts/build_exam_night.py --check` and `python -m mkdocs build --strict` after installation. The site and review remain bilingual.
