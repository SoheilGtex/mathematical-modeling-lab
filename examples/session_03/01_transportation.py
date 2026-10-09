"""Run the class's numerical 3-by-4 transportation problem."""
from modeling_lab.linear import solve
from modeling_lab.session03 import lecture_transportation_problem
from modeling_lab.verification import verify_solution

model = lecture_transportation_problem()
result = solve(model)
print(f"Minimum total cost: {result.objective_value:g} toman")
for name, amount in result.variable_values.items():
    print(f"{name} = {amount:g}")
print("LP optimality verified:", verify_solution(model, result).independent_optimality_verified)
