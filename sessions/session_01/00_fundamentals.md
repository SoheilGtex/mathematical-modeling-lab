# Session 01 — Fundamentals of mathematical modeling

**Source coverage:** introductory paragraphs on page 1 and the operations-research interpretation on page 4 of the handwritten notes. The generic checklist and example notations below are added for exam preparation.

## English — Exam-ready theory

### 1. What is mathematical modeling?

Mathematical modeling is the process of representing a real-world problem with mathematical quantities and relationships so that its requirements can be analyzed systematically. The first step is **understanding the problem statement**: what is being requested, what is unknown, and which conditions must be satisfied. A good model must preserve the meaning and units of the original question.

### 2. Components of an optimization model

- **Decision variables:** unknown quantities to be selected, such as food amounts or numbers of boats. State their units and their permitted domains.
- **Objective function:** a mathematical expression measuring the quantity to minimize (e.g., total cost) or maximize (e.g., total profit).
- **Constraints:** equations or inequalities expressing limits or requirements: minimum nutrition, maximum material, available working time, etc.
- **Feasible solution:** a choice of decision variables satisfying **all** constraints, including domain restrictions.
- **Optimal solution:** a feasible solution whose objective value is best among **all** feasible solutions.
- **Assumptions:** simplifications used to translate reality into mathematics, such as constant cost per food unit or proportional resource use per boat.

A common formulation is

$$
\begin{aligned}
\min_{x\in\mathbb R^n}\quad &f(x)\\
\text{subject to}\quad &g_i(x)\le 0\quad (i=1,\ldots,m),\\
&h_j(x)=0\quad (j=1,\ldots,r),\\
&x\in X.
\end{aligned}
$$

For a **linear programming (LP)** model, the objective and functional constraints are linear, and continuous decision variables are typically allowed. Nonnegativity, e.g., $x\ge0$, is a domain restriction. A count may require integer variables in a **different** model, but this must be stated rather than silently assumed.

### 3. How to write a complete descriptive answer

1. Define all decision variables with meaning, unit, and domain.
2. Write the objective and explain why it is minimized or maximized.
3. Derive **every** constraint from the problem data. Watch the inequality directions: *at least* $\Rightarrow\ge$; *at most / available* $\Rightarrow\le$.
4. Convert different units before combining them (e.g., $5$ hours $=300$ minutes).
5. Present the complete mathematical program.
6. If the question requests a numerical solution, solve it and **check every constraint**.
7. Justify optimality, not merely feasibility. A valid upper/lower bound attained by the candidate is a complete proof.
8. State the objective value with units and interpret the decision variables in words.

**A solver reporting “optimal” is not a substitute for the argument required in a handwritten proof.**

### 4. Operations-research interpretation

The lecture note describes operations research in terms of **allocating limited available resources optimally among competing activities**. In the production example the activities are two types of boats, the scarce resources are aluminum, machine time, and labor, and the objective is to maximize profit. Other models may instead minimize cost, time, or loss.

---

## فارسی — مبانی مناسب پاسخ تشریحی

### ۱. مدل‌سازی ریاضی چیست؟

مدل‌سازی ریاضی یعنی بیان یک مسئلهٔ واقعی با استفاده از کمیت‌ها و روابط ریاضی، به‌طوری که بتوان خواسته‌ها و محدودیت‌های آن را منظم بررسی کرد. **اولین مرحله، فهم دقیق صورت مسئله است**: چه چیزی خواسته شده، مجهول‌ها کدام‌اند و چه شرایطی باید برقرار باشد. مدل باید معنای مسئله و واحد کمیت‌ها را حفظ کند.

### ۲. اجزای اصلی یک مدل بهینه‌سازی

