import pytest
from solutions.p27_sort_lists_based_on_length import *

implementations = [sort_sublists_by_length_v1, sort_sublists_by_length_v2]
ids = ["merge sort", "direct"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_sort_sublists_by_length(solution):
    assert [len(t) for t in solution([
        ["a", "b", "c"], ["d", "e"], ["f", "g", "h"], ["d", "e"],
        ["i", "j", "k", "l"], ["m", "n"], ["o"]])] ==\
            [len(t) for t in [["o"], ["d", "e"], ["d", "e"], ["m", "n"], 
             ["a", "b", "c"], ["f", "g", "h"], ["i", "j", "k", "l"]]]
            