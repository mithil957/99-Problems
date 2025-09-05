import pytest
from solutions.p47_preorder_tree_traversal import *

implementations = [preorder_tree_traversal_v1]
ids = ["recursive"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_preorder_tree_traversal(solution):
    tree = string_to_tree_v1('a(b(d,e),c(,f(g,)))')
    assert solution(tree) == 'abdecfg'