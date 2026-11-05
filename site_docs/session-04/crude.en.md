# Light and Heavy Crude Oil — Full Worked Solution

> **Source:** Session 04, handwritten page 3. Oil prices, recovery rates, refined-product fractions and demand minimums are from the lecture. Numerical optimization and the lower-bound proof are independent additions.

## 1. Problem statement

A refinery can buy **light** and **heavy** crude oil. The purchase prices are **$20** and **$15** per crude unit, respectively. During refining, **5%** of light crude and **8%** of heavy crude is lost; thus their usable yields are $0.95$ and $0.92$. The usable amount of each crude type yields the indicated fractions of three petroleum products:

| Refined output / crude type | Light | Heavy | Minimum requirement |
| --- | ---: | ---: | ---: |
| Diesel | 0.40 | 0.32 | 1,000,000 |
| Kerosene | 0.20 | 0.40 | 500,000 |
| Jet fuel | 0.35 | 0.20 | 300,000 |

The percentages in the table apply **after refining losses**. For example, one purchased unit of heavy crude yields $0.92(0.32)=0.2944$ units of diesel. (Other unspecified output fractions are not assumed to be additional saleable products.)

## 2. Decision variables and LP model

Let $x_1\ge0$ be units of **light crude purchased** and $x_2\ge0$ units of **heavy crude purchased**. Minimize purchasing cost:

$$\boxed{\min\ Z=20x_1+15x_2}$$

subject to all three minimum output requirements:

$$
\boxed{\begin{aligned}
0.40(0.95)x_1+0.32(0.92)x_2&\ge1,000,000 &&\text{diesel}\\
0.20(0.95)x_1+0.40(0.92)x_2&\ge500,000 &&\text{kerosene}\\
0.35(0.95)x_1+0.20(0.92)x_2&\ge300,000 &&\text{jet fuel}\\
x_1,x_2&\ge0.
\end{aligned}}
$$

In decimals, the coefficients are $(0.38,0.2944)$, $(0.19,0.368)$, and $(0.3325,0.184)$. Output minimums use $\ge$. **Do not divide by recovery again:** the loss factor has already been multiplied into each coefficient.

## 3. Independent optimum and feasibility check

An optimal plan buys only heavy crude:

$$
\boxed{x_1^*=0,\qquad x_2^*=\frac{1,000,000}{0.32(0.92)}\approx3,396,739.130435.}
$$

It produces diesel 1,000,000; kerosene 1,250,000; and jet fuel 625,000. All requirements are met. The minimum expense is

$$
\boxed{Z_{\min}=15\cdot\frac{1,000,000}{0.2944}\approx50,951,086.96\text{ USD}.}
$$

## 4. Exact lower-bound proof

To make 1 unit of diesel using the best available feedstock, any feasible plan costs at least $15/0.2944$ per diesel unit. Indeed,

$$\frac{20}{0.38}>\frac{15}{0.2944},$$

so for any nonnegative $x_1,x_2$:

$$
20x_1+15x_2\ge\frac{15}{0.2944}(0.38x_1+0.2944x_2)\ge\frac{15}{0.2944}(1,000,000).
$$

The heavy-only plan reaches this bound **and** meets the other two minimums. This proves global optimality; the extra requirements are slack at the optimum.

## 5. Exam focus

Identify **purchased input amounts**, not amounts of refined outputs, as the variables. Write the $0.95$/$0.92$ recovery factors inside each constraint; the three minimums are $\ge$, and the objective is minimum purchase cost in dollars. The computed solution is a supplementary worked result.
