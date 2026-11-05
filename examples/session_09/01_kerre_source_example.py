"""Solve the new (2,5,12) vs (2,4,10) handwritten comparison exactly."""
from fractions import Fraction
from modeling_lab.fuzzy_comparison import source_result

result=source_result()
print('Maximum knots:',result.max_membership.nodes)
print('Distance M to maximum:',result.distance_first)
print('Distance N to maximum:',result.distance_second)
print('Pairwise score:',result.score)
print('Preferred triangle:',result.relation)
assert result.distance_second==Fraction(17,9)
assert result.score==-Fraction(17,9)
