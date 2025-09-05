import pytest
from solutions.p30_gcd import *

implementations = [gcd_v1]
ids = ["recursive"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_gcd(solution):
    assert solution(13, 27) == 1
    assert solution(20536, 7826) == 2
    