"""Assignment 03: max of two triangular fuzzy numbers via Zadeh extension.

This is a mathematical/educational calculation, not a stochastic model.
No numerical optimizer is needed; extension-principle suprema are exact.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import isfinite


@dataclass(frozen=True)
class TriangularFuzzy:
    """Continuous normalized fuzzy number with vertices (left, mode, right)."""

    left: float
    mode: float
    right: float

    def __post_init__(self) -> None:
        if not (all(isfinite(v) for v in (self.left, self.mode, self.right))
                and self.left < self.mode < self.right):
            raise ValueError("Expected finite left < mode < right")

    def membership(self, z: float) -> float:
        if not isfinite(z):
            raise ValueError("Expected a finite evaluation point")
        if z <= self.left or z >= self.right:
            return 0.0
        if z <= self.mode:
            return (z - self.left) / (self.mode - self.left)
        return (self.right - z) / (self.right - self.mode)

    def sup_membership_up_to(self, z: float) -> float:
        """Exact sup_{x <= z} mu(x) for a triangular fuzzy number."""
        if not isfinite(z):
            raise ValueError("Expected a finite evaluation point")
        if z < self.left:
            return 0.0
        if z < self.mode:
            return (z - self.left) / (self.mode - self.left)
        return 1.0

    def alpha_cut(self, alpha: float) -> tuple[float, float]:
        if not isfinite(alpha) or not 0.0 <= alpha <= 1.0:
            raise ValueError("alpha must belong to [0,1]")
        return (self.left + alpha*(self.mode - self.left),
                self.right - alpha*(self.right - self.mode))


A = TriangularFuzzy(1.0, 3.0, 7.0)
B = TriangularFuzzy(3.0, 5.0, 6.0)
CROSSOVER = 17.0 / 3.0


def max_membership_via_extension(z: float, a: TriangularFuzzy = A,
                                 b: TriangularFuzzy = B) -> float:
    """Exact Zadeh extension sup{min(mu_a(x),mu_b(y)):max(x,y)=z}.

    The constraint max(x,y)=z means (x=z,y<=z) OR (y=z,x<=z).
    """
    return max(min(a.membership(z), b.sup_membership_up_to(z)),
               min(b.membership(z), a.sup_membership_up_to(z)))


def max_membership_piecewise(z: float) -> float:
    """Analytical piecewise answer for A=(1,3,7) and B=(3,5,6)."""
    if not isfinite(z):
        raise ValueError("Expected a finite evaluation point")
    if z < 3.0 or z > 7.0:
        return 0.0
    if z <= 5.0:
        return (z - 3.0)/2.0
    if z <= CROSSOVER:
        return 6.0-z
    return (7.0-z)/4.0


def max_alpha_cut(alpha: float) -> tuple[float,float]:
    """Alpha cuts obey (max(A,B))_alpha = [max(A_L,B_L),max(A_R,B_R)]."""
    a_l,a_r=A.alpha_cut(alpha)
    b_l,b_r=B.alpha_cut(alpha)
    return max(a_l,b_l),max(a_r,b_r)


def plot_assignment(output_dir: str = 'plots') -> tuple[str, str]:
    """Write both requested figures, using the optional matplotlib dependency."""
    from pathlib import Path
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import numpy as np

    target=Path(output_dir)
    target.mkdir(parents=True, exist_ok=True)
    xs=np.linspace(0,8,801)
    a=[A.membership(float(x)) for x in xs]
    b=[B.membership(float(x)) for x in xs]
    c=[max_membership_piecewise(float(x)) for x in xs]

    fig, ax=plt.subplots(figsize=(8.5,4.5))
    line_a,=ax.plot(xs,a,label=r'$\mu_{\widetilde A}(z)$',linewidth=2.3)
    line_b,=ax.plot(xs,b,label=r'$\mu_{\widetilde B}(z)$',linewidth=2.3)
    ax.scatter([1,3,7],[0,1,0],color=line_a.get_color(),s=30,zorder=3)
    ax.scatter([3,5,6],[0,1,0],color=line_b.get_color(),s=30,zorder=3)
    ax.set(xlim=(0,8),ylim=(-.04,1.12),xlabel=r'$z$',ylabel=r'$\mu(z)$')
    ax.set_xticks([1,3,5,6,7]); ax.grid(alpha=.25); ax.legend()
    fig.tight_layout()
    first=target/'assignment03_fuzzy_A_B.png'
    fig.savefig(first,dpi=175); plt.close(fig)

    fig, ax=plt.subplots(figsize=(8.5,4.5))
    ax.plot(xs,c,label=r'$\mu_{\max(\widetilde A,\widetilde B)}(z)$',linewidth=2.5)
    ax.scatter([3,5,CROSSOVER,7],[0,1,1/3,0],zorder=3)
    ax.axvline(CROSSOVER,alpha=.25,linestyle='--')
    ax.annotate(r'$(17/3,\ 1/3)$', (CROSSOVER,1/3), xytext=(6.15,.6),
                arrowprops={'arrowstyle':'->'},fontsize=10)
    ax.set(xlim=(0,8),ylim=(-.04,1.12),xlabel=r'$z$',ylabel=r'$\mu(z)$')
    ax.set_xticks([1,3,5,CROSSOVER,6,7],['1','3','5','17/3','6','7'])
    ax.grid(alpha=.25); ax.legend(loc='upper right')
    fig.tight_layout()
    second=target/'assignment03_fuzzy_max.png'
    fig.savefig(second,dpi=175); plt.close(fig)
    return str(first),str(second)
