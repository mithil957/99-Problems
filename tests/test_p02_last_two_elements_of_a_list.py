import pytest
from solutions.p02_last_two_elements_of_a_list import *

implementations = [last_two_elements_of_a_list_v1, last_two_elements_of_a_list_v2]
ids = ["pattern_matching", "recursive"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_tail_of_list(solution):
    assert solution([]) is None
    assert solution([1]) is None
    assert solution([1, 2, 3]) == (2, 3)
    assert solution(['a', 'b', 'c', 'd']) == ('c', 'd')
