import pytest
from solutions.p11_decode_run_length_encoding import *

implementations = [decode_rle_list_v1, decode_rle_list_v2]
ids = ["recursive", "mapping"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_decode_rle_list(solution):
    assert solution([]) == []
    assert solution([1]) == [1]
    
    assert solution([1, 2, 3]) == [1, 2, 3]
    assert solution([(1, 2), 2]) == [1, 1, 2]
    assert solution([1, (2, 2)]) == [1, 2, 2]

    assert solution(['a', ('b', 2), ('c', 2), 'd', 'a', 'd']) == \
        ['a', 'b', 'b', 'c', 'c', 'd', 'a', 'd']