- **متغیرهای تصمیم:** مجهول‌هایی که مقدارشان باید انتخاب شود؛ مانند مقدار هر مادهٔ غذایی یا تعداد قایق‌ها. معنا، واحد و دامنهٔ آن‌ها باید تعیین شود.
- **تابع هدف:** رابطه‌ای ریاضی که مقدار موردنظر برای کمینه‌سازی (مثلاً هزینه) یا بیشینه‌سازی (مثلاً سود) را نشان می‌دهد.
- **قیود یا محدودیت‌ها:** تساوی‌ها یا نامساوی‌هایی که شرایط مسئله را بیان می‌کنند؛ مانند حداقل ویتامین یا حداکثر مواد اولیه.
- **جواب مجاز:** مقادیری برای متغیرها که **همهٔ** قیود و شروط دامنه را ارضا می‌کنند.
- **جواب بهینه:** جواب مجازی که مقدار تابع هدف آن در میان **تمام** جواب‌های مجاز بهترین است.
- **فرض‌های مدل‌سازی:** ساده‌سازی‌هایی مانند ثابت بودن هزینهٔ هر واحد یا متناسب بودن مصرف منبع با تعداد محصول.

صورت کلی یک مدل کمینه‌سازی چنین است:

$$
\begin{aligned}
\min_{x\in\mathbb R^n}\quad &f(x)\\
\text{s.t.}\quad &g_i(x)\le 0\quad (i=1,\ldots,m),\\
&h_j(x)=0\quad (j=1,\ldots,r),\\
&x\in X.
\end{aligned}
$$

در **برنامه‌ریزی خطی**، تابع هدف و قیود تابعی خطی‌اند و متغیرها در مدل پیوسته می‌توانند حقیقی باشند. شرطی مانند $x\ge0$ دامنهٔ متغیر را محدود می‌کند. اگر متغیری تعداد اشیای غیرقابل‌تقسیم را نمایش دهد، ممکن است در **مدلی متفاوت** لازم باشد صحیح بودن آن نیز تحمیل شود؛ این فرض نباید بدون توضیح وارد مدل اصلی شود.

### ۳. ترتیب نوشتن پاسخ کامل روی برگه

۱. متغیرهای تصمیم را همراه با معنا، واحد و دامنه تعریف کن.

۲. تابع هدف را بنویس و توضیح بده چرا کمینه یا بیشینه می‌شود.

۳. **تک‌تک قیود** را از داده‌های مسئله استخراج کن. جهت نامساوی را بررسی کن: «حداقل» یعنی $\ge$ و «حداکثر/موجودی» یعنی $\le$.

۴. پیش از نوشتن قید، واحدهای متفاوت را یکسان کن؛ مثلاً $۵$ ساعت $=۳۰۰$ دقیقه.

۵. مدل ریاضی نهایی را یک‌جا بنویس.

۶. اگر یافتن جواب عددی خواسته شده است، مسئله را حل کن و **همهٔ قیود** را برای جواب به‌دست‌آمده کنترل کن.

۷. فقط مجاز بودن جواب کافی نیست؛ باید **بهینگی** آن نیز توجیه شود. اگر کران مناسبی برای تابع هدف پیدا کنی و جواب تو به آن کران برسد، اثبات کامل است.

۸. مقدار بهینه را با واحد بنویس و نتیجه را به زبان مسئله تفسیر کن.

### ۴. ارتباط با تحقیق در عملیات

مطابق توضیح جزوه، تحقیق در عملیات را می‌توان از دید **تخصیص بهینهٔ منابع محدود موجود بین فعالیت‌های رقیب** توصیف کرد. در مثال تولید، فعالیت‌ها ساخت دو نوع قایق و منابع محدود، آلومینیوم و زمان ماشین و نیروی کار هستند. معیار بهینگی در آن مثال بیشینه کردن سود است؛ در مسئله‌ای دیگر می‌تواند کمینه کردن هزینه، زمان یا تلفات باشد.

**نکتهٔ مهم:** توضیحات نظری تکمیلی این صفحه برای یادگیری و پاسخ‌نویسی‌اند؛ جزوهٔ کلاس حدود و سطح دقیق سؤال‌های امتحان را تعیین نکرده است.
