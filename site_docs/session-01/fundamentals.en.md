# Fundamentals of Mathematical Modeling

> **Source boundary:** Introductory material from page 1 and the operations-research interpretation from page 4 of the handwritten lecture notes. General answer checklists and notation are independent educational additions.

## 1. What is mathematical modeling?

Mathematical modeling is the process of representing a real-world problem with mathematical quantities and relationships so that its requirements can be analyzed systematically. The first step is **understanding the problem statement**: what is being requested, what is unknown, and which conditions must be satisfied. A good model must preserve the meaning and units of the original question.

## 2. Components of an optimization model

- **Decision variables:** unknown quantities to be selected, such as food amounts or numbers of boats. State their units and their permitted domains.
- **Objective function:** a mathematical expression measuring the quantity to minimize (e.g., total cost) or maximize (e.g., total profit).
- **Constraints:** equations or inequalities expressing limits or requirements: minimum nutrition, maximum material, available working time, etc.
- **Feasible solution:** a choice of decision variables satisfying **all** constraints, including domain restrictions.
- **Optimal solution:** a feasible solution whose objective value is best among **all** feasible solutions.
- **Assumptions:** simplifications used to translate reality into mathematics, such as constant cost per food unit or proportional resource use per boat.

A common formulation is

$$
\begin{aligned}
\min_{x\in\mathbb R^n}\quad &f(x)\\
\text{subject to}\quad &g_i(x)\le 0\quad (i=1,\ldots,m),\\
&h_j(x)=0\quad (j=1,\ldots,r),\\
&x\in X.
\end{aligned}
$$

For a **linear programming (LP)** model, the objective and functional constraints are linear, and continuous decision variables are typically allowed. Nonnegativity, e.g., $x\ge0$, is a domain restriction. A count may require integer variables in a **different** model, but this must be stated rather than silently assumed.

## 3. How to write a complete descriptive answer

1. Define all decision variables with meaning, unit, and domain.
2. Write the objective and explain why it is minimized or maximized.
3. Derive **every** constraint from the problem data. Watch the inequality directions: *at least* $\Rightarrow\ge$; *at most / available* $\Rightarrow\le$.
4. Convert different units before combining them (e.g., $5$ hours $=300$ minutes).
5. Present the complete mathematical program.
6. If the question requests a numerical solution, solve it and **check every constraint**.
7. Justify optimality, not merely feasibility. A valid upper/lower bound attained by the candidate is a complete proof.
8. State the objective value with units and interpret the decision variables in words.

**A solver reporting “optimal” is not a substitute for the argument required in a handwritten proof.**

## 4. Operations-research interpretation

The lecture note describes operations research in terms of **allocating limited available resources optimally among competing activities**. In the production example the activities are two types of boats, the scarce resources are aluminum, machine time, and labor, and the objective is to maximize profit. Other models may instead minimize cost, time, or loss.
