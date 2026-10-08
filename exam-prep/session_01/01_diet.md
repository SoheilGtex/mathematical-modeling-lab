# Session 01 · Example 1 — Minimum-cost diet | مسئلهٔ رژیم غذایی

**Source:** handwritten lecture notes, pp. 1–2. **From the notes:** data, variable meanings, objective, two minimum-vitamin constraints, and nonnegativity. **Added for the exam guide:** explicit paper-and-pencil solution, optimality proof, checks, and study questions. The notes do **not** give a numerical optimum.

---

## ENGLISH — Complete written-exam answer

### A. Problem statement

A daily diet may contain three foods: **cheese**, **milk**, and **eggs**. Each food supplies vitamins A and B. The diet must provide at least **12 units of vitamin A** and **14 units of vitamin B** per day. The cost and vitamin contents **per food unit** are:

| Food | Vitamin A | Vitamin B | Cost (toman/unit) |
| --- | ---: | ---: | ---: |
| Cheese | 1 | 1 | 100 |
| Milk | 4 | 2 | 50 |
| Eggs | 2 | 3 | 40 |

**Question:** Determine the daily amounts of the foods that meet the nutritional requirements at **minimum total cost**. Formulate the optimization model and solve it.

### B. Decision variables and assumptions

Let

- $p$ = number of units of cheese consumed per day;
- $s$ = number of units of milk consumed per day;
- $t$ = number of units of eggs consumed per day.

The **lecture model** allows continuous, nonnegative quantities: $p,s,t\ge0$. It assumes each unit contributes a constant amount of each vitamin and has a constant price. Integer eggs would be an **additional** assumption, not present in the source formulation.

### C. Objective function

The cost of $p$ cheese units is $100p$ toman, of $s$ milk units is $50s$ toman, and of $t$ egg units is $40t$ toman. Therefore the daily total cost is

$$Z=100p+50s+40t.$$

We seek to **minimize** $Z$.

### D. Derivation of every constraint

1. **Vitamin A (minimum 12):** the foods contribute $p$, $4s$, and $2t$ units. Since the requirement is *at least* 12,

   $$p+4s+2t\ge12.$$

2. **Vitamin B (minimum 14):** the foods contribute $p$, $2s$, and $3t$ units. Thus,

   $$p+2s+3t\ge14.$$

3. **Nonnegative food amounts:**

   $$p\ge0,\qquad s\ge0,\qquad t\ge0.$$

**Direction check:** both nutritional constraints use $\ge$ because they are **minimum** requirements.

### E. Complete mathematical formulation

$$
\boxed{\begin{aligned}
\min\quad &Z=100p+50s+40t\\
\text{s.t.}\quad &p+4s+2t\ge12 &&\text{(vitamin A)}\\
&p+2s+3t\ge14 &&\text{(vitamin B)}\\
&p,s,t\ge0.
\end{aligned}}
$$

This is a **linear programming minimization problem**.

### F. Hand solution (without Python or a solver)

**Step 1 — Identify a promising candidate.** Start with $p=0$ and examine a point where both vitamin constraints are tight:

$$4s+2t=12,\qquad2s+3t=14.$$

The first equation gives $2s+t=6$, so $t=6-2s$. Substitute into the second:

$$2s+3(6-2s)=14\ \Longrightarrow\ -4s=-4\ \Longrightarrow\ s=1.$$

Then $t=6-2(1)=4$. Our **candidate** is

$$\boxed{(p,s,t)=(0,1,4)}.$$

**Important:** Solving two equalities gives a candidate, **not by itself a proof of optimality**. We must establish a lower bound on the cost of *every* feasible diet.

**Step 2 — Prove a universal lower bound.** Multiply the vitamin A constraint by $\frac{35}{4}=8.75$ and the vitamin B constraint by $\frac{15}{2}=7.5$. Both multipliers are nonnegative, so the inequality directions are preserved:

$$
\frac{35}{4}(p+4s+2t)+\frac{15}{2}(p+2s+3t)
\ge \frac{35}{4}(12)+\frac{15}{2}(14)=210.
$$

Expanding the left side yields

$$\frac{65}{4}p+50s+40t\ge210.$$

Since $p\ge0$,

$$
Z=100p+50s+40t
=\left(\frac{65}{4}p+50s+40t\right)+\frac{335}{4}p
\ge210.
$$

Hence **every feasible diet costs at least 210 toman/day**.

**Step 3 — Verify that our candidate attains the bound.** At $(p,s,t)=(0,1,4)$:

