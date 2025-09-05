import pytest
from solutions.p19_insert_element_at_idx import *

implementations = [insert_element_v1, insert_element_v2, insert_element_v3]
ids = ["recursive", "direct", "slices"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_insert_element(solution):
    elem = 42

    assert solution([], elem, 0) == [elem]
    assert solution([], elem, 1) == [elem]
    assert solution([], elem, 5) == [elem]
    
    assert solution([1], elem, 0) == [elem, 1]
    assert solution([1], elem, 1) == [1, elem]
    assert solution([1], elem, 100) == [1, elem]
    assert solution([1], elem, -37) == [1]
    
    assert solution([1, 2, 3], elem, 0) == [elem, 1, 2, 3]
    assert solution([1, 2, 3], elem, 1) == [1, elem, 2, 3]
    assert solution([1, 2, 3], elem, 2) == [1, 2, elem, 3]
    assert solution([1, 2, 3], elem, 3) == [1, 2, 3, elem]
    assert solution([1, 2, 3], elem, 4) == [1, 2, 3, elem]
    assert solution([1, 2, 3], elem, -44) == [1, 2, 3]

    elem = '42'

    assert solution(['a', 'b', 'b', 'c', 'c', 'd', 'a', 'd'], elem, 4) == \
        ['a', 'b', 'b', 'c', elem, 'c', 'd', 'a', 'd']