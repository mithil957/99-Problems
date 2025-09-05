import pytest
from solutions.p41_bst import *

implementations = [construct_bst_v1, construct_bst_v2]
ids = ["recursive", "recursive/no mutation"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_construct_bst(solution):
    assert solution([3, 2, 5, 7, 1]) == Node (3, 
                                            Node (2, Node (1, None, None), 
                                                     None), 
                                            Node (5, None, 
                                                     Node (7, None, None)))