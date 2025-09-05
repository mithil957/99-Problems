import pytest
from solutions.p49_tree_from_inorder_preorder_sequence import *

implementations = [tree_from_sequence_v1]
ids = ["recursive"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_(solution):
    tree = string_to_tree_v1('a(b(d,e),c(,f(g,)))')
    assert solution('abdecfg', 'dbeacgf') == tree