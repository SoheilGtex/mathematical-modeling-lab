# Session 03 — Numerical transport and production/inventory | جلسهٔ سوم

**Source:** Four scanned handwritten pages provided for Session 03. Pages 1–2 contain a numerical transportation table and model; pages 3–4 contain the five-month production and inventory formulation. The scanned pages themselves are **not redistributed**.

**محدودهٔ منبع:** چهار صفحهٔ دست‌نویس جلسهٔ سوم بررسی شده‌اند: صفحه‌های ۱ و ۲ مدل حمل‌ونقل عددی و صفحه‌های ۳ و ۴ مدل تولید و موجودی پنج‌ماهه را بیان می‌کنند. تصاویر جزوه در مخزن منتشر نمی‌شوند.

The handwritten material **formulates the LPs**; the optimal shipping plan, production schedule, objective values and optimality proofs are **independently derived** educational additions. The transportation note explicitly gives shipping costs in toman (text above the table).

## Complete solutions | حل‌های کامل

- [Numerical transportation / حمل‌ونقل عددی](01_transportation.md) — 3×4 lecture data; feasible shipments; exact dual-potential proof.
- [Production and inventory / تولید و موجودی](02_production_inventory.md) — 5 months; 14 decision variables; balance equations; exact lower-bound proof.
- [Computational notes / یادداشت‌های محاسباتی](computational_notes.md) — solver commands and interpretation.
- [Cumulative exam review / مرور یکپارچهٔ امتحان](../../EXAM_NIGHT.md) — one file for the entire term.

## Source excerpt for the cumulative review | منبع مرور شب امتحان

<!-- EXAM_NIGHT_START -->

### English — numerical transportation

For the [complete written transportation solution](01_transportation.md), use the cost matrix, origin capacities and destination requirements exactly as transcribed from the note:

$$
C=\begin{pmatrix}80&5&12&15\\1&9&4&5\\12&8&6&4\end{pmatrix},\quad
a=(150,300,200),\quad b=(150,200,100,200).
$$

The note has **origin $\le$**, **destination $\ge$**, and $x_{ij}\ge0$. Both total supply and total demand equal $650$, so all these inequalities become equalities in this specific example.

- **Optimal shipments:** $x_{12}=150$, $x_{21}=150$, $x_{22}=50$, $x_{23}=100$, $x_{34}=200$; all remaining $x_{ij}=0$.
- **Cost:** $\boxed{Z_{\min}=2550}$ toman (currency specified above the table).
- **Written optimality proof:** feasible potentials $u=(0,4,3)$, $v=(-3,5,0,1)$ satisfy $u_i+v_j\le c_{ij}$ and give $\sum_i u_i a_i+\sum_j v_jb_j=2550$.

### English — five-month production and inventory

For the [full written production solution](02_production_inventory.md), the monthly demands are $(1200,2100,2400,3000,4000)$. Let $x_i$ be regular production, $y_i$ overtime production, $s_i$ end-of-month inventory, with $s_0=s_5=0$.

$$
\begin{aligned}
\min\quad&10\sum_{i=1}^{5}x_i+15\sum_{i=1}^{5}y_i+2\sum_{i=1}^{4}s_i\\
\mathrm{s.t.}\quad&x_i\le2000,\quad y_i\le600\\
&x_i+y_i+s_{i-1}-s_i=d_i,\quad x_i,y_i,s_i\ge0.
\end{aligned}
$$

There are **14 independent variables** ($5+5+4$). The source writes 15 structural constraints plus nonnegativity.

- **Optimum:** $x=(2000,2000,2000,2000,2000)$, $y=(300,600,600,600,600)$, $s=(1100,1600,1800,1400)$.
- **Cost:** $\boxed{Z_{\min}=152300\text{ toman}}$.
- **Written proof:** multiply monthly balances by $p=(15,17,19,21,23)$, then use the upper bounds to derive $Z\ge254300-90000-12000=152300$.

### فارسی — حمل‌ونقل عددی

برای [حل کامل حمل‌ونقل](01_transportation.md)، داده‌های جدول بالا را با ترتیب مبدأهای **تبریز، یزد، کرمان** و مقصدهای **تهران، مشهد، اصفهان، شیراز** بخوانید. در جزوه، قیود عرضه $\le$ و قیود تقاضا $\ge$ هستند. چون مجموع هر دو برابر ۶۵۰ است، این قیود در جواب مجاز با تساوی برقرار می‌شوند.

- **برنامهٔ بهینه:** $x_{12}=150$، $x_{21}=150$، $x_{22}=50$، $x_{23}=100$، $x_{34}=200$ و سایر ارسال‌ها صفر.
- **هزینهٔ کمینه:** $\boxed{2550}$ تومان (طبق متن بالای جدول).
- **اثبات بهینگی:** پتانسیل‌های $u=(0,4,3)$ و $v=(-3,5,0,1)$ برای تمام مسیرها $u_i+v_j\le c_{ij}$ را برقرار می‌کنند و کران پایین ۲۵۵۰ می‌سازند.

### فارسی — تولید و موجودی پنج‌ماهه

برای [حل کامل برنامه‌ریزی تولید](02_production_inventory.md)، تقاضای ماه‌ها $(1200,2100,2400,3000,4000)$ است. $x_i$ تولید عادی، $y_i$ تولید اضافه‌کاری و $s_i$ موجودی پایان ماه است؛ $s_0=s_5=0$.

- **تابع هدف:** $10\sum_{i=1}^5x_i+15\sum_{i=1}^5y_i+2\sum_{i=1}^4s_i$.
- **قیود:** $0\le x_i\le2000$، $0\le y_i\le600$ و $x_i+y_i+s_{i-1}-s_i=d_i$ برای هر پنج ماه.
- **تعداد متغیرها:** ۱۴ متغیر مستقل؛ ۱۵ قید ساختاری به‌جز نامنفی بودن.
- **جواب بهینه:** $x=(2000,2000,2000,2000,2000)$، $y=(300,600,600,600,600)$، $s=(1100,1600,1800,1400)$.
- **هزینهٔ کمینه:** $\boxed{152300}$ تومان. **اثبات:** با وزن‌های $p=(15,17,19,21,23)$ برای قیود موازنه و با استفاده از سقف تولیدها، $Z\ge152300$ می‌شود و برنامهٔ بالا به کران می‌رسد.

<!-- EXAM_NIGHT_END -->
