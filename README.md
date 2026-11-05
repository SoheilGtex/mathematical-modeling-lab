# Mathematical Modeling Lab

[![Python tests](https://github.com/SoheilGtex/mathematical-modeling-lab/actions/workflows/ci.yml/badge.svg)](https://github.com/SoheilGtex/mathematical-modeling-lab/actions/workflows/ci.yml)
[![Julia examples](https://github.com/SoheilGtex/mathematical-modeling-lab/actions/workflows/julia.yml/badge.svg)](https://github.com/SoheilGtex/mathematical-modeling-lab/actions/workflows/julia.yml)

**Elementary Mathematical Modeling · Fall 2026 · Kharazmi University**

**Project contributors: [Soheil Salmani](https://github.com/SoheilGtex) · [Mahdieh Moghiseh](https://github.com/mahdiehmg).**

### [Read the complete course notes →](https://soheilgtex.github.io/mathematical-modeling-lab/)

The documentation opens in **English**. Use the small language selector at the top of any page to read the **complete Persian translation of that same page** (RTL). Dates and the academic term follow each language's calendar: Gregorian in English, Solar Hijri in Persian.

The reader-facing site has a short introduction, two separate period reviews (midterm and final), and the course sessions. Full handwritten-style solutions are available without running Python. Supplementary software explanations are kept in an optional technical section.

**Study:** [Complete course notes](https://soheilgtex.github.io/mathematical-modeling-lab/) — select a session from the site navigation; the home page does not repeat the growing session list.

**Assignments:** [All course assignments](https://soheilgtex.github.io/mathematical-modeling-lab/assignments/) — Assignment 01 has a complete investment-budgeting solution; Assignment 02 only required solving the already documented Session 03 transportation model in Python ([existing code](examples/session_03/01_transportation.py)); Assignment 03 provides the full analytical solution and graphs for triangular fuzzy numbers and their maximum.

**Exam preparation:** [Midterm Review (Sessions 01–09)](https://soheilgtex.github.io/mathematical-modeling-lab/exam/) · [Final Exam Review (Sessions 10 onward)](https://soheilgtex.github.io/mathematical-modeling-lab/exam-final/). The midterm guide includes a one-day plan, worked explanations and an independently authored self-test; the periods never overlap.

**Scope and attribution:** Lecture formulations come from student-supplied notes. Worked optima, optimality proofs, integer variants and the numeric transportation demonstration are independent educational additions. This is not an official university resource. The lecture scans are not redistributed.

---

## Session 06–07: Fuzzy modeling (two lecture meetings)

The six-page, student-supplied handwritten notes (pages 1–3 / pages 4–6) are
reconstructed as **Sessions 06 and 07**. The bilingual site includes all fuzzy-set
membership definitions, alpha-cuts, triangular/trapezoidal LR arithmetic,
rank-based fuzzy linear programs, the extension-principle maximum, and
Kerre-style distance comparison.

- [Session 06: membership, LR arithmetic and production](site_docs/session-06/index.en.md)
- [Session 07: LR optimization, extension max and Kerre](site_docs/session-07/index.en.md)
- [Persian Session 06](site_docs/session-06/index.fa.md) / [Persian Session 07](site_docs/session-07/index.fa.md)
- [Extraction and mathematical audit](docs/session_06_07_source_audit.md)

The scans are **not redistributed**. Ranked LP optima and evaluated integrals are
marked as independently derived supplements, not as handwritten solutions.

## Sessions 08–09: Extension maximum and exact Kerre comparison

The three-page handwritten scan dated 3 Aban substantially repeats the
Session 07 material on its first two pages. **Session 08 is deliberately a
rigorous recap, not a claim of new lecture definitions.** The last page
adds case-split integrals and a new example with triangular fuzzy numbers
$M=(2,5,12)$ and $N=(2,4,10)$. **Session 09** repairs inconsistent handwritten
membership denominators and independently evaluates the score $-17/9$.

- [Session 08 — English](site_docs/session-08/index.en.md) / [فارسی](site_docs/session-08/index.fa.md)
- [Session 09 — English](site_docs/session-09/index.en.md) / [فارسی](site_docs/session-09/index.fa.md)
- [Source overlap and mathematical audit](docs/session_08_09_source_audit.md)

The scan is not redistributed. Distinguish supplied data from independent
corrections and calculations; see the audit before attributing any result.

## Sessions 10–11: Hesitant fuzzy sets and hesitant production modeling

The five-page handwritten scan dated **10 Aban** is split editorially into
**Session 10** (pages 1–3: hesitant fuzzy membership, the tall-student example,
and hesitant fuzzy-number definition) and **Session 11** (pages 4–5: the
trapezoidal ranking formula and a two-product hesitant production model).

- [Session 10 (English)](site_docs/session-10/index.en.md) / [فارسی](site_docs/session-10/index.fa.md)
- [Session 11 (English)](site_docs/session-11/index.en.md) / [فارسی](site_docs/session-11/index.fa.md)
- [Source audit and ambiguous handwritten values](docs/session_10_11_source_audit.md)

**Exam separation:** Sessions 01–09 belong to the [Midterm Review](EXAM_NIGHT.md);
Sessions 10 onward have the independent [Final Exam Review](EXAM_FINAL.md).
Assumed corrections and numerical illustrations are clearly marked as such.

## Julia learning materials

The [Julia learning materials](Julia/README.md) are an optional part of the project. The current
[Basics examples](Julia/01_Basics/) cover variables, control flow, and functions;
Optimization and Course Examples are planned, not yet implemented.

Read the bilingual [Julia guide on the website](https://soheilgtex.github.io/mathematical-modeling-lab/julia/).
The Basics examples require Julia only (no JuMP or HiGHS). Julia and Python
are **optional computational supplements**, not requirements for the written
exam, which focuses on modeling the course sessions **and assignments**.

## Python quick start

Requires **Python 3.11+**.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"

python -m modeling_lab diet --verify
python -m modeling_lab boats --integer --verify
python -m modeling_lab boats --integer --plot plots/boats.png
python -m modeling_lab televisions --verify
python -m modeling_lab televisions --integer --verify
python -m modeling_lab transport-demo --verify
python -m modeling_lab transport-lecture --verify
python -m modeling_lab production-plan --verify
python examples/session_04/01_machine_allocation.py
python examples/session_04/02_crude_oil.py
python examples/session_04/03_revenue_cost_ratio.py
python examples/session_05/01_fractional_charnes_cooper.py
python examples/session_05/02_triangular_fuzzy.py
python examples/session_06/01_membership_and_arithmetic.py
python examples/session_06/02_ranked_production.py
python examples/session_07/01_ranked_lr_lp.py
python examples/session_07/02_extension_kerre.py
python examples/assignments/03_fuzzy_numbers_max.py
python -m pytest -q
```

**Additional technical notes (source files):** [Sensitivity analysis](docs/sensitivity_analysis.md) ·
[Solution verification](docs/solution_verification.md) ·
[Session 01 model notes](sessions/session_01/computational_notes.md) ·
[Session 02 model notes](sessions/session_02/computational_notes.md) ·
[Session 03 model notes](sessions/session_03/computational_notes.md) ·
[Session 04 model notes](sessions/session_04/computational_notes.md) ·
[Session 05 model notes](sessions/session_05/computational_notes.md)

## Build the bilingual documentation locally

```bash
python -m pip install -r requirements-docs.txt
python scripts/check_site_docs.py
python -m mkdocs serve
# Build verification: python -m mkdocs build --strict
```

GitHub Pages publishes the docs using `.github/workflows/pages.yml` after a
successful push to `main`. Configure **Settings → Pages → Build and deployment →
GitHub Actions** once in the repository settings. Both languages use equivalent
paths; the selector stays on the current topic.

When adding a session, add the `*.en.md` and `*.fa.md` pages together, update
`mkdocs.yml` navigation, and run the documentation checks. Keep course-notes
content separate from independently derived solutions. Date labels must use
Gregorian dates in English and Solar Hijri dates in Persian (for example,
**Fall 2026** (EN) / **Autumn 1405 SH** (FA)). Git metadata and the legal MIT copyright year
are not converted.

## Repository structure (for developers)

```text
EXAM_NIGHT.md              # generated Midterm Review, Sessions 01–09
EXAM_FINAL.md              # generated Final Exam Review, Sessions 10 onward
sessions/                  # written solutions + per-session review excerpts
examples/                  # runnable Python examples grouped by session
src/modeling_lab/           # reusable model/solver/plot/analysis code
docs/                      # technical documentation source
site_docs/                 # complete English and Persian website pages
mkdocs.yml                  # quiet, bilingual GitHub Pages navigation
templates/                 # written-solution and computational templates
scripts/build_exam_night.py # rebuild / check BOTH separated period reviews
tests/                     # automated regression tests
.github/workflows/ci.yml   # Python 3.11 / 3.12 CI
```

## Academic scope and attribution

The handwritten notes for Session 01 present the **diet** and **boat production**
model formulations, but **do not solve them numerically**. The full handwritten
solutions, optimality arguments, integer-programming variant, visualizations,
and sensitivity experiments are independent educational extensions. The scanned
source notes are not redistributed here.

Assignment 02 is only the Python implementation of the Session 03 lecture transportation problem, not a new dataset. Assignment 03 separately studies the maximum of two triangular fuzzy numbers using the extension principle; its worked solution is in the assignments section.

The single photographed Session 02 page gives a symbolic transport problem and
a TV production example with **60,000 person-hours of labor**, clarified
by the student after the initial transcription of the handwriting was
ambiguous. Numeric transport data in the Python demo are independently
constructed and are not presented as lecture data.

The four handwritten Session 03 pages contain the numerical transport and five-month
production-planning models. The optimizers and exact hand proofs are independent
educational additions. Both the numerical transport and production costs are stated in toman.

The four-page Session 04 note presents a 3×4 machine allocation LP, a two-crude refinery LP,
and a two-product **linear-fractional** revenue/cost model. The optima and proofs
in this repository are independently derived study additions; the original scan is not redistributed.

The seven-page Session 05 note covers the Charnes–Cooper conversion of linear-fractional
programs and a triangular fuzzy membership function. The fractional optimum and its
proof are independently derived; the note does not specify a fuzzy optimization problem.

This is **not an official course resource**, exam syllabus, or grading rubric.
The example data are instructional and should not be treated as real-world
nutrition or pricing guidance.

## Contributors

Meet the project team in [CONTRIBUTORS.md](CONTRIBUTORS.md).

## License

Copyright (c) 2026 Soheil Salmani.

Unless otherwise noted, all original content in this repository,
including Python source code, mathematical models, documentation,
written solutions, and exam preparation materials, is licensed
under the [MIT License](LICENSE).

Third-party materials remain subject to their respective
copyrights and are not relicensed without authorization.
