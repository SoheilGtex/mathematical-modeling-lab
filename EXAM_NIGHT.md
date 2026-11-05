# مرور میان‌ترم

**Midterm Review — Sessions 01–09 and their assigned coursework.**

این مرور برای مطالعهٔ جلسات **۱ تا ۹** و تمرین‌های مربوط به این دوره است.
مرور پایان‌ترم، از جلسهٔ **۱۰** به بعد، در فایل `EXAM_FINAL.md` نگهداری می‌شود.
این نوشته منبع مستقل دانشجویی است، نه اطلاعیه یا بارم‌بندی رسمی آزمون.

**Generated file:** Edit `review_sources/` and `review_guides/`, then run `python scripts/build_exam_night.py`.

## این مرور را چطور بخوانیم؟

این صفحه برای **مطالعهٔ روز قبل از میان‌ترم** نوشته شده است. هدف این نیست که فقط فرمول‌ها را حفظ کنید؛ باید بتوانید یک صورت‌مسئلهٔ تازه را بخوانید و **از صفر مدل ریاضی آن را بسازید**. مطالب جلسات ۱ تا ۹ و تمرین‌های مربوط به این بخش در همین صفحه گرد آمده‌اند. برای مطالعهٔ عمیق‌تر، کنار هر مسئله به صفحهٔ درس لینک داده شده است. مطالب جلسهٔ ۱۰ به بعد در مرور جداگانهٔ پایان‌ترم قرار دارند.

> **دربارهٔ محدودهٔ امتحان:** این راهنمای دانشجویی بر مدل‌سازی تأکید دارد؛ چون در منابع دوره برای مرور قبلی چنین تأکیدی ثبت شده است. زمان، بارم‌بندی و سؤالات قطعی امتحان از این صفحه قابل استنباط نیستند. نتایج عددی‌ای که در بعضی صفحات درس آمده‌اند، لزوماً بخشی از تکلیف امتحانی نیستند.

### نقشهٔ مطالعهٔ یک‌روزه

اگر حدود **۷ تا ۸ ساعت زمان مفید** دارید، این ترتیب را پیشنهاد می‌کنیم؛ بین بخش‌ها استراحت کوتاه در نظر بگیرید. مدت‌ها پیشنهادی‌اند، نه برنامهٔ رسمی درس.

| زمان خالص | کار اصلی | خروجی‌ای که باید روی کاغذ داشته باشید |
| --- | --- | --- |
| ۴۵ دقیقه | قواعد متغیر، تابع هدف، قید و واحد | یک الگوی ثابت برای نوشتن مدل |
| ۷۵ دقیقه | جلسات ۱ و ۲: رژیم غذایی، قایق، حمل‌ونقل نمادین، تلویزیون | چهار مدل از حافظه، با جهت درست نامساوی‌ها |
| ۹۰ دقیقه | جلسات ۳ و ۴: حمل‌ونقل عددی، تولید و انبار، ماشین‌ها و پالایش | متغیرهای اندیس‌دار و موازنه‌ها |
| ۵۵ دقیقه | تابع هدف کسری، چارنز–کوپر و مثال جلسهٔ ۵ | مدل تبدیلی و قید نرمال‌سازی |
| ۸۰ دقیقه | جلسات ۵ و ۶: فازی، برش آلفا، LR و رتبه‌بندی | رسم مثلث و نوشتن تابع عضویت از روی رأس‌ها |
| ۷۰ دقیقه | جلسات ۷ تا ۹: اصل گسترش و Kerre | برش‌های آلفا، بیشینهٔ فازی و تعریف فاصله |
| ۶۰ دقیقه | **آزمون خودآزمایی انتهای صفحه** و بررسی پاسخ‌ها | فهرست شخصیِ اشتباه‌های باقی‌مانده |

اگر زمان کمتر است، **نوشتن کامل مدل‌ها از روی صورت‌مسئله** را بر خواندن مکرر پاسخ‌های آماده مقدم بدانید. برای هر بخش ابتدا چند دقیقه بدون نگاه به فرمول تلاش کنید، سپس پاسخ را با جزوه تطبیق دهید.

### الگوی شش‌مرحله‌ای برای هر سؤال مدل‌سازی

1. **معلوم کنید چه چیزی انتخاب می‌شود.** «تعداد تولید»، «مقدار حمل»، «موجودی پایان ماه» و «مقدار سرمایه‌گذاری» همگی متغیر تصمیم‌اند، نه دادهٔ ثابت.
2. **متغیرها را دقیق تعریف کنید.** برای مثال بنویسید: «$x_{ij}$، تعداد واحد ارسالی از انبار $i$ به مقصد $j$». اندیس‌ها، واحد و بازهٔ شاخص را مشخص کنید.
3. **تابع هدف را از خواستهٔ مسئله بسازید.** «بیشترین سود» یعنی $\max$ و «کمترین هزینه» یعنی $\min$. نسبت درآمد به هزینه با اختلاف درآمد و هزینه یکی نیست.
4. **هر جملهٔ محدودکننده را جدا ترجمه کنید.** «حداکثر/ظرفیت» معمولاً $\le$، «دست‌کم/حداقل» معمولاً $\ge$، و «دقیقاً/تراز» معمولاً $=$ است. جهت نامساوی را با معنای جمله بسنجید، نه با نوع تابع هدف.
5. **دامنه و شرایط مرزی را بنویسید.** نامنفی‌بودن، صحیح‌بودن در صورت لزوم، شاخص‌های زمانی، و موجودی ابتدا یا انتهای افق را حذف نکنید.
6. **مدل را وارسی کنید.** واحد دو طرف قید باید یکسان باشد؛ هر متغیر در جای درستش ظاهر شود و قید ضروری جا نیفتاده باشد.

### چهار اشتباه پرتکرار

- **تفاوت داده و متغیر:** تقاضای ماه سوم ($d_3$) داده است؛ تولید ماه سوم ($x_3$) متغیر است. هیچ‌یک را بی‌دلیل ثابت فرض نکنید.
- **یکسان‌نبودن واحدها:** اگر قید زمان به دقیقه است، ۵ ساعت برابر ۳۰۰ دقیقه است؛ اگر تولید با ساعت بر واحد سنجیده می‌شود، ضریب هر متغیر باید با همان واحد باشد.
- **جابجایی جمع‌ها:** در حمل‌ونقل، جمع روی مقصدها برای *مبدأ ثابت* محدودیت عرضه است؛ جمع روی مبدأها برای *مقصد ثابت* قید تقاضاست.
- **حذف شرایط ابتدا و انتها:** در تولید و موجودی پنج‌ماهه، $s_0=s_5=0$ جزئی از مدل است و متغیرهای موجودی تصمیم فقط $s_1$ تا $s_4$ هستند.

### روش مطالعهٔ مطالب فازی

در فرمول‌های بازه‌ای این مرور، اگر $\alpha=0$ نوشته شده باشد، **بستهٔ تکیه‌گاه** مراد است؛ زیرا تعریف سادهٔ $\{x:\mu(x)\ge0\}$ روی فضای مرجع برابر کل فضا می‌شود.


ترتیب منطقی این بخش چنین است: **تابع عضویت ← عدد مثلثی و ذوزنقه‌ای ← برش آلفا و LR ← رتبه‌بندی ← تبدیل قید فازی ← اصل گسترش ← روش Kerre**. اگر در مرحله‌ای گیر کردید، به مفهوم مرحلهٔ قبل برگردید. هنگام تبدیل یک مدل فازی به مدل قطعی، حتماً مشخص کنید **از کدام قاعدهٔ مقایسه** استفاده می‌کنید؛ بدون این انتخاب، تبدیل یکتا نیست.

---

## How to study this review the day before the midterm

This is a **one-day study guide** for Sessions 01–09 and the assignments belonging to that period. Read it to learn how to *formulate* a model from a new word problem, not just recognize a completed solution. The Session 10+ material has its own separate final-exam review.

> **Scope caveat:** The recorded instructor clarification for the earlier review emphasized mathematical formulation. This independent student resource does not establish an official examination date, syllabus, grading distribution, or promised question types.

### Suggested seven-to-eight-hour plan

| Focus | Suggested time | Written deliverable |
| --- | --- | --- |
| Formulation principles | 45 min | One template for variables, objectives, constraints, and domains |
| Sessions 01–02 | 75 min | Diet, boats, symbolic transportation, and televisions |
| Sessions 03–04 | 90 min | Indexed transportation, inventory balances, machine allocation, refining |
| Fractional objectives and Charnes–Cooper | 55 min | Correct scaling and normalization constraint |
| Fuzzy foundations and LR numbers | 80 min | Membership graph, alpha-cuts, rank-based model |
| Extension principle and Kerre | 70 min | Alpha-cut maximum, distance and comparison criterion |
| Self-test and correction | 60 min | Corrected handwritten models, not just reread notes |

### Six-step formulation checklist

1. Identify what the decision maker chooses, rather than what is given as data.
2. Define variables, indices, units, and their domains.
3. Translate the objective into a minimum, maximum, or explicit ratio.
4. Translate each capacity, minimum requirement, and exact balance into an appropriately directed constraint.
5. Add nonnegativity, integrality **only when warranted**, and all boundary conditions.
6. Check dimensional consistency, missing constraints, and whether the fuzzy comparison rule is specified.

For formulas written at $\alpha=0$, interpret the interval as the **closure of support**; the literal set $\{x:\mu(x)\ge0\}$ would otherwise be the entire universe.

**Common traps:** reversing supply and demand sums, confusing an inventory balance with a capacity limit, omitting the constant in a fractional objective, treating LR spreads as endpoints, or replacing the extension-principle maximum with a pointwise maximum of memberships.

---

## فهرست جلسات | Contents

