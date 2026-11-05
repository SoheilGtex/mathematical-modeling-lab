"""Independently solve the four-parameter LR linear program on page 4."""
import numpy as np
from modeling_lab.fuzzy_sessions import large_scale_data, solve_ranked_lp


def main() -> None:
    obj, rows, capacities = large_scale_data()
    x, value = solve_ranked_lp(obj, rows, capacities)
    assert np.allclose(x, [77 / 96, 25 / 16], atol=1e-9)
    assert abs(value - 755 / 96) < 1e-8
    print(f"x1={x[0]:.9f}, x2={x[1]:.9f}, R(Z)={value:.9f}")


if __name__ == "__main__":
    main()
