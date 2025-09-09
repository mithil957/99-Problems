import pytest
from solutions.p06_palindrome import *

implementations = [check_palindrome_v1, 
                   check_palindrome_v2,
                   check_palindrome_v3]
ids = ["direct", "recursive", "tail recursive"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_palindrome(solution):
    assert solution([]) == True
    assert solution([1]) == True
    assert solution([1, 1]) == True
    assert solution([1, 2]) == False
    assert solution([1, 2, 3]) == False
    assert solution(['a', 'b', 'b', 'a']) == True
    assert solution(['a', 'b', 'c', 'b', 'a']) == True
    assert solution(['r', 'a', 'c', 'e', 'c', 'a', 'r']) == True
    