"""Independently solve page 3 production problem under lecture ranking R."""
import numpy as np
from modeling_lab.fuzzy_sessions import production_data, solve_ranked_lp


def main() -> None:
    obj, rows, capacities = production_data()
    x, value = solve_ranked_lp(obj, rows, capacities)
    a = np.array([[entry.rank() for entry in row] for row in rows])
    b = np.array([c.rank() for c in capacities])
    assert np.allclose(a @ x, b, atol=1e-7)
    print(f"x1={x[0]:.9f}, x2={x[1]:.9f}, R(Z)={value:.9f}")


if __name__ == "__main__":
    main()
