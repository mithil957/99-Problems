import pytest
from solutions.p37_shannon_fano_encoding import *

implementations = [generate_shannon_fano_encoding_v1]
ids = ["recursive"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_generate_shannon_fano_encoding(solution):
    assert solution([
        ("a", 45), ("b", 13), ("c", 12), 
        ("d", 16), ("e", 9), ("f", 5)
    ]) == [
        ('a', '0'), ('d', '100'), ('b', '101'),
        ('c', '110'), ('e', '1110'), ('f', '1111')]
    
    assert solution([
        ('a', 100), ('b', 1), ('c', 1)
    ]) == [
        ('a', '0'), ('b', '10'), ('c', '11')]