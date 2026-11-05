"""Lecture page 1–2: triangular membership, alpha-cuts and LR arithmetic."""
from modeling_lab.fuzzy_sessions import LR, Triangular


def main() -> None:
    t = Triangular(1.2, 2, 2.4)
    print("triangle:", t)
    print("membership at 1.6:", t.membership(1.6))
    print("closed half-cut:", t.alpha_cut(0.5))
    print("LR representation:", t.lr())
    print("negative LR:", t.lr().scaled(-1))
    print("two times LR:", t.lr().scaled(2))
    print("trapezoid membership at core:", LR(2, 3, 1, 1).membership(2.5))
    assert abs(t.membership(1.6) - 0.5) < 1e-10
    assert all(abs(x-y) < 1e-10 for x,y in zip(t.alpha_cut(.5),(1.6,2.2)))


if __name__ == "__main__":
    main()
