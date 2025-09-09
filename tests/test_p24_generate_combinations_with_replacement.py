import pytest
from solutions.p24_generate_combinations_with_replacement import *
from itertools import combinations_with_replacement


implementations = [combinations_with_replacement_v1, combinations_with_replacement_v2, combinations_with_replacement_v3, combinations_with_replacement_v4]
ids = ["recursive/dfs", "bfs", "generator", "direct"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_combinations_with_replacement(solution):
    assert set(solution([1, 2, 3, 4], 0)) == set(combinations_with_replacement([1, 2, 3, 4], 0))
    assert set(solution([1, 2, 3, 4], 1)) == set(combinations_with_replacement([1, 2, 3, 4], 1))
    assert set(solution([1, 2, 3, 4], 2)) == set(combinations_with_replacement([1, 2, 3, 4], 2))
    assert set(solution([1, 2, 3, 4, 5], 3)) == set(combinations_with_replacement([1, 2, 3, 4, 5], 3))
    assert set(solution([1, 2, 3, 4, 5, 6], 4)) == set(combinations_with_replacement([1, 2, 3, 4, 5, 6], 4))
    assert set(solution([1, 2, 3, 4, 5], 6)) == set(combinations_with_replacement([1, 2, 3, 4, 5], 6))
    assert set(solution(['a', 'b', 'c', 'd'], 3)) == set(combinations_with_replacement(['a', 'b', 'c', 'd'], 3))
    assert set(solution(['a', 'b', 'c', 'd'], 10)) == set(combinations_with_replacement(['a', 'b', 'c', 'd'], 10))
    assert set(solution(list(range(10)), 10)) == set(combinations_with_replacement(list(range(10)), 10))