import pytest
from solutions.p08_eliminate_duplicates import *

implementations = [eliminate_consecutive_duplicates_v1, 
                   eliminate_consecutive_duplicates_v2,
                   eliminate_consecutive_duplicates_v3
                   ]

ids = ["recursive", "iterative", 'direct']

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_tail_of_list(solution):
    assert solution([]) == []
    assert solution([1]) == [1]
    
    assert solution([1, 2, 3]) == [1, 2, 3]
    assert solution([1, 1, 2]) == [1, 2]
    assert solution([1, 2, 2]) == [1, 2]

    assert solution(['a', 'b', 'b', 'c', 'c', 'd', 'a', 'd']) == ['a', 'b', 'c', 'd', 'a', 'd']
    
    
    