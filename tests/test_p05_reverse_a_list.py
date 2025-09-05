import pytest
from solutions.p05_reverse_a_list import *

implementations = [reverse_list_v1, reverse_list_v2]
ids = ["direct", "recursive"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_tail_of_list(solution):
    assert solution([]) == []
    assert solution([1]) == [1]
    assert solution([1, 2, 3]) == [3, 2, 1]
    assert solution(['a', 'b', 'c', 'd']) == ['d', 'c', 'b', 'a']
