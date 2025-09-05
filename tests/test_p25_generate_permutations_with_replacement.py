import pytest
from solutions.p25_generate_permutations_with_replacement import *
from itertools import product, chain


implementations = [permutations_with_replacement_v1, permutations_with_replacements_v2, permutations_with_replacements_v3]
ids = ["recursive/dfs", "bfs", "generator"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_permutations_with_replacement(solution):
    assert set(solution([1], 2)) == set(product(*chain([1] for _ in range(2))))
    assert set(solution([1, 2], 2)) == set(product(*chain([1, 2] for _ in range(2))))
    assert set(solution([1, 2, 3, 4], 0)) == set(product(*chain([1, 2, 3, 4] for _ in range(0))))
    assert set(solution([1, 2, 3, 4], 1)) == set(product(*chain([1, 2, 3, 4] for _ in range(1))))
    assert set(solution([1, 2, 3, 4], 2)) == set(product(*chain([1, 2, 3, 4] for _ in range(2))))
    assert set(solution([1, 2, 3, 4, 5], 3)) == set(product(*chain([1, 2, 3, 4, 5] for _ in range(3))))
    assert set(solution([1, 2, 3, 4, 5, 6], 4)) == set(product(*chain([1, 2, 3, 4, 5, 6] for _ in range(4))))
    assert set(solution([1, 2, 3, 4, 5], 6)) == set(product(*chain([1, 2, 3, 4, 5] for _ in range(6))))
    assert set(solution(['a', 'b', 'c', 'd'], 3)) == set(product(*chain(['a', 'b', 'c', 'd'] for _ in range(3))))
    assert set(solution(['a', 'b', 'c', 'd'], 10)) == set(product(*chain(['a', 'b', 'c', 'd'] for _ in range(10))))