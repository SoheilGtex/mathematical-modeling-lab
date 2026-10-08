# Session 01 · Example 2 — Boat production | مسئلهٔ تولید قایق

**Source:** handwritten lecture notes, pp. 3–4. **From the notes:** the production data, linear objective, resource limits, and nonnegative variables; also the interpretation of optimal resource allocation. **Added here:** numerical solution, written optimality proof, resource checks, optional observations. The notes **do not** solve the optimization problem.

---

## ENGLISH — Complete written-exam answer

### A. Problem statement

A workshop produces **regular boats** and **single-person competition boats**. Each type consumes limited aluminum, machine time, and human labor. The per-boat requirements and available resources are:

| Quantity | Regular boat | Competition boat | Total available |
| --- | ---: | ---: | ---: |
| Aluminum | 50 kg | 30 kg | 1,000 kg |
| Machine time | 20 min | 15 min | **5 hours** |
| Human labor | 3 hours | 5 hours | 200 hours |
| Profit | 50,000 toman | 80,000 toman | — |

**Question:** How many boats of each type should the workshop produce to **maximize total profit**? Formulate the mathematical model and solve it.

### B. Decision variables and modeling assumptions

Let

- $x$ = number of regular boats produced;
- $y$ = number of competition boats produced.

The formulation **in the lecture notes** assumes $x,y\ge0$ as continuous quantities. Production resource consumption and profit are assumed proportional to the output. Because actual boats are indivisible, one could additionally require $x,y\in\mathbb Z_{\ge0}$, but this is an **explicit extension**, not a constraint written in the original notes.

### C. Objective function

One regular boat earns 50,000 toman, and one competition boat earns 80,000 toman. If profit $Z$ is measured in **thousand toman**, it is

$$Z=50x+80y.$$

We seek to **maximize** $Z$.

### D. Derivation of constraints

1. **Aluminum:** $50x+30y$ kilograms are used; at most 1,000 kilograms are available:

   $$50x+30y\le1000.$$

2. **Machine time:** one regular boat requires 20 minutes, and one competition boat requires 15 minutes. The available time is **5 hours = 300 minutes**, so

   $$20x+15y\le300.$$

3. **Human labor:** the total number of working hours required cannot exceed 200:

   $$3x+5y\le200.$$

4. **Nonnegative production:**

   $$x\ge0,\qquad y\ge0.$$

All capacity inequalities point toward $\le$, because consumption must **not exceed available resources**.

### E. Complete mathematical formulation

$$
\boxed{\begin{aligned}
\max\quad &Z=50x+80y &&\text{(thousand toman)}\\
\text{s.t.}\quad &50x+30y\le1000 &&\text{(aluminum: kg)}\\
&20x+15y\le300 &&\text{(machine: min)}\\
&3x+5y\le200 &&\text{(labor: hours)}\\
&x,y\ge0.
\end{aligned}}
$$

This is a **linear programming maximization problem**. The original constraints do not require integrality.

### F. Hand solution (without Python or a solver)

**Step 1 — Derive an upper bound on profit.** Since $x\ge0$,

$$
50x+80y
=\frac{16}{3}(20x+15y)-\frac{170}{3}x
\le\frac{16}{3}(20x+15y).
$$

By the machine-time restriction,

$$\frac{16}{3}(20x+15y)\le\frac{16}{3}(300)=1600.$$

Thus **every feasible production plan has profit at most 1,600 thousand toman**.

**Step 2 — Construct a feasible plan that reaches the bound.** To have equality in the first inequality above, take $x=0$. To use all machine capacity,

$$15y=300\ \Longrightarrow\ y=20.$$

The **candidate** is

$$\boxed{(x,y)=(0,20)}.$$

**Step 3 — Verify all requirements, not just machine time.**

| Resource | Use at $(0,20)$ | Capacity | Unused |
| --- | ---: | ---: | ---: |
| Aluminum | $50(0)+30(20)=600$ kg | 1,000 kg | 400 kg |
| Machine | $20(0)+15(20)=300$ min | 300 min | 0 min |
| Labor | $3(0)+5(20)=100$ hours | 200 hours | 100 hours |

Nonnegativity is also satisfied. The corresponding profit is

$$Z=50(0)+80(20)=1600\ \text{thousand toman}
=1{,}600{,}000\ \text{toman}.$$

The candidate is feasible and reaches the proven upper bound, so it is **globally optimal**.

### G. Final answer to write on the exam

