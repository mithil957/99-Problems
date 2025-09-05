import pytest
from solutions.p55_find_minimal_spanning_tree import *

implementations = [find_minimal_spanning_tree_v1]
ids = ["prim"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_final_minimal_spanning_tree(solution):
    g = Graph(nodes = ['a', 'b', 'c'],
                edges = [Edge('a', 'b', 2), Edge('a', 'c', 1), Edge('b', 'c', 1)])
    
    assert solution(g)[1] == 2