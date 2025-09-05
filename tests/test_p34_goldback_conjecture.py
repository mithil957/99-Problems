import pytest
from solutions.p34_goldbach_conjecture import *

implementations = [goldbach_v1, goldbach_v2]
ids = ["recursive", "sieve+twosum"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_goldbach_conjecture(solution):
    assert sum(solution(4)) == sum((2, 2))
    assert sum(solution(28)) == sum((5, 23))
    assert sum(solution(32)) == sum((3, 29))
    assert sum(solution(36)) == sum((7, 29))
    assert solution(35) is None