# Boat Production — Full Written Solution

**Source:** handwritten lecture notes, pp. 3–4. **From the notes:** the production data, linear objective, resource limits, and nonnegative variables; also the interpretation of optimal resource allocation. **Added here:** numerical solution, written optimality proof, resource checks, optional observations. The notes **do not** solve the optimization problem.

## A. Problem statement

A workshop produces **regular boats** and **single-person competition boats**. Each type consumes limited aluminum, machine time, and human labor. The per-boat requirements and available resources are:

| Quantity | Regular boat | Competition boat | Total available |
| --- | ---: | ---: | ---: |
| Aluminum | 50 kg | 30 kg | 1,000 kg |
| Machine time | 20 min | 15 min | **5 hours** |
| Human labor | 3 hours | 5 hours | 200 hours |
| Profit | 50,000 toman | 80,000 toman | — |

**Question:** How many boats of each type should the workshop produce to **maximize total profit**? Formulate the mathematical model and solve it.

## B. Decision variables and modeling assumptions

Let

- $x$ = number of regular boats produced;
- $y$ = number of competition boats produced.

The formulation **in the lecture notes** assumes $x,y\ge0$ as continuous quantities. Production resource consumption and profit are assumed proportional to the output. Because actual boats are indivisible, one could additionally require $x,y\in\mathbb Z_{\ge0}$, but this is an **explicit extension**, not a constraint written in the original notes.

## C. Objective function

One regular boat earns 50,000 toman, and one competition boat earns 80,000 toman. If profit $Z$ is measured in **thousand toman**, it is

$$Z=50x+80y.$$

We seek to **maximize** $Z$.

## D. Derivation of constraints

1. **Aluminum:** $50x+30y$ kilograms are used; at most 1,000 kilograms are available:

   $$50x+30y\le1000.$$

2. **Machine time:** one regular boat requires 20 minutes, and one competition boat requires 15 minutes. The available time is **5 hours = 300 minutes**, so

   $$20x+15y\le300.$$

3. **Human labor:** the total number of working hours required cannot exceed 200:

   $$3x+5y\le200.$$

4. **Nonnegative production:**

   $$x\ge0,\qquad y\ge0.$$

All capacity inequalities point toward $\le$, because consumption must **not exceed available resources**.

## E. Complete mathematical formulation

$$
\boxed{\begin{aligned}
\max\quad &Z=50x+80y &&\text{(thousand toman)}\\
\text{s.t.}\quad &50x+30y\le1000 &&\text{(aluminum: kg)}\\
&20x+15y\le300 &&\text{(machine: min)}\\
&3x+5y\le200 &&\text{(labor: hours)}\\
&x,y\ge0.
\end{aligned}}
$$

This is a **linear programming maximization problem**. The original constraints do not require integrality.

## F. Hand solution (without Python or a solver)

**Step 1 — Derive an upper bound on profit.** Since $x\ge0$,

$$
50x+80y
=\frac{16}{3}(20x+15y)-\frac{170}{3}x
\le\frac{16}{3}(20x+15y).
$$

By the machine-time restriction,

$$\frac{16}{3}(20x+15y)\le\frac{16}{3}(300)=1600.$$

Thus **every feasible production plan has profit at most 1,600 thousand toman**.

**Step 2 — Construct a feasible plan that reaches the bound.** To have equality in the first inequality above, take $x=0$. To use all machine capacity,

$$15y=300\ \Longrightarrow\ y=20.$$

The **candidate** is

$$\boxed{(x,y)=(0,20)}.$$

**Step 3 — Verify all requirements, not just machine time.**

| Resource | Use at $(0,20)$ | Capacity | Unused |
| --- | ---: | ---: | ---: |
| Aluminum | $50(0)+30(20)=600$ kg | 1,000 kg | 400 kg |
| Machine | $20(0)+15(20)=300$ min | 300 min | 0 min |
| Labor | $3(0)+5(20)=100$ hours | 200 hours | 100 hours |

Nonnegativity is also satisfied. The corresponding profit is

$$Z=50(0)+80(20)=1600\ \text{thousand toman}
=1{,}600{,}000\ \text{toman}.$$

The candidate is feasible and reaches the proven upper bound, so it is **globally optimal**.

## G. Final answer to write on the exam

> The workshop should produce **0 regular boats and 20 competition boats**. This uses 600 kg of aluminum, 300 minutes of machine time, and 100 hours of labor. The **maximum profit is 1,600 thousand toman (1,600,000 toman)**. Machine time is binding; 400 kg of aluminum and 100 labor hours remain. The upper-bound argument proves optimality.

## H. Alternative paper method: graphical solution (optional extension)

Since there are only two variables, this model can also be solved by a **feasible-region graph**:

1. Draw $x\ge0$ and $y\ge0$ in the first quadrant.
2. The machine-time boundary $20x+15y=300$ intersects the axes at $(15,0)$ and $(0,20)$.
3. The aluminum and labor constraints do not cut off any part of the triangle under that line. To check this without guessing from a drawing, verify both constraints at each of its three vertices.
4. The feasible-region vertices are $(0,0)$, $(15,0)$, and $(0,20)$. Evaluate the linear objective there:

   | Vertex $(x,y)$ | Profit $50x+80y$ (thousand toman) |
   | --- | ---: |
   | $(0,0)$ | $0$ |
   | $(15,0)$ | $750$ |
   | $(0,20)$ | $1600$ |

A linear objective on this bounded polygon has an optimum at a vertex, so **$(0,20)$ gives the maximum**. The preceding algebraic upper-bound proof is an alternative that needs no drawing. This graphical method is **added study material**, not a method shown in the handwritten notes.

## I. Optional extension: integer boats and redundant constraints

- **Integer model:** With $x,y\in\mathbb Z_{\ge0}$, the same answer $(0,20)$ remains optimal, because it is integer and already achieves the continuous model's global upper bound. This is **not** an added constraint in the lecture notes.
- **Why machine time is the bottleneck:** For nonnegative $x,y$, the machine constraint already implies

  $$50x+30y\le\tfrac52(20x+15y)\le750<1000,$$

  $$3x+5y\le\tfrac13(20x+15y)\le100<200.$$

  Thus the aluminum and labor constraints do not further restrict the feasible set for **these particular numbers**. This is extra analysis, not required to transcribe the source model.

## J. Common written-exam mistakes

- Putting $5$ on the right side of a constraint measured in **minutes** instead of using $5\times60=300$.
- Confusing total available resources with resources used *per boat*.
- Forgetting to scale the profit consistently: either $50{,}000x+80{,}000y$ in toman or $50x+80y$ in thousand toman.
- Using $\ge$ for an available-capacity constraint.
- Checking only the machine constraint and omitting aluminum, labor, or nonnegativity.
- Reporting a feasible plan as “optimal” without a proof or bound.
- Claiming integer restrictions appeared in the lecture notes when they did not.

## Self-check

Without looking at the solution: Why does machine time use the bound $20x+15y\le300$? Why is profit $50x+80y$ in thousands of toman? Which resources remain at $(0,20)$? How can you prove that no feasible solution exceeds a profit of 1,600 thousand toman?
