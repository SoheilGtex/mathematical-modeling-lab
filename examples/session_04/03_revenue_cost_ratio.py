"""Session 04, handwritten page 4: special linear-fractional objective."""
from modeling_lab.session04 import fractional_production_solution

sol = fractional_production_solution()
print(f"A = {sol.product_a:g}, B = {sol.product_b:g}")
print(f"Revenue = {sol.revenue:g} thousand toman")
print(f"Total cost = {sol.total_cost:g} thousand toman")
print(f"Maximum revenue/cost ratio = {sol.revenue_cost_ratio:.10f}")
