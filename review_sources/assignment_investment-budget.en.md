### Municipal investment budgeting — Assignment 01

See the [complete analytical assignment solution](assignments/investment-budget.md). The municipality needs $2,4,8,5$ **million USD** at the **start** of years 1–4. It issues interest-bearing long-term securities at coupon rates $7\%,6\%,6.5\%,7.5\%$ and can deposit any unspent funds for one year at returns $6\%,5.5\%,4.5\%$ (years 1–3).

- $x_i\ge0$: millions of USD in long-term securities sold at the start of year $i$, for $i=1,2,3,4$.
- $s_i\ge0$: millions of USD deposited after paying for year $i$, available next year with return, for $i=1,2,3$.

Assuming the same **20 nominal yearly coupon payments** for each issue (no discount rate is provided), define the total coupon-cost objective:

$$
\boxed{\begin{aligned}
\min\quad&Z=20(0.07x_1+0.06x_2+0.065x_3+0.075x_4)\\
\mathrm{s.t.}\quad&x_1-s_1=2\\
&x_2+1.06s_1-s_2=4\\
&x_3+1.055s_2-s_3=8\\
&x_4+1.045s_3=5\\
&x_i\ge0\ (i=1,\ldots,4),\quad s_i\ge0\ (i=1,2,3).
\end{aligned}}
$$

**Modeling explanation:** every year's available funds equal its required spending plus the next deposit. The factors $1.06,1.055,1.045$ include the principal **and** one year's deposit interest. This objective counts nominal coupon expense (not principal repayment or discounted present value). The handout calls the issued instruments “shares,” but because it specifies interest and maturity, the model interprets them as **bond-like interest-bearing securities**; state this assumption.
