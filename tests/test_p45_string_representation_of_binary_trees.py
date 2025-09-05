import pytest
from solutions.p45_string_representation_of_binary_trees import *

implementations = [tree_to_string_v1]
ids = ['recursive']

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_tree_to_string(solution):
    tree = Node('a', Node ('b', Node ('d', None, None), Node ('e', None, None)),
                        Node ('c', None, Node ('f', Node ('g', None, None), None)))
    assert solution(tree) == 'a(b(d,e),c(,f(g,)))'