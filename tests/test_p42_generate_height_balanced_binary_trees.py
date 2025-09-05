import pytest
from solutions.p42_generate_height_balanced_binary_trees import *

implementations = [generate_height_balanced_trees_v1]
ids = ["recursive"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_generate_height_balanced_binary_trees(solution):
    assert len(solution(2)) == 3
    assert len(solution(3)) == 15
    assert len(solution(4)) == 315
    assert len(solution(5)) == 108675