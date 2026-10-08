# Mathematical Modeling Lab

**Introductory Mathematical Modeling · Kharazmi University · Fall 1405 (2026)**

Bilingual, paper-exam-ready mathematical solutions **and** reproducible Python
optimization experiments. **Choose one path**; you do not need to understand the
Python code to study for the written exam.

## Choose your path | از کجا شروع کنم؟

| Goal | Open | فارسی |
| --- | --- | --- |
| **Review the whole term before the exam** | **[EXAM_NIGHT.md](EXAM_NIGHT.md)** | **تنها فایل مرور شب امتحان، همه جلسات** |
| Learn a lesson and hand-solve its problems | [Sessions](sessions/README.md) | جزوه کامل انگلیسی و فارسی، گام‌به‌گام |
| Run the actual Python models | [Examples](examples/session_01/) | اجرای حل‌های عددی |
| Understand the mathematical implementation | [Python package](src/modeling_lab/) | مدل، حل‌کننده، ترسیم، حساسیت و اعتبارسنجی |
| Understand cross-cutting technical methods | [Technical docs](docs/) | مستندات فنی |

## Course sessions | جلسات

| Session | Handwritten-exam notes | Computational implementation |
| --- | --- | --- |
| **01 — Introduction, diet, boat production** | [Session 01 (EN/FA)](sessions/session_01/README.md) | [Run examples](examples/session_01/) |

**Source vs. extensions:** The four-page session-01 handwritten notes
formulate the diet and production models but do not compute their optimal
solutions. Full hand solutions, proofs, the integer-model variant, and numerical
experiments here are **independent educational extensions**. The published
repository does not include the scanned original. This material is not an
official exam syllabus or grading rubric.

## One cumulative exam review | فقط یک فایل شب امتحان

**[Read EXAM_NIGHT.md — مرور یکپارچهٔ تمام ترم](EXAM_NIGHT.md)**

There are **no separate `quick_review.md` files**. Each session's `README.md`
contains a marked review excerpt. The standard-library-only generator compiles
all session excerpts in numerical order into the **single, bilingual**
`EXAM_NIGHT.md` at the repository root.

After editing or adding a session, run:

```bash
python3 scripts/build_exam_night.py
python3 scripts/build_exam_night.py --check
```

GitHub Actions rejects stale reviews. Detailed handwritten solutions remain
in `sessions/session_NN/`, so the one-file summary remains concise.
See the [contribution workflow](sessions/README.md#adding-a-new-session--افزودن-جلسه-جدید).

## Python quick start | اجرای کدها

Requires Python **3.11+**.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"

python -m modeling_lab diet --verify
python -m modeling_lab boats --integer --verify
python -m modeling_lab boats --integer --plot plots/boats.png
python -m pytest -q
```

Additional reusable tools:

- [Sensitivity analysis](docs/sensitivity_analysis.md) — parameter sweeps, LP shadow prices, LP/MILP differences.
- [Solution verification](docs/solution_verification.md) — independent feasibility checks and LP dual witnesses.
- [Session 01 computational notes](sessions/session_01/computational_notes.md) — coefficients, assumptions, solver outputs.

## Repository map

```text
EXAM_NIGHT.md               # the ONLY cumulative exam-night review
sessions/                   # sessions, paper solutions EN/FA, session source excerpts
examples/                   # runnable session examples
src/modeling_lab/            # shared mathematical models + SciPy solver tooling
docs/                        # cross-session computational methods
templates/                   # separate written/computational authoring templates
scripts/build_exam_night.py  # build/check the one-file final exam review
tests/                       # automated regression tests
.github/workflows/ci.yml    # Python 3.11 / 3.12 and review synchronization
```

Generated plots under `plots/` are gitignored. Model parameters in the course
examples are pedagogical, not real-world pricing or nutrition advice.
