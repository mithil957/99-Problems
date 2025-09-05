import pytest
from solutions.p17_rotate_list_n_places_to_left import *

implementations = [rotate_left_v1, rotate_left_v2, rotate_left_v3]
ids = ["recursive", "direct", "chain"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_rotate_left(solution):
    assert solution([], 0) == []
    assert solution([], 1) == []
    assert solution([], 5) == []
    
    assert solution([1], 0) == [1]
    assert solution([1], 1) == [1]
    assert solution([1], 100) == [1]
    
    assert solution([1, 2, 3], 0) == [1, 2, 3]
    assert solution([1, 2, 3], 1) == [2, 3, 1]
    assert solution([1, 2, 3], 2) == [3, 1, 2]
    assert solution([1, 2, 3], 3) == [1, 2, 3]
    assert solution([1, 2, 3], 4) == [2, 3, 1]
    assert solution([1, 2, 3], 100) == [2, 3, 1]

    assert solution(['a', 'b', 'b', 'c', 'c', 'd', 'a', 'd'], 4) == \
        ['c', 'd', 'a', 'd', 'a', 'b', 'b', 'c']