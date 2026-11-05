"""Course Sessions 10-11: exact finite HFS, hesitant fuzzy-number ranking.

The ranking and LP reduction implement a declared course convention; they are
not a universal ordering of hesitant fuzzy sets or a robust optimization rule.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from typing import Iterable, Mapping, TypeVar

T = TypeVar('T')


def q(v: int | str | F | float) -> F:
    if isinstance(v, float):
        return F(str(v))
    return F(v)


def hesitant_set(data: Mapping[T, Iterable[int | str | float | F]]) -> dict[T, tuple[F, ...]]:
    """A nonempty finite set of plausible membership degrees for each element.

    Deduplicate because this is a set, not a multiset or probability measure.
    """
    if not data:
        raise ValueError('Reference universe must not be empty')
    answer: dict[T, tuple[F, ...]] = {}
    for x, values in data.items():
        degrees = tuple(sorted({q(v) for v in values}))
        if not degrees or any(v < 0 or v > 1 for v in degrees):
            raise ValueError(f'Nonempty degree set inside [0,1] required at {x!r}')
        answer[x] = degrees
    return answer


def crisp_threshold(heights: Mapping[T, int | float], threshold: int | float) -> set[T]:
    """Strictly greater than threshold (as in the height example)."""
    return {x for x, value in heights.items() if value > threshold}


def tall_ramp(height: int | float, lower: int | float = 170, upper: int | float = 180) -> F:
    """Modeling choice: 0 below lower, linear up to 1 at upper."""
    lower, upper, height = q(lower), q(upper), q(height)
    if lower >= upper:
        raise ValueError('A ramp must have lower < upper')
    return max(F(0), min(F(1), (height - lower) / (upper - lower)))


@dataclass(frozen=True)
class Trapezoid:
    a: F
    b: F
    c: F
    d: F

    def __init__(self, a, b, c, d):
        vals = tuple(q(v) for v in (a, b, c, d))
        if tuple(sorted(vals)) != vals:
            raise ValueError('A trapezoidal fuzzy number requires a <= b <= c <= d')
        for name, val in zip(('a','b','c','d'), vals):
            object.__setattr__(self, name, val)

    @property
    def rank(self) -> F:
        """Course convention: arithmetic mean of four trapezoid corners."""
        return (self.a + self.b + self.c + self.d) / 4


@dataclass(frozen=True)
class Triangle:
    left: F
    mode: F
    right: F

    def __init__(self, left, mode, right):
        vals = tuple(q(v) for v in (left, mode, right))
        if tuple(sorted(vals)) != vals:
            raise ValueError('Triangle requires left <= mode <= right')
        for name, val in zip(('left','mode','right'), vals):
            object.__setattr__(self, name, val)

    @property
    def rank(self) -> F:
        """Explicit triangular-to-trapezoidal embedding (l,m,m,r)."""
        return (self.left + 2*self.mode + self.right) / 4

    @property
    def support(self) -> tuple[F, F]:
        return self.left, self.right


def hesitant_trapezoid_rank(values: Iterable[Trapezoid]) -> F:
    items = tuple(values)
    if not items:
        raise ValueError('At least one fuzzy number is required')
    if not all(isinstance(x, Trapezoid) for x in items):
        raise TypeError('The trapezoidal ranking requires Trapezoid objects')
    return sum((x.rank for x in items), F(0)) / len(items)


def hesitant_triangle_rank(values: Iterable[Triangle]) -> F:
    items = tuple(values)
    if not items:
        raise ValueError('At least one triangular number is required')
    if not all(isinstance(x, Triangle) for x in items):
        raise TypeError('The triangular scenario requires Triangle objects')
    return sum((x.rank for x in items), F(0)) / len(items)


def common_support_interval(values: Iterable[Triangle]) -> tuple[F, F] | None:
    items = tuple(values)
    if not items:
        raise ValueError('Empty family')
    left, right = max(x.left for x in items), min(x.right for x in items)
    return (left, right) if left < right else None


HEIGHTS = {'a':173, 'b':195, 'c':181, 'd':179, 'e':145}
CLASS_HFS = hesitant_set({
    'x1': ['0.2', '0.4', '0.5'],
    'x2': ['0.3', '0.4'],
    'x3': ['0.3', '0.2', '0.5', '0.6'],
})
RANK_A = (Trapezoid(1, 3, 5, 9), Trapezoid(2, 4, 5, 7))
RANK_B = (Trapezoid(-1, 2, 3, 8), Trapezoid(2, 3, 4, 9))


def ranked_production_scenario():
    """Independent illustration, NOT a verified numeric transcription.

    Handwriting ambiguity concerning an upper bound in the source is resolved
    by explicit modeling assumption 60, which must not be attributed to class.
    Scenario requires accepting mean ranking, a policy not proved in the scan.
    """
    profits_a = (Triangle(40,45,50), Triangle(50,55,60))
    profits_b = (Triangle(30,35,40), Triangle(40,45,50))
    time_a = (Triangle(1,'1.5',2), Triangle(2,'2.5',3))
    time_b = (Triangle(2,'2.5',3), Triangle(3,'3.5',4))
    capacity = (Triangle(50,55,60), Triangle(40,45,70))
    return {
        'profit_a': hesitant_triangle_rank(profits_a),
        'profit_b': hesitant_triangle_rank(profits_b),
        'time_a': hesitant_triangle_rank(time_a),
        'time_b': hesitant_triangle_rank(time_b),
        'capacity': hesitant_triangle_rank(capacity),
    }
