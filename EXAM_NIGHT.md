# EXAM NIGHT — Mathematical Modeling Only | مرور شب امتحان — فقط مدل‌سازی

> **Instructor clarification:** the examination focuses on **model formulation only**.
> **طبق توضیح استاد:** در امتحان **فقط مدل‌سازی ریاضی** مدنظر است.

This is one cumulative guide for **every course session and assignment**. Define decision variables,
write the objective and all constraints, and specify domains and units. Numerical solutions,
optimality proofs, simplex and software are intentionally excluded from this exam review.
Full worked solutions remain available from the linked pages.

این فایل شامل **تمام جلسات و تمرین‌ها** است. تمرکز مرور بر تعریف متغیرها، تابع هدف،
قیود، واحدها و دامنهٔ متغیرهاست؛ حل عددی و اثبات بهینگی در صفحات کامل باقی می‌مانند.
این مجموعه یک منبع دانشجویی مستقل است، نه بارم‌بندی رسمی امتحان.

**Generated file:** Edit the bilingual files in `review_sources/`, not this file.
Run `python scripts/build_exam_night.py` after adding or changing a session/assignment.

## Contents | فهرست

- [Session 01 | جلسهٔ اول](#session-01)
- [Session 02 | جلسهٔ دوم](#session-02)
- [Session 03 | جلسهٔ سوم](#session-03)
- [Assignment 01 | تمرین اول](#assignment-investment-budget)

---

<a id="session-01"></a>
## Session 01 | جلسهٔ اول

### English

#### Modeling fundamentals

- **Decision variable:** the quantity we choose; identify its meaning, measurement unit and domain.
- **Objective:** an expression to minimize (cost) or maximize (profit).
- **Constraint:** a limited resource uses $\le$; a required minimum uses $\ge$; an exact balance uses $=$.
- **Domain:** declare nonnegativity and use integrality only if the problem explicitly requires whole units.

#### Diet — minimum daily cost

From the [complete diet solution](site_docs/session-01/diet.en.md), let $p,s,t$ represent the quantities of cheese, milk and eggs, respectively. Costs are in toman per day; vitamin A and B requirements are minima.

$$
\boxed{\begin{aligned}
\min\quad&Z=100p+50s+40t\\
\mathrm{s.t.}\quad&p+4s+2t\ge12&&\text{(vitamin A)}\\
&p+2s+3t\ge14&&\text{(vitamin B)}\\
&p,s,t\ge0.
\end{aligned}}
$$

**Why these directions?** Daily cost is minimized while each nutrient intake must be **at least** its required amount.

#### Boat production — maximum profit

In the [boat model and full solution](site_docs/session-01/boats.en.md), $x$ is the number of ordinary boats and $y$ the number of racing boats; profit is measured in **thousand toman**.

$$
\boxed{\begin{aligned}
\max\quad&Z=50x+80y\\
\mathrm{s.t.}\quad&50x+30y\le1000&&\text{(aluminum, kg)}\\
&20x+15y\le300&&\text{(machine, minutes)}\\
&3x+5y\le200&&\text{(labor, hours)}\\
&x,y\ge0.
\end{aligned}}
$$

Convert the available **5 machine-hours to 300 minutes** before writing the machine constraint. The supplied lecture model does not explicitly require integer variables; do not silently add integrality.

### فارسی

#### مبانی مدل‌سازی

- **متغیر تصمیم:** کمیتی که مقدار آن را تعیین می‌کنیم؛ معنا، واحد و دامنه‌اش را بنویسید.
- **تابع هدف:** عبارت هزینه برای کمینه‌سازی یا عبارت سود برای بیشینه‌سازی.
- **قید:** سقف منابع با $\le$، حداقل نیاز با $\ge$ و موازنهٔ دقیق با $=$ نوشته می‌شود.
- **دامنه:** نامنفی بودن را ذکر کنید و فقط وقتی صورت مسئله لازم می‌داند، صحیح بودن را اضافه کنید.

#### رژیم غذایی — کمینه‌سازی هزینهٔ روزانه

در [حل کامل رژیم غذایی](site_docs/session-01/diet.fa.md)، $p$ مقدار پنیر، $s$ مقدار شیر و $t$ مقدار تخم‌مرغ است. هزینه به **تومان در روز** و نیازهای ویتامینی به‌صورت **حداقل** بیان شده‌اند. قید اول مربوط به ویتامین A و قید دوم مربوط به ویتامین B است.

$$
\boxed{\begin{aligned}
\min\quad&Z=100p+50s+40t\\
\mathrm{s.t.}\quad&p+4s+2t\ge12\\
&p+2s+3t\ge14\\
&p,s,t\ge0.
\end{aligned}}
$$

**علت جهت قیود:** هزینه را کمینه می‌کنیم، اما مقدار هر ویتامین باید **دست‌کم** به نیاز تعیین‌شده برسد.

#### تولید قایق — بیشینه‌سازی سود

در [مدل قایق و حل کامل آن](site_docs/session-01/boats.fa.md)، $x$ تعداد قایق معمولی و $y$ تعداد قایق مسابقه‌ای است؛ سود به **هزار تومان** محاسبه می‌شود. سه قید به‌ترتیب مربوط به آلومینیوم (کیلوگرم)، زمان ماشین (دقیقه) و نیروی کار (ساعت) هستند.

$$
\boxed{\begin{aligned}
\max\quad&Z=50x+80y\\
\mathrm{s.t.}\quad&50x+30y\le1000\\
&20x+15y\le300\\
&3x+5y\le200\\
&x,y\ge0.
\end{aligned}}
$$

برای قید زمان ماشین، **۵ ساعت را به ۳۰۰ دقیقه** تبدیل کنید. در مدل ارائه‌شده در جزوه، صحیح بودن متغیرها صریحاً خواسته نشده است؛ آن را بی‌دلیل به مدل اضافه نکنید.

---

<a id="session-02"></a>
## Session 02 | جلسهٔ دوم

### English

#### Transportation — symbolic lecture model

From the [complete transportation explanation](site_docs/session-02/transportation.en.md), let $x_{ij}$ be the shipment from source $i$ to destination $j$, $a_i$ the available supply, $b_j$ the **exact** destination demand and $c_{ij}$ the unit transport cost ($i=1,\ldots,m$, $j=1,\ldots,n$).

$$
\boxed{\begin{aligned}
\min\quad&Z=\sum_{i=1}^{m}\sum_{j=1}^{n}c_{ij}x_{ij}\\
\mathrm{s.t.}\quad&\sum_{j=1}^{n}x_{ij}\le a_i&&\forall i\\
&\sum_{i=1}^{m}x_{ij}=b_j&&\forall j\\
&x_{ij}\ge0&&\forall i,j.
\end{aligned}}
$$

The source limits are **upper bounds**, and every destination's stated requirement is **exact**. This lecture example has no lecturer-provided numerical cost matrix.

#### Television production — profit maximization

For the [television model](site_docs/session-02/televisions.en.md), let $x_1$ and $x_2$ be color and black-and-white televisions. Profit is in USD, labor in person-hours.

$$
\boxed{\begin{aligned}
\max\quad&Z=60x_1+30x_2\\
\mathrm{s.t.}\quad&20x_1+15x_2\le60000&&\text{(labor)}\\
&x_1\le2000&&\text{(color TV limit)}\\
&x_2\le4000&&\text{(black-and-white limit)}\\
&x_1,x_2\ge0.
\end{aligned}}
$$

The labor capacity is **60,000 person-hours**, confirmed from the corrected notes. Do not mix profit units with labor units.

### فارسی

#### حمل‌ونقل — مدل نمادین جزوه

طبق [توضیح کامل مدل حمل‌ونقل](site_docs/session-02/transportation.fa.md)، $x_{ij}$ مقدار ارسال از مبدأ $i$ به مقصد $j$، $a_i$ عرضهٔ موجود، $b_j$ تقاضای **دقیق** مقصد و $c_{ij}$ هزینهٔ حمل هر واحد است ($i=1,\ldots,m$ و $j=1,\ldots,n$).

$$
\boxed{\begin{aligned}
\min\quad&Z=\sum_{i=1}^{m}\sum_{j=1}^{n}c_{ij}x_{ij}\\
\mathrm{s.t.}\quad&\sum_{j=1}^{n}x_{ij}\le a_i&&\forall i\\
&\sum_{i=1}^{m}x_{ij}=b_j&&\forall j\\
&x_{ij}\ge0&&\forall i,j.
\end{aligned}}
$$

موجودی هر مبدأ **حداکثر** میزان قابل ارسال است؛ اما مقدار دریافتی هر مقصد باید **دقیقاً** برابر تقاضای آن باشد. برای این مدل نمادین، جدول هزینهٔ عددی از استاد داده نشده است.

#### تولید تلویزیون — بیشینه‌سازی سود

در [مدل تلویزیون](site_docs/session-02/televisions.fa.md)، $x_1$ تعداد تلویزیون رنگی و $x_2$ تعداد تلویزیون سیاه‌وسفید است. سود بر حسب دلار و زمان کار بر حسب **نفرساعت** است. سه قید به‌ترتیب ظرفیت نیروی کار، سقف تولید رنگی و سقف تولید سیاه‌وسفید را نشان می‌دهند.

$$
\boxed{\begin{aligned}
\max\quad&Z=60x_1+30x_2\\
\mathrm{s.t.}\quad&20x_1+15x_2\le60000\\
&x_1\le2000\\
&x_2\le4000\\
&x_1,x_2\ge0.
\end{aligned}}
$$

ظرفیت نیروی کار طبق تصحیح انجام‌شده در جزوه **۶۰٬۰۰۰ نفرساعت** است. واحد سود را با واحد زمان کار اشتباه نگیرید.

---

<a id="session-03"></a>
## Session 03 | جلسهٔ سوم

### English

#### Numerical transportation — the lecture's 3×4 table

In the [complete numerical transportation problem](site_docs/session-03/transportation.en.md), $x_{ij}$ is the amount shipped from origin $i$ (Tabriz, Yazd, Kerman) to destination $j$ (Tehran, Mashhad, Isfahan, Shiraz). The shipping costs $c_{ij}$ are **in toman per unit**.

$$
C=(c_{ij})=\begin{pmatrix}
80&5&12&15\\
1&9&4&5\\
12&8&6&4
\end{pmatrix},\quad a=(150,300,200),\quad b=(150,200,100,200).
$$

$$
\boxed{\begin{aligned}
\min\quad&Z=\sum_{i=1}^{3}\sum_{j=1}^{4}c_{ij}x_{ij}\\
\mathrm{s.t.}\quad&\sum_{j=1}^{4}x_{ij}\le a_i&&i=1,2,3\\
&\sum_{i=1}^{3}x_{ij}\ge b_j&&j=1,2,3,4\\
&x_{ij}\ge0&&\forall i,j.
\end{aligned}}
$$

Unlike Session 02's symbolic model, this note writes destination demand as **$\ge$**. Both totals equal $650$, so these constraints hold as equalities in any feasible plan **for this data**. Do not change the original inequality directions when initially modeling the question.

#### Five-month production and inventory planning

From the [complete production/inventory formulation](site_docs/session-03/production.en.md), $x_i$ denotes regular production, $y_i$ overtime production and $s_i$ the inventory at the **end** of month $i$. The demand vector is $d=(1200,2100,2400,3000,4000)$. Regular capacity is $2000$ units/month, overtime capacity is $600$ units/month. Unit costs: regular production $10$ toman, overtime $15$ toman, inventory holding $2$ toman per unit carried to the next month.

Set $s_0=s_5=0$ as boundary conditions; $s_1,\ldots,s_4$ are decision variables.

$$
\boxed{\begin{aligned}
\min\quad&Z=10\sum_{i=1}^{5}x_i+15\sum_{i=1}^{5}y_i+2\sum_{i=1}^{4}s_i\\
\mathrm{s.t.}\quad&x_i+y_i+s_{i-1}-s_i=d_i&&i=1,\ldots,5\\
&0\le x_i\le2000&&i=1,\ldots,5\\
&0\le y_i\le600&&i=1,\ldots,5\\
&s_i\ge0&&i=1,\ldots,4\\
&s_0=s_5=0.
\end{aligned}}
$$

There are **14 decision variables**: five $x_i$, five $y_i$ and four $s_i$. The monthly balance equations are **equalities**, not capacity inequalities.

### فارسی

#### حمل‌ونقل عددی — جدول ۳×۴ جزوه

در [مسئلهٔ کامل حمل‌ونقل عددی](site_docs/session-03/transportation.fa.md)، $x_{ij}$ مقدار ارسالی از مبدأ $i$ (**تبریز، یزد، کرمان**) به مقصد $j$ (**تهران، مشهد، اصفهان، شیراز**) است. هزینهٔ حمل $c_{ij}$ به **تومان برای هر واحد** داده شده است.

$$
C=(c_{ij})=\begin{pmatrix}
80&5&12&15\\
1&9&4&5\\
12&8&6&4
\end{pmatrix},\quad a=(150,300,200),\quad b=(150,200,100,200).
$$

$$
\boxed{\begin{aligned}
\min\quad&Z=\sum_{i=1}^{3}\sum_{j=1}^{4}c_{ij}x_{ij}\\
\mathrm{s.t.}\quad&\sum_{j=1}^{4}x_{ij}\le a_i&&i=1,2,3\\
&\sum_{i=1}^{3}x_{ij}\ge b_j&&j=1,2,3,4\\
&x_{ij}\ge0&&\forall i,j.
\end{aligned}}
$$

برخلاف مدل نمادین جلسهٔ دوم، در جزوهٔ این مثال قید تقاضا **$\ge$** نوشته شده است. مجموع عرضه و تقاضا هر دو **۶۵۰** است و در هر جواب مجاز، همهٔ این قیود با تساوی برقرار می‌شوند؛ بااین‌حال هنگام نوشتن **مدل اولیه**، جهت قیود صورت سؤال را حفظ کنید.

#### برنامه‌ریزی تولید و موجودی پنج‌ماهه

طبق [صورت‌بندی کامل تولید و موجودی](site_docs/session-03/production.fa.md)، $x_i$ مقدار تولید عادی، $y_i$ مقدار تولید اضافه‌کاری و $s_i$ موجودی **پایان ماه** $i$ است. تقاضاها $d=(1200,2100,2400,3000,4000)$، ظرفیت تولید عادی ماهانه ۲۰۰۰ و اضافه‌کاری ماهانه ۶۰۰ واحد است. هزینهٔ هر واحد تولید عادی ۱۰ تومان، اضافه‌کاری ۱۵ تومان و نگهداری در انبار ۲ تومان برای هر واحد در ماه است.

شرایط مرزی $s_0=s_5=0$ هستند؛ تنها $s_1,\ldots,s_4$ متغیر تصمیم‌اند.

$$
\boxed{\begin{aligned}
\min\quad&Z=10\sum_{i=1}^{5}x_i+15\sum_{i=1}^{5}y_i+2\sum_{i=1}^{4}s_i\\
\mathrm{s.t.}\quad&x_i+y_i+s_{i-1}-s_i=d_i&&i=1,\ldots,5\\
&0\le x_i\le2000&&i=1,\ldots,5\\
&0\le y_i\le600&&i=1,\ldots,5\\
&s_i\ge0&&i=1,\ldots,4\\
&s_0=s_5=0.
\end{aligned}}
$$

**۱۴ متغیر تصمیم** داریم: پنج تولید عادی، پنج اضافه‌کاری و چهار موجودی پایان ماه. قیود موازنهٔ ماهانه از نوع **تساوی** هستند.

---

<a id="assignment-investment-budget"></a>
## Assignment 01 | تمرین اول

### English

#### Municipal investment budgeting — Assignment 01

See the [complete analytical assignment solution](site_docs/assignments/investment-budget.en.md). The municipality needs $2,4,8,5$ **million USD** at the **start** of years 1–4. It issues interest-bearing long-term securities at coupon rates $7\%,6\%,6.5\%,7.5\%$ and can deposit any unspent funds for one year at returns $6\%,5.5\%,4.5\%$ (years 1–3).

- $x_i\ge0$: millions of USD in long-term securities sold at the start of year $i$, for $i=1,2,3,4$.
- $s_i\ge0$: millions of USD deposited after paying for year $i$, available next year with return, for $i=1,2,3$.

Assuming the same **20 nominal yearly coupon payments** for each issue (no discount rate is provided), define the total coupon-cost objective:

$$
\boxed{\begin{aligned}
\min\quad&Z=20(0.07x_1+0.06x_2+0.065x_3+0.075x_4)\\
\mathrm{s.t.}\quad&x_1-s_1=2\\
&x_2+1.06s_1-s_2=4\\
&x_3+1.055s_2-s_3=8\\
&x_4+1.045s_3=5\\
&x_i\ge0\ (i=1,\ldots,4),\quad s_i\ge0\ (i=1,2,3).
\end{aligned}}
$$

**Modeling explanation:** every year's available funds equal its required spending plus the next deposit. The factors $1.06,1.055,1.045$ include the principal **and** one year's deposit interest. This objective counts nominal coupon expense (not principal repayment or discounted present value). The handout calls the issued instruments “shares,” but because it specifies interest and maturity, the model interprets them as **bond-like interest-bearing securities**; state this assumption.

### فارسی

#### بودجه‌بندی سرمایه‌گذاری شهرداری — تمرین اول

[حل تشریحی کامل تمرین](site_docs/assignments/investment-budget.fa.md) جداگانه موجود است. شهرداری در **ابتدای** سال‌های اول تا چهارم به‌ترتیب به $2,4,8,5$ **میلیون دلار** نیاز دارد. نرخ بهرهٔ اوراق بلندمدت به‌ترتیب $7\%,6\%,6.5\%,7.5\%$ و نرخ سود سپردهٔ یک‌ساله برای سال‌های اول تا سوم $6\%,5.5\%,4.5\%$ است.

- $x_i\ge0$: مبلغ اوراق بلندمدت فروخته‌شده در ابتدای سال $i$، برای $i=1,2,3,4$؛ بر حسب میلیون دلار.
- $s_i\ge0$: مبلغ سپرده‌گذاری‌شده پس از تأمین هزینهٔ سال $i$، برای $i=1,2,3$؛ اصل و سود آن در ابتدای سال بعد وصول می‌شود.

با فرض **۲۰ پرداخت سالانهٔ بهرهٔ اسمی** برای همهٔ اوراق و بدون تنزیل (چون نرخ تنزیل داده نشده)، مدل کامل چنین است:

$$
\boxed{\begin{aligned}
\min\quad&Z=20(0.07x_1+0.06x_2+0.065x_3+0.075x_4)\\
\mathrm{s.t.}\quad&x_1-s_1=2\\
&x_2+1.06s_1-s_2=4\\
&x_3+1.055s_2-s_3=8\\
&x_4+1.045s_3=5\\
&x_i\ge0\ (i=1,\ldots,4),\quad s_i\ge0\ (i=1,2,3).
\end{aligned}}
$$

**علت قیود:** در هر سال «منابع قابل‌استفاده = هزینهٔ پروژه + سپردهٔ جدید»؛ بنابراین هر چهار قید **تساوی** است. ضرایب $1.06,1.055,1.045$ اصل سپرده و سود یک‌سالهٔ آن را در بر می‌گیرند. تابع هدف مجموع **اسمی بهرهٔ اوراق** است، نه بازپرداخت اصل یا ارزش فعلی. در صورت سؤال واژهٔ «سهام» آمده، ولی با توجه به نرخ بهره و سررسید، آن را **اوراق بهره‌دار مشابه بدهی** تفسیر می‌کنیم؛ این فرض باید ذکر شود.
