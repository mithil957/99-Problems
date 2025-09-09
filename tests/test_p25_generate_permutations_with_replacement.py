import pytest
from solutions.p25_generate_permutations_with_replacement import *
from itertools import product, repeat


implementations = [permutations_with_replacement_v1, permutations_with_replacements_v2, permutations_with_replacements_v3, permutations_with_replacements_v4]
ids = ["recursive/dfs", "bfs", "generator", "direct"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_permutations_with_replacement(solution):
    assert set(solution([1], 2)) == set(product([1], repeat=2))
    assert set(solution([1, 2], 2)) == set(product([1, 2], repeat=2))
    assert set(solution([1, 2, 3, 4], 0)) == set(product([1, 2, 3, 4], repeat=0))
    assert set(solution([1, 2, 3, 4], 1)) == set(product([1, 2, 3, 4], repeat=1))
    assert set(solution([1, 2, 3, 4], 2)) == set(product([1, 2, 3, 4], repeat=2))
    assert set(solution([1, 2, 3, 4, 5], 3)) == set(product([1, 2, 3, 4, 5], repeat=3))
    assert set(solution([1, 2, 3, 4, 5, 6], 4)) == set(product([1, 2, 3, 4, 5, 6], repeat=4))
    assert set(solution([1, 2, 3, 4, 5], 6)) == set(product([1, 2, 3, 4, 5], repeat=6))
    assert set(solution(['a', 'b', 'c', 'd'], 3)) == set(product(['a', 'b', 'c', 'd'], repeat=3))
    assert set(solution(['a', 'b', 'c', 'd'], 10)) == set(product(['a', 'b', 'c', 'd'], repeat=10))