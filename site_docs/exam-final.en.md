# Final Exam Review — Sessions 10 Onward

**Period separation:** the former midterm (Sessions 01–09) was withdrawn. This review intentionally includes only Sessions 10 onward.
This is an independent study summary, not an official exam announcement. The final-exam question types have not been specified by the supplied scan.
Retain definitions, modeling choices, complete formulations and any verified worked calculations; do not invent missing source data.

## Session 10

### Hesitant membership: define the modeling object

- A usual fuzzy set uses \(\mu:X\to[0,1]\). A **hesitant** fuzzy set assigns each \(x\) a finite nonempty **set** \(h(x)\subseteq[0,1]\), not a probability distribution.
- For the lecture's \(X=\{x_1,x_2,x_3\}\), specify \(h(x_1)=\{0.2,0.4,0.5\}\), \(h(x_2)=\{0.3,0.4\}\), \(h(x_3)=\{0.2,0.3,0.5,0.6\}\).
- In the five-student height example, write the crisp threshold set \(\{b,c\}\) for heights strictly greater than 180 cm. Explain what additional membership function an ordinary fuzzy set requires and why differing definitions of "tall" motivate hesitant grades.
- Distinguish a **hesitant fuzzy set** (several grades per element) from a **hesitant fuzzy number** (a family of fuzzy-number estimates). The lecture's fuzzy-intersection requirement is not fully specified.
- [Formal HFS definition](session-10/hesitant.md) · [height example](session-10/heights.md) · [fuzzy numbers](session-10/numbers.md).

## Session 11

### Hesitant fuzzy numbers: ranking and production formulation

- For \(\mathcal H=\{(a_j,b_j,c_j,d_j):1\le j\le p\}\), formulate the lecture's ranking \(R_1(\mathcal H)=\frac{1}{4p}\sum_j(a_j+b_j+c_j+d_j)\). State that these are *trapezoidal* estimates.
- In the source comparison, \(\mathcal A=\{(1,3,5,9),(2,4,5,7)\}\) and \(\mathcal B=\{(-1,2,3,8),(2,3,4,9)\}\), giving \(R_1(A)=4.5>R_1(B)=3.75\).
- For production, define \(x_A,x_B\ge0\), hesitant fuzzy profits \(\widetilde P_A,\widetilde P_B\), hesitant processing times \(\widetilde T_A,\widetilde T_B\), and capacity \(\widetilde C\). Formulate \(\max\widetilde Z=\widetilde P_Ax_A+\widetilde P_Bx_B\) subject to \(\widetilde T_Ax_A+\widetilde T_Bx_B\preceq\widetilde C\).
- **Do not invent** a deterministic equivalent before defining the fuzzy comparison rule. In particular, the source's questionable final digits of A's second profit and first capacity require verification.
- [Ranking derivation](session-11/ranking.md) · [production modeling](session-11/production.md) · [source audit](session-11/audit.md).

## Final-exam preparation checklist

- [ ] State whether the object is an ordinary fuzzy set, a hesitant fuzzy set, or a hesitant fuzzy number.
- [ ] Verify each fuzzy tuple has ordered coordinates.
- [ ] Give the source-defined ranking or explicitly state any additional rule.
- [ ] Formulate variables, objective, constraints and units without fabricating ambiguous coefficients.
