import pytest
from solutions.p23_generate_permutations_from_list import *
from itertools import permutations

implementations = [generate_permutations_v1, generate_permutations_v2, generate_permutations_v3]
ids = ["recursive/df", "bfs", "generator"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_generate_permutations(solution):
    assert set(solution([1, 2, 3, 4], 1)) == set(permutations([1, 2, 3, 4], 1))
    assert set(solution([1, 2, 3, 4], 2)) == set(permutations([1, 2, 3, 4], 2))
    assert set(solution([1, 2, 3, 4, 5], 3)) == set(permutations([1, 2, 3, 4, 5], 3))
    assert set(solution([1, 2, 3, 4, 5, 6], 4)) == set(permutations([1, 2, 3, 4, 5, 6], 4))
    assert set(solution(['a', 'b', 'c', 'd'], 3)) == set(permutations(['a', 'b', 'c', 'd'], 3))
    assert set(solution(['a', 'b', 'c', 'd'], 10)) == set(permutations(['a', 'b', 'c', 'd'], 10))
    assert set(solution(list(range(10)), 7)) == set(permutations(list(range(10)), 7))