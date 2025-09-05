import pytest
from solutions.p62_fold import *

implementations = [fold_v1, fold_v2, fold_v3]
ids = ["recursive", "iterative", "direct"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_fold(solution):
    assert solution(
        0,
        lambda acc, next_elem: acc + next_elem,
        iter([1, 2, 3, 4, 5])
    ) == 15