- [Session 01 | جلسهٔ اول](#session-01)
- [Session 02 | جلسهٔ دوم](#session-02)
- [Session 03 | جلسهٔ سوم](#session-03)
- [Session 04 | جلسهٔ چهارم](#session-04)
- [Session 05 | جلسهٔ پنجم](#session-05)
- [Session 06 | جلسهٔ ششم](#session-06)
- [Session 07 | جلسهٔ هفتم](#session-07)
- [Session 08 | جلسهٔ هشتم](#session-08)
- [Session 09 | جلسهٔ نهم](#session-09)
- [Assignment 01 | تمرین اول](#assignment-investment-budget)
- [Assignment 02 | تمرین دوم](#assignment-transportation-python)
- [Assignment 03 | تمرین سوم](#assignment-fuzzy-numbers-max)

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

#### از متن سؤال تا مدل: روش حل جلسهٔ اول

در **مسئلهٔ رژیم غذایی** اول بپرسید «چه مقدار از هر مادهٔ غذایی خریداری کنیم؟»؛ پاسخ همین سؤال، سه متغیر $p,s,t$ را مشخص می‌کند. سپس هزینهٔ هر واحد را در مقدار خرید آن ضرب کنید و جمع بزنید. به همین دلیل تابع هدف $100p+50s+40t$ است. حالا ردیف نیاز به ویتامین A را مستقل بخوانید: هر واحد پنیر ۱، شیر ۴ و تخم‌مرغ ۲ واحد ویتامین A تأمین می‌کند و حاصل باید دست‌کم ۱۲ باشد. قید دوم دقیقاً با همین منطق برای ویتامین B نوشته می‌شود. **کمینه‌شدن هزینه، جهت قید ویتامین را به $\le$ تبدیل نمی‌کند.**

در **مسئلهٔ قایق** برعکس، برای هر نوع تولید سود مشخصی داریم؛ پس تابع هدف بیشینه‌سازی است. برای قید آلومینیوم باید مصرف هر قایق را در تعداد همان نوع ضرب و مجموع را با موجودی ۱۰۰۰ کیلوگرم مقایسه کرد. در قید زمان ماشین، سقف ۵ ساعت است، اما مصرف هر واحد به **دقیقه** داده شده؛ پس سمت راست باید $5\times60=300$ دقیقه باشد. قید نیروی کار نیز جداگانه نوشته می‌شود و سقف آن ۲۰۰ ساعت است.

**خودآزمایی سریع:** اگر کسی قید ویتامین A را $p+4s+2t\le12$ بنویسد، چه چیزی را اشتباه فهمیده است؟ پاسخ: «حداقل نیاز» را به «حداکثر مجاز» تبدیل کرده است. اگر در مدل قایق قید دوم را $20x+15y\le5$ بنویسد، واحد دقیقه و ساعت را یکسان فرض کرده است.

**پیش از رفتن به جلسهٔ دوم:** هر دو مدل را بدون نگاه‌کردن به کادرهای بالا بازنویسی کنید و کنار هر قید، معنی فارسی و واحدش را یادداشت کنید.

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

#### چگونه مجموع‌های مدل حمل‌ونقل را بفهمیم؟

در مدل حمل‌ونقل دو نوع سؤال داریم: «از انبار $i$ در مجموع چقدر خارج می‌شود؟» و «به مقصد $j$ در مجموع چقدر می‌رسد؟» در سؤال اول **$i$ ثابت** است و روی تمام مقصدها $j$ جمع می‌زنیم؛ در سؤال دوم **$j$ ثابت** است و روی تمام مبدأها $i$ جمع می‌زنیم. به همین دلیل عبارت‌های $\sum_jx_{ij}$ و $\sum_ix_{ij}$ با وجود شباهت ظاهری، دو قید کاملاً متفاوت‌اند.

در **مدل نمادین جلسهٔ دوم**، هر مبدأ فقط به اندازهٔ عرضهٔ خود می‌تواند ارسال کند، پس $\sum_jx_{ij}\le a_i$؛ هر مقصد باید دقیقاً تقاضای خود را دریافت کند، پس $\sum_ix_{ij}=b_j$. حواستان باشد که در **مثال عددی جلسهٔ سوم** جهت قید تقاضا در متن جزوه $\ge$ است. درست‌بودن یک فرمول به *صورت سؤال مشخص* وابسته است.

#### خواندن مسئلهٔ تلویزیون

$x_1$ و $x_2$ تعداد تلویزیون‌های رنگی و سیاه‌وسفید هستند. ضریب‌های ۲۰ و ۱۵ در قید اصلی، **نفرساعت به ازای هر تلویزیون**‌اند؛ ضرب آن‌ها در تعداد تولید، نفرساعت مصرف‌شده را می‌دهد. سقف نیروی کار **۶۰٬۰۰۰ نفرساعت** است، نه ۶۰۰۰ و نه ۶۰٬۰۰۰ نفر. دو قید $x_1\le2000$ و $x_2\le4000$ به‌طور مستقل سقف تولید هر محصول‌اند و جایگزین قید نیروی کار نیستند.

**خودآزمایی سریع:** آیا می‌توان حداکثر هر دو محصول، یعنی $x_1=2000,x_2=4000$ را هم‌زمان تولید کرد؟ خیر؛ چون $20(2000)+15(4000)=100000>60000$. این بررسی برای کنترل معنی قیود مفید است، هرچند حل مسئلهٔ بهینه‌سازی نیست.

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

#### حمل‌ونقل عددی: تفاوت فرم اولیه و نتیجهٔ موازنه

مجموع عرضه‌ها $150+300+200=650$ و مجموع تقاضاها $150+200+100+200=650$ است. جزوه در مثال عددی برای هر مقصد شرط **حداقل دریافت** نوشته است. چون کل کالای موجود و کل حداقل نیاز برابرند، در هر جواب مجاز نه می‌توان کالایی را بدون استفاده گذاشت و نه به مقصدی بیش از نیازش فرستاد و همچنان همهٔ نیازها را تأمین کرد. بنابراین قیود مربوط به عرضه و تقاضا در نهایت با **تساوی** برقرار می‌شوند. ولی در مدل‌نویسی از روی جزوه، همان $\le$ و $\ge$ اولیه را نشان دهید و اگر لازم بود این نتیجه را بعداً توضیح دهید.

#### تولید و انبار: قید ماهانه را واقعاً درک کنید

موازنهٔ هر ماه از یک حساب ساده به دست می‌آید:

$$
\underbrace{s_{i-1}}_{\text{موجودی اول ماه}}+
\underbrace{x_i+y_i}_{\text{تولید همان ماه}}
=\underbrace{d_i}_{\text{تقاضا}}+
\underbrace{s_i}_{\text{موجودی آخر ماه}}.
$$

برای ماه اول، چون $s_0=0$، معادله $x_1+y_1-s_1=1200$ است. برای ماه دوم داریم $x_2+y_2+s_1-s_2=2100$؛ یعنی موجودی ماه قبل به تأمین تقاضای این ماه کمک می‌کند. برای ماه پنجم، چون $s_5=0$، معادله $x_5+y_5+s_4=4000$ می‌شود. **اشتباه رایج** این است که $s_i$ را بدون توجه به جایگاه زمانی، در هر ماه با علامت مثبت وارد کنیم؛ درحالی‌که موجودی پایان ماه از منابع همان ماه کسر می‌شود.

در تابع هدف هزینهٔ نگهداری فقط برای $s_1,s_2,s_3,s_4$ می‌آید؛ زیرا $s_0$ و $s_5$ ثابت و صفرند. سقف تولید عادی ۲۰۰۰ و اضافه‌کاری ۶۰۰ **برای هر ماه** اعمال می‌شود، نه فقط برای مجموع پنج ماه.

**خودآزمایی سریع:** چرا تعداد متغیرها ۱۴ است، نه ۱۵؟ چون پنج $x_i$، پنج $y_i$ و فقط چهار موجودی پایان ماه متغیرند؛ $s_5$ طبق شرط مرزی صفر است.

---

<a id="session-04"></a>
## Session 04 | جلسهٔ چهارم

### English

#### Three products on four machines

In the [full machine-allocation problem](site_docs/session-04/machines.en.md), $x_{ij}\ge0$ is the **number of units of product $i$ made on machine $j$**, for $i=1,2,3$ and $j=1,2,3,4$.

Unit production costs (in USD), machine time (hours per unit), minimum product requirements and maximum machine hours come from the lecture:

$$
C=\begin{pmatrix}4&4&5&7\\6&7&5&6\\12&10&8&11\end{pmatrix},\quad
T=\begin{pmatrix}.30&.25&.20&.20\\.20&.30&.20&.25\\.80&.60&.60&.50\end{pmatrix},
$$

$$d=(3000,6000,4000),\qquad H=(1500,1200,1500,2000).$$

$$
\boxed{\begin{aligned}
\min\ &Z=\sum_{i=1}^3\sum_{j=1}^4 c_{ij}x_{ij}\\
\mathrm{s.t.}\ &\sum_{i=1}^3t_{ij}x_{ij}\le H_j &&j=1,\ldots,4\\
&\sum_{j=1}^4x_{ij}\ge d_i &&i=1,2,3\\
&x_{ij}\ge0 &&\forall i,j.
\end{aligned}}
$$

**Remember:** four $\le$ hour limits and three $\ge$ production minimums; there are **12** nonnegative decision variables. Costs are USD, not toman.

#### Light/heavy crude oil procurement

In the [full crude-oil example](site_docs/session-04/crude.en.md), let $x_1,x_2\ge0$ be the **amounts of light/heavy raw crude purchased** (before processing losses). Prices are $20 and $15 per unit; recovery is $95\%$ and $92\%$. The products are **diesel, kerosene and jet fuel**, and the output requirements are $1{,}000{,}000$, $500{,}000$, $300{,}000$:

$$
\boxed{\begin{aligned}
\min\quad&Z=20x_1+15x_2\\
\mathrm{s.t.}\quad&0.40(0.95)x_1+0.32(0.92)x_2\ge1{,}000{,}000\\
&0.20(0.95)x_1+0.40(0.92)x_2\ge500{,}000\\
&0.35(0.95)x_1+0.20(0.92)x_2\ge300{,}000\\
&x_1,x_2\ge0.
\end{aligned}}
$$

Apply the recovery factor **before** each product's yield; all requirements are lower bounds ($\ge$).

#### Maximum revenue-to-cost ratio (fractional objective)

In the [full fractional model](site_docs/session-04/ratio.en.md), $x_1,x_2\ge0$ denote quantities of products $A,B$. Sale prices $(80,40)$, variable costs $(40,20)$ and fixed cost $200$ are measured in **thousand toman**. Products use $(2,3)$ hours and $(3,2)$ kg of raw materials per unit, respectively.

$$
\boxed{\begin{aligned}
\max\quad&Z=\frac{80x_1+40x_2}{40x_1+20x_2+200}\\
\mathrm{s.t.}\quad&2x_1+3x_2\le120\\
&3x_1+2x_2\le150\\
&x_1,x_2\ge0.
\end{aligned}}
$$

**Do not replace the ratio with profit.** This is a **linear-fractional**, not an ordinary linear, objective. The denominator is positive because fixed cost is $200>0$.

### فارسی

#### تخصیص تولید سه محصول به چهار ماشین

در [مسئلهٔ کامل تخصیص ماشین](site_docs/session-04/machines.fa.md)، $x_{ij}\ge0$ تعداد واحد **محصول $i$ تولیدشده روی ماشین $j$** است؛ $i=1,2,3$ و $j=1,2,3,4$.

جدول هزینهٔ هر واحد (**دلار**)، زمان ساخت هر واحد (**ساعت**)، حداقل تولید هر محصول و ساعت موجود هر ماشین از جزوه آمده است:

$$
C=\begin{pmatrix}4&4&5&7\\6&7&5&6\\12&10&8&11\end{pmatrix},\quad
T=\begin{pmatrix}.30&.25&.20&.20\\.20&.30&.20&.25\\.80&.60&.60&.50\end{pmatrix},
$$

$$d=(3000,6000,4000),\qquad H=(1500,1200,1500,2000).$$

$$
\boxed{\begin{aligned}
\min\ &Z=\sum_{i=1}^3\sum_{j=1}^4 c_{ij}x_{ij}\\
\mathrm{s.t.}\ &\sum_{i=1}^3t_{ij}x_{ij}\le H_j &&j=1,\ldots,4\\
&\sum_{j=1}^4x_{ij}\ge d_i &&i=1,2,3\\
&x_{ij}\ge0 &&\forall i,j.
\end{aligned}}
$$

**برای مدل‌سازی:** چهار قید **$\le$** برای ساعت ماشین‌ها و سه قید **$\ge$** برای حداقل تولید داریم؛ تعداد متغیرهای نامنفی **۱۲** است. واحد هزینه **دلار** است.

#### خرید نفت خام سبک و سنگین

در [مسئلهٔ کامل پالایش](site_docs/session-04/crude.fa.md)، $x_1,x_2\ge0$ مقدار **خرید نفت خام سبک و سنگین قبل از اتلاف** هستند. قیمت‌ها ۲۰ و ۱۵ دلار و بازده پس از پالایش $0.95$ و $0.92$ است. فرآورده‌ها **گازوئیل، نفت سفید و سوخت هواپیما** با حداقل مقدار $1{,}000{,}000$، $500{,}000$ و $300{,}000$ هستند:

$$
\boxed{\begin{aligned}
\min\quad&Z=20x_1+15x_2\\
\mathrm{s.t.}\quad&0.40(0.95)x_1+0.32(0.92)x_2\ge1{,}000{,}000\\
&0.20(0.95)x_1+0.40(0.92)x_2\ge500{,}000\\
&0.35(0.95)x_1+0.20(0.92)x_2\ge300{,}000\\
&x_1,x_2\ge0.
\end{aligned}}
$$

درصد بازده هر نوع نفت خام در ضریب تولید **هر فرآورده** ضرب می‌شود؛ هر سه قید «حداقل نیاز» با $\ge$ نوشته می‌شوند.

#### بیشینه‌کردن نسبت درآمد به هزینه (تابع هدف کسری)

در [مسئلهٔ کامل نسبت درآمد به هزینه](site_docs/session-04/ratio.fa.md)، $x_1,x_2\ge0$ تعداد محصولات $A,B$ هستند. قیمت فروش $(80,40)$، هزینهٔ متغیر $(40,20)$ و هزینهٔ ثابت ۲۰۰، همگی **هزار تومان** هستند. زمان ساخت $(2,3)$ ساعت و مصرف مواد اولیه $(3,2)$ کیلوگرم برای هر واحد است.

$$
\boxed{\begin{aligned}
\max\quad&Z=\frac{80x_1+40x_2}{40x_1+20x_2+200}\\
\mathrm{s.t.}\quad&2x_1+3x_2\le120\\
&3x_1+2x_2\le150\\
&x_1,x_2\ge0.
\end{aligned}}
$$

**نسبت را با سود اشتباه نگیرید.** تابع هدف **کسری خطی** است و نه خطی معمولی. چون هزینهٔ ثابت ۲۰۰ است، مخرج در ناحیهٔ مجاز مثبت می‌ماند.

#### تخصیص ماشین‌ها: دو اندیس، دو خانواده قید

در مسئلهٔ سه محصول و چهار ماشین، $x_{ij}$ **مقدار محصول $i$ روی ماشین $j$** است. اگر می‌خواهیم بدانیم «از محصول $i$ دست‌کم چند واحد ساخته می‌شود»، روی ماشین‌ها جمع می‌زنیم: $\sum_jx_{ij}\ge d_i$. اگر می‌خواهیم «ماشین $j$ چند ساعت کار می‌کند»، روی محصولات جمع می‌زنیم، اما **با ضریب زمان ساخت**: $\sum_it_{ij}x_{ij}\le H_j$. بنابراین سه قید حداقل تقاضا و چهار قید ظرفیت ماشین داریم. این ساختار را به‌جای حفظ تک‌تک ۱۲ جملهٔ ماتریس، از روی مفهوم اندیس‌ها بازسازی کنید.

#### پالایش نفت: ضرایب درصدی را از کجا می‌آوریم؟

$x_1$ و $x_2$ **مقدار نفت خام خریداری‌شده** هستند؛ هنوز اتلاف پالایش روی آن‌ها اعمال نشده است. از هر واحد نفت سبک فقط $0.95$ واحد و از هر واحد نفت سنگین فقط $0.92$ واحد محصول قابل‌استفاده باقی می‌ماند. سهم هر فرآورده از مقدار باقی‌مانده محاسبه می‌شود. مثلاً سهم گازوئیل نفت سبک $0.40\times0.95x_1$ است، نه $0.40x_1$ و نه $0.95x_1$. همهٔ خروجی‌ها باید **حداقل** نیاز بازار را پوشش دهند، پس هر سه قید به طرف $\ge$ هستند.

#### مدل کسری: نسبت با اختلاف فرق دارد

تابع هدف $\frac{80x_1+40x_2}{40x_1+20x_2+200}$ نسبت **درآمد فروش** به **کل هزینهٔ متغیر و ثابت** را اندازه می‌گیرد. اگر $80x_1+40x_2-(40x_1+20x_2+200)$ را بنویسید، مسئلهٔ تازه‌ای ساخته‌اید: بیشینه‌سازی سود، نه بیشینه‌سازی نسبت. هزینهٔ ثابت $200$ در مخرج باقی می‌ماند و باعث می‌شود مخرج برای $x_1,x_2\ge0$ مثبت باشد.

**خودآزمایی سریع:** در تخصیص ماشین، چرا $\sum_jt_{ij}x_{ij}\le H_i$ معمولاً نادرست است؟ چون $H_i$ ظرفیت ماشین است و برای ماشین **ثابت** باید روی *محصول‌ها* جمع زد؛ نوشتن اندیس‌ها بخشی از معنی مدل است.

---

<a id="session-05"></a>
## Session 05 | جلسهٔ پنجم

### English

#### Linear-fractional objective and Charnes–Cooper model

The [fractional-programming lecture example](site_docs/session-05/fractional.en.md) is

$$\boxed{\begin{aligned}
\max\quad &\frac{10x_1+20x_2+10}{3x_1+4x_2+20}\\
\mathrm{s.t.}\quad &x_1+3x_2\le50,\\
&3x_1+2x_2\le80,\\
&x_1,x_2\ge0.
\end{aligned}}$$

The denominator is **strictly positive** ($\ge20$). Let $t=1/(3x_1+4x_2+20)$ and $y_i=tx_i$ ($x_i=y_i/t$). Multiply **both** resource constraints by $t$ and normalize the denominator:

$$\boxed{\begin{aligned}
\max\quad&10y_1+20y_2+10t\\
\mathrm{s.t.}\quad&y_1+3y_2\le50t,\\
&3y_1+2y_2\le80t,\\
&3y_1+4y_2+20t=1,\\
&y_1,y_2,t\ge0.
\end{aligned}}$$

**Remember:** in general $t>0$ is needed to invert the transformation; for this model, $t=0$ is impossible because the first scaled constraint and $y\ge0$ contradict the normalizing equality. Do not drop the constant $10$ in the numerator or $20$ in the denominator.

#### Triangular fuzzy membership as a mathematical model

From the [fuzzy-number lecture](site_docs/session-05/fuzzy.en.md), a crisp characteristic function has values only $0$ or $1$, while fuzzy membership satisfies $\mu_{\widetilde A}(x)\in[0,1]$. For the triangular fuzzy number $\widetilde M=(1,5,7)$:

$$\boxed{\mu_{\widetilde M}(x)=\begin{cases}
0,&x\le1,\\
(x-1)/4,&1<x\le5,\\
(7-x)/2,&5<x<7,\\
0,&x\ge7.
\end{cases}}$$

**Modeling point:** derive the two straight-line equations from $(1,0)$, $(5,1)$ and $(7,0)$. This is a **membership-function model**, not a fuzzy optimization problem; no numerical optimizer is included in the exam review.

### فارسی

#### تابع هدف کسری و مدل تبدیلی چارنز–کوپر

در [مثال برنامه‌ریزی کسری جلسه](site_docs/session-05/fractional.fa.md) مدل اولیه عبارت است از

$$\boxed{\begin{aligned}
\max\quad &\frac{10x_1+20x_2+10}{3x_1+4x_2+20}\\
\mathrm{s.t.}\quad&x_1+3x_2\le50,\\
&3x_1+2x_2\le80,\\
&x_1,x_2\ge0.
\end{aligned}}$$

مخرج همواره **مثبت** (حداقل ۲۰) است. با $t=1/(3x_1+4x_2+20)$ و $y_i=tx_i$ (و $x_i=y_i/t$) هر **دو** قید را در $t$ ضرب کرده، قید نرمال‌سازی می‌نویسیم:

$$\boxed{\begin{aligned}
\max\quad &10y_1+20y_2+10t\\
\mathrm{s.t.}\quad&y_1+3y_2\le50t,\\
&3y_1+2y_2\le80t,\\
&3y_1+4y_2+20t=1,\\
&y_1,y_2,t\ge0.
\end{aligned}}$$

**نکته:** در حالت کلی برای بازگشت به مدل اول باید $t>0$ باشد. در این مثال $t=0$ به‌دلیل تناقض قید اول و قید تساوی ممکن نیست. عدد ثابت ۱۰ صورت و عدد ثابت ۲۰ مخرج را فراموش نکنید.

#### مدل‌سازی تابع عضویت فازی مثلثی

در [بخش مجموعه‌های فازی](site_docs/session-05/fuzzy.fa.md)، تابع مشخصهٔ مجموعهٔ معمولی فقط صفر یا یک می‌گیرد؛ اما درجهٔ عضویت فازی در بازهٔ $[0,1]$ است. عدد فازی مثلثی جزوه $\widetilde M=(1,5,7)$ است:

$$\boxed{\mu_{\widetilde M}(x)=\begin{cases}
0,&x\le1,\\
(x-1)/4,&1<x\le5,\\
(7-x)/2,&5<x<7,\\
0,&x\ge7.
\end{cases}}$$

**نکتهٔ مدل‌سازی:** دو معادلهٔ خط را از سه رأس $(1,0)$، $(5,1)$ و $(7,0)$ بنویسید. این یک **مدل تابع عضویت** است و در جزوه مسئلهٔ بهینه‌سازی فازی تعریف نشده؛ حل عددی در مرور شب امتحان نمی‌آید.

#### تبدیل چارنز–کوپر را قدم‌به‌قدم بنویسید

ایدهٔ اصلی این است که با یک متغیر کمکی مثبت، **مخرج کسر را برابر ۱** کنیم. برای تابع هدف جلسهٔ پنجم بگذارید

$$
t=\frac{1}{3x_1+4x_2+20},\qquad y_1=tx_1,\quad y_2=tx_2.
$$

در این مثال $t>0$ است چون مخرج همواره دست‌کم ۲۰ است. اکنون صورت کسر در $t$ ضرب می‌شود و به $10y_1+20y_2+10t$ تبدیل می‌شود. دو قید اصلی نیز باید *هر دو* در $t$ ضرب شوند: $y_1+3y_2\le50t$ و $3y_1+2y_2\le80t$. مهم‌ترین بخش تبدیل، **قید نرمال‌سازی** $3y_1+4y_2+20t=1$ است. اگر فقط تابع هدف را تبدیل کنید و این تساوی را ننویسید، مدل جدید هم‌ارز نیست. برای بازگشت، $x_i=y_i/t$ را به یاد داشته باشید.

#### ساختن تابع عضویت مثلثی از سه رأس

برای $M=(1,5,7)$، تابع عضویت باید از صفر در $x=1$ به یک در $x=5$ برسد و سپس در $x=7$ دوباره صفر شود. شیب قسمت صعودی $1/(5-1)=1/4$ و شیب قسمت نزولی $(0-1)/(7-5)=-1/2$ است. پس قسمت صعودی $(x-1)/4$ و قسمت نزولی $(7-x)/2$ می‌شود. **هیچ نیازی به حفظ‌کردن صورت کسرها نیست؛ کافی است خط را از دو نقطهٔ هر شاخه بنویسید.**

از همین مثلث، برش آلفای معمولی برای $0<\alpha\le1$ چنین به دست می‌آید:

$$
[M]_{\alpha}=[1+4\alpha,\ 7-2\alpha].
$$

برای $\alpha=1$ بازه به نقطهٔ $5$ تبدیل می‌شود؛ این همان هستهٔ مثلث است.

**خودآزمایی سریع:** در مدل تبدیلی اگر $10t$ را از صورت تابع هدف حذف کنید، چه خطایی کرده‌اید؟ عدد ثابت ۱۰ در صورت کسر اصلی را از بین برده‌اید؛ بنابراین تابع هدف دیگر معادل نیست.

---

<a id="session-06"></a>
## Session 06 | جلسهٔ ششم

### English

#### Fuzzy definitions and production formulation

- State the membership function $\mu_{\widetilde A}:\mathbb R\to[0,1]$, the strong alpha-cut $\{x:\mu(x)>\alpha\}$, the weak alpha-cut $\{x:\mu(x)\ge\alpha\}$ for $\alpha>0$, support $\{\mu>0\}$ and core $\{\mu=1\}$.
- Distinguish the conventional triangle $(a,b,c)$ from the LR core/spread form $(a^L,a^U,\ell,r)_{LR}$ and write their piecewise-linear membership functions.
- For LR numbers with triangular/trapezoidal linear sides, use $R(A)=(a^L+a^U)/2+(r-\ell)/4$ when the comparison relation is **explicitly** $\le_R$.
- In the [two-product lecture model](site_docs/session-06/ranking-production.en.md), define $x_1,x_2\ge0$ and write

$$\begin{aligned}
\max\ \widetilde Z&=(35,40,45)x_1+(45,50,55)x_2,\\
(1.5,2,2.5)x_1+(0.75,1,1.2)x_2&\le_R(98,100,102),\\
(0.25,1,1.5)x_1+(2,2.2,2.5)x_2&\le_R(78,80,82).
\end{aligned}$$

Identify which rows are machine hours and raw-material kilograms. For the exam-oriented **modeling** review, focus on the fuzzy formulation and the meaning of the order relation; the separately calculated optimum is not necessary.

### فارسی

#### تعریف مجموعهٔ فازی و صورت‌بندی تولید

- تعریف تابع عضویت $\mu_{\widetilde A}:\mathbb R\to[0,1]$، برش قوی $\{x:\mu(x)>\alpha\}$، برش معمولی $\{x:\mu(x)\ge\alpha\}$ برای $\alpha>0$، تکیه‌گاه $\{\mu>0\}$ و هستهٔ $\{\mu=1\}$ را بدانید.
- عدد مثلثی $(a,b,c)$ را از نمایش $LR$ به‌صورت $(a^L,a^U,\ell,r)$ تشخیص دهید و فرمول تابع عضویت هرکدام را بنویسید.
- در مقایسهٔ مبتنی بر رتبه‌بندی $R(A)=(a^L+a^U)/2+(r-\ell)/4$، معنای دقیق علامت $\le_R$ را مشخص کنید.
- در [مسئلهٔ دو محصول جزوه](site_docs/session-06/ranking-production.fa.md)، متغیرهای نامنفی $x_1,x_2$ را تعریف کنید و مدل فازی زیر را بنویسید:

$$\begin{aligned}
\max\ \widetilde Z&=(35,40,45)x_1+(45,50,55)x_2,\\
(1.5,2,2.5)x_1+(0.75,1,1.2)x_2&\le_R(98,100,102),\\
(0.25,1,1.5)x_1+(2,2.2,2.5)x_2&\le_R(78,80,82).
\end{aligned}$$

ردیف اول محدودیت ساعت کار ماشین و ردیف دوم محدودیت کیلوگرم مواد اولیه است. در مرور **مدل‌سازی** بر فرم قیود، جهت نامساوی‌ها و روش مقایسه تمرکز کنید؛ جواب عددیِ تکمیلی الزامی نیست.

#### تفاوت مجموعهٔ معمولی، فازی و برش آلفا

در مجموعهٔ معمولی، هر عضو یا متعلق است یا نیست؛ تابع مشخصه فقط ۰ یا ۱ می‌گیرد. در مجموعهٔ فازی، درجهٔ عضویت هر $x$ می‌تواند هر مقداری بین صفر و یک باشد. **برش معمولی** $[A]_{\alpha}=\{x:\mu_A(x)\ge\alpha\}$ و **برش قوی** $\{x:\mu_A(x)>\alpha\}$ است؛ تفاوت در نقاط مرزی‌ای است که عضویت دقیقاً برابر آلفاست. تکیه‌گاه $\{x:\mu_A(x)>0\}$ و هسته $\{x:\mu_A(x)=1\}$ را نیز از هم تشخیص دهید.

یک عدد فازی مثلثی $(a,b,c)$ سه جایگاه هندسی دارد: **شروع تکیه‌گاه، قله، پایان تکیه‌گاه**. نمایش ذوزنقه‌ای $LR$ با $(a^L,a^U,\ell,r)_{LR}$ اما شامل **دو سر هسته و دو گستردگی** است؛ این چهار عدد را نباید به‌عنوان چهار رأس ذوزنقه بخوانید. برای شکل‌های خطی، دو سر برش آلفا برابرند با

$$
[A]_{\alpha}=
[a^L-\ell(1-\alpha),\ a^U+r(1-\alpha)],
\qquad 0\le\alpha\le1.
$$

در $\alpha=0$، بازهٔ حاصل را بستهٔ تکیه‌گاه در نظر می‌گیریم. این رابطه برای نمایش خطی در چپ و راست است؛ برای توابع شکل دلخواه $L,R$، وارون آن توابع در فرمول وارد می‌شود.

#### تبدیل قید فازی با رتبه‌بندی

در مدل تولید دو محصول، ضرایب تابع هدف، مصرف منابع و ظرفیت‌ها **اعداد فازی مثلثی** هستند. نوشتن نامساوی $\widetilde A\le_R\widetilde B$ بدون تعریف $R$ کافی نیست. در این جزوه، برای عدد ذوزنقه‌ای خطی $R(A)=\tfrac{a^L+a^U}{2}+\tfrac{r-\ell}{4}$ به کار می‌رود و پس از محاسبهٔ رتبهٔ هر طرف، نامساوی عددی نوشته می‌شود. اگر $x_1,x_2\ge0$ باشد، ضرب اسکالر نامنفی و جمع LR را می‌توان پیش از رتبه‌بندی انجام داد؛ حالت ضریب منفی قواعد دیگری دارد.

**خودآزمایی سریع:** برای مثلث $(1,3,7)$ هسته کجاست و برش آلفا چیست؟ هسته نقطهٔ $3$ است و $[A]_{\alpha}=[1+2\alpha,7-4\alpha]$؛ توجه کنید طول دو دامنهٔ چپ و راست برابر نیست.

---

<a id="session-07"></a>
## Session 07 | جلسهٔ هفتم

### English

#### LR fuzzy LP, extension-principle maximum and Kerre comparison

- Interpret $(a^L,a^U,\ell,r)_{LR}$ as **core and spreads**, not as four trapezoid vertices.
- Formulate the [page 4 fuzzy LP](site_docs/session-07/lr-model.en.md) with $x_1,x_2\ge0$ and an explicitly specified ranking-based order:

$$\begin{aligned}
\max\ \widetilde Z&=(2,3,1,1)_{LR}x_1+(3,4,1,2)_{LR}x_2,\\
(1,2,1,1)_{LR}x_1+(2,3,1,2)_{LR}x_2&\le_R(5,6,2,2)_{LR},\\
(2,3,1,3)_{LR}x_1+(1,2,1,1)_{LR}x_2&\le_R(4,6,2,1)_{LR}.
\end{aligned}$$

- For [the extension principle](site_docs/session-07/extension-max.en.md), model $D=\max(M,N)$ by $\mu_D(z)=\sup_{\max(x,y)=z}\min(\mu_M(x),\mu_N(y))$; do **not** replace this with pointwise max of membership functions. For $M=(0,2,5)$, $N=(2,3,4)$, the key breakpoints are $2,3,3.5,5$.
- For [Kerre comparison](site_docs/session-07/kerre.en.md), state $d(A,B)=\int|\mu_A-\mu_B|$ and the pairwise rule comparing $d(N,D)$ with $d(M,D)$, where $D$ is the **extension maximum**.

These are formulation/definition tasks. Numerical LP results and evaluated distance integrals are separately marked as extensions.

### فارسی

#### مدل فازی LR، اصل گسترش و مقایسهٔ Kerre

- چهارتایی $(a^L,a^U,\ell,r)_{LR}$ را به‌عنوان **هسته و گستردگی‌ها** بشناسید، نه چهار رأس ذوزنقه.
- [مدل فازی صفحهٔ چهارم](site_docs/session-07/lr-model.fa.md) را با متغیرهای $x_1,x_2\ge0$ و ترتیب مبتنی بر رتبه‌بندی بنویسید:

$$\begin{aligned}
\max\ \widetilde Z&=(2,3,1,1)_{LR}x_1+(3,4,1,2)_{LR}x_2,\\
(1,2,1,1)_{LR}x_1+(2,3,1,2)_{LR}x_2&\le_R(5,6,2,2)_{LR},\\
(2,3,1,3)_{LR}x_1+(1,2,1,1)_{LR}x_2&\le_R(4,6,2,1)_{LR}.
\end{aligned}$$

- برای [اصل گسترش](site_docs/session-07/extension-max.fa.md)، بیشینهٔ دو عدد فازی را از رابطهٔ $\mu_D(z)=\sup_{\max(x,y)=z}\min(\mu_M(x),\mu_N(y))$ بسازید؛ این با بیشینهٔ نقطه‌ای توابع عضویت تفاوت دارد. در مثال $M=(0,2,5)$ و $N=(2,3,4)$ نقاط شکست $2,3,3.5,5$ هستند.
- برای [مقایسهٔ Kerre](site_docs/session-07/kerre.fa.md)، فاصلهٔ $d(A,B)=\int|\mu_A-\mu_B|$ و مقایسهٔ $d(N,D)$ با $d(M,D)$ را بنویسید؛ $D$ باید از **اصل گسترش** محاسبه شده باشد.

این‌ها برای مرور تعریف‌ها و صورت‌بندی‌اند. جواب بهینهٔ عددی و مقدار انتگرال‌ها به‌طور جداگانه و به‌عنوان مطالب تکمیلی آمده‌اند.

#### تفاوت دو نوع «بیشینه» در مسائل فازی

اگر دو عدد فازی $M,N$ دارید، نوشتن $\max\{\mu_M(z),\mu_N(z)\}$ به‌معنی عضویت اجتماع دو مجموعهٔ فازی است، **نه الزاماً تابع عضویت عدد تصادفی‌مانند $\max(M,N)$**. برای بیشینهٔ فازی، طبق اصل گسترش باید همهٔ زوج‌های $(x,y)$ با شرط $\max(x,y)=z$ را بررسی کنیم و بهترین مقدار $\min(\mu_M(x),\mu_N(y))$ را بگیریم:

$$
\mu_D(z)=\sup_{\max(x,y)=z}\min\{\mu_M(x),\mu_N(y)\}.
$$

برای اعداد فازی معمول با برش‌های بازه‌ای، راه ساده‌تر این است که **دو انتهای برش‌های آلفا** را جداگانه بیشینه بگیریم. پس

$$
[D]_{\alpha}=
[\max(L_M(\alpha),L_N(\alpha)),\ \max(R_M(\alpha),R_N(\alpha))].
$$

در مثال جلسهٔ هفتم $M=(0,2,5)$ و $N=(2,3,4)$، نقطهٔ گذار در شاخهٔ راست از برخورد $5-3\alpha=4-\alpha$ و در نتیجه $\alpha=1/2$ به دست می‌آید. آن نقطه در محور $z$ برابر $3.5$ است. این عدد را از **برش‌ها** نتیجه بگیرید، نه از حدس‌زدن روی نمودار.

#### معیار Kerre چه می‌پرسد؟

ابتدا $D=\widetilde{\max}(M,N)$ را بسازید. سپس مساحت اختلاف مطلق دو تابع عضویت را حساب کنید:

$$d(A,B)=\int_{-\infty}^{\infty}|\mu_A(z)-\mu_B(z)|\,dz.$$

طبق قرارداد استفاده‌شده در جزوه، امتیاز $r(M,N)=d(M,D)-d(N,D)$ است. اگر این مقدار **منفی** باشد، $M$ به بیشینهٔ فازی نزدیک‌تر است و بر اساس همین قرارداد بر $N$ ترجیح داده می‌شود. برای محاسبهٔ انتگرال، ابتدا نقاط شکست و تقاطع شاخه‌ها را پیدا و بازه‌ها را تقسیم کنید.

**خودآزمایی سریع:** چرا نمی‌توان فاصله را بدون بررسی قدرمطلق یک‌باره انتگرال گرفت؟ چون ممکن است علامت $\mu_M-\mu_N$ در نقاط تقاطع تغییر کند.

---

<a id="session-08"></a>
## Session 08 | جلسهٔ هشتم

### English

#### Extension maximum and Kerre distance: modeling essentials

- This session **revisits** the prior lecture's definitions; the first two scanned pages substantially overlap with Session 07. Preserve the distinction between fuzzy max and pointwise max of memberships.
- State the extension-principle maximum: $\mu_D(z)=\sup_{\max(x,y)=z}\min\{\mu_M(x),\mu_N(y)\}$.
- For $M=(0,2,5)$ and $N=(2,3,4)$, write $[M]_\alpha=[2\alpha,5-3\alpha]$ and $[N]_\alpha=[2+\alpha,4-\alpha]$. **Model** the maximum with the maximum of corresponding endpoints: $[D]_\alpha=[\max(L_M,L_N),\max(R_M,R_N)]$.
- For Kerre-style comparison, define $d(M,N)=\int|\mu_M-\mu_N|\,dz$ and $r(M,N)=d(M,D)-d(N,D)$; write the comparison direction with its sign convention.
- [Complete extension derivation](site_docs/session-08/extension-recap.en.md) and [distance formulation](site_docs/session-08/distance.en.md). Exact values are independently derived additions, not necessary to state the model.

### فارسی

#### بیشینهٔ فازی و فاصلهٔ Kerre: نکات مدل‌سازی

- این جلسه **مرور تکمیلی** مطالب جلسهٔ هفتم است؛ دو صفحهٔ اول اسکن با جزوهٔ قبلی هم‌پوشانی دارد. بیشینهٔ دو عدد فازی را با بیشینهٔ نقطه‌ای درجات عضویت اشتباه نگیرید.
- تعریف اصل گسترش: $\mu_D(z)=\sup_{\max(x,y)=z}\min\{\mu_M(x),\mu_N(y)\}$.
- برای $M=(0,2,5)$ و $N=(2,3,4)$، دو برش آلفا را $[M]_\alpha=[2\alpha,5-3\alpha]$ و $[N]_\alpha=[2+\alpha,4-\alpha]$ بنویسید. **صورت‌بندی** بیشینه: $[D]_\alpha=[\max(L_M,L_N),\max(R_M,R_N)]$.
- برای مقایسهٔ Kerre، $d(M,N)=\int|\mu_M-\mu_N|\,dz$ و $r(M,N)=d(M,D)-d(N,D)$ را تعریف و جهت علامت را مشخص کنید.
- [استخراج بیشینه](site_docs/session-08/extension-recap.fa.md) و [صورت‌بندی فاصله](site_docs/session-08/distance.fa.md). مقادیر دقیق انتگرال‌ها تکمیل مستقل‌اند، نه شرط تعریف مدل.

#### یک بار اصل گسترش را تا انتها حل کنیم

برای $M=(0,2,5)$ و $N=(2,3,4)$، برش‌های آلفا از خط‌های دو ضلع مثلث‌ها به دست می‌آیند:

$$[M]_{\alpha}=[2\alpha,5-3\alpha],\qquad
[N]_{\alpha}=[2+\alpha,4-\alpha].$$

در بازهٔ $0\le\alpha\le1$، انتهای چپ بیشینه همیشه $2+\alpha$ است؛ زیرا $2+\alpha\ge2\alpha$. انتهای راست به این بستگی دارد که $5-3\alpha$ بزرگ‌تر باشد یا $4-\alpha$. دو مقدار در $\alpha=1/2$ برابرند. بنابراین

$$
[D]_{\alpha}=\begin{cases}
[2+\alpha,\ 5-3\alpha],&0\le\alpha\le\tfrac12,\\
[2+\alpha,\ 4-\alpha],&\tfrac12\le\alpha\le1.
\end{cases}
$$

از این رابطه، تابع عضویتِ بیشینه نیز قابل بازسازی است: در سمت چپ تا رأس $z=3$، مقدار $z-2$ داریم؛ بعد از رأس تا $z=3.5$، شاخهٔ $4-z$ و از $z=3.5$ تا $z=5$، شاخهٔ $(5-z)/3$ برقرار است. در خارج از تکیه‌گاه $[2,5]$ عضویت صفر است.

#### برای آزمون چه چیزی را روی برگه نشان بدهیم؟

اگر سؤال از شما «ساختن» بیشینهٔ فازی را خواست، فقط نوشتن فرمول $\sup$ کافی نیست. **برش‌های آلفا، مقایسهٔ انتهاها، نقطهٔ تغییر شاخه و تابع عضویت حاصل** را نیز بنویسید. اگر سؤال تنها «صورت‌بندی» خواست، تعریف اصل گسترش و قاعدهٔ برش‌ها پایهٔ پاسخ‌اند. هنگام ادامه به معیار Kerre، **اول $D$ را درست بسازید** و بعد سراغ مساحت اختلاف‌ها بروید.

**خودآزمایی سریع:** مقدار $\mu_D(4)$ چقدر است؟ در بازهٔ $3.5\le z\le5$، $\mu_D(z)=(5-z)/3$؛ پس $\mu_D(4)=1/3$.

---

<a id="session-09"></a>
## Session 09 | جلسهٔ نهم

### English

#### LR triangular comparison: correcting the model before solving it

- The new source example is $M=(2,5,12)$ and $N=(2,4,10)$, using **(support left, mode, support right)** rather than four-parameter LR core/spread tuples.
- Write the correct branches $M_L(z)=(z-2)/3$ for $2\le z\le5$, $M_R(z)=(12-z)/7$ for $5\le z\le12$, $N_L(z)=(z-2)/2$ for $2\le z\le4$, and $N_R(z)=(10-z)/6$ for $4\le z\le10$. The handwritten denominators of $N$ are inconsistent with its stated endpoints; the corrected branches here are an explicit mathematical repair.
- Formulate $[D]_\alpha=[\max(L_M,L_N),\max(R_M,R_N)]$ and the Kerre score $r(M,N)=d(M,D)-d(N,D)$. Distinguish model specification from computing the score.
- [Corrected membership model](site_docs/session-09/source-example.en.md) and [general case analysis](site_docs/session-09/case-analysis.en.md). The evaluated value $-17/9$ is an independent extension.

### فارسی

#### مقایسهٔ مثلث‌های LR: ابتدا مدل را درست تعریف کنیم

- مثال جدید جزوه $M=(2,5,12)$ و $N=(2,4,10)$ است؛ ترتیب اجزا **کران چپ، رأس و کران راست** است، نه چهارتایی هسته و گستردگی‌های LR.
- شاخه‌های درست: $M_L(z)=(z-2)/3$ در $2\le z\le5$، $M_R(z)=(12-z)/7$ در $5\le z\le12$، $N_L(z)=(z-2)/2$ در $2\le z\le4$ و $N_R(z)=(10-z)/6$ در $4\le z\le10$. مخرج‌های شاخه‌های $N$ در دست‌نویس با رأس‌ها ناسازگارند؛ این فرمول‌ها اصلاح مستند و مستقل هستند.
- صورت‌بندی بیشینه: $[D]_\alpha=[\max(L_M,L_N),\max(R_M,R_N)]$. صورت‌بندی امتیاز Kerre: $r(M,N)=d(M,D)-d(N,D)$. تعریف مدل را از محاسبهٔ نهایی امتیاز جدا نگه دارید.
- [بازسازی تابع عضویت](site_docs/session-09/source-example.fa.md) و [بررسی حالت‌ها](site_docs/session-09/case-analysis.fa.md). مقدار عددی $-17/9$ نتیجهٔ تکمیل مستقل حل است.

#### حل مثال جدید بدون تکرار اشتباه دست‌نویس

برای $M=(2,5,12)$ و $N=(2,4,10)$، عدد اول در هر سه‌تایی ابتدای تکیه‌گاه، عدد دوم قله و عدد سوم انتهای تکیه‌گاه است. بنابراین طول شاخهٔ چپ $M$ برابر $5-2=3$ و طول شاخهٔ راست آن $12-5=7$ است؛ برای $N$ همین طول‌ها $4-2=2$ و $10-4=6$ هستند. فرمول‌های تابع عضویت از این فاصله‌ها ساخته می‌شوند؛ **مخرج‌های ناسازگار جزوه را نباید عیناً تکرار کرد**. این اصلاح ریاضی در صفحهٔ شرح مثال مستند شده است.

برش‌های آلفا عبارت‌اند از

$$
[M]_{\alpha}=[2+3\alpha,\ 12-7\alpha],\qquad
[N]_{\alpha}=[2+2\alpha,\ 10-6\alpha].
$$

برای هر $0\le\alpha\le1$، هر دو انتهای برش $M$ از انتهای متناظر $N$ بزرگ‌تر یا مساوی‌اند. پس برش‌های بیشینهٔ فازی دقیقاً با برش‌های $M$ برابرند و $D=M$ است. در این حالت معیار Kerre ساده می‌شود:

$$
r(M,N)=d(M,M)-d(N,M)=-d(M,N).
$$

از آنجا که دو مثلث یکسان نیستند، فاصله مثبت است و **علامت رتبه منفی** می‌شود؛ یعنی طبق قرارداد همین جزوه، $M$ ترجیح داده می‌شود. مقدار $17/9$ برای فاصله و $-17/9$ برای امتیاز، حاصل **محاسبهٔ تکمیلی مستقل** است و نباید به‌عنوان عدد نهایی نوشته‌شده در یادداشت دست‌نویس معرفی شود.

**خودآزمایی سریع:** اگر فقط علامت امتیاز را بخواهند، آیا محاسبهٔ همهٔ انتگرال‌ها ضروری است؟ خیر؛ وقتی ثابت کردید $D=M$ و $M\ne N$، آنگاه $r(M,N)=-d(M,N)<0$ کافی است.

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

#### چهار موازنهٔ مالی را از منطق جریان پول به دست آورید

در این تمرین به‌جای حفظ چهار معادله، یک قانون ثابت به کار ببرید: **پول تازه‌وارد به ابتدای سال + سپردهٔ برگشتی از سال قبل = هزینهٔ همان سال + سپردهٔ تازه**. سال اول سپردهٔ قبلی نداریم؛ پس $x_1=2+s_1$. در سال دوم سپردهٔ $s_1$ همراه با سود ۶ درصد برمی‌گردد: $x_2+1.06s_1=4+s_2$. همین منطق برای سال سوم با $1.055s_2$ و سال چهارم با $1.045s_3$ تکرار می‌شود؛ سال چهارم دیگر سپردهٔ جدیدی تعریف نکرده‌ایم.

چون مبلغ‌ها بر حسب **میلیون دلار** هستند، بهتر است ضرایب را بدون تبدیل‌های بی‌دلیل واحد به کار ببرید. نرخ‌های ۷، ۶، ۶٫۵ و ۷٫۵ درصد در تابع هدف، نرخ بهرهٔ اوراق مربوط به همان سال‌اند و نرخ سود سپرده‌های کوتاه‌مدت نیستند. عامل ۲۰ در تابع هدف به‌فرض **۲۰ پرداخت بهرهٔ سالانه** مربوط است که در صورت‌بندی این پروژه تصریح شده است؛ اگر فرض مالی دیگری مطرح شد، تابع هدف نیز باید متناسب با آن بازنویسی شود.

**خودآزمایی سریع:** چرا در معادلهٔ سال سوم به‌جای $0.055s_2$، عبارت $1.055s_2$ می‌آید؟ چون هم **اصل سپرده** و هم سود ۵٫۵ درصدی آن در ابتدای سال سوم قابل استفاده است.

---

<a id="assignment-transportation-python"></a>
## Assignment 02 | تمرین دوم

### English

#### Python solution to the existing transportation problem

Assignment 02 was **only the Python implementation** of the existing [Session 03 transportation model](site_docs/session-03/transportation.en.md). No second transport dataset or different mathematical formulation was assigned. The [existing Python code](site_docs/assignments/transportation-python.en.md) solves that lecture example; the model is already included under Session 03 in this cumulative review. There is no need to repeat its constraints here.

### فارسی

#### حل پایتونی مسئلهٔ حمل‌ونقل جلسهٔ سوم

تمرین دوم **فقط حل مسئلهٔ حمل‌ونقل جلسهٔ سوم با Python** بود؛ مسئله یا مدل جدیدی ندارد. [مدل کامل حمل‌ونقل](site_docs/session-03/transportation.fa.md) در مرور جلسهٔ سوم موجود است و [کد آمادهٔ پایتون](site_docs/assignments/transportation-python.fa.md) نیز در سایت معرفی شده است. قیود تکراری اینجا دوباره نوشته نمی‌شوند.

#### برای مرور میان‌ترم چه چیزی از این تمرین باید بلد باشیم؟

تمرین دوم صورت‌مسئلهٔ حمل‌ونقل جدیدی ندارد؛ هدف آن پیاده‌سازی و حل **همان مدل جلسهٔ سوم** با Python است. برای مرور مدل‌سازی، باید بتوانید متغیر $x_{ij}$، تابع هدف $\sum c_{ij}x_{ij}$، قیود عرضه و تقاضا و شرط نامنفی‌بودن را **بدون اجرای کد** بنویسید. در جزوهٔ عددی، عرضه و تقاضا هر کدام جمعاً ۶۵۰ واحدند؛ از این برابری می‌توان نتیجه گرفت که همهٔ محدودیت‌های فعالِ عرضه و تقاضا در جواب مجاز با تساوی برقرارند.

**اشتباه رایج:** فرض نکنید چون تکلیف با پایتون انجام شده است، سؤال امتحانی حتماً برنامه‌نویسی است؛ چنین نتیجه‌ای از صورت تمرین به دست نمی‌آید. کد، روش محاسبهٔ جواب مدل موجود است، نه تعریف یک مدل تازه.

---

<a id="assignment-fuzzy-numbers-max"></a>
## Assignment 03 | تمرین سوم

### English

#### Triangular fuzzy memberships and the maximum operator

The full [fuzzy-number assignment solution](site_docs/assignments/fuzzy-numbers-max.en.md) uses $\widetilde A=(1,3,7)$ and $\widetilde B=(3,5,6)$. Model the membership functions with the triangular definition, then use **Zadeh's extension-principle constraint**:

$$\mu_{\max(\widetilde A,\widetilde B)}(z)=
\sup_{\substack{x,y\in\mathbb R\\\max(x,y)=z}}
\min\bigl(\mu_{\widetilde A}(x),\mu_{\widetilde B}(y)\bigr).$$

The constraint $\max(x,y)=z$ requires $x\le z$, $y\le z$, and **at least one equality**. Identify the triangle vertices and sketch both membership functions and their maximum; all detailed interval calculations and proofs are on the full assignment page. This is a fuzzy-membership modeling exercise, **not** an extra linear-programming objective.

### فارسی

#### مدل تابع عضویت و عملگر ماکزیمم فازی

در [حل کامل تمرین اعداد فازی](site_docs/assignments/fuzzy-numbers-max.fa.md)، دو عدد مثلثی $\widetilde A=(1,3,7)$ و $\widetilde B=(3,5,6)$ داده شده‌اند. توابع عضویت را از تعریف عدد فازی مثلثی مدل کنید و برای ماکزیمم آن‌ها **اصل گسترش زاده** را بنویسید:

$$\mu_{\max(\widetilde A,\widetilde B)}(z)=
\sup_{\substack{x,y\in\mathbb R\\\max(x,y)=z}}
\min\bigl(\mu_{\widetilde A}(x),\mu_{\widetilde B}(y)\bigr).$$

شرط $\max(x,y)=z$ می‌گوید $x\le z$ و $y\le z$ و **حداقل یکی باید برابر $z$ باشد**. نقاط شکست توابع عضویت را مشخص و نمودارها را رسم کنید. محاسبات کاملِ بازه‌ای و اثبات‌ها در صفحهٔ تشریحی تمرین هستند. این مبحث مدل‌سازی تابع عضویت است، **نه** یک مسئلهٔ اضافی برنامه‌ریزی خطی.

#### اصل گسترش را روی عددهای همین تمرین اجرا کنیم

برای $A=(1,3,7)$ و $B=(3,5,6)$، ابتدا برش‌های آلفا را از دو ضلع مثلث‌ها بسازید:

$$
[A]_{\alpha}=[1+2\alpha,\ 7-4\alpha],\qquad
[B]_{\alpha}=[3+2\alpha,\ 6-\alpha].
$$

در بیشینهٔ فازی، انتهای چپِ بازهٔ حاصل همیشه $3+2\alpha$ است. انتهای راست از مقایسهٔ $7-4\alpha$ و $6-\alpha$ تعیین می‌شود. این دو در $\alpha=\tfrac13$ برابرند؛ پس

$$
[D]_{\alpha}=\begin{cases}
[3+2\alpha,\ 7-4\alpha],&0\le\alpha\le\tfrac13,\\
[3+2\alpha,\ 6-\alpha],&\tfrac13\le\alpha\le1.
\end{cases}
$$

این محاسبهٔ برش‌ها، **تکمیل آموزشی** برای فهم اصل گسترش است؛ اگر سؤال صرفاً تعریف عملگر را بخواهد، رابطهٔ $\sup_{\max(x,y)=z}\min(\mu_A(x),\mu_B(y))$ مبنای پاسخ است. تصور نکنید که تابع عضویت بیشینه الزاماً $\max\{\mu_A(z),\mu_B(z)\}$ است.

---

## آزمون خودآزمایی روز قبل از میان‌ترم

این **سؤالات تألیفیِ تمرینی** بر اساس مدل‌ها و تعریف‌های جلسات ۱ تا ۹ طراحی شده‌اند؛ سؤال رسمی یا نمونه‌سؤال تأییدشدهٔ استاد نیستند. یک برگهٔ خالی بردارید، ابتدا **۴۵ تا ۶۰ دقیقه بدون دیدن پاسخ‌ها** حل کنید و سپس از پاسخنامهٔ پایین همین بخش استفاده کنید. وقتی مدل را می‌نویسید، برای هر متغیر معنا، واحد و دامنه را نیز ذکر کنید.

### بخش اول: مدل‌سازی خطی و کسری

**سؤال ۱ — تشخیص جهت قید.** در یک مسئلهٔ رژیم غذایی گفته شده «ویتامین دریافتی باید دست‌کم ۱۲ واحد باشد» و مصرف هر واحد پنیر، شیر و تخم‌مرغ به‌ترتیب ۱، ۴ و ۲ است. قید را بنویسید و معنی علامت آن را توضیح دهید.

**سؤال ۲ — واحد زمان.** در تولید قایق، ماشین حداکثر ۵ ساعت در دسترس است و برای دو نوع قایق ۲۰ و ۱۵ دقیقه زمان می‌خواهد. قید زمان ماشین را بنویسید.

**سؤال ۳ — اندیس‌گذاری حمل‌ونقل.** با $m$ مبدأ و $n$ مقصد، شرط «از مبدأ $i$ بیشتر از عرضهٔ $a_i$ ارسال نشود» و شرط «مقصد $j$ دقیقاً $b_j$ واحد دریافت کند» را بنویسید.

**سؤال ۴ — موجودی پایان ماه.** در مدل پنج‌ماهه، موازنهٔ ماه دوم و ماه پنجم را با استفاده از تقاضاهای داده‌شده و شرایط $s_0=s_5=0$ بنویسید. توضیح دهید موجودی کدام ماه با علامت مثبت می‌آید.

**سؤال ۵ — ظرفیت ماشین.** برای محصول $i$ و ماشین $j$، با $x_{ij}$ و زمان $t_{ij}$ و ظرفیت $H_j$، قید ماشین شمارهٔ ۳ را بنویسید. چرا روی $i$ جمع می‌زنیم؟

**سؤال ۶ — پالایش.** اگر $x_1$ مقدار نفت خام سبک خریداری‌شده باشد، ۹۵ درصد آن بعد از پالایش باقی بماند و ۴۰ درصد محصول باقی‌مانده گازوئیل باشد، مقدار گازوئیل حاصل از نفت سبک چقدر است؟

**سؤال ۷ — تابع هدف کسری.** چرا $\frac{80x_1+40x_2}{40x_1+20x_2+200}$ با $80x_1+40x_2-(40x_1+20x_2+200)$ هم‌ارز نیست؟

**سؤال ۸ — چارنز–کوپر.** برای مخرج $3x_1+4x_2+20$، متغیرهای تبدیلی و قید نرمال‌سازی را بنویسید.

### بخش دوم: مجموعه‌ها و اعداد فازی

**سؤال ۹ — تابع عضویت.** برای عدد مثلثی $A=(1,5,7)$ تابع عضویت را در دو شاخهٔ غیرصفر و برش آلفا را برای $0<\alpha\le1$ بنویسید.

**سؤال ۱۰ — تعریف‌ها.** تکیه‌گاه، هسته، برش آلفای معمولی و برش آلفای قوی را تعریف کنید. آیا برای یک نقطه با $\mu(x)=\alpha$، آن نقطه در هر دو برش است؟

**سؤال ۱۱ — نمایش LR.** در $(a^L,a^U,\ell,r)_{LR}$ هر پارامتر چه معنایی دارد؟ آیا $\ell$ و $r$ خودشان دو انتهای تکیه‌گاه‌اند؟

**سؤال ۱۲ — رتبه‌بندی.** برای یک عدد ذوزنقه‌ای خطی با $a^L=3$, $a^U=5$, $\ell=1$, $r=3$، رتبهٔ $R=(a^L+a^U)/2+(r-\ell)/4$ را حساب کنید.

**سؤال ۱۳ — بیشینهٔ فازی.** برای $M=(0,2,5)$ و $N=(2,3,4)$، دو برش آلفا و برش بیشینهٔ فازی $D$ را بنویسید. نقطهٔ تغییر شاخهٔ راست در کدام آلفا است؟

**سؤال ۱۴ — Kerre.** در مثال $M=(2,5,12)$ و $N=(2,4,10)$ نشان دهید چرا $D=\widetilde{\max}(M,N)=M$. بدون محاسبهٔ انتگرال، علامت $r(M,N)$ را تعیین کنید.

**سؤال ۱۵ — جریان مالی.** با نرخ ۶ درصد سپردهٔ سال اول و نیاز ۴ میلیون دلاری در ابتدای سال دوم، قید موازنهٔ سال دوم تمرین سرمایه‌گذاری را بنویسید.

**سؤال ۱۶ — تمرین سوم (ماکزیمم فازی).** برای $A=(1,3,7)$ و $B=(3,5,6)$، برش‌های آلفا را بنویسید و آلفایی را پیدا کنید که در آن انتهای راستِ برش بیشینه از یک شاخه به شاخهٔ دیگر تغییر می‌کند.

### پاسخنامهٔ تشریحی کوتاه

پاسخ‌ها را با نوشتهٔ خودتان مقایسه کنید. اگر جواب درست است اما **معنی متغیر یا جهت قید** را توضیح نداده‌اید، آن را کامل محسوب نکنید.

1. $p+4s+2t\ge12$. این قید حداقل مقدار ویتامین A را تضمین می‌کند؛ علامت $\le$ معنی را برعکس می‌کند.
2. $20x+15y\le300$؛ چون ۵ ساعت را به ۳۰۰ دقیقه تبدیل کرده‌ایم.
3. $\sum_{j=1}^n x_{ij}\le a_i$ برای هر $i$ و $\sum_{i=1}^m x_{ij}=b_j$ برای هر $j$. عرضه جمع بر مقصد و تقاضا جمع بر مبدأ است.
4. $x_2+y_2+s_1-s_2=2100$ و $x_5+y_5+s_4=4000$. موجودی *ابتدای* ماه یعنی $s_{i-1}$ با علامت مثبت و موجودی *پایان* ماه یعنی $s_i$ با علامت منفی است.
5. $\sum_{i=1}^3t_{i3}x_{i3}\le H_3$. ماشین ۳ می‌تواند چند محصول بسازد و ساعت‌های مصرفی آن باید با هم جمع شوند.
6. $0.40(0.95)x_1=0.38x_1$. ابتدا مقدار باقیمانده بعد از پالایش و سپس سهم فرآورده محاسبه می‌شود.
7. عبارت اول **نسبت** درآمد به هزینه است؛ عبارت دوم **اختلاف** درآمد و هزینه. این دو عموماً به جواب بهینهٔ یکسان منجر نمی‌شوند.
8. $t=1/(3x_1+4x_2+20)$، $y_i=tx_i$ و $3y_1+4y_2+20t=1$. در تبدیل قیود نیز هر طرف در $t$ ضرب می‌شود.
9. $\mu_A(x)=(x-1)/4$ برای $1<x\le5$ و $(7-x)/2$ برای $5<x<7$؛ در بیرون از $[1,7]$ صفر است. $[A]_{\alpha}=[1+4\alpha,7-2\alpha]$.
10. تکیه‌گاه $\{\mu>0\}$، هسته $\{\mu=1\}$، برش معمولی $\{\mu\ge\alpha\}$ و برش قوی $\{\mu>\alpha\}$ است. نقطه با $\mu=\alpha$ فقط در برش معمولی قرار می‌گیرد.
11. $a^L,a^U$ دو سر هسته‌اند و $\ell,r$ گستردگی سمت چپ و راست‌اند. برای شکل خطی، دو سر تکیه‌گاه به‌ترتیب $a^L-\ell$ و $a^U+r$ است؛ خودِ گستردگی‌ها مختصات مرزی نیستند.
12. $R=(3+5)/2+(3-1)/4=4.5$.
13. $[M]_{\alpha}=[2\alpha,5-3\alpha]$ و $[N]_{\alpha}=[2+\alpha,4-\alpha]$. برش $D$ با بیشینهٔ دو انتهای هر بازه ساخته می‌شود. نقطهٔ تغییر شاخه در $\alpha=1/2$ است.
14. $[M]_{\alpha}=[2+3\alpha,12-7\alpha]$ و $[N]_{\alpha}=[2+2\alpha,10-6\alpha]$؛ هر دو سر برش $M$ بزرگ‌تر یا مساوی‌اند، پس $D=M$. بنابراین $r(M,N)=d(M,M)-d(N,M)=-d(M,N)<0$.
15. $x_2+1.06s_1-s_2=4$. ضریب $1.06$، اصل سپرده و سود یک‌سالهٔ آن است.
16. $[A]_{\alpha}=[1+2\alpha,7-4\alpha]$ و $[B]_{\alpha}=[3+2\alpha,6-\alpha]$. با حل $7-4\alpha=6-\alpha$ به $\alpha=1/3$ می‌رسیم؛ انتهای چپ در تمام آلفاها $3+2\alpha$ است.

### چک نهایی پیش از خواب

- [ ] می‌توانم از صفر، بدون نگاه‌کردن به پاسخ، یک مدل **بیشینه‌سازی** و یک مدل **کمینه‌سازی** بنویسم.
- [ ] در حمل‌ونقل، اندیس عرضه و تقاضا را جابه‌جا نمی‌کنم.
- [ ] در تولید و موجودی، پنج موازنه و دو شرط مرزی را می‌نویسم.
- [ ] در مدل کسری، صورت و مخرج را حفظ می‌کنم و در چارنز–کوپر قید نرمال‌سازی را فراموش نمی‌کنم.
- [ ] می‌توانم تابع عضویت یک عدد مثلثی و برش آلفا را از رأس‌های آن به دست بیاورم.
- [ ] تفاوت برش معمولی و قوی و معنای گستردگی‌های LR را توضیح می‌دهم.
- [ ] برای بیشینهٔ فازی، به‌جای بیشینهٔ نقطه‌ای عضویت‌ها، از اصل گسترش یا برش آلفا استفاده می‌کنم.
- [ ] در Kerre، ابتدا بیشینهٔ فازی را می‌سازم و بعد فاصله را مقایسه می‌کنم.
- [ ] فرض‌های داده‌نشده را بدون توضیح وارد مدل نمی‌کنم و هر نتیجهٔ تکمیلی را از متن جزوه جدا می‌دانم.

**اگر فقط ۳۰ دقیقه تا پایان مطالعه فرصت دارید:** از میان سؤال‌های ۳، ۴، ۸، ۹، ۱۳ و ۱۴ سه مورد را روی کاغذ حل کنید. این‌ها چند خطای رایج و مهم را با هم پوشش می‌دهند.

## Day-before self-assessment

These are **independently written practice questions based on Sessions 01–09**, not official examination questions. Work without looking up the answers first. Always state variable meanings, units, domains, and the rationale for each inequality.

### Questions

1. What is the vitamin-A minimum constraint for diet quantities $p,s,t$ when contributions are $1,4,2$ and the daily requirement is 12?
2. Write the machine-time constraint for 20 and 15 minutes per boat when only five machine-hours are available.
3. Write the supply and exact-demand constraints for a transportation model, making explicit which index is summed.
4. Write the second- and fifth-month balances of the published production/inventory model.
5. Express the capacity constraint of machine 3 when $t_{i3}$ is the time for product $i$ on that machine.
6. Derive usable diesel from purchased light crude when the refinery yield is 95% and the diesel fraction is 40%.
7. Explain why maximizing revenue-to-cost differs from maximizing revenue minus cost.
8. Give the Charnes–Cooper variables and normalization for the denominator $3x_1+4x_2+20$.
9. Derive the two nonzero membership branches and the alpha-cut for $(1,5,7)$.
10. Distinguish support, core, ordinary alpha-cut, and strong alpha-cut.
11. Interpret the four parameters $(a^L,a^U,\ell,r)_{LR}$.
12. Evaluate the course ranking formula for $(3,5,1,3)_{LR}$.
13. Construct the alpha-cut maximum of $(0,2,5)$ and $(2,3,4)$ and determine the switching alpha.
14. Explain why the extension-principle maximum of $(2,5,12)$ and $(2,4,10)$ is the first triangular number, and infer the Kerre score sign.
15. Write the second-year financing balance with a 6% return on the previous year's deposit.
16. For $A=(1,3,7)$ and $B=(3,5,6)$, identify the alpha where the right endpoint of their extension-principle maximum switches branches.

### Answer key

1. $p+4s+2t\ge12$.
2. $20x+15y\le300$ minutes.
3. $\sum_jx_{ij}\le a_i$ and $\sum_ix_{ij}=b_j$.
4. $x_2+y_2+s_1-s_2=2100$ and $x_5+y_5+s_4=4000$.
5. $\sum_{i=1}^3t_{i3}x_{i3}\le H_3$.
6. $0.40\cdot0.95x_1=0.38x_1$.
7. A ratio and a difference represent different objectives.
8. $t=1/(3x_1+4x_2+20)$, $y_i=tx_i$, $3y_1+4y_2+20t=1$.
9. $(x-1)/4$ and $(7-x)/2$ on their respective intervals; $[A]_\alpha=[1+4\alpha,7-2\alpha]$.
10. $\{\mu>0\}$, $\{\mu=1\}$, $\{\mu\ge\alpha\}$, $\{\mu>\alpha\}$.
11. Two core endpoints and two spreads.
12. $4.5$.
13. $[M]_\alpha=[2\alpha,5-3\alpha]$, $[N]_\alpha=[2+\alpha,4-\alpha]$, switching at $\alpha=1/2$.
14. Both alpha-cut endpoints of the first dominate, hence $D=M$ and $r(M,N)=-d(M,N)<0$.
15. $x_2+1.06s_1-s_2=4$.
16. $[A]_{\alpha}=[1+2\alpha,7-4\alpha]$, $[B]_{\alpha}=[3+2\alpha,6-\alpha]$; the right bounds cross at $\alpha=1/3$.

### Final checklist

- [ ] I can rebuild each model from the word problem, not just recall its finished expression.
- [ ] I can explain the direction and units of each constraint.
- [ ] I keep all temporal boundaries, fractional-objective constants, and fuzzy comparison definitions.
- [ ] I distinguish results explicitly supplied by the course notes from independent mathematical extensions.
