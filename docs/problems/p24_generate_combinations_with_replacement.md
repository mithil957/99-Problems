---
tags:
    - List
    - Intermediate
---

# Generate Combinations with Replacement

Generate the combinations of K objects from the N elements of a list. We will pick K times but we are allowed to pick the same element more than once. This is known as combination with replacement. 



=== "Test"
    ```python
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
    ```

=== "Recursive"
    ```python
    def combinations_with_replacement_v1[T](lst: list[T], num_of_items: int) -> list[tuple[T]]:
        if num_of_items == 0: return [()]
        valid_selections = []

        def aux(selected: tuple[T], remaining_choices: list[T]):
            if len(selected) == num_of_items:
                valid_selections.append(selected)
                return

            for idx, choice in enumerate(remaining_choices):
                aux(selected + (choice,), remaining_choices[idx:])
        
        aux((), lst)
        return valid_selections
    ```

=== "BFS"
    ```python
    from collections import deque

    def combinations_with_replacement_v2[T](lst: list[T], num_of_items: int) -> list[tuple[T]]:
        if num_of_items == 0: return [()]
        valid_selections = []
        nodes = deque([((), lst)])

        while nodes:
            selected, remaining_choices = nodes.popleft()

            for idx, val in enumerate(remaining_choices):
                new_selected = selected + (val,)
                new_remaining_choices = remaining_choices[idx:]

                if len(new_selected) == num_of_items:
                    valid_selections.append(new_selected)
                else:
                    nodes.append((new_selected, new_remaining_choices))
        
        return valid_selections
    ```

=== "Generator/Recursive"
    ```python
    from typing import Generator

    def combinations_with_replacement_v3[T](lst: list[T], num_of_items: int) -> list[tuple[T]]:
        def combinations_iter(lst: list[T], num_of_items: int) -> Generator[tuple[T]]:
            if len(lst) == 0:
                return
            
            if num_of_items == 0:
                yield ()
                return
            
            head, *tail = lst
            yield from ((head,) + combo for combo in combinations_iter(lst, num_of_items - 1))
            yield from combinations_iter(tail, num_of_items)
        
        return list(combinations_iter(lst, num_of_items))
    ```

=== "Direct"
    ```python
    from itertools import combinations_with_replacement
    
    def combinations_with_replacement_v4[T](lst: list[T], num_of_items: int) -> list[tuple[T]]:
        return list(combinations_with_replacement(lst, num_of_items))
    ```