# Hesitant fuzzy numbers versus hesitant fuzzy sets

## Definition recorded on page 3

The notes introduce a *hesitant fuzzy number* as a finite family of fuzzy numbers:

$$\mathcal H=\{\widetilde N^{(1)},\widetilde N^{(2)},\ldots,\widetilde N^{(p)}\}.$$

The class writes a nonempty intersection condition for the constituent fuzzy numbers. This needs clarification: the literal intersection of their graphs, intersection of supports, and intersection of positive-level \(\alpha\)-cuts are **different mathematical statements**. Without a specified convention, one should not substitute any of them silently.

For the computational illustration we choose the explicit **positive-width common support** condition:

$$\max_i \ell_i < \min_i r_i,$$

where \((\ell_i,r_i)\) are supports of the triangular numbers. This is a declared **interpretation for the example**, not a theorem asserted by the scan.

## What changes from a finite HFS?

| Hesitant fuzzy set | Hesitant fuzzy number (class representation) |
|---|---|
| For each \(x\), several **membership grades** | Several **entire fuzzy numbers** |
| \(h_H(x)\subseteq[0,1]\) | \(\{\widetilde N^{(1)},\ldots,\widetilde N^{(p)}\}\) |
| Information is indexed by a universe element | Information is indexed by alternative fuzzy estimates |

A triangular fuzzy number is written \((\ell,m,r)\) with \(\ell\le m\le r\), and a trapezoidal fuzzy number is \((a,b,c,d)\) with \(a\le b\le c\le d\). The two should not be conflated when averaging parameters.

See [Session 11](../session-11/ranking.md) for the ranking rule and [the mathematical audit](../session-11/audit.md) for the assumptions and transcription issues.
