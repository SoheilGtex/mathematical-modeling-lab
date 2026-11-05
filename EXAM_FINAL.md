# مرور پایان‌ترم

**Final Exam Review: Sessions 10+ only. Sessions 01–09 are covered in EXAM_NIGHT.md.**

**فقط جلسات ۱۰ به بعد. مرور میان‌ترمِ جلسات ۱ تا ۹ در EXAM_NIGHT.md قرار دارد.**

This is an independent student learning aid, not a published exam syllabus.

**Generated file:** edit review_sources, then run python scripts/build_exam_night.py.

## Session 10 | جلسهٔ دهم

### English

#### Hesitant membership: define the modeling object

- A usual fuzzy set uses \(\mu:X\to[0,1]\). A **hesitant** fuzzy set assigns each \(x\) a finite nonempty **set** \(h(x)\subseteq[0,1]\), not a probability distribution.
- For the lecture's \(X=\{x_1,x_2,x_3\}\), specify \(h(x_1)=\{0.2,0.4,0.5\}\), \(h(x_2)=\{0.3,0.4\}\), \(h(x_3)=\{0.2,0.3,0.5,0.6\}\).
- In the five-student height example, write the crisp threshold set \(\{b,c\}\) for heights strictly greater than 180 cm. Explain what additional membership function an ordinary fuzzy set requires and why differing definitions of "tall" motivate hesitant grades.
- Distinguish a **hesitant fuzzy set** (several grades per element) from a **hesitant fuzzy number** (a family of fuzzy-number estimates). The lecture's fuzzy-intersection requirement is not fully specified.
- [Formal HFS definition](site_docs/session-10/hesitant.en.md) · [height example](site_docs/session-10/heights.en.md) · [fuzzy numbers](site_docs/session-10/numbers.en.md).

### فارسی

#### عضویت مردد: صورت‌بندی دقیق مفهوم

- در مجموعهٔ فازی معمولی تابع \(\mu:X\to[0,1]\) داریم؛ در مجموعهٔ فازی **مردد**، برای هر عضو \(x\) مجموعه‌ای متناهی و ناتهی از درجات \(h(x)\subseteq[0,1]\) تعریف می‌کنیم. این درجات احتمال نیستند.
- برای مثال جزوه با \(X=\{x_1,x_2,x_3\}\)، بنویسید: \(h(x_1)=\{0.2,0.4,0.5\}\)، \(h(x_2)=\{0.3,0.4\}\) و \(h(x_3)=\{0.2,0.3,0.5,0.6\}\).
- در مسئلهٔ قد پنج دانشجو، مجموعهٔ قطعی با معیار قد **بزرگ‌تر از ۱۸۰ سانتی‌متر** برابر \(\{b,c\}\) است. توضیح بدهید چگونه یک تابع عضویت فازی و اختلاف‌نظر دربارهٔ مفهوم «قدبلند» به مدل مردد می‌رسد.
- **مجموعهٔ فازی مردد** (چند درجه برای یک عضو) با **عدد فازی مردد** (چند عدد فازی به‌عنوان برآورد) تفاوت دارد. شرط اشتراک اعداد فازی در جزوه نیازمند تعیین تعریف دقیق اشتراک است.
- [تعریف HFS](site_docs/session-10/hesitant.fa.md) · [مثال قد](site_docs/session-10/heights.fa.md) · [اعداد فازی مردد](site_docs/session-10/numbers.fa.md).

## Session 11 | جلسهٔ یازدهم

### English

#### Hesitant fuzzy numbers: ranking and production formulation

- For \(\mathcal H=\{(a_j,b_j,c_j,d_j):1\le j\le p\}\), formulate the lecture's ranking \(R_1(\mathcal H)=\frac{1}{4p}\sum_j(a_j+b_j+c_j+d_j)\). State that these are *trapezoidal* estimates.
- In the source comparison, \(\mathcal A=\{(1,3,5,9),(2,4,5,7)\}\) and \(\mathcal B=\{(-1,2,3,8),(2,3,4,9)\}\), giving \(R_1(A)=4.5>R_1(B)=3.75\).
- For production, define \(x_A,x_B\ge0\), hesitant fuzzy profits \(\widetilde P_A,\widetilde P_B\), hesitant processing times \(\widetilde T_A,\widetilde T_B\), and capacity \(\widetilde C\). Formulate \(\max\widetilde Z=\widetilde P_Ax_A+\widetilde P_Bx_B\) subject to \(\widetilde T_Ax_A+\widetilde T_Bx_B\preceq\widetilde C\).
- **Do not invent** a deterministic equivalent before defining the fuzzy comparison rule. In particular, the source's questionable final digits of A's second profit and first capacity require verification.
- [Ranking derivation](site_docs/session-11/ranking.en.md) · [production modeling](site_docs/session-11/production.en.md) · [source audit](site_docs/session-11/audit.en.md).

### فارسی

#### رتبه‌بندی و مدل تولید با اعداد فازی مردد

- برای \(\mathcal H=\{(a_j,b_j,c_j,d_j):1\le j\le p\}\)، امتیاز جزوه را بنویسید: \(R_1(\mathcal H)=\frac{1}{4p}\sum_j(a_j+b_j+c_j+d_j)\). این فرمول مربوط به **مؤلفه‌های ذوزنقه‌ای** است.
- در مثال مقایسه، \(\mathcal A=\{(1,3,5,9),(2,4,5,7)\}\) و \(\mathcal B=\{(-1,2,3,8),(2,3,4,9)\}\)؛ رتبه‌ها به‌ترتیب \(4.5\) و \(3.75\) هستند.
- در تولید، \(x_A,x_B\ge0\) را متغیر مقدار تولید تعریف کنید. اگر سودهای مردد \(\widetilde P_A,\widetilde P_B\)، زمان‌های مردد \(\widetilde T_A,\widetilde T_B\) و ظرفیت \(\widetilde C\) باشند، مدل \(\max\widetilde Z=\widetilde P_Ax_A+\widetilde P_Bx_B\) با قید \(\widetilde T_Ax_A+\widetilde T_Bx_B\preceq\widetilde C\) نوشته می‌شود.
- **قبل از تعریف قاعدهٔ مقایسهٔ فازی، مدل قطعی معادل حدس نزنید.** چند رقم دست‌نویس در سود دوم A و ظرفیت اول نیازمند تأییدند.
- [محاسبهٔ رتبه‌ها](site_docs/session-11/ranking.fa.md) · [مدل تولید](site_docs/session-11/production.fa.md) · [ممیزی دست‌نویس](site_docs/session-11/audit.fa.md).
