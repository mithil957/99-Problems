import pytest
from solutions.p18_remove_kth_element import *

implementations = [remove_kth_element_v1, remove_kth_element_v2, 
                   remove_kth_element_v3, remove_kth_element_v4]
ids = ["recursive", "direct", "list comp", "slice concat"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_remove_kth_element(solution):
    assert solution([], 0) == []
    assert solution([], 1) == []
    assert solution([], 5) == []
    
    assert solution([1], 0) == []
    assert solution([1], 1) == [1]
    assert solution([1], 100) == [1]
    
    assert solution([1, 2, 3], 0) == [2, 3]
    assert solution([1, 2, 3], 1) == [1, 3]
    assert solution([1, 2, 3], 2) == [1, 2]
    assert solution([1, 2, 3], 3) == [1, 2, 3]
    assert solution([1, 2, 3], 4) == [1, 2, 3]

    assert solution(['a', 'b', 'b', 'c', 'c', 'd', 'a', 'd'], 4) == \
        ['a', 'b', 'b', 'c', 'd', 'a', 'd']