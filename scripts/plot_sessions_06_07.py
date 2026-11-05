#!/usr/bin/env python3
"""Regenerate the source-grounded triangular and extension-maximum SVG figures."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from modeling_lab.fuzzy_sessions import LECTURE_M, LECTURE_N, Triangular, lecture_max_membership

OUTPUT = Path(__file__).resolve().parents[1] / "site_docs" / "assets"


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    x = np.linspace(.9, 2.7, 600)
    t = Triangular(1.2, 2, 2.4)
    fig, ax = plt.subplots(figsize=(7.0, 3.4))
    ax.plot(x, [t.membership(float(v)) for v in x], label="T = (1.2, 2, 2.4)")
    for v in (1.2, 2.0, 2.4):
        ax.axvline(v, ls=":", lw=.9)
    ax.set_xlim(1, 2.6)
    ax.set_ylim(0, 1.07)
    ax.set_xlabel("x")
    ax.set_ylabel("Membership")
    ax.set_xticks([1.2, 1.6, 2.0, 2.2, 2.4])
    ax.grid(alpha=.18)
    ax.legend(loc="upper left")
    fig.tight_layout()
    fig.savefig(OUTPUT / "session06_triangle.svg")
    plt.close(fig)

    x = np.linspace(-.2, 5.5, 850)
    fig, ax = plt.subplots(figsize=(7.3, 3.6))
    ax.plot(x, [LECTURE_M.membership(float(v)) for v in x], label="M = (0, 2, 5)", ls="--", alpha=.8)
    ax.plot(x, [LECTURE_N.membership(float(v)) for v in x], label="N = (2, 3, 4)", ls=":", alpha=.9)
    ax.plot(x, [lecture_max_membership(float(v)) for v in x], label="max(M, N) by extension", lw=2.3)
    for v in (2, 3, 3.5, 5):
        ax.axvline(v, ls=":", lw=.8, alpha=.5)
    ax.set_xlim(-.2, 5.5)
    ax.set_ylim(0, 1.08)
    ax.set_xticks([0, 1, 2, 3, 3.5, 4, 5])
    ax.set_xlabel("z")
    ax.set_ylabel("Membership")
    ax.grid(alpha=.2)
    ax.legend(loc="upper left")
    fig.tight_layout()
    fig.savefig(OUTPUT / "session07_extension_max.svg")
    plt.close(fig)
    print("Generated two SVG plots")


if __name__ == "__main__":
    main()
