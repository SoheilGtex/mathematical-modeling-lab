"""Solve the five-month production, overtime and inventory planning model."""
from modeling_lab.linear import solve
from modeling_lab.session03 import production_inventory_problem
from modeling_lab.verification import verify_solution

model = production_inventory_problem()
result = solve(model)
print(f"Minimum five-month cost: {result.objective_value:g} toman")
for name, amount in result.variable_values.items():
    print(f"{name} = {amount:g}")
print("LP optimality verified:", verify_solution(model, result).independent_optimality_verified)
