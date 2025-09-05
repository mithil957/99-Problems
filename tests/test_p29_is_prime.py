import pytest
from solutions.p29_is_prime import *

implementations = [is_prime_v1]
ids = ["recursive"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_is_prime(solution):
    assert solution(0) == False
    assert solution(1) == False
    assert solution(2) == True
    assert solution(3) == True
    assert solution(5) == True
    assert solution(7) == True
    assert solution(13) == True
    assert solution(1299827) == True
    assert solution(6) == False
    assert solution(1000000) == False
    