# Session 01 — Introduction to Mathematical Modeling | جلسهٔ اول

**Course:** Introductory Mathematical Modeling, Kharazmi University, Fall 1405.

**Source boundary / تفکیک منبع:** The handwritten session-one notes formulate the diet
and boat production problems but do not compute their optimal solutions.
Our hand solutions, proofs, and exam tips are independent educational additions;
these are not a statement of exam coverage or marking criteria.

جزوهٔ اصلی دو مسئله را مدل‌سازی می‌کند، اما جواب بهینهٔ آن‌ها را به دست نمی‌آورد.
حل دستی، اثبات بهینگی و نکات امتحانی زیر افزوده‌های آموزشی هستند، نه نقل‌قول از استاد.

## Start here | ترتیب مطالعه

1. [Fundamentals / مفاهیم پایه](00_fundamentals.md)
2. [Diet — complete written solution EN/FA / رژیم غذایی](01_diet.md)
3. [Boat production — complete written solution EN/FA / تولید قایق](02_boat_production.md)
4. [Computational notes / توضیح روش محاسباتی](computational_notes.md) — optional for the paper exam
5. [One-file exam review / جزوهٔ یکپارچهٔ شب امتحان](../../EXAM_NIGHT.md)

**No programming is needed for the written exam.** The full EN/FA worked
solutions are the primary study material. The review section below is the
source excerpt from which the single term-long `EXAM_NIGHT.md` is generated.

## Source excerpt for the cumulative review | متن منبع مرور نهایی

<!-- EXAM_NIGHT_START -->

**Use this page last**, after reading the full [diet](01_diet.md) and [boat](02_boat_production.md) solutions. This is a **study aid**, not an official syllabus or an official grading rubric.

**این صفحه برای مرور نهایی است**؛ ابتدا حل تشریحی کامل [رژیم غذایی](01_diet.md) و [تولید قایق](02_boat_production.md) را بخوان. مطالب این صفحه جایگزین محدودهٔ رسمی امتحان یا بارم‌بندی استاد نیستند.

## English — What you should be able to reproduce on paper

### Core vocabulary

- **Decision variable:** a quantity chosen by the decision-maker.
- **Objective:** what we minimize or maximize.
- **Constraint:** a required or limiting condition.
- **Feasible:** satisfies all constraints and domain restrictions.
- **Optimal:** feasible and no other feasible choice is better.
- **Binding / active constraint:** equality holds at the reported solution.
- **Slack:** unused resource in a $\le$ capacity constraint; for a $\ge$ minimum constraint, the amount above the minimum is a *surplus*.
- **Operations research:** optimal allocation of limited resources among competing activities (interpretation given in the lecture notes).

### Model 1 — Diet (cost in toman/day)

$$
\begin{aligned}
\min\quad &100p+50s+40t\\
\text{s.t.}\quad&p+4s+2t\ge12\\
&p+2s+3t\ge14\\
&p,s,t\ge0.
\end{aligned}
$$

- $p$ = cheese, $s$ = milk, $t$ = eggs.
- **Optimal:** $(p,s,t)=(0,1,4)$, cost $210$ toman/day.
- **Feasibility:** A $=12$, B $=14$, all variables nonnegative.
- **Why optimal:** multiplying the A constraint by $35/4$ and the B constraint by $15/2$ gives $\frac{65}{4}p+50s+40t\ge210$; since $p\ge0$, the cost is $\ge210$, attained by $(0,1,4)$.

### Model 2 — Boats (profit in thousand toman)

$$
\begin{aligned}
\max\quad&50x+80y\\
\text{s.t.}\quad&50x+30y\le1000\\
&20x+15y\le300\\
&3x+5y\le200\\
&x,y\ge0.
\end{aligned}
$$

- $x$ = regular boats, $y$ = competition boats; **5 hours = 300 minutes**.
- **Optimal:** $(x,y)=(0,20)$, profit $1600$ thousand toman.
- **Feasibility:** uses $600/1000$ kg aluminum, $300/300$ minutes machine time, $100/200$ labor hours.
- **Graphical check:** feasible vertices $(0,0)$, $(15,0)$, $(0,20)$; profits $0$, $750$, $1600$.
- **Why optimal:** $50x+80y=\frac{16}{3}(20x+15y)-\frac{170}{3}x\le\frac{16}{3}(300)=1600$, attained by $(0,20)$.
- The original notes impose $x,y\ge0$ but **do not explicitly require integers**.

### Final written-answer checklist

- [ ] Variables defined, with units and domain
- [ ] Minimize or maximize chosen correctly
- [ ] Every coefficient derived from the statement
- [ ] Every inequality points in the correct direction
- [ ] Hours and minutes converted consistently
- [ ] Complete model written clearly
- [ ] Numerical candidate found and all constraints checked
- [ ] Optimality justified (not only feasibility)
- [ ] Result written with units and interpretation
- [ ] Source assumptions separated from later extensions

---

## فارسی — حفظیات ضروری و مرور سریع

### مفاهیم مهم

