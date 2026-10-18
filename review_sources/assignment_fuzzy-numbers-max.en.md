### Triangular fuzzy memberships and the maximum operator

The full [fuzzy-number assignment solution](assignments/fuzzy-numbers-max.md) uses $\widetilde A=(1,3,7)$ and $\widetilde B=(3,5,6)$. Model the membership functions with the triangular definition, then use **Zadeh's extension-principle constraint**:

$$\mu_{\max(\widetilde A,\widetilde B)}(z)=
\sup_{\substack{x,y\in\mathbb R\\\max(x,y)=z}}
\min\bigl(\mu_{\widetilde A}(x),\mu_{\widetilde B}(y)\bigr).$$

The constraint $\max(x,y)=z$ requires $x\le z$, $y\le z$, and **at least one equality**. Identify the triangle vertices and sketch both membership functions and their maximum; all detailed interval calculations and proofs are on the full assignment page. This is a fuzzy-membership modeling exercise, **not** an extra linear-programming objective.
