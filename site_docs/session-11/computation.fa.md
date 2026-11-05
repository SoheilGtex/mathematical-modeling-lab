# محاسبات جلسهٔ یازدهم

[کد مبتنی بر کسرهای دقیق](https://github.com/SoheilGtex/mathematical-modeling-lab/blob/main/src/modeling_lab/hesitant_final.py) ترتیب مؤلفه‌های مثلثی و ذوزنقه‌ای را بررسی می‌کند و رتبهٔ تعریف‌شده در جزوه را به‌دست می‌آورد.

```bash
python examples/session_11/01_ranked_hesitant_numbers.py
python -m pytest -q tests/test_session_10_11.py
```

خروجی مثال اصلی باید \(R_1(A)=4.5\) و \(R_1(B)=3.75\) باشد. در یک **سناریوی فرضی و مستقل** نیز مدل \(\max 50x_A+40x_B\) با قید \(2x_A+3x_B\le52.5\) بررسی می‌شود؛ این مدل عددی، رونویسی قطعی از جزوه نیست.

شرح تمام ابهام‌ها در [صفحهٔ ممیزی](audit.md) آمده است.
