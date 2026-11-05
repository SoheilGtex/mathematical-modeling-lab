"""Session 04, handwritten page 3: light/heavy crude-oil blending."""
from modeling_lab.linear import solve
from modeling_lab.session04 import crude_oil_problem
from modeling_lab.verification import verify_solution

model = crude_oil_problem()
sol = solve(model)
print(f"Minimum crude purchase cost: {sol.objective_value:,.2f} USD")
for name, amount in sol.variable_values.items():
    print(f"{name} = {amount:,.3f}")
print("Independent LP verification:", verify_solution(model, sol).independent_optimality_verified)
