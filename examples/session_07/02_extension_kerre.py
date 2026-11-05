"""Verify page 4–6 extension maximum and independently evaluate distances."""
import numpy as np
from modeling_lab.fuzzy_sessions import (
    LECTURE_M, LECTURE_N, kerre_lecture_distances,
    lecture_max_membership, max_extension_membership,
)


def main() -> None:
    for z in np.linspace(0, 5.5, 111):
        exact = lecture_max_membership(float(z))
        via_cuts = max_extension_membership(LECTURE_M, LECTURE_N, float(z))
        assert abs(exact - via_cuts) < 1e-8, (z, exact, via_cuts)
    dm, dn, score = kerre_lecture_distances()
    assert np.allclose((dm, dn, score), (1.5, 0.25, 1.25), atol=1e-8)
    print(f"d(M,max)={dm:.9f}; d(N,max)={dn:.9f}; Kerre score={score:.9f}")
    print("Conclusion under the lecture comparison: M <=_K N")


if __name__ == "__main__":
    main()
