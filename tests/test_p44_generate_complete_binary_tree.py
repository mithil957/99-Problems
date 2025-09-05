import pytest
from solutions.p44_generate_complete_binary_tree import *

implementations = [generate_cbt_v1]
ids = ["recursive"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_generate_complete_binary_tree(solution):
    assert is_cbt_v1(solution(0), 0)
    assert is_cbt_v1(solution(1), 1)
    assert is_cbt_v1(solution(2), 2)
    assert is_cbt_v1(solution(3), 3)
    assert is_cbt_v1(solution(8), 8)
    assert is_cbt_v1(solution(17), 17)
    assert is_cbt_v1(solution(17), 19) == False