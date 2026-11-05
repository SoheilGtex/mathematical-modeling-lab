"""Optional reproducible computation for Assignment 03.

Run from the repository root after `pip install -e '.[dev]'`:
  python examples/assignments/03_fuzzy_numbers_max.py
"""
from modeling_lab.assignment03 import (
    A, B, CROSSOVER, max_alpha_cut, max_membership_via_extension,
    max_membership_piecewise, plot_assignment,
)


def main() -> None:
    print('A=(1,3,7), B=(3,5,6)')
    print(f'Change point: z=17/3={CROSSOVER:.9f}, mu=1/3')
    for z in (3.,4.,5.,5.5,CROSSOVER,6.,7.):
        analytical=max_membership_piecewise(z)
        extension=max_membership_via_extension(z)
        assert abs(analytical-extension)<1e-10
        print(f'z={z:9.6f}, mu_A={A.membership(z):.6f}, '
              f'mu_B={B.membership(z):.6f}, mu_max={extension:.6f}')
    print('Alpha cuts:')
    for alpha in (0., 1/3, .5, 1.):
        left,right=max_alpha_cut(alpha)
        print(f'alpha={alpha:.6f}: [{left:.6f}, {right:.6f}]')
    first,second=plot_assignment('plots')
    print('Saved charts:', first, second)


if __name__=='__main__':
    main()
