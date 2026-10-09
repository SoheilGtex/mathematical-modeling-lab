# Session 02 — Transportation model | مدل حمل‌ونقل

> **Source scope:** The photographed Session 02 page gives a **symbolic** transportation model and a source-to-destination graph, but **no numeric costs, capacities, or demands**. The numeric 2×2 example below was *constructed independently for learning* and is NOT a class example.
>
> **حدود منبع:** عکس جلسه دوم فقط مدل **کلی و نمادین** حمل‌ونقل را ارائه می‌کند. در جزوه مقدار عددی برای هزینه‌ها، ظرفیت‌ها یا تقاضاها نیامده است. مثال عددی پایین صرفاً **ساختهٔ آموزشی ما** است، نه دادهٔ استاد.

## English — Paper-ready solution

### Problem statement (faithful English rendering)

A transportation company moves goods from $m$ origin warehouses to $n$
destination warehouses. Warehouse $i$ has available supply/capacity $a_i$;
destination $j$ requires $b_j$ units. Shipping one unit from origin $i$
to destination $j$ costs $c_{ij}$. Determine the amounts shipped so that
all destination requirements are fulfilled and the total transport cost is
minimized without exceeding any origin's capacity.

### Decision variables and parameters

- $i=1,\dots,m$ is an origin; $j=1,\dots,n$ is a destination.
- $a_i\ge0$: available quantity at origin $i$ (units of goods).
- $b_j\ge0$: amount required by destination $j$ (same units).
- $c_{ij}$: monetary cost per unit on route $i\to j$.
- $x_{ij}\ge0$: amount sent from origin $i$ to destination $j$.

There are $mn$ decision variables. The arrows in the source diagram represent
possible shipping routes; the handwritten model does not specify route-specific
upper bounds other than source capacities.

### Objective and mathematical formulation

Every route contributes $c_{ij}x_{ij}$ to cost, so:

$$
\boxed{\begin{aligned}
\min_{x}\quad & Z=\sum_{i=1}^{m}\sum_{j=1}^{n}c_{ij}x_{ij}\\
\text{subject to}\quad
&\sum_{j=1}^{n}x_{ij}\le a_i, && i=1,\ldots,m\\
&\sum_{i=1}^{m}x_{ij}=b_j, && j=1,\ldots,n\\
&x_{ij}\ge0, &&i=1,\ldots,m,\quad j=1,\ldots,n.
\end{aligned}}
$$

Why do the directions differ? **Origin stock is a maximum**, so $\le$;
**destination demand must be exactly met** in the source model, so $=$.
Replacing $=$ with $\ge$ is not faithful to the photographed formulation.

### Feasibility check (proof)

Summing destination equalities gives $\sum_{i,j}x_{ij}=\sum_j b_j$.
Summing origin inequalities gives $\sum_{i,j}x_{ij}\le\sum_i a_i$.
Thus a necessary condition is

$$\boxed{\sum_{i=1}^{m}a_i\ge\sum_{j=1}^{n}b_j.}$$

For a complete network where **every origin can ship to every destination**
and there are no extra route restrictions, this is also sufficient for
nonnegative continuous flows. If total supply equals demand, every source
capacity is tight; if supply exceeds demand, some source capacity may remain
unused. This claim must not be transferred to networks with forbidden routes
or additional arc capacities without further checks.

### Supplemental worked numerical example — NOT in the lecture note

To illustrate solving on paper, consider two origins and two destinations:

| Cost per unit | Destination 1 | Destination 2 | Supply |
| --- | ---: | ---: | ---: |
| Origin 1 | 2 | 5 | 10 |
| Origin 2 | 4 | 1 | 20 |
| Demand | 12 | 18 | 30 |

The model is

$$
\begin{aligned}
\min\quad&2x_{11}+5x_{12}+4x_{21}+x_{22}\\
\text{s.t.}\quad&x_{11}+x_{12}\le10,\\
&x_{21}+x_{22}\le20,\\
&x_{11}+x_{21}=12,\\
&x_{12}+x_{22}=18,\\
&x_{ij}\ge0.
\end{aligned}
$$

Because the total supply $10+20=30$ equals total demand $12+18=30$,
both supply inequalities hold with equality in every feasible solution.
Let $t=x_{12}$. Then

$$x_{11}=10-t,\qquad x_{21}=2+t,\qquad x_{22}=18-t.$$

Nonnegativity implies $0\le t\le10$. Substitution into the objective:

$$Z(t)=2(10-t)+5t+4(2+t)+(18-t)=46+6t.$$

As the coefficient of $t$ is positive, the minimum is attained at $t=0$:

$$\boxed{(x_{11},x_{12},x_{21},x_{22})=(10,0,2,18),\quad Z_{\min}=46.}$$

**Why globally optimal?** Every feasible solution has the form above, and
$Z(t)\ge46$ on $[0,10]$. Thus $Z=46$ is a global minimum, not merely a
feasible cost. Destination totals are $10+2=12$ and $0+18=18$; origin totals
are $10$ and $20$.

### Common written-exam pitfalls

1. Defining $x_{ij}$ without explaining the meanings of $i$ and $j$.
2. Using $\ge$ for source capacity instead of $\le$.
3. Using $\le$ for destination demand instead of the source's equality.
4. Forgetting nonnegativity or mixing supply/demand units.
5. Claiming a numerical solution for the lecturer's abstract model without data.
6. Treating an LP solver result as a handwritten optimality proof.

---

## فارسی — پاسخ تشریحی آمادهٔ امتحان

