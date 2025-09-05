import pytest
from solutions.p39_generate_completely_balanced_binary_trees import *

implementations = [generate_completely_balanced_binary_trees_v1]
ids = ["recursive"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_generate_trees(solution):
    assert solution(0) == [None]
    
    assert solution(4) == [
        Node(left=Node(left=None, right=None, value='x'), right=Node(left=None, right=Node(left=None, right=None, value='x'), value='x'), value='x'),
        Node(left=Node(left=None, right=None, value='x'), right=Node(left=Node(left=None, right=None, value='x'), right=None, value='x'), value='x'),
        Node(left=Node(left=None, right=Node(left=None, right=None, value='x'), value='x'), right=Node(left=None, right=None, value='x'), value='x'),
        Node(left=Node(left=Node(left=None, right=None, value='x'), right=None, value='x'), right=Node(left=None, right=None, value='x'), value='x')
    ]