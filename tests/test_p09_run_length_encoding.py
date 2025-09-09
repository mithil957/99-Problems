import pytest
from solutions.p09_run_length_encoding import *

implementations = [rle_encode_v1, rle_encode_v2, rle_encode_v3]

ids = ["recursive", "reduce/fold", "direct"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_run_length_encoding(solution):
    assert solution([]) == []
    assert solution([1]) == [(1, 1)]
    
    assert solution([1, 2, 3]) == [(1, 1), (2, 1), (3, 1)]
    assert solution([1, 1, 2]) == [(1, 2), (2, 1)]
    assert solution([1, 2, 2]) == [(1, 1), (2, 2)]

    assert solution(['a', 'b', 'b', 'c', 'c', 'd', 'a', 'd']) == \
        [('a', 1), ('b', 2), ('c', 2), ('d', 1), ('a', 1), ('d', 1)]
    
    
    