### صورت مسئله

یک شرکت ترابری کالا را از $m$ انبار مبدأ به $n$ انبار مقصد منتقل می‌کند.
ظرفیت/موجودی انبار مبدأ $i$ برابر $a_i$، تقاضای انبار مقصد $j$ برابر $b_j$
و هزینهٔ انتقال هر واحد کالا از مبدأ $i$ به مقصد $j$ برابر $c_{ij}$ است.
می‌خواهیم مقدار انتقال کالا را طوری تعیین کنیم که تمام تقاضاها دقیقاً تأمین
شوند و هزینهٔ کل حمل‌ونقل کمینه باشد، بدون آنکه موجودی هیچ مبدأیی تجاوز شود.

### گام ۱ — تعریف پارامترها و متغیر تصمیم

- $i=1,\ldots,m$: اندیس انبار مبدأ.
- $j=1,\ldots,n$: اندیس انبار مقصد.
- $a_i$: حداکثر کالای قابل ارسال از مبدأ $i$.
- $b_j$: مقدار کالای موردنیاز در مقصد $j$.
- $c_{ij}$: هزینهٔ حمل **یک واحد** کالا از $i$ به $j$.
- $x_{ij}$: تعداد/مقدار واحد کالایی که واقعاً از $i$ به $j$ ارسال می‌شود.

در کل $mn$ متغیر تصمیم داریم.

### گام ۲ — تابع هدف

هزینهٔ مسیر $(i,j)$ برابر $c_{ij}x_{ij}$ است. پس هزینهٔ کل برابر جمع هزینهٔ
تمام مسیرهاست:

$$\boxed{\min Z=\sum_{i=1}^{m}\sum_{j=1}^{n}c_{ij}x_{ij}.}$$

### گام ۳ — استخراج قیود

**قید عرضه/ظرفیت مبدأ:** خروجی انبار $i$ نباید از موجودی آن بیشتر شود:

$$\boxed{\sum_{j=1}^{n}x_{ij}\le a_i\quad (i=1,\ldots,m).}$$

**قید تقاضای مقصد:** ورودی انبار $j$ باید دقیقاً به مقدار تقاضا باشد:

$$\boxed{\sum_{i=1}^{m}x_{ij}=b_j\quad (j=1,\ldots,n).}$$

**قید نامنفی بودن:** مقدار کالای ارسال‌شده منفی نیست:

$$\boxed{x_{ij}\ge0.}$$

### گام ۴ — مدل نهایی

$$
\boxed{\begin{aligned}
\min\quad &\sum_{i=1}^{m}\sum_{j=1}^{n}c_{ij}x_{ij}\\
\text{s.t.}\quad&\sum_{j=1}^{n}x_{ij}\le a_i &&\forall i,\\
&\sum_{i=1}^{m}x_{ij}=b_j &&\forall j,\\
&x_{ij}\ge0 &&\forall i,j.
\end{aligned}}
$$

### گام ۵ — بررسی امکان‌پذیری

از جمع قیود تقاضا:

$$\sum_i\sum_j x_{ij}=\sum_j b_j.$$

از جمع قیود عرضه:

$$\sum_i\sum_j x_{ij}\le\sum_i a_i.$$

پس شرط لازم وجود جواب مجاز عبارت است از:

$$\boxed{\sum_i a_i\ge\sum_j b_j.}$$

در شبکهٔ کامل بدون محدودیت اضافی برای مسیرها، این شرط برای جریان‌های
پیوستهٔ نامنفی کافی نیز هست. در شبکه‌های دارای مسیر ممنوع، به بررسی بیشتری
نیاز داریم.

### گام ۶ — نمونهٔ عددی تکمیلی (نه مثال عددی جزوه)

برای تمرین روش حل دستی، ماتریس هزینهٔ $(2,5;4,1)$، عرضه‌های $(10,20)$ و
تقاضاهای $(12,18)$ را **خودمان انتخاب کرده‌ایم**.

چون مجموع عرضه و تقاضا هر دو ۳۰ است، قیود عرضه با تساوی برقرار می‌شوند.
با قرار دادن $t=x_{12}$:

$$x_{11}=10-t,\quad x_{21}=2+t,\quad x_{22}=18-t,\quad 0\le t\le10.$$

تابع هدف:

$$Z(t)=2(10-t)+5t+4(2+t)+(18-t)=46+6t.$$

چون $t\ge0$ داریم $Z(t)\ge46$. در $t=0$ این کران به دست می‌آید. در نتیجه:

$$\boxed{x_{11}=10,\;x_{12}=0,\;x_{21}=2,\;x_{22}=18,\quad Z_{\min}=46.}$$

**کنترل جواب:** موجودی مبدأها $10$ و $20$ و تقاضای مقصدها $12$ و $18$
دقیقاً رعایت می‌شوند. چون تمام جواب‌های مجاز بررسی‌شده در قالب $t$ قرار
دارند و هزینه $46+6t$ است، این جواب بهینهٔ سراسری است.

### اشتباهات رایج

- جابه‌جا گرفتن اندیس مبدأ و مقصد در $x_{ij}$.
- اشتباه گرفتن «حداکثر موجودی» با «حداقل تقاضا».
- نوشتن نامساوی برای قید تقاضایی که در جزوه به‌صورت **تساوی** آمده است.
- حذف شرط $x_{ij}\ge0$.
- ساختن دادهٔ عددی و نسبت‌دادن آن به استاد؛ **جزوه هیچ دادهٔ عددی حمل‌ونقل ندارد**.