> The workshop should produce **0 regular boats and 20 competition boats**. This uses 600 kg of aluminum, 300 minutes of machine time, and 100 hours of labor. The **maximum profit is 1,600 thousand toman (1,600,000 toman)**. Machine time is binding; 400 kg of aluminum and 100 labor hours remain. The upper-bound argument proves optimality.

### H. Alternative paper method: graphical solution (optional extension)

Since there are only two variables, this model can also be solved by a **feasible-region graph**:

1. Draw $x\ge0$ and $y\ge0$ in the first quadrant.
2. The machine-time boundary $20x+15y=300$ intersects the axes at $(15,0)$ and $(0,20)$.
3. The aluminum and labor constraints do not cut off any part of the triangle under that line. To check this without guessing from a drawing, verify both constraints at each of its three vertices.
4. The feasible-region vertices are $(0,0)$, $(15,0)$, and $(0,20)$. Evaluate the linear objective there:

   | Vertex $(x,y)$ | Profit $50x+80y$ (thousand toman) |
   | --- | ---: |
   | $(0,0)$ | $0$ |
   | $(15,0)$ | $750$ |
   | $(0,20)$ | $1600$ |

A linear objective on this bounded polygon has an optimum at a vertex, so **$(0,20)$ gives the maximum**. The preceding algebraic upper-bound proof is an alternative that needs no drawing. This graphical method is **added study material**, not a method shown in the handwritten notes.

### I. Optional extension: integer boats and redundant constraints

- **Integer model:** With $x,y\in\mathbb Z_{\ge0}$, the same answer $(0,20)$ remains optimal, because it is integer and already achieves the continuous model's global upper bound. This is **not** an added constraint in the lecture notes.
- **Why machine time is the bottleneck:** For nonnegative $x,y$, the machine constraint already implies

  $$50x+30y\le\tfrac52(20x+15y)\le750<1000,$$

  $$3x+5y\le\tfrac13(20x+15y)\le100<200.$$

  Thus the aluminum and labor constraints do not further restrict the feasible set for **these particular numbers**. This is extra analysis, not required to transcribe the source model.

### J. Common written-exam mistakes

- Putting $5$ on the right side of a constraint measured in **minutes** instead of using $5\times60=300$.
- Confusing total available resources with resources used *per boat*.
- Forgetting to scale the profit consistently: either $50{,}000x+80{,}000y$ in toman or $50x+80y$ in thousand toman.
- Using $\ge$ for an available-capacity constraint.
- Checking only the machine constraint and omitting aluminum, labor, or nonnegativity.
- Reporting a feasible plan as “optimal” without a proof or bound.
- Claiming integer restrictions appeared in the lecture notes when they did not.

---

## فارسی — پاسخ تشریحی کامل

### الف) صورت مسئله

یک کارگاه دو نوع قایق **معمولی** و **تک‌نفرهٔ مسابقه‌ای** تولید می‌کند. ساخت هر قایق به آلومینیوم، زمان ماشین‌کاری و نیروی انسانی نیاز دارد. اطلاعات مسئله عبارت‌اند از:

| کمیت | قایق معمولی | قایق مسابقه‌ای | موجودی کل |
| --- | ---: | ---: | ---: |
| آلومینیوم | ۵۰ کیلوگرم | ۳۰ کیلوگرم | ۱۰۰۰ کیلوگرم |
| زمان ماشین‌کاری | ۲۰ دقیقه | ۱۵ دقیقه | **۵ ساعت** |
| نیروی انسانی | ۳ ساعت | ۵ ساعت | ۲۰۰ ساعت |
| سود | ۵۰٬۰۰۰ تومان | ۸۰٬۰۰۰ تومان | — |

**خواسته:** تعداد تولید از هر نوع قایق را به‌گونه‌ای تعیین کنید که **سود کل بیشینه** شود. مدل را تشکیل دهید و حل کنید.

### ب) تعریف متغیرهای تصمیم و فرض‌ها

فرض می‌کنیم:

- $x$: تعداد قایق‌های معمولی تولیدی؛
- $y$: تعداد قایق‌های مسابقه‌ای تولیدی.

در **مدل نوشته‌شده در جزوه** فقط $x,y\ge0$ آمده است؛ یعنی مدل پایه به‌صورت پیوسته نوشته شده. فرض می‌کنیم میزان مصرف هر منبع و سود با تعداد قایق‌ها متناسب است. چون قایق را نمی‌توان به‌صورت کسری تولید کرد، می‌توان در **مدل تکمیلی** شرط $x,y\in\mathbb Z_{\ge0}$ را اضافه کرد؛ ولی این قید در جزوهٔ اصلی نوشته نشده است.

