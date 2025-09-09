import pytest
from solutions.p43_generate_height_balanced_binary_trees_given_nodes import *

implementations = [generate_height_balanced_trees_given_nodes_v1]
ids = ["recursive"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_generate_height_balanced_binary_trees_given_nodes(solution):
    assert len(solution(0)) == 1
    assert len(solution(1)) == 1
    assert len(solution(2)) == 2
    assert len(solution(3)) == 1
    assert len(solution(4)) == 4
    assert len(solution(5)) == 6
    assert len(solution(15)) == 1553