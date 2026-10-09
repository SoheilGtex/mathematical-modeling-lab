# Exam Review

A concise review of the models, solutions, and key ideas covered in class. This page grows as new sessions are added. Follow the links in each section for full written solutions and proofs. This guide is not an official exam syllabus or grading scheme.

## Session 01

**Full worked solutions:** [Diet](session-01/diet.md) and [Boat production](session-01/boats.md).

### Core vocabulary

- **Decision variable:** a quantity chosen by the decision-maker.
- **Objective:** what we minimize or maximize.
- **Constraint:** a required or limiting condition.
- **Feasible:** satisfies all constraints and domain restrictions.
- **Optimal:** feasible and no other feasible choice is better.
- **Binding / active constraint:** equality holds at the reported solution.
- **Slack:** unused resource in a $\le$ capacity constraint; for a $\ge$ minimum constraint, the amount above the minimum is a *surplus*.
- **Operations research:** optimal allocation of limited resources among competing activities (interpretation given in the lecture notes).

### Model 1 — Diet (cost in toman/day)

$$
\begin{aligned}
\min\quad &100p+50s+40t\\
\text{s.t.}\quad&p+4s+2t\ge12\\
&p+2s+3t\ge14\\
&p,s,t\ge0.
\end{aligned}
$$

- $p$ = cheese, $s$ = milk, $t$ = eggs.
- **Optimal:** $(p,s,t)=(0,1,4)$, cost $210$ toman/day.
- **Feasibility:** A $=12$, B $=14$, all variables nonnegative.
- **Why optimal:** multiplying the A constraint by $35/4$ and the B constraint by $15/2$ gives $\frac{65}{4}p+50s+40t\ge210$; since $p\ge0$, the cost is $\ge210$, attained by $(0,1,4)$.

### Model 2 — Boats (profit in thousand toman)

$$
\begin{aligned}
\max\quad&50x+80y\\
\text{s.t.}\quad&50x+30y\le1000\\
&20x+15y\le300\\
&3x+5y\le200\\
&x,y\ge0.
\end{aligned}
$$

- $x$ = regular boats, $y$ = competition boats; **5 hours = 300 minutes**.
- **Optimal:** $(x,y)=(0,20)$, profit $1600$ thousand toman.
- **Feasibility:** uses $600/1000$ kg aluminum, $300/300$ minutes machine time, $100/200$ labor hours.
- **Graphical check:** feasible vertices $(0,0)$, $(15,0)$, $(0,20)$; profits $0$, $750$, $1600$.
- **Why optimal:** $50x+80y=\frac{16}{3}(20x+15y)-\frac{170}{3}x\le\frac{16}{3}(300)=1600$, attained by $(0,20)$.
- The original notes impose $x,y\ge0$ but **do not explicitly require integers**.

### Final written-answer checklist

- [ ] Variables defined, with units and domain
- [ ] Minimize or maximize chosen correctly
- [ ] Every coefficient derived from the statement
- [ ] Every inequality points in the correct direction
- [ ] Hours and minutes converted consistently
- [ ] Complete model written clearly
- [ ] Numerical candidate found and all constraints checked
- [ ] Optimality justified (not only feasibility)
- [ ] Result written with units and interpretation
- [ ] Source assumptions separated from later extensions

## Session 02

**Full worked solutions:** [Transportation](session-02/transportation.md) and [Television production](session-02/televisions.md).

### Transportation — symbolic model from the lecture

- $x_{ij}$: goods shipped from origin $i$ to destination $j$; $a_i$: origin supply; $b_j$: exact destination demand; $c_{ij}$: unit shipping cost.

$$
\boxed{\begin{aligned}
\min\quad & Z=\sum_{i=1}^{m}\sum_{j=1}^{n}c_{ij}x_{ij}\\
\mathrm{s.t.}\quad&\sum_{j=1}^{n}x_{ij}\le a_i &&\forall i\\
&\sum_{i=1}^{m}x_{ij}=b_j &&\forall j\\
&x_{ij}\ge0 &&\forall i,j.
\end{aligned}}
$$

- Minimum cost: **min**. Source capacity: **$\le$**. Destination demand: **$=$**. Nonnegativity is mandatory.
- Necessary feasibility check: $\sum_i a_i\ge\sum_j b_j$. For a fully connected network with no extra route bounds, this is sufficient for continuous flows too.
- **The lecture provides no numbers for transportation**, so there is no lecturer-specified numeric optimum.

### Television production

- $x_1$: color TVs, $x_2$: black-and-white TVs; profit in dollars; labor in person-hours.

$$
\boxed{\begin{aligned}
\max\quad& Z=60x_1+30x_2\\
\mathrm{s.t.}\quad &20x_1+15x_2\le H\\
&x_1\le2000,\quad x_2\le4000\\
&x_1,x_2\ge0.
\end{aligned}}
$$

- **Corrected labor capacity:** $H=60,000$ person-hours, as clarified by the student.
- **Continuous optimum:** $(x_1,x_2)=(2000,4000/3)$ with $Z_{\max}=160,000$. Proof: $Z=2(20x_1+15x_2)+20x_1\le120,000+40,000=160,000$; equality is attained.
- **Integer extension not written in the note:** $(2000,1333)$ with $Z=159,990$; all integer profits are multiples of 30 and $Z\le160,000$.

**Written-answer checklist:** Define the variables, units, and domains; derive the objective and constraints from the problem statement; check inequality directions and the confirmed labor capacity; verify feasibility; and justify optimality rather than simply reporting the solver output.
