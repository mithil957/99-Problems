import pytest
from solutions.p15_split_list_into_two_parts import *

implementations = [split_list_v1, split_list_v2, split_list_v3]
ids = ["recursive", "direct", "iterative"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_split_list(solution):
    assert solution([], 0) == ([], [])
    assert solution([], 5) == ([], [])
    
    assert solution([1], 0) == ([], [1])
    assert solution([1], 1) == ([1], [])
    assert solution([1], 3) == ([1], [])
    
    assert solution([1, 2, 3], 0) == ([], [1, 2, 3])
    assert solution([1, 2, 2], 1) == ([1], [2, 2])
    assert solution([1, 2, 2], 3) == ([1, 2, 2], [])

    assert solution(['a', 'b', 'b', 'c', 'c', 'd', 'a', 'd'], 4) == \
        (['a', 'b', 'b', 'c'], ['c', 'd', 'a', 'd'])