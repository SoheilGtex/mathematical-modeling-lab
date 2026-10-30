# Julia for Mathematical Modeling

This directory contains Julia learning materials and code examples for the Mathematical Modeling course.

The goal is to learn Julia step by step and use it to formulate, implement, and solve mathematical models.

## Objectives

- Learn the fundamentals of the Julia programming language.
- Practice Julia through small, practical examples.
- Implement mathematical models using Julia.
- Use optimization packages such as JuMP and HiGHS to formulate and solve optimization problems.
- Organize course examples into readable, reusable, and well-documented code.

## Contents

This directory includes the following sections:

- **Julia Fundamentals:** Introduction to the Julia programming language and its basic features.
- **Mathematical Modeling:** Translating mathematical formulations into Julia code.
- **Optimization:** Modeling objective functions and constraints using JuMP.
- **Solvers:** Solving optimization problems with HiGHS.
- **Course Examples:** Practical implementations of mathematical modeling and optimization problems.

### Course Examples

The `03_Course_Examples/` directory contains seven Julia examples covering different mathematical modeling and optimization problems:

| File | Description |
|---|---|
| `boat-production.jl` | Boat production planning and profit maximization. |
| `diet.jl` | Diet optimization and minimum-cost food selection. |
| `investment.jl` | Investment planning and financial optimization over multiple years. |
| `production-and-inventory.jl` | Production planning, overtime, and inventory management. |
| `scheduling.jl` | Production scheduling and machine capacity allocation. |
| `television-production.jl` | Television production planning and profit maximization. |
| `transportation.jl` | Transportation planning and minimum-cost distribution. |

These examples use linear programming to define decision variables, objective functions, and constraints. They are solved using the JuMP modeling package and the HiGHS optimization solver.


## Requirements

### Julia Basics

