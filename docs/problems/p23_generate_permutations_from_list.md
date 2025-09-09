---
tags:
    - List
    - Intermediate
---

# Generate Permutations

Generate the permutations of K objects from the N elements of a list. We will pick K times without repeating any previous objects. This is known as permutation without replacement. 

<description>

=== "Test"
    ```python
    def test_generate_permutations(solution):
        assert set(solution([1, 2, 3, 4], 1)) == set(permutations([1, 2, 3, 4], 1))
        assert set(solution([1, 2, 3, 4], 2)) == set(permutations([1, 2, 3, 4], 2))
        assert set(solution([1, 2, 3, 4, 5], 3)) == set(permutations([1, 2, 3, 4, 5], 3))
        assert set(solution([1, 2, 3, 4, 5, 6], 4)) == set(permutations([1, 2, 3, 4, 5, 6], 4))
        assert set(solution(['a', 'b', 'c', 'd'], 3)) == set(permutations(['a', 'b', 'c', 'd'], 3))
        assert set(solution(['a', 'b', 'c', 'd'], 10)) == set(permutations(['a', 'b', 'c', 'd'], 10))
        assert set(solution(list(range(10)), 7)) == set(permutations(list(range(10)), 7))
    ```

=== "Recursive"
    ```python
    def generate_permutations_v1[T](lst: list[T], num_of_items: int) -> list[tuple[T]]:
        accumulated = []

        def aux(selected: tuple[T], remaining_choices: list[T]):
            if len(selected) + len(remaining_choices) < num_of_items:
                return
            
            if len(selected) == num_of_items:
                accumulated.append(selected)
                return
            
            for idx, choice in enumerate(remaining_choices):
                aux(selected + (choice,), remaining_choices[:idx] + remaining_choices[idx + 1:])
        
        aux((), lst)
        return accumulated
    ```

=== "BFS"
    ```python
    from collections import deque

    def generate_permutations_v2[T](lst: list[T], num_of_items: int) -> list[tuple[T]]:
        accumulated = []
        nodes = deque([((), lst)])

        while nodes:
            selected, remaining_choices = nodes.popleft()

            for idx, choice in enumerate(remaining_choices):
                new_selected = selected + (choice,)
                new_remaining_choices = remaining_choices[:idx] + remaining_choices[idx + 1:]

                if len(new_selected) == num_of_items:
                    accumulated.append(new_selected)
                elif len(new_selected) + len(new_remaining_choices) >= num_of_items:
                    nodes.append((new_selected, new_remaining_choices))
        
        return accumulated
    ```

=== "Generator/Recursive"
    ```python
    from typing import Generator

    def generate_permutations_v3[T](lst: list[T], num_of_items: int) -> list[tuple[T]]:
        def permutations_iter(lst: list[T], num_of_items: int) -> Generator[tuple[T]]:
            if len(lst) == 0 or num_of_items > len(lst):
                return
            
            if num_of_items == 0:
                yield ()
                return

            yield from ((val,) + perm
                        for idx, val in enumerate(lst)
                        for perm in permutations_iter(lst[:idx] + lst[idx + 1:], num_of_items - 1))
        
        return list(permutations_iter(lst, num_of_items))
    ```

=== "Direct"
    ```python
    from itertools import permutations

    def generate_permutations_v4[T](lst: list[T], num_of_items: int) -> list[tuple[T]]:
        return list(permutations(lst, num_of_items))
    ```