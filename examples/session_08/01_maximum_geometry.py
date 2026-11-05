"""Exact extension max and Kerre distances for the repeated lecture example."""
from modeling_lab.fuzzy_sessions import Triangular
from modeling_lab.fuzzy_comparison import compare

m,n=Triangular(0,2,5),Triangular(2,3,4)
result=compare(m,n)
print('Extension max membership nodes:',result.max_membership.nodes)
print('d(M,D), d(N,D), r:',result.distance_first,result.distance_second,result.score)
assert (result.distance_first,result.distance_second,result.score)==(3/2,1/4,5/4)
