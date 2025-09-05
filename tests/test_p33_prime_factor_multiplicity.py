import pytest
from solutions.p33_prime_factor_multiplicity import *

implementations = [prime_factor_counts_v1, prime_factor_counts_v2]
ids = ["recursive", "compounding other solutions"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_prime_factor_multiplicity(solution):
    assert solution(1) == []
    assert solution(315) == [(3, 2), (5, 1), (7, 1)]
    assert solution(9999) == [(3, 2), (11, 1), (101, 1)]
    assert solution(1009899) == [(3, 2), (11, 1), (101, 2)]
    assert solution(99999) == [(3, 2), (41, 1), (271, 1)]