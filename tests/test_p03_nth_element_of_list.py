import pytest
from solutions.p03_nth_element_of_list import *

implementations = [nth_element_of_list_v1, nth_element_of_list_v2]
ids = ["recursive", "direct"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_tail_of_list(solution):
    assert solution([], 5) is None
    assert solution([1], 5) is None
    assert solution([1], 0) is 1
    assert solution([1, 2, 3], 2) == 3
    assert solution(['a', 'b', 'c', 'd'], 2) == 'c'
    assert solution(['a', 'b', 'c', 'd'], 89) is None
