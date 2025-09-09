---
tags:
    - Pattern
    - Advanced
---

# Nary Recursion

Implement n-ary recursion which has 4 parts.

A function __at_base_case__ which tells us if we reached the base case.

A function __calulate_base_case__ which calculates the value when we reach the base case.

A function __transform__ which outputs up to N values given a state.

A function __combine__ which combines the results of the recursive calls.


=== "Test"
    ```python
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
    ```

=== "Recursive"
    ```python
    from __future__ import annotations
    from typing import Callable

    type State[T] = T
    type Result[V] = V

    def nary_recursion_v1(state: State,
                          at_base_case: Callable[[State], bool],
                          calculate_base_case: Callable[[State], Result],
                          transform: Callable[[State], tuple[State, ...]],
                          combine: Callable[[State, *tuple[Result, ...]], Result]) -> Result:
        
        if at_base_case(state):
            return calculate_base_case(state)
        
        next_states = transform(state)
        results = (nary_recursion_v1(next_state, at_base_case, calculate_base_case, transform, combine)
                   for next_state in next_states)

        return combine(state, *results)
    ```

=== "Iterative"
    ```python
    from __future__ import annotations
    from typing import Callable
    from dataclasses import dataclass

    type State[T] = T
    type Result[V] = V

    @dataclass
    class Unevaluated[State]:
        value: State

    @dataclass
    class Evaluated[Result]:
        value: Result

    type Parameter = Unevaluated | Evaluated

    @dataclass
    class FunctionFrame:
        parnet_state: State
        parameters: list[Parameter]
        uneval_idx: int | None

        def __init__(self, parnet_state: State, params: list[Parameter]) -> FunctionFrame:
            self.parnet_state = parnet_state
            self.parameters = params
            self.uneval_idx = next((idx for idx, p in enumerate(params) if isinstance(p, Unevaluated)), None)
        
        def move_idx(self):
            if (self.uneval_idx + 1) >= len(self.parameters):
                self.uneval_idx = None
            else:
                self.uneval_idx += 1


    def nary_recursion_v2(state: State,
                          at_base_case: Callable[[State], bool],
                          calculate_base_case: Callable[[State], Result],
                          transform: Callable[[State], tuple[State, ...]],
                          combine: Callable[[State, *tuple[Result, ...]], Result]) -> Result:
        
        def construct_function_args(s: State) -> list[Parameter]:
            params = []
            for next_s in transform(s):
                if at_base_case(next_s): 
                    params.append(Evaluated(calculate_base_case(next_s)))
                else: 
                    params.append(Unevaluated(next_s))
            
            return params

        if at_base_case(state):
            return calculate_base_case(state)

        call_stack: list[FunctionFrame] = [FunctionFrame(state, construct_function_args(state))]
        last_result: Result | None = None

        while call_stack:
            func: FunctionFrame = call_stack[-1]
            uneval_idx = func.uneval_idx
            param = None if uneval_idx is None else func.parameters[uneval_idx]

            match (param, last_result):
                case (None, None):
                    last_result = combine(func.parnet_state, *(evaluated.value for evaluated in func.parameters))
                    call_stack.pop()
                
                case (Unevaluated(val), None):
                    new_frame = FunctionFrame(val, construct_function_args(val))
                    call_stack.append(new_frame)
                        
                case (Unevaluated(val), res):
                    func.parameters[uneval_idx] = Evaluated(res)
                    func.move_idx()
                    last_result = None
                
                case (Evaluated(val), _):
                    func.move_idx()

        return last_result
    ```