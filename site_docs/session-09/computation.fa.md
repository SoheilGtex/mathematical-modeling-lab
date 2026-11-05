# جلسهٔ نهم — بازتولید پاسخ مثال اصلاح‌شده

دادهٔ مثال دست‌نویس $M=(2,5,12)$ و $N=(2,4,10)$ است. در [بازبینی ریاضی فرمول‌ها](source-example.md) توضیح دادیم چرا شیب شاخهٔ چپ $N$ باید $1/2$ و شیب شاخهٔ راست آن $-1/6$ باشد.

مثال اختیاری [`examples/session_09/01_kerre_source_example.py`](https://github.com/SoheilGtex/mathematical-modeling-lab/blob/main/examples/session_09/01_kerre_source_example.py) از پیاده‌سازی دقیق [`fuzzy_comparison.py`](https://github.com/SoheilGtex/mathematical-modeling-lab/blob/main/src/modeling_lab/fuzzy_comparison.py) استفاده می‌کند.

```bash
python examples/session_09/01_kerre_source_example.py
python -m pytest tests/test_session_08_09.py -q
```

خروجی مورد انتظار:

```text
Distance M to maximum: 0
Distance N to maximum: 17/9
Pairwise score: -17/9
Preferred triangle: first
```

**خودِ دو عدد فازی از جزوه حفظ شده‌اند.** فقط مخرج‌های ناسازگار تابع عضویت بر اساس تعریف رسمی مثلث تصحیح شده‌اند. نتیجهٔ عددی و محاسبهٔ انتگرال‌ها در خود دست‌نویس کامل نشده بود.

## چرا کسر دقیق مهم است؟

نقطهٔ تقاطع $14/3$ اعشار مختوم نیست. اگر از همان ابتدا آن را $4.67$ بگیریم، خطای گردکردن به انتگرال منتقل می‌شود و حتی ممکن است تغییر علامت تفاضل را پنهان کند. برنامه از `fractions.Fraction` برای کران‌ها و نقاط شکست استفاده می‌کند و مساحت هر قطعهٔ خطی را دقیق به دست می‌آورد. این بررسی، مکمل حل تشریحی است؛ جای آن را نمی‌گیرد.
