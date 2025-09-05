import pytest
from solutions.p36_gray_code import *

implementations = [generate_gray_code_v1, generate_gray_code_v2]
ids = ["recursive", "formula"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_generate_gray_code(solution):
    assert solution(1) == ['0', '1']
    assert solution(2) == ['00', '01', '11', '10']
    assert solution(3) == ['000', '001', '011', '010', '110', '111', '101', '100']