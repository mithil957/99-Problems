import pytest
from solutions.p63_linear_recursion import *

implementations = [linear_recursion_v1, linear_recursion_v2, linear_recursion_v3]
ids = ["recursive", "iterative", "unfold/fold"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_linear_recursion(solution):
    assert solution(
        state = 5,
        at_base_case = lambda state: state == 0,
        calculate_base_case = lambda state: 1,
        transform = lambda state: state - 1, 
        combine = lambda rec_result, state: state * rec_result
    ) == 120


    assert solution(
        state = [1, 1, 2, 2, 3, 4, 5, 5],
        at_base_case = lambda state: len(state) < 1,
        calculate_base_case = lambda state: state,
        transform = lambda state: state[1:], 
        combine = lambda rec_result, state: rec_result 
                                            if len(rec_result) > 0 and state[0] == rec_result[0]
                                            else [state[0]] + rec_result 
    ) == [1, 2, 3, 4, 5]