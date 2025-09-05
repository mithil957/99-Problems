import pytest
from solutions.p01_tail_of_list import *

implementations = [tail_of_list]
ids = ["pattern_matching"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_tail_of_list(solution):
    assert solution([]) is None
    assert solution([1]) == 1
    assert solution([1, 2, 3]) == 3
    assert solution(['a', 'b', 'c']) == 'c'
