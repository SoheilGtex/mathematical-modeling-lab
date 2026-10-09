"""Solve the corrected session-02 television production example."""

from modeling_lab.linear import solve
from modeling_lab.session02 import television_problem

if __name__ == "__main__":
    model = television_problem()  # 60,000 person-hours
    for integer in (False, True):
        result = solve(model, integer_variables=model.variables if integer else ())
        print(f"{('Integer' if integer else 'Continuous')}: "
              f"x1={result.variable_values['x1']:g}, "
              f"x2={result.variable_values['x2']:g}, "
              f"profit=${result.objective_value:g}")
