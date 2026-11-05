# جلسهٔ هشتم — کنترل دقیق با پایتون (اختیاری)

محاسبات [بیشینهٔ فازی](extension-recap.md) و [فاصلهٔ Kerre](distance.md) بدون نرم‌افزار کامل‌اند. در این بخش فقط پاسخ‌ها را با **کسرهای دقیق** و بدون خطای تقریبی انتگرال‌گیری کنترل می‌کنیم.

کد اصلی در [`src/modeling_lab/fuzzy_comparison.py`](https://github.com/SoheilGtex/mathematical-modeling-lab/blob/main/src/modeling_lab/fuzzy_comparison.py) و مثال اجرایی در [`examples/session_08/01_maximum_geometry.py`](https://github.com/SoheilGtex/mathematical-modeling-lab/blob/main/examples/session_08/01_maximum_geometry.py) قرار دارد.

از ریشهٔ مخزن، پس از فعال‌کردن محیط پایتون، اجرا کنید:

```bash
python examples/session_08/01_maximum_geometry.py
python -m pytest tests/test_session_08_09.py -q
```

| کمیت | مقدار دقیق |
| --- | ---: |
| نقاط تابع بیشینه $(z,\mu_D(z))$ | $(2,0),(3,1),(7/2,1/2),(5,0)$ |
| $d(M,D)$ | $3/2$ |
| $d(N,D)$ | $1/4$ |
| $r(M,N)$ | $5/4$ |

برنامه ابتدا کران‌های برش آلفا را بیشینه می‌گیرد، منحنی حاصل را به شکل قطعه‌ای می‌سازد و انتگرال قدرمطلق را در نقاط برخورد تفکیک می‌کند. **به‌جای اصل گسترش از بیشینهٔ نقطه‌ای توابع عضویت استفاده نشده است.** این کد برای بررسی تکمیلی است و جزو شرط حل امتحان تشریحیِ مدل‌سازی نیست.
