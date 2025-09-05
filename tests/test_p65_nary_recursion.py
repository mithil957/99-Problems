import pytest
from solutions.p65_nary_recursion import *
from heapq import merge
from itertools import chain, combinations

implementations = [nary_recursion_v1, nary_recursion_v2]
ids = ["recursive", "iterative"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_nary_recursion(solution):

    # Merge sort
    assert solution(
        ['z', 'c', 'd', 'b', 'a'],
        lambda state: len(state) <= 1,
        lambda state: state,
        lambda state: (state[:len(state) // 2], state[len(state) // 2:]),
        lambda state, res1, res2: list(merge(res1, res2))
    ) == ['a', 'b', 'c', 'd', 'z']

    # Square all elements of arb. nested list
    assert solution(
        [1, [2, 3], 4, [5, [6]]],
        lambda state: not isinstance(state, list),
        lambda state: state * state,
        lambda state: state,
        lambda state, *results: list(results)
    ) == [1, [4, 9], 16, [25, [36]]]

    # Flatten list
    assert solution(
        [1, [2, 3], 4, [5, [6]]],
        lambda state: not isinstance(state, list),
        lambda state: [state],
        lambda state: state,
        lambda state, *results: list(chain.from_iterable(results))
    ) == [1, 2, 3, 4, 5, 6]

    # Eliminate consecutive duplicates
    assert solution(
        [1, 1, 2, 2, 3, 4, 5, 5],
        lambda state: len(state) <= 2,
        lambda state: [state[0]] if len(state) == 2 and state[0] == state[1] else state,
        lambda state: (state[:len(state) // 2], state[len(state) // 2:]),
        lambda state, res1, res2: res1 + res2[1:] if res1[-1] == res2[0] else res1 + res2 
    ) == [1, 2, 3, 4, 5]

    # Combinations
    def transform(state):
        choices, num_remaining = state
        head, *tail = choices
        return (tail, num_remaining - 1), (tail, num_remaining)

    def combine(state, res1, res2):
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