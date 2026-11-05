"""Optional independent numerical verification of the lecture's ratio example."""
from modeling_lab.session05 import solve_fractional_example


def main():
    result = solve_fractional_example()
    print(f"x1={result.x1:.10g}, x2={result.x2:.10g}")
    print(f"y1={result.y1:.10g}, y2={result.y2:.10g}, t={result.t:.10g}")
    print(f"max objective={result.value:.10g} (exact 103/26)")


if __name__ == '__main__':
    main()
