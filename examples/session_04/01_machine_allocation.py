"""Session 04, handwritten pages 1–2: machine allocation."""
from modeling_lab.linear import solve
from modeling_lab.session04 import machine_allocation_problem
from modeling_lab.verification import verify_solution

model = machine_allocation_problem()
sol = solve(model)
print(f"Minimum production cost: {sol.objective_value:,.2f} USD")
for name, amount in sol.variable_values.items():
    if abs(amount) > 1e-7:
        print(f"{name} = {amount:,.2f}")
print("Independent LP verification:", verify_solution(model, sol).independent_optimality_verified)
