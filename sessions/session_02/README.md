# Session 02 — Transportation and television production | جلسه دوم

**Material received:** one photographed, handwritten page headed “جلسه دوم — مدل‌سازی”. No later pages of Session 02 have been supplied. Only the two problems visible on this page are represented here.

**مبنای این بخش:** یک عکس از یک صفحهٔ دست‌نویسِ جلسهٔ دوم. ممکن است جزوهٔ این جلسه صفحات دیگری هم داشته باشد که هنوز دریافت نشده‌اند. در اینجا فقط همین دو مسئله پوشش داده شده‌اند.

## Read in this order | ترتیب مطالعه

1. [Transportation model — full English/Persian answer](01_transportation.md) — **symbolic model from class; supplemental 2×2 numeric demonstration is invented and marked as such**.
2. [Television production — full English/Persian answer](02_television_production.md) — **labor capacity corrected to 60,000 person-hours; complete written solution**.
3. [Computational notes and commands](computational_notes.md) — optional programming; **not required for the paper exam**.
4. [Single cumulative exam-night review](../../EXAM_NIGHT.md) — generated from the excerpt below, combined with all earlier sessions.

## Source transcription checkpoints | نکات دقیق خوانش تصویر

- **Transportation:** $m$ supply origins, $n$ demand destinations; $a_i$ origin capacities, $b_j$ destination demands, $c_{ij}$ shipping cost per unit, $x_{ij}$ shipped amount. The note writes $\sum_j x_{ij}\le a_i$, $\sum_i x_{ij}=b_j$, $x_{ij}\ge0$.
- **Televisions:** sales limits 2,000 color and 4,000 black-and-white; 20 versus 15 person-hours; profits $60 versus $30. **The student clarified the monthly labor capacity as 60,000 person-hours after an ambiguous initial transcription.**
- The handwritten page **formulates** both models; the explicit optimal solutions and proofs below are original worked additions. The transportation problem has no numerical costs/supplies/demands in the notes.

## Source excerpt for the cumulative review | متن منبع مرور نهایی

<!-- EXAM_NIGHT_START -->

**EN:** Exam-ready summaries only. For fully justified answers, read [Transportation](01_transportation.md) and [Television production](02_television_production.md).

**فارسی:** این بخش مرور سریع است. برای پاسخ تشریحی کامل و اثبات‌ها، [حمل‌ونقل](01_transportation.md) و [تولید تلویزیون](02_television_production.md) را بخوان.

### English — Essential formulations

**1. Transportation (lecture's symbolic example)**

- $x_{ij}$: goods shipped from origin $i$ to destination $j$; $a_i$: origin supply; $b_j$: exact destination demand; $c_{ij}$: unit shipping cost.

$$
\boxed{\begin{aligned}
\min\quad & Z=\sum_{i=1}^{m}\sum_{j=1}^{n}c_{ij}x_{ij}\\
\mathrm{s.t.}\quad&\sum_{j=1}^{n}x_{ij}\le a_i &&\forall i\\
&\sum_{i=1}^{m}x_{ij}=b_j &&\forall j\\
&x_{ij}\ge0 &&\forall i,j.
\end{aligned}}
$$

- Minimum cost: **min**. Source capacity: **$\le$**. Destination demand: **$=$**. Nonnegativity is mandatory.
- Necessary feasibility check: $\sum_i a_i\ge\sum_j b_j$. For a fully connected network with no extra route bounds, this is sufficient for continuous flows too.
- **The lecture provides no numbers for transportation**, so there is no lecturer-specified numeric optimum.

**2. Television production (lecture's production example)**

- $x_1$: color TVs, $x_2$: black-and-white TVs; profit in dollars; labor in person-hours.

$$
\boxed{\begin{aligned}
\max\quad& Z=60x_1+30x_2\\
\mathrm{s.t.}\quad &20x_1+15x_2\le H\\
&x_1\le2000,\quad x_2\le4000\\
&x_1,x_2\ge0.
\end{aligned}}
$$

- **Corrected labor capacity:** $H=60,000$ person-hours, as clarified by the student.
- **Continuous optimum:** $(x_1,x_2)=(2000,4000/3)$ with $Z_{\max}=160,000$. Proof: $Z=2(20x_1+15x_2)+20x_1\le120,000+40,000=160,000$; equality is attained.
- **Integer extension not written in the note:** $(2000,1333)$ with $Z=159,990$; all integer profits are multiples of 30 and $Z\le160,000$.

**Checklist:** define variables with meanings/units; justify objective and each constraint; preserve the inequality directions; check the corrected labor capacity; verify candidate feasibility; prove optimality instead of merely quoting Python.

---

### فارسی — مرور سریع شب امتحان

**۱. مدل حمل‌ونقل (مدل نمادینِ جزوه)**

- $x_{ij}$: مقدار کالای ارسالی از مبدأ $i$ به مقصد $j$.
- $a_i$: ظرفیت مبدأ؛ $b_j$: تقاضای مقصد؛ $c_{ij}$: هزینهٔ واحد حمل.

$$
\boxed{\begin{aligned}
\min\quad&Z=\sum_{i=1}^{m}\sum_{j=1}^{n}c_{ij}x_{ij}\\
\mathrm{s.t.}\quad&\sum_{j=1}^{n}x_{ij}\le a_i\quad\forall i\\
&\sum_{i=1}^{m}x_{ij}=b_j\quad\forall j\\
&x_{ij}\ge0\quad\forall i,j.
\end{aligned}}
$$

- ظرفیت مبدأ $\le$، تقاضای مقصد **تساوی** و تمام متغیرها نامنفی‌اند.
- از جمع قیود، شرط لازم امکان‌پذیری $\sum_i a_i\ge\sum_j b_j$ به دست می‌آید.
- **در جزوه برای این مدل دادهٔ عددی نداریم**؛ جواب بهینهٔ عددی منتسب به استاد وجود ندارد.

**۲. تولید تلویزیون**

- $x_1$: تعداد تلویزیون رنگی؛ $x_2$: تعداد تلویزیون سیاه‌وسفید.

$$
\boxed{\begin{aligned}
\max\quad&Z=60x_1+30x_2\\
\mathrm{s.t.}\quad&20x_1+15x_2\le H\\
&x_1\le2000,\quad x_2\le4000\\
&x_1,x_2\ge0.
\end{aligned}}
$$

- **ظرفیت تصحیح‌شده:** بنا بر اصلاح دانشجو $H=60\,000$ نفرساعت است.
- **مدل پیوسته:** $x_1^*=2000$, $x_2^*=4000/3$ و سود $160\,000$ دلار. **اثبات:** $Z=2(20x_1+15x_2)+20x_1\le160\,000$ و جواب این کران را می‌گیرد.
- **توسعهٔ صحیح‌بودن تعداد دستگاه (نه متن استاد):** $(2000,1333)$ با سود $159\,990$ دلار؛ این مقدار بزرگ‌ترین مضرب ۳۰ِ کمتر از $160\,000$ است.

**چک‌لیست نمره‌آور:** متغیرها، دامنه و واحد را توضیح بده؛ تابع هدف و قیود را از متن استخراج کن؛ جهت نامساوی‌ها را کنترل کن؛ ظرفیت ۶۰٬۰۰۰ نفرساعت را درست بنویس؛ جواب را در تمام قیود جای‌گذاری و **بهینگی را ثابت کن**.

<!-- EXAM_NIGHT_END -->