| Check | Calculation | Result |
| --- | --- | --- |
| Vitamin A | $0+4(1)+2(4)=12$ | $12\ge12$ ✓ |
| Vitamin B | $0+2(1)+3(4)=14$ | $14\ge14$ ✓ |
| Nonnegativity | $0,1,4\ge0$ | Satisfied ✓ |
| Cost | $100(0)+50(1)+40(4)$ | $210$ toman/day |

Because this feasible candidate reaches the universal lower bound of $210$, it is **globally optimal**.

### G. Final answer to write on the exam

> The optimal continuous daily diet consists of **0 units of cheese, 1 unit of milk, and 4 units of eggs**. It provides exactly 12 units of vitamin A and 14 units of vitamin B. The **minimum daily cost is 210 toman**. The constructed lower bound proves that no other feasible diet can be cheaper.

### H. Common written-exam mistakes

- Reversing the $\ge$ sign: these are **minimum** vitamin requirements, not available capacities.
- Mixing up the table columns: milk provides $(A,B)=(4,2)$; eggs provide $(2,3)$.
- Giving only $(0,1,4)$ without defining $p,s,t$ or writing the optimization model.
- Treating simultaneous equalities as an automatic proof of minimum cost.
- Imposing integer restrictions without explaining that this modifies the lecture model.
- Omitting the objective's unit (**toman per day**) and the final interpretation.

---

## فارسی — پاسخ تشریحی کامل

### الف) صورت مسئله

می‌خواهیم یک رژیم غذایی روزانه را از سه مادهٔ **پنیر، شیر و تخم‌مرغ** تشکیل دهیم. بدن روزانه حداقل به **۱۲ واحد ویتامین A** و **۱۴ واحد ویتامین B** نیاز دارد. مقدار ویتامین و هزینهٔ **هر واحد** مادهٔ غذایی در جدول آمده است:

| مادهٔ غذایی | ویتامین A | ویتامین B | هزینهٔ هر واحد (تومان) |
| --- | ---: | ---: | ---: |
| پنیر | ۱ | ۱ | ۱۰۰ |
| شیر | ۴ | ۲ | ۵۰ |
| تخم‌مرغ | ۲ | ۳ | ۴۰ |

**خواسته:** مقدار مصرف روزانهٔ هر ماده را به‌گونه‌ای تعیین کنید که نیاز ویتامین‌ها تأمین و **هزینهٔ کل کمینه** شود. مدل ریاضی را تشکیل دهید و مسئله را حل کنید.

### ب) تعریف متغیرها و فرض‌های مدل

فرض می‌کنیم:

- $p$: تعداد واحد پنیر مصرفی در روز؛
- $s$: تعداد واحد شیر مصرفی در روز؛
- $t$: تعداد واحد تخم‌مرغ مصرفی در روز.

در **مدل جزوه**، متغیرها حقیقی و نامنفی‌اند: $p,s,t\ge0$. فرض شده مقدار ویتامین دریافتی و قیمت با مقدار مصرف متناسب‌اند. صحیح فرض کردن تعداد تخم‌مرغ **فرض اضافه** است و در مدل اصلی جزوه نیامده است.

### ج) تعیین تابع هدف

هزینهٔ پنیر برابر $100p$، هزینهٔ شیر برابر $50s$ و هزینهٔ تخم‌مرغ برابر $40t$ تومان است. پس هزینهٔ کل روزانه:

$$Z=100p+50s+40t.$$

چون می‌خواهیم رژیم غذایی **کم‌هزینه** باشد، تابع هدف باید **مینیمم** شود.

### د) استخراج تک‌تک قیود

۱. **قید ویتامین A:** مقدار تأمین‌شده از پنیر، شیر و تخم‌مرغ به‌ترتیب $p$، $4s$ و $2t$ است. چون حداقل نیاز ۱۲ واحد است:

$$p+4s+2t\ge12.$$

۲. **قید ویتامین B:** مقدار تأمین‌شده از سه ماده به‌ترتیب $p$، $2s$ و $3t$ است. چون حداقل نیاز ۱۴ واحد است:

$$p+2s+3t\ge14.$$

۳. **قید نامنفی بودن:** مقدار مصرف هیچ ماده‌ای نمی‌تواند منفی باشد:

$$p\ge0,\qquad s\ge0,\qquad t\ge0.$$

**دقت:** چون در صورت مسئله عبارت «حداقل نیاز» آمده، جهت نامساوی‌های ویتامین‌ها $\ge$ است.

### هـ) مدل ریاضی نهایی

