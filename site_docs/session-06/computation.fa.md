# جلسهٔ ششم — بررسی محاسباتی اختیاری

کدهای این بخش برای کنترل فرمول‌ها و مثال‌های درس هستند و **جزو جواب‌های عددی نوشته‌شده در جزوه نیستند**.

از ریشهٔ مخزن اجرا کنید:

```bash
python examples/session_06/01_membership_and_arithmetic.py
python examples/session_06/02_ranked_production.py
python -m pytest tests/test_session_06_07.py -q
```

پیاده‌سازی اصلی در فایل [`src/modeling_lab/fuzzy_sessions.py`](https://github.com/SoheilGtex/mathematical-modeling-lab/blob/main/src/modeling_lab/fuzzy_sessions.py) قرار دارد. مثال اول تابع عضویت، برش‌ها، قرینه و حساب LR را بررسی می‌کند. مثال دوم مدل خطی **مبتنی بر رتبه‌بندی جزوه** را با SciPy/HiGHS حل و فعال‌بودن قیود را کنترل می‌کند.

جواب مورد انتظار این محاسبهٔ مستقل $x_1\approx40.71824429$، $x_2\approx18.79849257$ و رتبهٔ تابع هدف $\approx2568.65440035$ است.

برای مطالعهٔ فرمول‌ها به [مبانی](foundations.md)، [حساب LR](arithmetic.md) و [مدل تولید](ranking-production.md) مراجعه کنید.
