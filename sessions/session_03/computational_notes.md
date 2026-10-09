# Session 03 — Computational notes | محاسبات جلسهٔ سوم

**Source:** Session 03 has a numerical 3×4 transport problem and a five-month production plan. The numerical data come from the handwritten pages; optimized values and proofs are independently computed. Transportation unit costs are explicitly stated in toman in the source text above the table.

Run from the repository root after installing the package:

```bash
python -m modeling_lab transport-lecture --verify
python -m modeling_lab production-plan --verify
python examples/session_03/01_transportation.py
python examples/session_03/02_production_inventory.py
```

Both are continuous LPs in the lecture. In a balanced transportation instance the source's $\ge$ demand constraints are equivalent to exact equalities. The implementation uses the equality-capable builder from Session 02 (equalities represented by paired inequalities). An equality is **not** being assumed in the general unbalanced case.

Production planning uses $s_0=s_5=0$ and 14 decision variables. All five inventory balance equalities are represented by two inequalities in the common solver class. The **15 mathematical model constraints** mentioned in the lecture comprise 5 regular capacities, 5 overtime capacities and 5 equality balances, without counting nonnegativity. The lower and upper bounds are represented as variable bounds, and the 5 equalities become 10 computational inequalities. This is a representation detail, not a different mathematical model.

**Expected continuous solutions:** transport minimum 2550 toman, production minimum 152300 toman. The paper-and-pencil proofs appear in [transportation](01_transportation.md) and [production](02_production_inventory.md).

**فارسی:** مسئلهٔ حمل‌ونقل جلسهٔ سوم، برخلاف مثال عددیِ ساختگی جلسهٔ دوم، داده‌های عددیِ خود جزوه را دارد. در مدل تولید نیز موجودی فقط برای پایان چهار ماه نخست متغیر است. پاسخ‌های عددی و اثبات بهینگی افزوده‌های مستقل‌اند، نه نقل‌قول مستقیم از استاد.
