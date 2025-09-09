---
tags:
    - Pattern
    - Intermediate
---

# Fold

Implement fold which takes a state $S$, a function $F$, and elements $E$.

It applies $F(S, E_h)$ → $S_n$ where $E_h$ is the head of $E$ and $S_n$ is the new state.
Then we move "forward" along $E$ and apply again. 

Repeat this until we run out elements and return the final state.

=== "Test"
    ```python
    def test_fold(solution):
        assert solution(
            state = 0,
            func = lambda acc, next_elem: acc + next_elem,
            elements = iter([1, 2, 3, 4, 5])
        ) == 15
    ```

=== "Recursive"
    ```python
    from typing import Callable, Generator

    def fold_v1[T](state: T, func: Callable[[T, T], T], elements: Generator[T]) -> T:
        if (head := next(elements, None)) is not None:
            next_state = func(state, head)
            return fold_v1(next_state, func, elements)
        
        return state
    ```

=== "Iterative"
    ```python
    from typing import Callable, Generator

    def fold_v2[T](state: T, func: Callable[[T, T], T], elements: Generator[T]) -> T:
        current_state = state
        while (head := next(elements, None)) is not None:
            current_state = func(current_state, head)
        
        return current_state
    ```

=== "Direct"
    ```python
    from typing import Callable, Generator
    from functools import reduce

    def fold_v3[T](state: T, func: Callable[[T, T], T], elements: Generator[T]) -> T:
        return reduce(func, elements, state)
    ```