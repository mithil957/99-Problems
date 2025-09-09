---
tags:
    - Patterns
    - Intermediate
---

# Unfold

Implement unfold which applies a function $F$ to a starting value $S$ until a predicate $P$ is true. 


=== "Test"
    ```python
    def test_unfold(solution):
        assert list(solution(
            seed = 5,
            func = lambda x: x - 1,
            stop_condition = lambda x: x == 0
        )) == [5, 4, 3, 2, 1]
    ```

=== "Recursive"
    ```python
    from typing import Callable, Generator

    def unfold_v1[T](seed: T, func: Callable[[T], T], stop_condition: Callable[[T], bool]) -> Generator[T]:
        if stop_condition(seed):
            return
        
        yield seed
        yield from unfold_v1(func(seed), func, stop_condition)
    ```

=== "Iterative"
    ```python
    from typing import Callable, Generator
    
    def unfold_v2[T](seed: T, func: Callable[[T], T], stop_condition: Callable[[T], bool]) -> Generator[T]:
        current_state = seed
        while not stop_condition(current_state):
            yield current_state
            current_state = func(current_state)
    ```