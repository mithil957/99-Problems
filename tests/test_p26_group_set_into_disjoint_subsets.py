import pytest
from solutions.p26_group_set_into_disjoint_subsets import *

implementations = [generate_ordered_partitions_v1, generate_ordered_partitions_v2]
ids = ["recursive/generator", "bfs"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_disjoint_subsets(solution):
    assert len(solution(['a','b', 'c', 'd'], [2, 1])) == len([
        [("a", "b"), ("c")], [("a", "c"),("b")], [("b", "c"), ("a")],
        [("a", "b"), ("d")], [("a", "c"),("d")], [("b", "c"), ("d")],
        [("a", "d"), ("b")], [("b", "d"),("a")], [("a", "d"), ("c")],
        [("b", "d"), ("c")], [("c", "d"),("a")], [("c", "d"), ("b")]
    ])

    assert len(solution(['a','b', 'b'], [2, 1])) == len([
        [("a", "b"), ("c")], [("a", "c"),("b")], [("b", "c"), ("a")],
    ])

    assert len(solution([1, 2, 3, 4, 5], [1, 3, 1])) == len([
        [(1), (2, 3, 4), (5)], [(1), (2, 3, 5), (4)], [(1), (2, 4, 5), (3)], [(1), (3, 4, 5), (2)],
        [(2), (1, 3, 4), (5)], [(2), (1, 3, 5), (4)], [(2), (1, 4, 5), (3)], [(2), (3, 4, 5), (1)],
        [(3), (1, 2, 4), (5)], [(3), (1, 2, 5), (4)], [(3), (1, 4, 5), (2)], [(3), (2, 4, 5), (1)],
        [(4), (1, 2, 3), (5)], [(4), (1, 2, 5), (3)], [(4), (1, 3, 5), (2)], [(4), (2, 3, 5), (1)],
        [(5), (1, 2, 3), (4)], [(5), (1, 2, 4), (3)], [(5), (1, 3, 4), (2)], [(5), (2, 3, 4), (1)]
    ])

    assert len(solution(['a', 'b', 'c', 'd'], [2, 2])) == len([
        [('a', 'b'), ('c', 'd')],
        [('a', 'c'), ('b', 'd')],
        [('a', 'd'), ('b', 'c')],
        [('b', 'c'), ('a', 'd')],
        [('b', 'd'), ('a', 'c')],
        [('c', 'd'), ('a', 'b')]
    ])