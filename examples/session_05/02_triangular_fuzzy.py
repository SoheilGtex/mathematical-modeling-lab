"""Optional numerical demonstration of the handwritten triangular fuzzy number."""
from modeling_lab.session05 import triangular_membership


def main():
    for x in (0., 1., 1.2, 3., 5., 6., 7., 8.):
        print(f"mu({x:g})={triangular_membership(x):.5g}")


if __name__ == '__main__':
    main()
