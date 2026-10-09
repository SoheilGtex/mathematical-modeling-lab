# Mathematical Modeling Lab

[![Python tests](https://github.com/SoheilGtex/mathematical-modeling-lab/actions/workflows/ci.yml/badge.svg)](https://github.com/SoheilGtex/mathematical-modeling-lab/actions/workflows/ci.yml)

**Introductory Mathematical Modeling · Fall 1405 (2026) · Kharazmi University**

**English / فارسی · Written exam preparation + Python optimization**

An **independent educational repository** combining paper-based mathematical
solutions with reproducible Python implementations. You can study for the
written exam without running any code.

## Start here | از اینجا شروع کن

| I want to... | Go to | توضیح |
| --- | --- | --- |
| **Review for the final exam** | **[EXAM_NIGHT.md](EXAM_NIGHT.md)** | **تنها فایل مرور تجمعی کل ترم** |
| Study full written solutions | [Course sessions](sessions/README.md) | صورت سؤال و حل تشریحی انگلیسی و فارسی |
| Run class examples | [Python examples](examples/session_01/) | اجرای مدل‌ها و مشاهده جواب عددی |
| Explore the reusable code | [Modeling package](src/modeling_lab/) | حل‌کننده، نمودار، حساسیت و اعتبارسنجی |

## Course coverage | جلسات درس

| Session | Written notes (EN/FA) | Runnable examples |
| --- | --- | --- |
| **01 — Foundations, diet, boat production** | [Session 01](sessions/session_01/README.md) | [Session 01 scripts](examples/session_01/) |
| **02 — Transportation, TV production** | [Session 02](sessions/session_02/README.md) | [Session 02 scripts](examples/session_02/) |

New sessions are added as the course progresses.

## Written exam workflow | مطالعهٔ شب امتحان

- **[EXAM_NIGHT.md](EXAM_NIGHT.md)** is the **single cumulative review file**.
  It is assembled in session order from the marked review sections in each
  session's `README.md`.
- Complete hand-worked formulations, solutions, explanations, and optimality
  arguments live in `sessions/session_NN/`. They are provided in **English and Persian**.
- The Python code and technical analyses remain separate: **no programming is
  needed for the paper exam**.

After adding or updating a session, rebuild and check the cumulative review:

```bash
python3 scripts/build_exam_night.py
python3 scripts/build_exam_night.py --check
```

CI checks that `EXAM_NIGHT.md` is up to date. For the process and templates,
see [Sessions](sessions/README.md) and [Templates](templates/).

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

**Computational references:** [Sensitivity analysis](docs/sensitivity_analysis.md) ·
[Solution verification](docs/solution_verification.md) ·
[Session 01 model notes](sessions/session_01/computational_notes.md) ·
[Session 02 model notes](sessions/session_02/computational_notes.md)

## Repository structure

```text
EXAM_NIGHT.md              # single cumulative exam review
sessions/                  # written solutions + per-session review excerpts
examples/                  # runnable Python examples grouped by session
src/modeling_lab/           # reusable model/solver/plot/analysis code
docs/                      # technical documentation
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
