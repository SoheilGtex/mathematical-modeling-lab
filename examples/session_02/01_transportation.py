"""Run an explicitly constructed numeric demo of the symbolic transport model.

The session-02 source contains symbols only, NOT these example numbers.
"""

from modeling_lab.linear import solve
from modeling_lab.session02 import transportation_demo_problem

if __name__ == "__main__":
    result = solve(transportation_demo_problem())
    print("Illustrative, independently invented data (not the class worksheet)")
    print("Optimal transport cost:", result.objective_value)
    for name, value in result.variable_values.items():
        print(f"  {name} = {value:g}")
