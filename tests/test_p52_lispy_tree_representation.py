import pytest
from solutions.p52_lispy_tree_representation import *

implementations = [lispy_tree_repr_v1]
ids = ["recursive"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_lispy_tree_representation(solution):
    t = Node('a', [])
    assert solution(t) == 'a'

    t = Node('a', [Node('b', [])])
    assert solution(t) == '(a b)'

    t = Node('a', [Node('b', [Node('c', [])])])
    assert solution(t) == '(a (b c))'

    t = Node('a', [Node('b', []), Node('c', [])])
    assert solution(t) == '(a b c)'

    