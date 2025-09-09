import pytest
from solutions.p16_extract_slice import *

implementations = [extract_slice_v1, extract_slice_v2, extract_slice_v3, extract_slice_v4]
ids = ["recursive", "direct", "generator", "mask"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_extract_slice(solution):
    assert solution([], 0, 0) == []
    assert solution([], 0, 1) == []
    assert solution([], 0, 5) == []
    assert solution([], 3, 5) == []
    
    assert solution([1], 0, 0) == [1]
    assert solution([1], 0, 1) == [1]
    assert solution([1], 1, 1) == []
    assert solution([1], 0, 5) == [1]
    assert solution([1], 3, 5) == []
    
    assert solution([1, 2, 3], 0, 0) == [1]
    assert solution([1, 2, 3], 0, 1) == [1, 2]
    assert solution([1, 2, 3], 0, 2) == [1, 2, 3]
    assert solution([1, 2, 3], 1, 2) == [2, 3]
    assert solution([1, 2, 3], 2, 3) == [3]
    assert solution([1, 2, 3], 4, 7) == []

    assert solution(['a', 'b', 'b', 'c', 'c', 'd', 'a', 'd'], 4, 6) == \
        ['c', 'd', 'a']