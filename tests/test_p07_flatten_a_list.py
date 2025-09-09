import pytest
from solutions.p07_flatten_a_list import *

implementations = [flatten_list_v1, flatten_list_v2]
ids = ["recursive", "iterative"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_flatten_a_list(solution):
    assert solution([]) == []
    assert solution([1]) == [1]
    
    assert solution([1, 2, 3]) == [1, 2, 3]
    assert solution(['a', 'b', 'b', 'a']) == ['a', 'b', 'b', 'a']

    assert solution(['a', ['b'], 'b', ['a']]) == ['a', 'b', 'b', 'a']
    
    assert solution([[1, 2], 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert solution([[1, 2], 
                     [[3, 4], 5], 
                     [[[]]], 
                     [6, 7]]) == [1, 2, 3, 4, 5, 6, 7]
    
    assert solution([[[[[[[[1]]]]]]]]) == [1]
    