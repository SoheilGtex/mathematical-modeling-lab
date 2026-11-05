"""Exact scores and optional illustrated LP; not a class-supplied optimum."""
from modeling_lab.hesitant_final import (
    RANK_A, RANK_B, hesitant_trapezoid_rank, ranked_production_scenario,
)

if __name__ == '__main__':
    print('R(A) =', hesitant_trapezoid_rank(RANK_A))
    print('R(B) =', hesitant_trapezoid_rank(RANK_B))
    model = ranked_production_scenario()
    print('Independent assumed/corrected scenario:', model)
    print('Illustrative optimal production of A:',model['capacity']/model['time_a'])
