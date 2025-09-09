---
tags:
    - Pattern
    - Intermediate
---

# Binary Recursion

Implement binary recursion which has 4 parts.

A function __at_base_case__ which tells us if we reached the base case.

A function __calulate_base_case__ which calculates the value when we reach the base case.

A function __transform__ which outputs 2 values given a state.

A function __combine__ which combines the results of the recursive calls with the state.


=== "Test"
    ```python
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
    ```

=== "Recursive"
    ```python
    from __future__ import annotations
    from typing import Callable

    type State[T] = T
    type Result[V] = V

    def binary_recursion_v1(state: State,
                            at_base_case: Callable[[State], bool],
                            calculate_base_case: Callable[[State], Result],
                            transform: Callable[[State], tuple[State, State]],
                            combine: Callable[[Result, Result, State], Result]) -> Result:
        
        if at_base_case(state):
            return calculate_base_case(state)
        
        next_state_1, next_state_2 = transform(state)

        result_from_1 = binary_recursion_v1(next_state_1,
                                            at_base_case, calculate_base_case,
                                            transform, combine)
        
        result_from_2 = binary_recursion_v1(next_state_2,
                                            at_base_case, calculate_base_case,
                                            transform, combine)
        
        return combine(result_from_1, result_from_2, state)
    ```