# محاسبات جلسهٔ دهم

ماژول [`src/modeling_lab/hesitant_final.py`](https://github.com/SoheilGtex/mathematical-modeling-lab/blob/main/src/modeling_lab/hesitant_final.py) برای درجات عضویت و تابع رمپ از کسرهای دقیق استفاده می‌کند.

پس از نصب بستهٔ Python مخزن، اجرا کن:

```bash
python examples/session_10/01_hesitant_membership.py
python -m pytest -q tests/test_session_10_11.py
```

کد، مجموعهٔ خالی را رد می‌کند، قرارداشتن درجه‌ها در بازهٔ \([0,1]\) را کنترل می‌کند، درجات تکراری را حذف می‌کند و نتیجهٔ قطعی \(\{b,c\}\) را بررسی می‌کند.

**محدودیت:** درجات مردد، احتمال نیستند؛ همچنین بازه‌های مختلف «قدبلند بودن» صرفاً انتخاب‌های مدل‌سازی‌اند و از داده‌ها برآورد آماری نشده‌اند.
