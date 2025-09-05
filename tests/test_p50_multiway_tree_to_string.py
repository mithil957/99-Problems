import pytest
from solutions.p50_multiway_tree_to_string import *

implementations = [tree_to_string]
ids = ["recursive"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_tree_to_string(solution):
    tree = Node('a', [Node('f', [Node('g', [])]),
                      Node('c', [])])
    assert solution(tree) == 'afg^^c^^'