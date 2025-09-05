import pytest
from solutions.p61_unfold import *

implementations = [unfold_v1, unfold_v2]
ids = ["recursive", "iterative"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_unfold(solution):
    assert list(solution(
        5,
        lambda x: x - 1,
        lambda x: x == 0
    )) == [5, 4, 3, 2, 1]