### Modeling fundamentals

- **Decision variable:** the quantity we choose; identify its meaning, measurement unit and domain.
- **Objective:** an expression to minimize (cost) or maximize (profit).
- **Constraint:** a limited resource uses $\le$; a required minimum uses $\ge$; an exact balance uses $=$.
- **Domain:** declare nonnegativity and use integrality only if the problem explicitly requires whole units.

### Diet — minimum daily cost

From the [complete diet solution](session-01/diet.md), let $p,s,t$ represent the quantities of cheese, milk and eggs, respectively. Costs are in toman per day; vitamin A and B requirements are minima.

$$
\boxed{\begin{aligned}
\min\quad&Z=100p+50s+40t\\
\mathrm{s.t.}\quad&p+4s+2t\ge12&&\text{(vitamin A)}\\
&p+2s+3t\ge14&&\text{(vitamin B)}\\
&p,s,t\ge0.
\end{aligned}}
$$

**Why these directions?** Daily cost is minimized while each nutrient intake must be **at least** its required amount.

### Boat production — maximum profit

In the [boat model and full solution](session-01/boats.md), $x$ is the number of ordinary boats and $y$ the number of racing boats; profit is measured in **thousand toman**.

$$
\boxed{\begin{aligned}
\max\quad&Z=50x+80y\\
\mathrm{s.t.}\quad&50x+30y\le1000&&\text{(aluminum, kg)}\\
&20x+15y\le300&&\text{(machine, minutes)}\\
&3x+5y\le200&&\text{(labor, hours)}\\
&x,y\ge0.
\end{aligned}}
$$

Convert the available **5 machine-hours to 300 minutes** before writing the machine constraint. The supplied lecture model does not explicitly require integer variables; do not silently add integrality.
