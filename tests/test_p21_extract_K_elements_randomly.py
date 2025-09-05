import pytest
from solutions.p21_extract_K_elements_randomly import *

implementations = [extract_elements_v1, extract_elements_v2]
ids = ["direct", "recursive"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_extract_elements(solution):
    assert solution([1, 2, 3], 0) == []
    assert solution([1, 2, 3], 4) is None
    assert solution([1, 2, 3], 10) is None
    assert len(solution([1, 2, 3], 3)) == 3
    assert len(solution([1, 2, 3], 2)) == 2