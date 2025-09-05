import pytest
from solutions.p12_duplicate_the_elements_of_a_list import *

implementations = [duplicate_elements_v1, duplicate_elements_v2, 
                   duplicate_elements_v3, duplicate_elements_v4,
                   duplicate_elements_v5]
ids = ["recursive", "map", "zip", "reduce", "direct"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_duplicate_elements(solution):
    assert solution([]) == []
    assert solution([1]) == [1, 1]
    
    assert solution([1, 2, 3]) == [1, 1, 2, 2, 3, 3]
    assert solution([1, 2, 2]) == [1, 1, 2, 2, 2, 2]

    assert solution(['a', 'b', 'b', 'c', 'c', 'd', 'a', 'd']) == \
        ['a', 'a', 
         'b', 'b', 'b', 'b', 
         'c', 'c', 'c', 'c', 
         'd', 'd',
         'a', 'a',
         'd', 'd']