### ج) تشکیل تابع هدف

هر قایق معمولی ۵۰ هزار تومان و هر قایق مسابقه‌ای ۸۰ هزار تومان سود دارد. اگر سود $Z$ را **برحسب هزار تومان** بنویسیم:

$$Z=50x+80y.$$

چون هدف کسب بیشترین سود است، تابع هدف باید **ماکزیمم** شود.

### د) استخراج قیود به‌همراه دلیل

۱. **آلومینیوم:** برای $x$ قایق معمولی $50x$ و برای $y$ قایق مسابقه‌ای $30y$ کیلوگرم لازم است. موجودی حداکثر ۱۰۰۰ کیلوگرم است:

$$50x+30y\le1000.$$

۲. **زمان ماشین‌کاری:** هر قایق معمولی ۲۰ دقیقه و هر قایق مسابقه‌ای ۱۵ دقیقه زمان می‌گیرد. کل زمان موجود **۵ ساعت = ۳۰۰ دقیقه** است:

$$20x+15y\le300.$$

۳. **نیروی انسانی:** هر قایق معمولی ۳ ساعت و هر قایق مسابقه‌ای ۵ ساعت کار لازم دارد. حداکثر ۲۰۰ ساعت در اختیار داریم:

$$3x+5y\le200.$$

۴. **نامنفی بودن:** تعداد تولید نمی‌تواند منفی باشد:

$$x\ge0,\qquad y\ge0.$$

**دقت:** همهٔ قیود ظرفیت از نوع $\le$ هستند، چون مصرف منابع نباید از موجودی تجاوز کند.

### هـ) مدل ریاضی نهایی

$$
\boxed{\begin{aligned}
\max\quad &Z=50x+80y &&\text{(هزار تومان)}\\
\text{s.t.}\quad &50x+30y\le1000 &&\text{(آلومینیوم: کیلوگرم)}\\
&20x+15y\le300 &&\text{(ماشین: دقیقه)}\\
&3x+5y\le200 &&\text{(نیروی کار: ساعت)}\\
&x,y\ge0.
\end{aligned}}
$$

این یک **مسئلهٔ برنامه‌ریزی خطی از نوع بیشینه‌سازی** است.

### و) حل دستی مرحله‌به‌مرحله

**گام اول — یافتن کران بالا برای سود.** با توجه به نامنفی بودن $x$، داریم:

$$
50x+80y
=\frac{16}{3}(20x+15y)-\frac{170}{3}x
\le\frac{16}{3}(20x+15y).
$$

از طرفی به دلیل قید زمان ماشین:

$$\frac{16}{3}(20x+15y)\le\frac{16}{3}(300)=1600.$$

پس سود **هیچ برنامهٔ تولید مجازی از ۱۶۰۰ هزار تومان بیشتر نیست**.

**گام دوم — یافتن جوابی که به کران بالا برسد.** برای اینکه در نامساوی اول تساوی برقرار شود، $x=0$ قرار می‌دهیم. برای استفاده از تمام زمان ماشین‌کاری:

$$15y=300\ \Longrightarrow\ y=20.$$

در نتیجه جواب کاندید:

$$\boxed{(x,y)=(0,20)}.$$

**گام سوم — بررسی تمام قیود و محاسبهٔ سود.**

- آلومینیوم: $50(0)+30(20)=600\le1000$؛ **۴۰۰ کیلوگرم باقی می‌ماند**.
- ماشین‌کاری: $20(0)+15(20)=300\le300$؛ **ظرفیت کاملاً مصرف می‌شود**.
- نیروی انسانی: $3(0)+5(20)=100\le200$؛ **۱۰۰ ساعت باقی می‌ماند**.
- نامنفی بودن نیز برقرار است.

سود به‌دست‌آمده:

$$Z=50(0)+80(20)=1600\ \text{هزار تومان}=1{,}600{,}000\ \text{تومان}.$$

چون این جواب هم **مجاز** است و هم به **کران بالای ثابت‌شده** می‌رسد، جواب **بهینهٔ سراسری** است.

### ز) پاسخ نهایی مناسب برگهٔ امتحان

