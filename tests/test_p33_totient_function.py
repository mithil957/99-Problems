import pytest
from solutions.p33_totient_function import *

implementations = [totient_fn_v1, totient_fn_v2]
ids = ['direct', 'formula']

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_totient_fn(solution):
    assert solution(10) == 4
    assert solution(20) == 8
    assert solution(40) == 16
    assert solution(99) == 60
    assert solution(33) == 20
    assert solution(1) == 1
    