To run the introductory Julia examples in `01_Basics/`, you only need to install [Julia](https://julialang.org/downloads/).

No additional packages are required for these examples.

### Course and Optimization Examples

The examples in `03_Course_Examples/` require the following Julia packages:

- [JuMP](https://jump.dev/JuMP.jl/stable/): For mathematical optimization modeling.
- [HiGHS](https://highs.dev/): An optimization solver used to solve linear programming models.
- [MathOptInterface](https://jump.dev/MathOptInterface.jl/stable/): For accessing solver statuses and optimization model information.

Install these packages in your Julia environment:

```julia
using Pkg
Pkg.add(["JuMP", "HiGHS", "MathOptInterface"])
```

**Note:** These packages are not required for the basic Julia examples in `01_Basics/`.

## Getting Started

1. Install Julia.
2. Open the Julia REPL or a Julia-compatible editor.
3. Install the packages required by the example.
4. Navigate to the relevant `.jl` file and run it.

## Contributing

Contributions, corrections, and suggestions are welcome. Please keep examples clear, reproducible, and consistent with the mathematical formulation they implement.

---

# جولیا برای مدل‌سازی ریاضی

این پوشه شامل مطالب آموزشی و مثال‌های کدنویسی به زبان جولیا برای درس مدل‌سازی ریاضی است.

هدف این بخش، یادگیری گام‌به‌گام زبان جولیا و استفاده از آن برای صورت‌بندی، پیاده‌سازی و حل مدل‌های ریاضی است.

## اهداف

- یادگیری مبانی زبان برنامه‌نویسی جولیا.
- تمرین جولیا از طریق مثال‌های کوچک و کاربردی.
- پیاده‌سازی مدل‌های ریاضی با استفاده از جولیا.
- استفاده از بسته‌های بهینه‌سازی مانند JuMP و HiGHS برای صورت‌بندی و حل مسائل بهینه‌سازی.
- سازمان‌دهی مثال‌های درسی به‌صورت کدهایی خوانا، قابل استفاده مجدد و مستند.

## محتوا

این پوشه شامل بخش‌های زیر است:

- **مبانی جولیا:** آشنایی با زبان برنامه‌نویسی جولیا و قابلیت‌های پایه آن.
- **مدل‌سازی ریاضی:** تبدیل صورت‌بندی‌های ریاضی به کد جولیا.
- **بهینه‌سازی:** تعریف تابع هدف و محدودیت‌ها با استفاده از JuMP.
- **حل‌کننده‌ها:** حل مسائل بهینه‌سازی با استفاده از HiGHS.
- **مثال‌های درسی:** پیاده‌سازی کاربردی مسائل مدل‌سازی ریاضی و بهینه‌سازی.

### مثال‌های درسی

پوشه `03_Course_Examples/` شامل هفت مثال برنامه‌نویسی جولیا است که موضوعات مختلف مدل‌سازی ریاضی و بهینه‌سازی را پوشش می‌دهند:

| فایل | توضیحات |
|---|---|
| `boat-production.jl` | برنامه‌ریزی تولید قایق و بیشینه‌سازی سود. |
| `diet.jl` | بهینه‌سازی رژیم غذایی و انتخاب مواد غذایی با حداقل هزینه. |
| `investment.jl` | برنامه‌ریزی سرمایه‌گذاری و بهینه‌سازی مالی در چند سال. |
| `production-and-inventory.jl` | برنامه‌ریزی تولید، اضافه‌کاری و مدیریت موجودی. |
| `scheduling.jl` | زمان‌بندی تولید و تخصیص ظرفیت ماشین‌آلات. |
| `television-production.jl` | برنامه‌ریزی تولید تلویزیون و بیشینه‌سازی سود. |
| `transportation.jl` | برنامه‌ریزی حمل‌ونقل و توزیع با حداقل هزینه. |

این مثال‌ها با استفاده از برنامه‌ریزی خطی، متغیرهای تصمیم، توابع هدف و محدودیت‌ها را تعریف می‌کنند. حل مسائل نیز با استفاده از بسته مدل‌سازی JuMP و حل‌کننده بهینه‌سازی HiGHS انجام می‌شود.

## پیش‌نیازها

### مبانی زبان Julia

برای اجرای مثال‌های مقدماتی زبان جولیا در پوشه `01_Basics/`، تنها کافی است زبان برنامه‌نویسی [Julia](https://julialang.org/downloads/) را نصب کنید.

برای اجرای این مثال‌ها، به نصب هیچ پکیج اضافی نیاز ندارید.

### مثال‌های درسی و بهینه‌سازی

مثال‌های موجود در پوشه `03_Course_Examples/` به پکیج‌های زیر در زبان Julia نیاز دارند:

- [JuMP](https://jump.dev/JuMP.jl/stable/): برای مدل‌سازی مسائل بهینه‌سازی ریاضی.
- [HiGHS](https://highs.dev/): یک حل‌گر بهینه‌سازی برای حل مسائل برنامه‌ریزی خطی.
- [MathOptInterface](https://jump.dev/MathOptInterface.jl/stable/): برای دسترسی به وضعیت حل‌کننده و اطلاعات مدل‌های بهینه‌سازی.

برای نصب این پکیج‌ها، دستورات زیر را در محیط Julia اجرا کنید:

```julia
using Pkg
Pkg.add(["JuMP", "HiGHS", "MathOptInterface"])
```

**نکته:** نصب این پکیج‌ها برای اجرای مثال‌های مقدماتی زبان جولیا در پوشه `01_Basics/` ضروری نیست.

## شروع کار

۱. زبان جولیا را نصب کنید.

۲. محیط تعاملی جولیا (Julia REPL) یا یک ویرایشگر سازگار با آن را باز کنید.

۳. بسته‌های موردنیاز مثال را نصب کنید.

۴. فایل `.jl` مربوط به مثال را پیدا کرده و اجرا کنید.

## مشارکت

از مشارکت‌ها، اصلاحات و پیشنهادها استقبال می‌شود. لطفاً مثال‌ها را خوانا، قابل بازتولید و سازگار با صورت‌بندی ریاضی مسئله نگه دارید.