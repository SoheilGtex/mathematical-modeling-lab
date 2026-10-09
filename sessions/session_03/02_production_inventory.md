# Five-Month Production and Inventory — Full Written Solution

> **Source:** Session 03, handwritten pages 3–4. Numerical demands, capacities and unit costs are from the note. The five-month optimal schedule, numerical answer and rigorous optimality proof are independent worked additions. No inventory is permitted before month 1 or after month 5.

## Problem statement

A factory plans production over five months. It can produce at most **2,000 units per month** in regular time and **600 additional units per month** in overtime. Regular production costs **10 toman/unit**; overtime costs **15 toman/unit**. Any unit held at the end of a month and carried into the next costs **2 toman/unit per month**. Demands for months 1–5 are **1,200, 2,100, 2,400, 3,000 and 4,000 units**, respectively. Meet all demands on time, with no initial stock and no stock remaining after the fifth month, at minimum total cost.

| Month $i$ | 1 | 2 | 3 | 4 | 5 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Demand $d_i$ | 1,200 | 2,100 | 2,400 | 3,000 | 4,000 |
| Regular capacity | 2,000 | 2,000 | 2,000 | 2,000 | 2,000 |
| Overtime capacity | 600 | 600 | 600 | 600 | 600 |

The total demand is $12,700$ units versus a maximum five-month production capacity of $13,000$ units. Aggregate capacity is necessary but does not by itself verify the month-by-month feasibility of a production plan.

## Decision variables and model

For each month $i=1,\ldots,5$:

- $x_i\ge0$: units made in regular time;
- $y_i\ge0$: units made in overtime;
- $s_i\ge0$: units held at the **end** of month $i$.

The boundary conditions are $s_0=s_5=0$, so $s_5$ is **not an independent variable**. There are 5 regular-production variables, 5 overtime variables and 4 inventory variables: **14 decision variables**. The note states 15 structural constraints before variable nonnegativity (5 regular limits, 5 overtime limits, 5 material-balance equalities).

$$
\boxed{\begin{aligned}
\min\quad Z={}&10\sum_{i=1}^{5}x_i+15\sum_{i=1}^{5}y_i+2\sum_{i=1}^{4}s_i\\
\mathrm{s.t.}\quad &0\le x_i\le2000 &&i=1,\ldots,5\\
&0\le y_i\le600 &&i=1,\ldots,5\\
&x_i+y_i+s_{i-1}-s_i=d_i &&i=1,\ldots,5\\
&s_i\ge0 &&i=1,\ldots,4,\\
&s_0=s_5=0.
\end{aligned}}
$$

In particular, the month-by-month material balances are:

$$
\begin{aligned}
x_1+y_1-s_1&=1200,\\
x_2+y_2+s_1-s_2&=2100,\\
x_3+y_3+s_2-s_3&=2400,\\
x_4+y_4+s_3-s_4&=3000,\\
x_5+y_5+s_4&=4000.
\end{aligned}
$$

**Inventory sign convention:** Incoming stock $s_{i-1}$ helps meet this month's demand; outgoing stock $s_i$ is what remains for the next month and is therefore subtracted. Holding cost is incurred only for $s_1,\ldots,s_4$, not for a fictitious $s_5$.

## Optimal production schedule

| Month | Regular $x_i$ | Overtime $y_i$ | Demand $d_i$ | End stock $s_i$ |
| --- | ---: | ---: | ---: | ---: |
| 1 | 2,000 | 300 | 1,200 | 1,100 |
| 2 | 2,000 | 600 | 2,100 | 1,600 |
| 3 | 2,000 | 600 | 2,400 | 1,800 |
| 4 | 2,000 | 600 | 3,000 | 1,400 |
| 5 | 2,000 | 600 | 4,000 | 0 |
| **Total** | **10,000** | **2,700** | **12,700** | — |

For example, month 2 has $2000+600+1100-1600=2100$ and month 5 has $2000+600+1400=4000$. All bounds hold. The monthly material balances verify feasibility independently of the solver.

The total objective cost is

$$
\begin{aligned}
Z&=10(10000)+15(2700)+2(1100+1600+1800+1400)\\
 &=100000+40500+11800=\boxed{152300\text{ toman}}.
\end{aligned}
$$

## Paper-and-pencil global optimality proof

Let $p_i=15+2(i-1)$, so $p=(15,17,19,21,23)$. Multiply each of the five material-balance equalities by the corresponding $p_i$ and add them. Inventory terms telescope:

$$
\sum_{i=1}^5p_id_i=\sum_{i=1}^5p_i(x_i+y_i)+2\sum_{i=1}^4s_i.
$$

Subtract this identity from the objective formula:

$$
Z=\sum_{i=1}^5p_id_i+\sum_{i=1}^5(10-p_i)x_i+\sum_{i=1}^5(15-p_i)y_i.
$$

Every $10-p_i$ is negative; because $x_i\le2000$, one has $(10-p_i)x_i\ge(10-p_i)2000$. For months 2–5, $15-p_i<0$; because $y_i\le600$, one has $(15-p_i)y_i\ge(15-p_i)600$. For month 1, $15-p_1=0$. Therefore **every feasible plan** satisfies