> کارگاه باید **صفر قایق معمولی و ۲۰ قایق مسابقه‌ای** تولید کند. در این حالت ۶۰۰ کیلوگرم آلومینیوم، ۳۰۰ دقیقه ماشین‌کاری و ۱۰۰ ساعت نیروی انسانی مصرف می‌شود. **حداکثر سود ۱۶۰۰ هزار تومان، معادل ۱٬۶۰۰٬۰۰۰ تومان** است. قید زمان ماشین‌کاری فعال است و ۴۰۰ کیلوگرم آلومینیوم و ۱۰۰ ساعت نیروی انسانی باقی می‌ماند. اثبات کران بالا نشان می‌دهد سود بیشتری امکان‌پذیر نیست.

### ح) روش ترسیمی روی کاغذ (روش تکمیلی)

چون مسئله دو متغیر دارد، می‌توان آن را با **رسم ناحیهٔ مجاز** نیز حل کرد:

۱. محورهای $x\ge0$ و $y\ge0$ را در ربع اول رسم می‌کنیم.

۲. خط قید ماشین‌کاری $20x+15y=300$ محور $x$ را در $(15,0)$ و محور $y$ را در $(0,20)$ قطع می‌کند.

۳. قیود آلومینیوم و نیروی انسانی، هیچ قسمت دیگری از مثلث زیر این خط را حذف نمی‌کنند. این موضوع را می‌توان با کنترل هر دو قید در سه رأس مثلث ثابت کرد.

۴. رأس‌های ناحیهٔ مجاز $(0,0)$، $(15,0)$ و $(0,20)$ هستند. تابع هدف را در رأس‌ها محاسبه می‌کنیم:

| رأس $(x,y)$ | سود $50x+80y$ (هزار تومان) |
| --- | ---: |
| $(0,0)$ | $0$ |
| $(15,0)$ | $750$ |
| $(0,20)$ | $1600$ |

چون تابع هدف خطی است و ناحیهٔ مجاز یک چندضلعی کراندار است، حداقل یک جواب بهینه در رأس‌ها وجود دارد. بنابراین **بیشترین سود در رأس $(0,20)$ به دست می‌آید**. اثبات جبری قسمت قبل بدون شکل نیز کامل است. **این روش ترسیمی به‌عنوان مطلب تکمیلی اضافه شده و در متن چهار صفحهٔ جزوه نیامده است.**

### ط) نکات تکمیلی؛ خارج از تشکیل مدل در جزوه

- **مدل صحیح:** اگر شرط $x,y\in\mathbb Z_{\ge0}$ را اضافه کنیم، باز هم $(0,20)$ بهینه می‌ماند؛ زیرا جواب به‌دست‌آمده صحیح است و به کران بالای مدل پیوسته می‌رسد. **این فرض اضافه است.**
- **قید گلوگاه:** قید ماشین‌کاری تعیین‌کننده است. برای $x,y\ge0$ از آن نتیجه می‌شود:

  $$50x+30y\le\tfrac52(20x+15y)\le750<1000,$$

  $$3x+5y\le\tfrac13(20x+15y)\le100<200.$$

  بنابراین با **همین اعداد خاص مسئله**، قیود آلومینیوم و نیروی انسانی ناحیهٔ مجاز را بیشتر محدود نمی‌کنند. این مشاهده جزو توضیحات تکمیلی است، نه چیزی که لازم باشد به متن اصلی جزوه نسبت دهیم.

### ی) اشتباهات رایج در پاسخ تشریحی

- نوشتن $5$ به‌جای $300$ در سمت راست قید **دقیقه‌ای** ماشین‌کاری.
- اشتباه گرفتن مصرف هر قایق با موجودی کل منابع.
- ترکیب نادرست سود ۵۰ هزار و ۸۰ هزار تومان با واحد پول متفاوت.
- استفاده از علامت $\ge$ برای منابعی که سقف ظرفیت دارند.
- بررسی نکردن همهٔ قیود، مخصوصاً نامنفی بودن و موجودی منابع.
- اعلام یک جواب مجاز به‌عنوان بهینه بدون ارائهٔ دلیل.
- نسبت دادن قید صحیح‌بودن به جزوهٔ اصلی.

### مرور فعال / Self-check

بدون نگاه به حل پاسخ بده: چرا قید ماشین $20x+15y\le300$ است؟ چرا تابع هدف به‌صورت $50x+80y$ نوشته شده؟ برای نقطهٔ $(0,20)$ چه منابعی باقی می‌ماند؟ چگونه ثابت می‌کنی هیچ جواب مجازی سودی بیش از ۱۶۰۰ هزار تومان ندارد؟
