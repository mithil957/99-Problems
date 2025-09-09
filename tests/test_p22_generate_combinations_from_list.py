import pytest
from solutions.p22_generate_combinations_from_list import *
from itertools import combinations

implementations = [generate_combinations_v1, generate_combinations_v2, generate_combinations_v3, generate_combinations_v4]
ids = ["recursive/dfs", "bfs", "generator", 'direct']

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_generate_combinations(solution):
    assert set(solution([1, 2, 3, 4], 1)) == set(combinations([1, 2, 3, 4], 1))
    assert set(solution([1, 2, 3, 4], 2)) == set(combinations([1, 2, 3, 4], 2))
    assert set(solution([1, 2, 3, 4, 5], 3)) == set(combinations([1, 2, 3, 4, 5], 3))
    assert set(solution(['a', 'b', 'c', 'd'], 3)) == set(combinations(['a', 'b', 'c', 'd'], 3))
    assert set(solution(['a', 'b', 'c', 'd'], 10)) == set(combinations(['a', 'b', 'c', 'd'], 10))
    assert set(solution(list(range(20)), 10)) == set(combinations(list(range(20)), 10))