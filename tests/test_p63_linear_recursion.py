import pytest
from solutions.p63_linear_recursion import *

implementations = [linear_recursion_v1, linear_recursion_v2]
ids = ["recursive", "iterative"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_linear_recursion(solution):
    assert solution(
        5,
        lambda state: state == 0,
        lambda state: 1,
        lambda state: state - 1, 
        lambda state, rec_result: state * rec_result
    ) == 120


    assert solution(
        [1, 1, 2, 2, 3, 4, 5, 5],
        lambda state: len(state) <= 1,
        lambda state: state,
        lambda state: state[1:], 
        lambda state, rec_result: rec_result 
                                  if len(rec_result) > 0 and state[0] == rec_result[0]
                                  else [state[0]] + rec_result 
    ) == [1, 2, 3, 4, 5]