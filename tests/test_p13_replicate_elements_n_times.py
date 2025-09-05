import pytest
from solutions.p13_replicate_elements_n_times import *

implementations = [replicate_elements_v1, replicate_elements_v2, replicate_elements_v3]
ids = ["recursive", "reduce", "direct"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_replicate_elements(solution):
    assert solution([], 0) == []
    assert solution([], 5) == []
    
    assert solution([1], 0) == []
    assert solution([1], 1) == [1]
    assert solution([1], 3) == [1, 1, 1]
    
    assert solution([1, 2, 3], 0) == []
    assert solution([1, 2, 2], 1) == [1, 2, 2]
    assert solution([1, 2, 2], 3) == [1, 1, 1, 2, 2, 2, 2, 2, 2]

    assert solution(['a', 'b', 'b', 'c', 'c', 'd', 'a', 'd'], 4) == \
        ['a', 'a', 'a', 'a',
         'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b',
         'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c',
         'd', 'd', 'd', 'd',
         'a', 'a', 'a', 'a',
         'd', 'd', 'd', 'd']
    