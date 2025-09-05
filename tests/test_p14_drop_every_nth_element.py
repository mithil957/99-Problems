import pytest
from solutions.p14_drop_every_nth_element import *

implementations = [drop_every_nth_element_v1, drop_every_nth_element_v2]
ids = ["reduce", "generator/filter"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_drop_every_nth_element(solution):
    assert solution([], 0) == []
    assert solution([], 5) == []
    
    assert solution([1], 0) == [1]
    assert solution([1], 1) == []
    assert solution([1], 3) == [1]
    
    assert solution([1, 2, 3], 0) == [1, 2, 3]
    assert solution([1, 2, 2], 1) == []
    assert solution([1, 2, 2], 3) == [1, 2]

    assert solution(['a', 'b', 'b', 'c', 'c', 'd', 'a', 'd'], 4) == \
        ['a', 'b', 'b', 'c', 'd', 'a']