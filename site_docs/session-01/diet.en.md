# Minimum-Cost Diet — Full Written Solution

**Source:** handwritten lecture notes, pp. 1–2. **From the notes:** data, variable meanings, objective, two minimum-vitamin constraints, and nonnegativity. **Added for the exam guide:** explicit paper-and-pencil solution, optimality proof, checks, and study questions. The notes do **not** give a numerical optimum.

## A. Problem statement

A daily diet may contain three foods: **cheese**, **milk**, and **eggs**. Each food supplies vitamins A and B. The diet must provide at least **12 units of vitamin A** and **14 units of vitamin B** per day. The cost and vitamin contents **per food unit** are:

| Food | Vitamin A | Vitamin B | Cost (toman/unit) |
| --- | ---: | ---: | ---: |
| Cheese | 1 | 1 | 100 |
| Milk | 4 | 2 | 50 |
| Eggs | 2 | 3 | 40 |

**Question:** Determine the daily amounts of the foods that meet the nutritional requirements at **minimum total cost**. Formulate the optimization model and solve it.

## B. Decision variables and assumptions

Let

- $p$ = number of units of cheese consumed per day;
- $s$ = number of units of milk consumed per day;
- $t$ = number of units of eggs consumed per day.

The **lecture model** allows continuous, nonnegative quantities: $p,s,t\ge0$. It assumes each unit contributes a constant amount of each vitamin and has a constant price. Integer eggs would be an **additional** assumption, not present in the source formulation.

## C. Objective function

The cost of $p$ cheese units is $100p$ toman, of $s$ milk units is $50s$ toman, and of $t$ egg units is $40t$ toman. Therefore the daily total cost is

$$Z=100p+50s+40t.$$

We seek to **minimize** $Z$.

## D. Derivation of every constraint

1. **Vitamin A (minimum 12):** the foods contribute $p$, $4s$, and $2t$ units. Since the requirement is *at least* 12,

   $$p+4s+2t\ge12.$$

2. **Vitamin B (minimum 14):** the foods contribute $p$, $2s$, and $3t$ units. Thus,

   $$p+2s+3t\ge14.$$

3. **Nonnegative food amounts:**

   $$p\ge0,\qquad s\ge0,\qquad t\ge0.$$

**Direction check:** both nutritional constraints use $\ge$ because they are **minimum** requirements.

## E. Complete mathematical formulation

$$
\boxed{\begin{aligned}
\min\quad &Z=100p+50s+40t\\
\text{s.t.}\quad &p+4s+2t\ge12 &&\text{(vitamin A)}\\
&p+2s+3t\ge14 &&\text{(vitamin B)}\\
&p,s,t\ge0.
\end{aligned}}
$$

This is a **linear programming minimization problem**.

## F. Hand solution (without Python or a solver)

**Step 1 — Identify a promising candidate.** Start with $p=0$ and examine a point where both vitamin constraints are tight:

$$4s+2t=12,\qquad2s+3t=14.$$

The first equation gives $2s+t=6$, so $t=6-2s$. Substitute into the second:

$$2s+3(6-2s)=14\ \Longrightarrow\ -4s=-4\ \Longrightarrow\ s=1.$$

Then $t=6-2(1)=4$. Our **candidate** is

$$\boxed{(p,s,t)=(0,1,4)}.$$

**Important:** Solving two equalities gives a candidate, **not by itself a proof of optimality**. We must establish a lower bound on the cost of *every* feasible diet.

**Step 2 — Prove a universal lower bound.** Multiply the vitamin A constraint by $\frac{35}{4}=8.75$ and the vitamin B constraint by $\frac{15}{2}=7.5$. Both multipliers are nonnegative, so the inequality directions are preserved:

$$
\frac{35}{4}(p+4s+2t)+\frac{15}{2}(p+2s+3t)
\ge \frac{35}{4}(12)+\frac{15}{2}(14)=210.
$$

Expanding the left side yields

$$\frac{65}{4}p+50s+40t\ge210.$$

Since $p\ge0$,

$$
Z=100p+50s+40t
=\left(\frac{65}{4}p+50s+40t\right)+\frac{335}{4}p
\ge210.
$$

Hence **every feasible diet costs at least 210 toman/day**.

**Step 3 — Verify that our candidate attains the bound.** At $(p,s,t)=(0,1,4)$:

| Check | Calculation | Result |
| --- | --- | --- |
| Vitamin A | $0+4(1)+2(4)=12$ | $12\ge12$ ✓ |
| Vitamin B | $0+2(1)+3(4)=14$ | $14\ge14$ ✓ |
| Nonnegativity | $0,1,4\ge0$ | Satisfied ✓ |
| Cost | $100(0)+50(1)+40(4)$ | $210$ toman/day |

Because this feasible candidate reaches the universal lower bound of $210$, it is **globally optimal**.

## G. Final answer to write on the exam

> The optimal continuous daily diet consists of **0 units of cheese, 1 unit of milk, and 4 units of eggs**. It provides exactly 12 units of vitamin A and 14 units of vitamin B. The **minimum daily cost is 210 toman**. The constructed lower bound proves that no other feasible diet can be cheaper.

## H. Common written-exam mistakes

- Reversing the $\ge$ sign: these are **minimum** vitamin requirements, not available capacities.
- Mixing up the table columns: milk provides $(A,B)=(4,2)$; eggs provide $(2,3)$.
- Giving only $(0,1,4)$ without defining $p,s,t$ or writing the optimization model.
- Treating simultaneous equalities as an automatic proof of minimum cost.
- Imposing integer restrictions without explaining that this modifies the lecture model.
- Omitting the objective's unit (**toman per day**) and the final interpretation.

## Self-check

Without looking at the solution: Why do both vitamin constraints use $\ge$? Why is $(0,1,4)$ feasible? How does a nonnegative linear combination of the constraints prove $Z\ge210$? Which claims are from the lecture and which are independent derivations?
