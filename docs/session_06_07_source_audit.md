# Sessions 06–07: transcription and mathematical audit

**Provenance:** six-page handwritten student-supplied scan labeled «مدلسازی (۲۶ مهر)»; two classroom meetings. Pages **1–3** were assigned to Session 06 and pages **4–6** to Session 07 by the course participant. The scan is **not** included in this repository. These notes and validations are independent student educational materials, not an instructor-approved transcription.

## Page-specific extraction ledger

| Scan page | Source content | Repository location | Clarifications / independently derived additions |
|---|---|---|---|
| 1 | Fuzzy membership in [0,1]; strong alpha-cut > alpha; support >0; core =1; triangular (1.2,2,2.4); triangular/trapezoidal LR membership | `site_docs/session-06/foundations.{en,fa}.md` | Distinguish strong cuts from conventional weak cuts; reserve lambda for the cut level to avoid confusing it with LR spread alpha; zero-cut uses support closure |
| 2 | LR straight-line derivation, signed scalar/negation and addition; rank-based fuzzy comparison, general linear ranking template | `site_docs/session-06/arithmetic.{en,fa}.md`, `ranking-production` | Explicit negative-scalar endpoint reversal; derive rank as integral of cut midpoints |
| 3 | Rank R = (left-core+right-core)/2 + (right-spread-left-spread)/4; fuzzy two-product profit/resource data, objective and two constraints | `site_docs/session-06/ranking-production.{en,fa}.md` | Profit unit unspecified; rank-based deterministic LP and its optimum are independently calculated |
| 4 | Second fuzzy LP with 4-parameter LR coefficients; Zadeh extension maximum of M=(0,2,5), N=(2,3,4) and first case analysis | `site_docs/session-07/lr-model.{en,fa}.md`, `extension-max` | Distinguish four LR parameters from conventional four trapezoid vertices; solve ranking-based LP independently; derive extension output by alpha-cuts |
| 5 | Complete max membership case analysis; L1 membership distance and Kerre-type comparison; triangular shortcut with ordered modes | `site_docs/session-07/extension-max.{en,fa}.md`, `kerre` | Verify breakpoint z=3.5; make clear extension max != pointwise max of membership functions; exact L1 integrals added independently |
| 6 | Pairwise comparison score r(M,N) = d(M,D) - d(N,D), where D = extension max | `site_docs/session-07/kerre.{en,fa}.md` | Score is pair-dependent; evaluated score 5/4 derived separately |

## Confirmed exact data (page 3)

- Profit per unit: A=(35,40,45), B=(45,50,55).
- Machine-hour coefficients: A=(1.5,2,2.5), B=(0.75,1,1.2); capacity=(98,100,102).
- Raw-material coefficients: A=(0.25,1,1.5), B=(2,2.2,2.5); capacity=(78,80,82).
- Decision variables are nonnegative product quantities, with fuzzy inequalities made explicit as ranking-based inequalities.

The ranking reduction gives objective `(40,50)`, resource rows `(2,0.9875)` and `(0.9375,2.225)`, and bounds `(100,80)`. The optimal ranked point is approximately `(40.718244292,18.798492574)` with rank objective `2568.654400355`.

## Confirmed exact data (page 4)

- Objective LR tuples: `(2,3,1,1)` and `(3,4,1,2)`.
- First inequality: `(1,2,1,1) x1 + (2,3,1,2) x2 <=_R (5,6,2,2)`.
- Second inequality: `(2,3,1,3) x1 + (1,2,1,1) x2 <=_R (4,6,2,1)`.
- Ranked solution: `(77/96,25/16)`, objective `755/96`.

## Extension maximum and Kerre verification

- Inputs `M=(0,2,5)`, `N=(2,3,4)` are triangle endpoint-mode-endpoint triples.
- Exact alpha-cut max: `[2+lambda, max(5-3lambda,4-lambda)]`. Right endpoint switches at `lambda=1/2`.
- Membership curve: `0` outside `(2,5)`, `z-2` on `(2,3]`, `4-z` on `(3,3.5]`, `(5-z)/3` on `(3.5,5)`.
- Distances computed by subdividing the integrals at all corners/intersections: `d(M,D)=3/2`, `d(N,D)=1/4`, `r(M,N)=5/4`.

## Mathematical interpretation and limits

1. The source uses `mu > alpha` for the cut. Many mathematical sources use `mu >= alpha` instead. We name both instead of silently correcting it; at alpha=1 the strict cut is empty.
2. **Handwritten inconsistency (p. 1):** the right-shoulder domain appears to terminate at `aL + beta`, although the accompanying diagram and the right-hand formula use `aU` as the right core endpoint. To preserve a continuous trapezoid with right spread `beta`, the published piecewise formula uses `aU + beta`; this is a documented mathematical correction, not a literal transcription.
3. A four-tuple `(aL,aU,alpha,beta)_LR` uses core/spreads. A conventional trapezoid `(a,b,c,d)` uses support/core endpoints. Mixing them corrupts ranking and constraints.
4. `<=_R` depends on the course's chosen rank functional. This is **not** the same as universally ordering fuzzy numbers, robust constraints or probabilistic chance constraints.
5. The notes' triangular max shortcut depends on ordered modes. The more general and safely reusable algorithm for fuzzy intervals is level-wise `max` of both alpha-cut endpoints.
6. The Kerre score is based on **L1 distance to the extension maximum**, not a pointwise membership maximum and not the Session 06 scalar ranking `R`.
7. The handwritten notes stop before supplying the numerical optima or Kerre integral values. Every such result in this repository is explicitly marked as an independently derived educational supplement.

## Verification

Run `python -m pytest tests/test_session_06_07.py -q`, `python scripts/check_site_docs.py`, `python scripts/build_exam_night.py --check`, and `python -m mkdocs build --strict` from the project root after the local site is updated. Source image itself must not be republished.
