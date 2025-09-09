import pytest
from solutions.p51_multiway_tree_from_string import *

implementations = [string_to_tree_v1]
ids = ["recursive"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_tree_from_string(solution):
    assert tree_to_string(solution('afg^^c^^')) == 'afg^^c^^'