$$
\begin{aligned}
Z&\ge\sum_{i=1}^5p_id_i+\sum_{i=1}^5(10-p_i)2000
 +\sum_{i=2}^5(15-p_i)600\\
 &=254300-90000-12000=\boxed{152300}.
\end{aligned}
$$

The displayed feasible schedule attains this exact lower bound, proving **global optimality without relying on SciPy**. Because all five regular capacities and overtime capacities in months 2–5 must bind for equality, the schedule is also **unique** (balances fix $y_1$ and the four inventories).

## Exam checkpoints

- Write $s_0=s_5=0$ explicitly; there are **14**, not 15, independent decision variables.
- Monthly balances are **equalities**, not supply inequalities.
- Holding cost is paid on the **four month-end stocks**, not on all five months.
- A feasible five-month schedule must satisfy **each** month's demand on time.
- Distinguish the **lecture model** from our computed optimum and proof; the note does not solve the LP numerically.


---

# برنامه‌ریزی تولید و موجودی پنج‌ماهه — حل تشریحی کامل

> **منبع:** صفحه‌های ۳ و ۴ جزوهٔ جلسهٔ سوم. تقاضا، ظرفیت‌ها و هزینه‌های واحد از جزوه‌اند. برنامهٔ تولید بهینه، پاسخ عددی و اثبات دقیق بهینگی را به‌صورت مستقل به دست آورده‌ایم. موجودی آغاز ماه اول و موجودی پایان ماه پنجم هر دو صفرند.

## صورت مسئله

یک کارخانه باید تولید پنج ماه آینده را برنامه‌ریزی کند. در هر ماه، ظرفیت تولید عادی **۲۰۰۰ واحد** و ظرفیت تولید در اضافه‌کاری **۶۰۰ واحد** است. هزینهٔ تولید عادی **۱۰ تومان** و هزینهٔ تولید اضافه‌کاری **۱۵ تومان** برای هر واحد است. نگهداری هر واحد کالا از پایان یک ماه تا ماه بعد **۲ تومان** هزینه دارد. تقاضای ماه‌های اول تا پنجم به‌ترتیب **۱۲۰۰، ۲۱۰۰، ۲۴۰۰، ۳۰۰۰ و ۴۰۰۰ واحد** است. باید همهٔ تقاضاها به‌موقع تأمین شوند و در پایان ماه پنجم موجودی باقی نماند.

| ماه | اول | دوم | سوم | چهارم | پنجم |
| --- | ---: | ---: | ---: | ---: | ---: |
| تقاضا | ۱۲۰۰ | ۲۱۰۰ | ۲۴۰۰ | ۳۰۰۰ | ۴۰۰۰ |
| ظرفیت عادی | ۲۰۰۰ | ۲۰۰۰ | ۲۰۰۰ | ۲۰۰۰ | ۲۰۰۰ |
| ظرفیت اضافه‌کاری | ۶۰۰ | ۶۰۰ | ۶۰۰ | ۶۰۰ | ۶۰۰ |

تقاضای کل ۱۲٬۷۰۰ واحد و حداکثر ظرفیت تولید پنج‌ماهه ۱۳٬۰۰۰ واحد است. البته کافی بودن ظرفیت کل **به‌تنهایی** نشان نمی‌دهد که تقاضای تک‌تک ماه‌ها به‌موقع تأمین می‌شود.

## تعریف متغیرها و صورت‌بندی

برای ماه $i=1,\ldots,5$ تعریف می‌کنیم:

- $x_i\ge0$: تعداد تولیدشده در ساعت‌های عادی؛
- $y_i\ge0$: تعداد تولیدشده در اضافه‌کاری؛
- $s_i\ge0$: موجودی کالای باقی‌مانده **در پایان** ماه $i$.

طبق فرض مسئله $s_0=s_5=0$ است؛ پس $s_5$ متغیر تصمیم مستقل نیست. در مجموع، **۱۴ متغیر تصمیم** داریم: پنج $x_i$، پنج $y_i$ و چهار $s_i$. همچنین مدل جزوه دارای **۱۵ قید ساختاری** (پنج ظرفیت عادی، پنج ظرفیت اضافه‌کاری و پنج موازنهٔ ماهانه) است؛ شرط نامنفی بودن جداگانه اعمال می‌شود.

$$
\boxed{\begin{aligned}
\min\quad Z={}&10\sum_{i=1}^{5}x_i+15\sum_{i=1}^{5}y_i+2\sum_{i=1}^{4}s_i\\
\mathrm{s.t.}\quad&0\le x_i\le2000 &&i=1,\ldots,5\\
&0\le y_i\le600 &&i=1,\ldots,5\\
&x_i+y_i+s_{i-1}-s_i=d_i &&i=1,\ldots,5\\
&s_i\ge0 &&i=1,\ldots,4,\\
&s_0=s_5=0.
\end{aligned}}
$$

پنج قید موازنه به‌صورت بازشده عبارت‌اند از:

$$
\begin{aligned}
x_1+y_1-s_1&=1200,\\
x_2+y_2+s_1-s_2&=2100,\\
x_3+y_3+s_2-s_3&=2400,\\
x_4+y_4+s_3-s_4&=3000,\\
x_5+y_5+s_4&=4000.
\end{aligned}
$$

**دلیل علامت‌ها:** موجودی ماه پیش $s_{i-1}$ برای پاسخ به تقاضای ماه فعلی در دسترس است؛ موجودی پایان ماه $s_i$ کنار گذاشته می‌شود تا ماه بعد استفاده شود، پس از مقدار در دسترس کم می‌شود. هزینهٔ نگهداری نیز فقط برای $s_1$ تا $s_4$ منظور می‌شود.

## برنامهٔ بهینهٔ تولید

| ماه | تولید عادی $x_i$ | اضافه‌کاری $y_i$ | تقاضا $d_i$ | موجودی پایان ماه $s_i$ |
| --- | ---: | ---: | ---: | ---: |
| اول | ۲۰۰۰ | ۳۰۰ | ۱۲۰۰ | ۱۱۰۰ |
| دوم | ۲۰۰۰ | ۶۰۰ | ۲۱۰۰ | ۱۶۰۰ |
| سوم | ۲۰۰۰ | ۶۰۰ | ۲۴۰۰ | ۱۸۰۰ |
| چهارم | ۲۰۰۰ | ۶۰۰ | ۳۰۰۰ | ۱۴۰۰ |
| پنجم | ۲۰۰۰ | ۶۰۰ | ۴۰۰۰ | ۰ |
| **جمع** | **۱۰٬۰۰۰** | **۲۷۰۰** | **۱۲٬۷۰۰** | — |

برای نمونه، موازنهٔ ماه دوم $2000+600+1100-1600=2100$ و موازنهٔ ماه پنجم $2000+600+1400=4000$ است. همهٔ ظرفیت‌ها رعایت شده‌اند و جدول از نظر قیود ماهانه مجاز است.

هزینهٔ کل:

$$
\begin{aligned}
Z&=10(10000)+15(2700)+2(1100+1600+1800+1400)\\
&=100000+40500+11800=\boxed{152300\text{ تومان}}.
\end{aligned}
$$

## اثبات دستی بهینگی

برای نشان‌دادن اینکه هیچ برنامهٔ مجاز دیگری ارزان‌تر نیست، ضرایب $p_i=15+2(i-1)$ را در نظر می‌گیریم؛ یعنی

$$p=(15,17,19,21,23).$$

هر قید موازنهٔ ماهانه را در ضریب متناظر ضرب می‌کنیم و آن‌ها را جمع می‌زنیم. پس از ساده‌شدن جمله‌های موجودی داریم:

$$
\sum_{i=1}^{5}p_id_i=\sum_{i=1}^{5}p_i(x_i+y_i)+2\sum_{i=1}^{4}s_i.
$$

از این رابطه و تابع هدف به دست می‌آید:

$$
Z=\sum_{i=1}^5p_id_i+\sum_{i=1}^5(10-p_i)x_i+\sum_{i=1}^5(15-p_i)y_i.
$$

چون تمام ضرایب $(10-p_i)$ منفی‌اند و $x_i\le2000$، داریم $(10-p_i)x_i\ge(10-p_i)2000$. همچنین برای ماه‌های دوم تا پنجم، $(15-p_i)<0$ و $y_i\le600$؛ بنابراین $(15-p_i)y_i\ge(15-p_i)600$. در ماه اول ضریب مربوط به $y_1$ برابر صفر است. در نتیجه برای **هر جواب مجاز**:

$$
\begin{aligned}
Z&\ge\sum_{i=1}^5p_id_i+\sum_{i=1}^5(10-p_i)2000
 +\sum_{i=2}^5(15-p_i)600\\
&=254300-90000-12000=\boxed{152300}.
\end{aligned}
$$

برنامهٔ جدولی دقیقاً به این کران پایین می‌رسد؛ بنابراین **بهینهٔ سراسری** است و این نتیجه بدون اجرای پایتون هم اثبات می‌شود. برای برابری، تمام ظرفیت‌های عادی و ظرفیت اضافه‌کاری ماه‌های دوم تا پنجم باید پر شوند؛ با موازنه‌ها، مقدار اضافه‌کاری ماه اول و موجودی‌های چهار ماه هم یکتا تعیین می‌شود. پس این برنامه **جواب بهینهٔ یکتا** است.

## نکات مهم امتحانی

۱. حتماً $s_0=s_5=0$ را بنویسید؛ تعداد متغیرهای مستقل **۱۴** است، نه ۱۵.

۲. موازنهٔ کالا در هر ماه از نوع **تساوی** است؛ زیرا تمام تقاضا باید تأمین شود.

۳. هزینهٔ انبارداری به **چهار موجودی پایان ماه** تعلق می‌گیرد، نه به موجودی پایان ماه پنجم.

۴. تنها بررسی تقاضای کل کافی نیست؛ هر پنج موازنه را با عدد امتحان کنید.

۵. جزوه مدل را ارائه کرده است؛ برنامهٔ تولید بهینه و اثبات بالا حل تکمیلی ما هستند.
