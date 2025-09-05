import pytest
from solutions.p20_create_list_given_range import *

implementations = [create_range_v1, create_range_v2]
ids = ["recursive", "direct"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_create_range(solution):
    assert solution(0, 0) == [0]
    assert solution(1, 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert solution(5, 3) == [5, 4, 3]
    assert solution(-2, 2) == [-2, -1, 0, 1, 2]