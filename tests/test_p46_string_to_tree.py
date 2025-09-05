import pytest
from solutions.p46_string_to_tree import *

implementations = [string_to_tree_v1]
ids = ['recursive']

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_string_to_tree(solution):
    tree = Node('a', Node ('b', Node ('d', None, None), Node ('e', None, None)),
                        Node ('c', None, Node ('f', Node ('g', None, None), None)))
    assert solution('a(b(d,e),c(,f(g,)))') == tree
