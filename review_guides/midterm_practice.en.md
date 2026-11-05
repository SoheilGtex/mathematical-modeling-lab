## Day-before self-assessment

These are **independently written practice questions based on Sessions 01–09**, not official examination questions. Work without looking up the answers first. Always state variable meanings, units, domains, and the rationale for each inequality.

### Questions

1. What is the vitamin-A minimum constraint for diet quantities $p,s,t$ when contributions are $1,4,2$ and the daily requirement is 12?
2. Write the machine-time constraint for 20 and 15 minutes per boat when only five machine-hours are available.
3. Write the supply and exact-demand constraints for a transportation model, making explicit which index is summed.
4. Write the second- and fifth-month balances of the published production/inventory model.
5. Express the capacity constraint of machine 3 when $t_{i3}$ is the time for product $i$ on that machine.
6. Derive usable diesel from purchased light crude when the refinery yield is 95% and the diesel fraction is 40%.
7. Explain why maximizing revenue-to-cost differs from maximizing revenue minus cost.
8. Give the Charnes–Cooper variables and normalization for the denominator $3x_1+4x_2+20$.
9. Derive the two nonzero membership branches and the alpha-cut for $(1,5,7)$.
10. Distinguish support, core, ordinary alpha-cut, and strong alpha-cut.
11. Interpret the four parameters $(a^L,a^U,\ell,r)_{LR}$.
12. Evaluate the course ranking formula for $(3,5,1,3)_{LR}$.
13. Construct the alpha-cut maximum of $(0,2,5)$ and $(2,3,4)$ and determine the switching alpha.
14. Explain why the extension-principle maximum of $(2,5,12)$ and $(2,4,10)$ is the first triangular number, and infer the Kerre score sign.
15. Write the second-year financing balance with a 6% return on the previous year's deposit.
16. For $A=(1,3,7)$ and $B=(3,5,6)$, identify the alpha where the right endpoint of their extension-principle maximum switches branches.

### Answer key

1. $p+4s+2t\ge12$.
2. $20x+15y\le300$ minutes.
3. $\sum_jx_{ij}\le a_i$ and $\sum_ix_{ij}=b_j$.
4. $x_2+y_2+s_1-s_2=2100$ and $x_5+y_5+s_4=4000$.
5. $\sum_{i=1}^3t_{i3}x_{i3}\le H_3$.
6. $0.40\cdot0.95x_1=0.38x_1$.
7. A ratio and a difference represent different objectives.
8. $t=1/(3x_1+4x_2+20)$, $y_i=tx_i$, $3y_1+4y_2+20t=1$.
9. $(x-1)/4$ and $(7-x)/2$ on their respective intervals; $[A]_\alpha=[1+4\alpha,7-2\alpha]$.
10. $\{\mu>0\}$, $\{\mu=1\}$, $\{\mu\ge\alpha\}$, $\{\mu>\alpha\}$.
11. Two core endpoints and two spreads.
12. $4.5$.
13. $[M]_\alpha=[2\alpha,5-3\alpha]$, $[N]_\alpha=[2+\alpha,4-\alpha]$, switching at $\alpha=1/2$.
14. Both alpha-cut endpoints of the first dominate, hence $D=M$ and $r(M,N)=-d(M,N)<0$.
15. $x_2+1.06s_1-s_2=4$.
16. $[A]_{\alpha}=[1+2\alpha,7-4\alpha]$, $[B]_{\alpha}=[3+2\alpha,6-\alpha]$; the right bounds cross at $\alpha=1/3$.

### Final checklist

- [ ] I can rebuild each model from the word problem, not just recall its finished expression.
- [ ] I can explain the direction and units of each constraint.
- [ ] I keep all temporal boundaries, fractional-objective constants, and fuzzy comparison definitions.
- [ ] I distinguish results explicitly supplied by the course notes from independent mathematical extensions.
