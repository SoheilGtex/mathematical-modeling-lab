# آموزش زبان جولیا

این آموزش‌های اختیاری Julia، مکمل مباحث درس مدل‌سازی ریاضی هستند.

بخش Julia به‌صورت جداگانه از پیاده‌سازی‌های پایتون و از **مرور شب امتحان مبتنی بر مدل‌سازیِ تمام جلسات و تمرین‌ها** نگهداری می‌شود.

## مباحث مقدماتی موجود

- [متغیرها](https://github.com/SoheilGtex/mathematical-modeling-lab/blob/main/Julia/01_Basics/01_variables.jl): تعریف متغیر و محاسبه هزینه تولید.
- [ساختارهای کنترلی](https://github.com/SoheilGtex/mathematical-modeling-lab/blob/main/Julia/01_Basics/04_control_flow.jl): شرط‌ها، حلقه‌ها و انشعاب‌های شرطی.
- [توابع](https://github.com/SoheilGtex/mathematical-modeling-lab/blob/main/Julia/01_Basics/05_functions.jl): آرگومان‌ها، مقادیر بازگشتی و محاسبات قابل استفاده مجدد.

## مثال‌های درسی

پوشه `03_Course_Examples/` شامل هفت مثال کاربردی از مدل‌سازی ریاضی و بهینه‌سازی با استفاده از Julia، JuMP و HiGHS است.

- [تولید قایق](https://github.com/SoheilGtex/mathematical-modeling-lab/blob/main/Julia/03_Course_Examples/boat-production.jl): برنامه‌ریزی تولید و بیشینه‌سازی سود.
- [مسئله رژیم غذایی](https://github.com/SoheilGtex/mathematical-modeling-lab/blob/main/Julia/03_Course_Examples/diet.jl): انتخاب مواد غذایی با حداقل هزینه و با رعایت نیازهای تغذیه‌ای.
- [سرمایه‌گذاری](https://github.com/SoheilGtex/mathematical-modeling-lab/blob/main/Julia/03_Course_Examples/investment.jl): برنامه‌ریزی سرمایه‌گذاری و بهینه‌سازی مالی در چند سال.
- [تولید و مدیریت موجودی](https://github.com/SoheilGtex/mathematical-modeling-lab/blob/main/Julia/03_Course_Examples/production-and-inventory.jl): برنامه‌ریزی تولید، اضافه‌کاری و مدیریت موجودی.
- [زمان‌بندی](https://github.com/SoheilGtex/mathematical-modeling-lab/blob/main/Julia/03_Course_Examples/scheduling.jl): زمان‌بندی تولید و تخصیص ظرفیت ماشین‌آلات.
- [تولید تلویزیون](https://github.com/SoheilGtex/mathematical-modeling-lab/blob/main/Julia/03_Course_Examples/television-production.jl): برنامه‌ریزی تولید تلویزیون و بیشینه‌سازی سود.
- [مسئله حمل‌ونقل](https://github.com/SoheilGtex/mathematical-modeling-lab/blob/main/Julia/03_Course_Examples/transportation.jl): برنامه‌ریزی حمل‌ونقل و توزیع با حداقل هزینه.

این مثال‌ها نحوه تعریف متغیرهای تصمیم، توابع هدف و محدودیت‌ها و حل مدل‌های بهینه‌سازی خطی را نشان می‌دهند.

## نحوه اجرا

ابتدا زبان [Julia](https://julialang.org/downloads/) را نصب کنید.

### اجرای مثال‌های مقدماتی

از مسیر اصلی مخزن، دستورهای زیر را اجرا کنید:

```bash
julia Julia/01_Basics/01_variables.jl
julia Julia/01_Basics/04_control_flow.jl
julia Julia/01_Basics/05_functions.jl
```

برای اجرای این مثال‌های مقدماتی فقط خود Julia لازم است و نصب **JuMP و HiGHS** ضروری نیست.

### اجرای مثال‌های درسی

مثال‌های درسی به پکیج‌های زیر نیاز دارند:

- [JuMP](https://jump.dev/JuMP.jl/stable/): برای مدل‌سازی مسائل بهینه‌سازی ریاضی.
- [HiGHS](https://highs.dev/): حل‌کننده مسائل بهینه‌سازی.
- [MathOptInterface](https://jump.dev/MathOptInterface.jl/stable/): برای دسترسی به اطلاعات مدل و وضعیت حل‌کننده.

برای نصب این پکیج‌ها، دستورهای زیر را در محیط Julia اجرا کنید:

```julia
using Pkg
Pkg.add(["JuMP", "HiGHS", "MathOptInterface"])
```

سپس از مسیر اصلی مخزن، فایل مثال موردنظر را اجرا کنید. برای نمونه:

```bash
julia Julia/03_Course_Examples/boat-production.jl
```

برای اجرای سایر مثال‌ها، کافی است نام فایل موردنظر را جایگزین `boat-production.jl` کنید.

## منابع تکمیلی

برای اطلاعات بیشتر به [راهنمای Julia در GitHub](https://github.com/SoheilGtex/mathematical-modeling-lab/blob/main/Julia/README.md) مراجعه کنید. همچنین فهرست [مشارکت‌کنندگان پروژه](https://github.com/SoheilGtex/mathematical-modeling-lab/blob/main/CONTRIBUTORS.md) در دسترس است.