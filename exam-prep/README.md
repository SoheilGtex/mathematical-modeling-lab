# Paper-exam study guide | راهنمای امتحان تشریحی

> **Read this section to prepare for the written exam; no Python is required.**
>
> **این بخش مخصوص مطالعه و پاسخ‌دادن روی کاغذ است؛ برای استفاده از آن به کدنویسی نیازی نیست.**

The source for Session 01 is the four-page handwritten lecture note **`sec1 (1).pdf`**, supplied separately. It **formulates** two models but does not solve them. The worked solutions, hand proofs, and extra exam advice in this directory are **independent educational additions**, **not** claims about what the lecturer covered or what the exam will require. The scanned original is deliberately not committed.

منبع جلسهٔ اول، جزوهٔ دست‌نویس چهارصفحه‌ای `sec1 (1).pdf` است که جداگانه در اختیار دانشجو قرار گرفته. جزوه **دو مدل را تشکیل می‌دهد ولی جواب بهینه را حساب نمی‌کند**؛ راه‌حل‌های تشریحی، اثبات‌های دستی و نکات امتحانی این بخش **تکمیل آموزشی مستقل** هستند، نه نقل‌قول از استاد یا اعلام محدودهٔ قطعی امتحان. فایل اسکن‌شده عمداً در ریپو منتشر نشده است.

## Study order | ترتیب مطالعه

| Order | Topic | فارسی | What you should be able to write |
| --- | --- | --- | --- |
| 1 | [Modeling fundamentals](session_01/00_fundamentals.md) | مبانی مدل‌سازی | Explain decision variables, objective, constraints, feasible solutions, assumptions |
| 2 | [Diet problem](session_01/01_diet.md) | مسئلهٔ رژیم غذایی | Formulate, solve by hand, verify, prove minimum cost |
| 3 | [Boat production](session_01/02_boat_production.md) | مسئلهٔ تولید قایق | Formulate, convert units, solve by hand, verify, prove maximum profit |
| 4 | [Night-before review](session_01/quick_review.md) | مرور شب امتحان | Reproduce both models and all written-answer steps without looking |
| 5 | [Reusable bilingual template](EXAMPLE_TEMPLATE.md) | قالب مثال‌های بعدی | Keep the same written-exam format for each new class problem |

## Format | قالب ثابت

Each worked example includes a complete **English** problem statement and written solution, followed by a complete **Persian** problem statement and written solution. Both contain:

1. Problem data and units / داده‌ها و واحدها
2. Decision variables / متغیرهای تصمیم
3. Objective function / تابع هدف
4. Constraints, each justified / قیود همراه با دلیل
5. Domain and modeling assumptions / دامنه و فرض‌های مدل
6. Mathematical model / مدل نهایی
7. Hand solution and optimality argument / حل دستی و استدلال بهینگی
8. Feasibility and units check / کنترل قیود و واحدها
9. Final answer in ordinary language / پاسخ نهایی با تفسیر
10. Common mistakes and short exam checklist / اشتباهات رایج و چک‌لیست امتحان

**No solver outputs, screenshots, or Python snippets are necessary to write these answers on paper.** They are maintained in [`src/`](../src/modeling_lab/) and [`docs/`](../docs/) as complementary computational materials, unchanged by the exam-prep feature.

**ملاک پاسخ تشریحی:** نوشتن یک عدد بهینه کافی نیست؛ باید مشخص باشد چه چیزی را بهینه می‌کنیم، چه قیودی داریم، چرا جواب مجاز است و چرا هیچ جواب مجازی بهتر نیست. روش اثبات بهینگی در مثال‌های حاضر قابل نوشتن روی کاغذ است و به دوگان‌سازی رسمی یا نرم‌افزار احتیاج ندارد.
