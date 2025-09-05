import pytest
from solutions.p38_huffman_encoding import *

implementations = [generate_huffman_codes_v1]
ids = ["sortedlist"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_generate_huffman_encoding(solution):
    assert solution([
        ("a", 45), ("b", 13), ("c", 12), 
        ("d", 16), ("e", 9), ("f", 5)
    ]) == [
        ("a", "0"), ("c", "100"), ("b", "101"), 
        ("f", "1100"), ("e", "1101"), ("d", "111")]