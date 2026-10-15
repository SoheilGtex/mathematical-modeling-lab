# Julia for Mathematical Modeling

**Project contributors:** [Soheil Salmani](https://github.com/SoheilGtex) · [Mahdieh Moghiseh](https://github.com/mahdiehmg)

This directory contains Julia learning materials and code examples for the Mathematical Modeling course.

The goal is to learn Julia step by step and use it to formulate, implement, and solve mathematical models.

## Objectives

- Learn the fundamentals of the Julia programming language.
- Practice Julia through small, practical examples.
- Implement mathematical models using Julia.
- Use optimization packages such as JuMP and HiGHS to formulate and solve optimization problems.
- Organize course examples into readable, reusable, and well-documented code.

## Contents

The directory will gradually include:

- **Julia Fundamentals** 
- **Mathematical Modeling:** Translating mathematical formulations into Julia code.
- **Optimization:** Modeling objective functions and constraints using JuMP.
- **Solvers:** Solving optimization problems with HiGHS.
- **Course Examples:** Julia implementations of relevant mathematical modeling exercises and examples.

## Requirements

### Julia Basics

To run the introductory Julia examples in `01_Basics/`, you only need to install [Julia](https://julialang.org/downloads/).

No additional packages are required for these examples.

### Optimization Examples

The optimization examples in `02_Optimization/` may require the following Julia packages:

- [JuMP](https://jump.dev/JuMP.jl/stable/): for mathematical optimization modeling.
- [HiGHS](https://highs.dev/): an optimization solver used to solve supported optimization models.

Install these packages in the Julia environment you use to run the optimization examples:

```julia
using Pkg
Pkg.add(["JuMP", "HiGHS"])
```

**Note:** Install JuMP and HiGHS only if you intend to run examples that use them. They are not required for the basic Julia examples.

## Getting Started

1. Install Julia.
2. Open the Julia REPL or a Julia-compatible editor.
3. Install the packages required by the example.
4. Navigate to the relevant `.jl` file and run it.

## Contributing

Contributions, corrections, and suggestions are welcome. Please keep examples clear, reproducible, and consistent with the mathematical formulation they implement.

---

# جولیا برای مدل‌سازی ریاضی

**مشارکت‌کنندگان پروژه:** [سهیل سلمانی](https://github.com/SoheilGtex) · [مهدیه مقیسه](https://github.com/mahdiehmg)

این پوشه شامل مطالب آموزشی و مثال‌های کدنویسی به زبان جولیا برای درس مدل‌سازی ریاضی است.

هدف این بخش، یادگیری گام‌به‌گام زبان جولیا و استفاده از آن برای  پیاده‌سازی و حل مدل‌های ریاضی است.

## اهداف

- یادگیری مبانی زبان برنامه‌نویسی جولیا.
- تمرین جولیا از طریق مثال‌های کوچک و کاربردی.
- پیاده‌سازی مدل‌های ریاضی با استفاده از جولیا.
- استفاده از بسته‌های بهینه‌سازی مانند JuMP و HiGHS برای صورت‌بندی و حل مسائل بهینه‌سازی.
- سازمان‌دهی مثال‌های درسی به‌صورت کدهایی خوانا، قابل استفادهٔ مجدد و مستند.

## محتوا

این پوشه به‌تدریج شامل بخش‌های زیر خواهد شد:

- **مبانی جولیا**
- **مدل‌سازی ریاضی:** تبدیل صورت‌بندی‌های ریاضی به کد جولیا.
- **بهینه‌سازی:** تعریف تابع هدف و محدودیت‌ها با استفاده از JuMP.
- **حل‌کننده‌ها:** حل مسائل بهینه‌سازی با استفاده از HiGHS.
- **مثال‌های درسی:** پیاده‌سازی مثال‌ها و تمرین‌های مرتبط با درس مدل‌سازی ریاضی در جولیا.

## پیش‌نیازها

### مبانی زبان Julia

برای اجرای مثال‌های مقدماتی زبان Julia در پوشه `01_Basics/`، تنها کافی است زبان برنامه‌نویسی [Julia](https://julialang.org/downloads/) را نصب کنید.

برای اجرای این مثال‌ها، به نصب هیچ پکیج اضافی نیاز ندارید.

### مثال‌های بهینه‌سازی

مثال‌های بهینه‌سازی در پوشه `02_Optimization/` ممکن است به پکیج‌های زیر در زبان Julia نیاز داشته باشند:

- [JuMP](https://jump.dev/JuMP.jl/stable/): برای مدل‌سازی مسائل بهینه‌سازی ریاضی.
- [HiGHS](https://highs.dev/): یک حل‌گر بهینه‌سازی که برای حل مدل‌های بهینه‌سازی پشتیبانی‌شده استفاده می‌شود.

این پکیج‌ها را در محیط Julia مورد استفاده برای اجرای مثال‌های بهینه‌سازی نصب کنید:

```julia
using Pkg
Pkg.add(["JuMP", "HiGHS"])
```

**نکته:** نصب JuMP و HiGHS تنها زمانی لازم است که قصد اجرای مثال‌هایی را داشته باشید که از این ابزارها استفاده می‌کنند. این پکیج‌ها برای اجرای مثال‌های مقدماتی زبان Julia ضروری نیستند.
## شروع کار

۱. زبان جولیا را نصب کنید.

۲. محیط تعاملی جولیا (Julia REPL) یا یک ویرایشگر سازگار با آن را باز کنید.

۳. بسته‌های موردنیاز مثال را نصب کنید.

۴. فایل `.jl` مربوط به مثال را پیدا کرده و اجرا کنید.

## مشارکت

از مشارکت‌ها، اصلاحات و پیشنهادها استقبال می‌شود. لطفاً مثال‌ها را خوانا، قابل بازتولید و سازگار با صورت‌بندی ریاضی مسئله نگه دارید.
