# Mathematical Modeling Lab

[![Python tests](https://github.com/SoheilGtex/mathematical-modeling-lab/actions/workflows/ci.yml/badge.svg)](https://github.com/SoheilGtex/mathematical-modeling-lab/actions/workflows/ci.yml)

**Elementary Mathematical Modeling · Fall 2026 · Kharazmi University**

**Independent course notes and reproducible Python models by Soheil Salmani.**

### [Read the complete course notes →](https://soheilgtex.github.io/mathematical-modeling-lab/)

The documentation opens in **English**. Use the small language selector at the top of any page to read the **complete Persian translation of that same page** (RTL). Dates and the academic term follow each language's calendar: Gregorian in English, Solar Hijri in Persian.

The reader-facing site has a short introduction, a cumulative exam review and two course sessions. Full handwritten-style solutions are available without running Python. Supplementary software explanations are kept in an optional technical section.

| Read | Contents |
| --- | --- |
| [Exam review](https://soheilgtex.github.io/mathematical-modeling-lab/exam/) | One cumulative written-exam guide for both sessions |
| [Session 01](https://soheilgtex.github.io/mathematical-modeling-lab/session-01/) | Fundamentals, diet, and boat production |
| [Session 02](https://soheilgtex.github.io/mathematical-modeling-lab/session-02/) | Transportation and television production (60,000 person-hours) |

**Scope and attribution:** Lecture formulations come from student-supplied notes. Worked optima, optimality proofs, integer variants and the numeric transportation demonstration are independent educational additions. This is not an official university resource. The lecture scans are not redistributed.

---

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
python -m pytest -q
```

**Additional technical notes (source files):** [Sensitivity analysis](docs/sensitivity_analysis.md) ·
[Solution verification](docs/solution_verification.md) ·
[Session 01 model notes](sessions/session_01/computational_notes.md) ·
[Session 02 model notes](sessions/session_02/computational_notes.md)

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
EXAM_NIGHT.md              # source-generated cumulative review (legacy EN/FA source)
sessions/                  # written solutions + per-session review excerpts
examples/                  # runnable Python examples grouped by session
src/modeling_lab/           # reusable model/solver/plot/analysis code
docs/                      # technical documentation source
site_docs/                 # complete English and Persian website pages
mkdocs.yml                  # quiet, bilingual GitHub Pages navigation
templates/                 # written-solution and computational templates
scripts/build_exam_night.py # rebuild / check cumulative exam review
tests/                     # automated regression tests
.github/workflows/ci.yml   # Python 3.11 / 3.12 CI
```

## Academic scope and attribution

The handwritten notes for Session 01 present the **diet** and **boat production**
model formulations, but **do not solve them numerically**. The full handwritten
solutions, optimality arguments, integer-programming variant, visualizations,
and sensitivity experiments are independent educational extensions. The scanned
source notes are not redistributed here.

The single photographed Session 02 page gives a symbolic transport problem and
a TV production example with **60,000 person-hours of labor**, clarified
by the student after the initial transcription of the handwriting was
ambiguous. Numeric transport data in the Python demo are independently
constructed and are not presented as lecture data.

This is **not an official course resource**, exam syllabus, or grading rubric.
The example data are instructional and should not be treated as real-world
nutrition or pricing guidance.

## License

Copyright (c) 2026 Soheil Salmani.

Unless otherwise noted, all original content in this repository,
including Python source code, mathematical models, documentation,
written solutions, and exam preparation materials, is licensed
under the [MIT License](LICENSE).

Third-party materials remain subject to their respective
copyrights and are not relicensed without authorization.
