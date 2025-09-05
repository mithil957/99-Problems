import pytest
from solutions.p10_modified_run_length_encoding import *

implementations = [modded_rle_encode_v1, modded_rle_encode_v2]

ids = ["4fun/dsl", "direct"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_tail_of_list(solution):
    assert solution([]) == []
    assert solution([1]) == [1]
    
    assert solution([1, 2, 3]) == [1, 2, 3]
    assert solution([1, 1, 2]) == [(1, 2), 2]
    assert solution([1, 2, 2]) == [1, (2, 2)]

    assert solution(['a', 'b', 'b', 'c', 'c', 'd', 'a', 'd']) == \
        ['a', ('b', 2), ('c', 2), 'd', 'a', 'd']