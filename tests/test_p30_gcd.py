import pytest
from solutions.p30_gcd import *

implementations = [gcd_v1, gcd_v2, gcd_v3]
ids = ["recursive", "iterative", "direct"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_gcd(solution):
    assert solution(13, 27) == 1
    assert solution(24, 18) == 6
    assert solution(20536, 7826) == 2
    