$$
\boxed{\begin{aligned}
\min\quad &Z=100p+50s+40t\\
\text{s.t.}\quad &p+4s+2t\ge12 &&\text{(ویتامین A)}\\
&p+2s+3t\ge14 &&\text{(ویتامین B)}\\
&p,s,t\ge0.
\end{aligned}}
$$

این یک **مسئلهٔ برنامه‌ریزی خطی از نوع کمینه‌سازی** است.

### و) حل دستی مرحله‌به‌مرحله

**گام اول — پیدا کردن یک جواب کاندید.** برای شروع $p=0$ می‌گذاریم و حالتی را بررسی می‌کنیم که هر دو قید ویتامین با تساوی برقرار باشند:

$$4s+2t=12,\qquad2s+3t=14.$$

از رابطهٔ اول $2s+t=6$، بنابراین $t=6-2s$. جای‌گذاری در رابطهٔ دوم:

$$2s+3(6-2s)=14\ \Longrightarrow\ -4s=-4\ \Longrightarrow\ s=1.$$

در نتیجه $t=4$ و جواب کاندید به دست می‌آید:

$$\boxed{(p,s,t)=(0,1,4)}.$$

**توجه:** صفر گذاشتن $p$ و مساوی گرفتن قیود فقط یک جواب کاندید می‌دهد؛ برای اینکه ثابت کنیم این جواب واقعاً بهینه است، باید نشان دهیم هیچ جواب مجازی هزینهٔ کمتری ندارد.

**گام دوم — اثبات کران پایین هزینه.** قید ویتامین A را در $\frac{35}{4}$ و قید ویتامین B را در $\frac{15}{2}$ ضرب می‌کنیم. چون ضرایب مثبت‌اند، جهت نامساوی‌ها عوض نمی‌شود:

$$
\frac{35}{4}(p+4s+2t)+\frac{15}{2}(p+2s+3t)
\ge\frac{35}{4}(12)+\frac{15}{2}(14)=210.
$$

با جمع‌کردن جملات مشابه:

$$\frac{65}{4}p+50s+40t\ge210.$$

از طرفی $p\ge0$، پس:

$$
Z=100p+50s+40t
=\left(\frac{65}{4}p+50s+40t\right)+\frac{335}{4}p
\ge210.
$$

بنابراین **هزینهٔ هر رژیم غذایی مجاز حداقل ۲۱۰ تومان در روز است**.

**گام سوم — کنترل مجاز بودن جواب و رسیدن به کران.** در نقطهٔ $(0,1,4)$ داریم:

- ویتامین A: $0+4(1)+2(4)=12$؛ قید برقرار است.
- ویتامین B: $0+2(1)+3(4)=14$؛ قید برقرار است.
- نامنفی بودن: $0,1,4\ge0$؛ برقرار است.
- هزینه: $100(0)+50(1)+40(4)=210$ تومان در روز.

چون جواب مجاز ما به کران پایین ۲۱۰ می‌رسد، **بهینگی سراسری آن ثابت می‌شود**.

### ز) پاسخ نهایی مناسب برگهٔ امتحان

> در مدل پیوستهٔ مسئله، رژیم بهینه شامل **صفر واحد پنیر، یک واحد شیر و چهار واحد تخم‌مرغ در روز** است. با این انتخاب، دقیقاً ۱۲ واحد ویتامین A و ۱۴ واحد ویتامین B دریافت می‌شود و **حداقل هزینهٔ روزانه ۲۱۰ تومان** است. با اثبات کران پایین نشان دادیم که هیچ جواب مجازی هزینهٔ کمتری ندارد.

### ح) اشتباهات رایج در پاسخ تشریحی

- استفاده از $\le$ برای قیود ویتامین، درحالی‌که مسئله «حداقل» نیاز را بیان کرده است.
- جابه‌جا خواندن مقادیر ویتامینِ شیر و تخم‌مرغ.
- نوشتن فقط مقادیر متغیرها بدون تعریف آن‌ها یا تابع هدف و قیود.
- فرض کردن اینکه جواب حاصل از برابر گرفتن قیود **حتماً** بهینه است، بدون اثبات.
- افزودن شرط صحیح‌بودن متغیرها بدون توضیح تفاوت آن با جزوه.
- حذف واحد هزینه و تفسیر نهایی جواب.

### مرور فعال / Self-check

بدون نگاه به حل، توضیح بده: چرا قیود ویتامین از نوع $\ge$ هستند؟ چرا $(0,1,4)$ مجاز است؟ چگونه با ترکیب دو قید ثابت می‌شود که $Z\ge210$؟ کدام قسمتِ پاسخ در جزوهٔ اصلی آمده و کدام قسمت حل تکمیلی ماست؟
