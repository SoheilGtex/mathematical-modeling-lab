# Session 04 — Independent computational verification

For reproducible Python examples, run from the repository root after installing dependencies:

```bash
python examples/session_04/01_machine_allocation.py
python examples/session_04/02_crude_oil.py
python examples/session_04/03_revenue_cost_ratio.py
python -m pytest -q tests/test_session_04.py
```

- Machine allocation: 12 variables, seven structural inequalities, $82,500 minimum in USD. Its independent LP certificate uses product multipliers $p=(4,6,11)$ and machine multipliers $q=(0,5/3,5,0)$.
- Crude purchase: 2 variables, three minimum output inequalities; $50,951,086.9565 minimum in USD. The diesel minimum alone supplies the lower-bound proof, and the heavy-only optimum satisfies kerosene and jet-fuel minimums.
- Revenue/cost: linear-fractional objective, maximum $20/11$. It is reduced to an ordinary LP **only for the particular lecture data** because revenue equals twice variable cost and fixed cost is positive.

The exam review contains only decision variables, units, the exact source formulation and variable domains; no numerical optimum or software work.
