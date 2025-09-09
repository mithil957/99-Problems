import pytest
from solutions.p31_prime_factors import *

implementations = [prime_factors_v1, prime_factors_v2, prime_factors_v3, prime_factors_v4]
ids = ["recursive", "generator/iterative", "changing upper bound", "wheel"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_prime_factors(solution):
    assert solution(1) == []
    assert solution(2) == [2]
    assert solution(3) == [3]
    assert solution(315) == [3, 3, 5, 7]
    assert solution(9999) == [3, 3, 11, 101]
    assert solution(1009899) == [3, 3, 11, 101, 101]
    assert solution(99999) == [3, 3, 41, 271]