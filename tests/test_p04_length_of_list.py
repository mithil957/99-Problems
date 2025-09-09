import pytest
from solutions.p04_length_of_list import *

implementations = [number_of_elements_in_list_v1, 
                   number_of_elements_in_list_v2,
                   number_of_elements_in_list_v3]
ids = ["direct", "recursive", "tail recursive"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_length_of_list(solution):
    assert solution([]) == 0
    assert solution([1]) == 1
    assert solution([1, 2, 3]) == 3
    assert solution(['a', 'b', 'c', 'd']) == 4
