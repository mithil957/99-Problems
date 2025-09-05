import pytest
from solutions.p28_sort_lists_based_on_frequency_of_length import *

implementations = [sort_by_frequency_of_length_v1]
ids = ["direct"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_sort_by_frequency_of_length(solution):
    assert [len(t) for t in solution([
            ["a", "b", "c"], ["d", "e"], ["f", "g", "h"], ["d", "e"],
            ["i", "j", "k", "l"], ["m", "n"], ["o"]])
        ] ==\
            [len(t) for t in [
                ["i", "j", "k", "l"], ["o"], ["a", "b", "c"], ["f", "g", "h"], ["d", "e"], ["d", "e"], ["m", "n"]]
            ]
            