# Study sessions | جلسات درس

For the **paper-based written exam**, start with the full bilingual problems
below. No Python is required. Use the single [EXAM_NIGHT.md](../EXAM_NIGHT.md)
only for the final, cumulative review.

**برای امتحان تشریحی،** هر جلسه را از بخش مفاهیم و سپس حل تشریحی کامل
مثال‌های همان جلسه بخوان. در پایان ترم **فقط یک فایل مرور شب امتحان**
خواهی داشت: [EXAM_NIGHT.md](../EXAM_NIGHT.md).

| Session | Topics / مباحث | Full notes |
| --- | --- | --- |
| 01 | Modeling fundamentals, diet, boat production / مبانی مدل‌سازی، رژیم غذایی، تولید قایق | [Session 01](session_01/README.md) |
| 02 | Transportation, TV production / حمل‌ونقل، تولید تلویزیون | [Session 02](session_02/README.md) |

The original four-page session-one note **does not solve** the example models.
Hand solutions and optimality arguments are independently derived educational
extensions; they are not claims about guaranteed exam requirements.

## Adding a new session | افزودن جلسه جدید

1. Create `sessions/session_NN/README.md` (and the complete English/Persian
   written solutions for its examples, starting with the [written template](../templates/written_solution.md)).
2. In that session's README, describe the source and link the full solutions.
   Include exactly one block between the following markers:

   ```markdown
   <!-- EXAM_NIGHT_START -->
   ### English — exam essentials
   ... key definitions, formulations, hand solution checkpoints ...
   ### فارسی — نکات ضروری امتحان
   ... تعاریف، فرمول‌ها، روش دستی و خطاهای رایج ...
   <!-- EXAM_NIGHT_END -->
   ```

3. Run `python3 scripts/build_exam_night.py` from the repository root to
   rebuild the one-file term review. **Do not create a session-specific
   `quick_review.md` or edit `EXAM_NIGHT.md` manually.**
4. Run `python3 scripts/build_exam_night.py --check` and `python -m pytest -q`.
   CI enforces the update so it cannot be forgotten when submitting a PR.
5. For runnable models, add a Python entry under `examples/session_NN/`,
   define its data in `src/modeling_lab/problems.py` or a suitable model module,
   and add regression tests. Use the [computational template](../templates/computational_example.md).
6. Update the two short session-index tables in this file and in the root README.

این روند تضمین می‌کند که با تکمیل هر جلسه، چکیدهٔ آن به یک فایل جامع و مرتب
اضافه شود؛ اما **صحت علمی مطالب هنوز نیازمند بازبینی است** و CI فقط کامل
بودن به‌روزرسانی و اجرای تست‌ها را بررسی می‌کند.