- **متغیر تصمیم:** مجهولی که باید مقدار آن تعیین شود.
- **تابع هدف:** کمیتی که قرار است کمینه یا بیشینه شود.
- **قید:** شرط یا محدودیت لازم‌الاجرا در مسئله.
- **جواب مجاز:** جوابی که تمام قیود و شروط دامنه را ارضا کند.
- **جواب بهینه:** جواب مجازی که هیچ جواب مجاز دیگری از آن بهتر نباشد.
- **قید فعال:** قیدی که در جواب موردنظر با تساوی برقرار است.
- **مقدار باقیمانده:** در قید ظرفیت از نوع $\le$، مقدار استفاده‌نشدهٔ منبع؛ در قید حداقل از نوع $\ge$، مقدار اضافه بر حداقل را مازاد می‌گوییم.
- **تحقیق در عملیات:** تخصیص بهینهٔ منابع محدود موجود بین فعالیت‌های رقیب (برداشت مطرح‌شده در جزوه).

### مثال ۱ — رژیم غذایی (هزینه به تومان در روز)

$$
\begin{aligned}
\min\quad&100p+50s+40t\\
\text{s.t.}\quad&p+4s+2t\ge12\\
&p+2s+3t\ge14\\
&p,s,t\ge0.
\end{aligned}
$$

- $p$: پنیر، $s$: شیر، $t$: تخم‌مرغ.
- **جواب بهینه:** $(0,1,4)$، هزینهٔ ۲۱۰ تومان در روز.
- **کنترل قیود:** ویتامین A برابر ۱۲ و ویتامین B برابر ۱۴؛ تمام متغیرها نامنفی‌اند.
- **دلیل بهینگی:** از جمع قید A با ضریب $35/4$ و قید B با ضریب $15/2$ نتیجه می‌شود $\frac{65}{4}p+50s+40t\ge210$؛ با $p\ge0$، هزینه دست‌کم ۲۱۰ است و جواب ما به آن می‌رسد.

### مثال ۲ — تولید قایق (سود به هزار تومان)

$$
\begin{aligned}
\max\quad&50x+80y\\
\text{s.t.}\quad&50x+30y\le1000\\
&20x+15y\le300\\
&3x+5y\le200\\
&x,y\ge0.
\end{aligned}
$$

- $x$: قایق معمولی، $y$: قایق مسابقه‌ای؛ **۵ ساعت = ۳۰۰ دقیقه**.
- **جواب بهینه:** $(0,20)$، سود ۱۶۰۰ هزار تومان.
- **کنترل منابع:** ۶۰۰ از ۱۰۰۰ کیلوگرم آلومینیوم، ۳۰۰ از ۳۰۰ دقیقه ماشین، ۱۰۰ از ۲۰۰ ساعت نیروی انسانی.
- **روش ترسیمی:** رأس‌های ناحیهٔ مجاز $(0,0)$، $(15,0)$، $(0,20)$ با سودهای $0$، $750$، $1600$.
- **دلیل بهینگی:** $50x+80y=\frac{16}{3}(20x+15y)-\frac{170}{3}x\le1600$ و جواب $(0,20)$ به همین مقدار می‌رسد.
- در جزوه فقط $x,y\ge0$ آمده و **صحیح بودن صریحاً ذکر نشده است**.

### چک‌لیست پاسخ تشریحی

- [ ] متغیرها را با معنا، واحد و دامنه تعریف کرده‌ام.
- [ ] تابع هدف را با جهت صحیح مینیمم/ماکزیمم نوشته‌ام.
- [ ] تمام ضرایب را از داده‌های مسئله استخراج کرده‌ام.
- [ ] جهت $\le$ و $\ge$ را با «حداکثر» و «حداقل» تطبیق داده‌ام.
- [ ] ساعت و دقیقه را یکسان کرده‌ام.
- [ ] مدل کامل را یک‌جا نوشته‌ام.
- [ ] جواب عددی را در **تمام قیود** امتحان کرده‌ام.
- [ ] بهینگی را **اثبات** یا به‌اندازهٔ خواستهٔ سؤال توجیه کرده‌ام.
- [ ] پاسخ را با **واحد و تفسیر** نوشته‌ام.
- [ ] فرض‌های تکمیلی را به‌جای متن اصلی جزوه معرفی نکرده‌ام.

### خودآزمایی بدون نگاه‌کردن به پاسخ

۱. تفاوت جواب مجاز و جواب بهینه چیست؟

۲. چرا در رژیم غذایی از $\ge$ و در قایق‌ها از $\le$ استفاده می‌کنیم؟

۳. مدل هر دو مثال را از حافظه بنویس.

۴. با جای‌گذاری عددی، تمام قیود هر دو جواب را بررسی کن.

۵. برای هر مثال، در چند سطر اثبات کن که جواب فقط مجاز نیست، بلکه بهینه است.

۶. اگر در مثال قایق‌ها قید صحیح بودن اضافه شود، آیا جواب تغییر می‌کند؟ **چرا؟**

**برای پاسخ و اثبات کامل، به فایل‌های مثال‌ها مراجعه کن؛ این صفحه عمداً خلاصه است.**

<!-- EXAM_NIGHT_END -->
