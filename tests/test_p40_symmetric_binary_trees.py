import pytest
from solutions.p40_symmetric_binary_trees import *

implementations = [is_symmetric_tree_v1, is_symmetric_tree_v2]
ids = ["recursive w/o aux", "recursive"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_is_symmetric_tree(solution):
    assert solution(Branch(None, None)) == True
    assert solution(Branch(Branch(None, Branch(None, None)), 
                           Branch(Branch(None, None), None))) == True
    