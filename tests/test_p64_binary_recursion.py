import pytest
from solutions.p64_binary_recursion import *
from heapq import merge
from itertools import combinations

implementations = [binary_recursion_v1]
ids = ["recursive"]


@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_binary_recursion(solution):
    # Fibonacci
    assert solution(
        6,
        lambda state: state <= 1,
        lambda state: 1 if state == 1 else 0,
        lambda state: (state - 1, state - 2),
        lambda res1, res2, _: res1 + res2
    ) == 8

    # Merge Sort
    assert solution(
        ['z', 'c', 'd', 'b', 'a'],
        lambda state: len(state) <= 1,
        lambda state: state,
        lambda state: (state[:len(state) // 2], state[len(state) // 2:]),
        lambda res1, res2, _: list(merge(res1, res2))
    ) == ['a', 'b', 'c', 'd', 'z']

    # Combinations
    def transform(state):
        choices, num_remaining = state
        head, *tail = choices
        return (tail, num_remaining - 1), (tail, num_remaining)

    def combine(res1, res2, state):
        head, *_ = state[0]
        combos_with_head = [(head,) + combo for combo in res1]
        combos_without_head = res2
        return combos_with_head + combos_without_head
    
    assert solution(
        ([1, 2, 3, 4, 5], 3),
        lambda state: state[1] == 0 or len(state[0]) < state[1],
        lambda state: [()] if state[1] == 0 else [],
        transform,
        combine
    ) == list(combinations([1, 2, 3, 4, 5], 3))