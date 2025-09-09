---
tags:
    - List
    - Intermediate 
---

# Permutations with replacement

Generate the permutations of K objects from the N elements of a list. Repeats are allowed. 


=== "Test"
    ```python
    def test_permutations_with_replacement(solution):
        assert set(solution([1], 2)) == set(product([1], repeat=2))
        assert set(solution([1, 2], 2)) == set(product([1, 2], repeat=2))
        assert set(solution([1, 2, 3, 4], 0)) == set(product([1, 2, 3, 4], repeat=0))
        assert set(solution([1, 2, 3, 4], 1)) == set(product([1, 2, 3, 4], repeat=1))
        assert set(solution([1, 2, 3, 4], 2)) == set(product([1, 2, 3, 4], repeat=2))
        assert set(solution([1, 2, 3, 4, 5], 3)) == set(product([1, 2, 3, 4, 5], repeat=3))
        assert set(solution([1, 2, 3, 4, 5, 6], 4)) == set(product([1, 2, 3, 4, 5, 6], repeat=4))
        assert set(solution([1, 2, 3, 4, 5], 6)) == set(product([1, 2, 3, 4, 5], repeat=6))
        assert set(solution(['a', 'b', 'c', 'd'], 3)) == set(product(['a', 'b', 'c', 'd'], repeat=3))
        assert set(solution(['a', 'b', 'c', 'd'], 10)) == set(product(['a', 'b', 'c', 'd'], repeat=10))
    ```

=== "Recursive"
    ```python
    def permutations_with_replacement_v1[T](lst: list[T], num_of_items: int) -> list[tuple[T]]:
        if len(lst) == 0: return []
        if num_of_items == 0: return [()]

        valid_selections = []

        def aux(selection: tuple[T]):
            if len(selection) == num_of_items:
                valid_selections.append(selection)
                return
            
            for val in lst:
                aux(selection + (val,))
        
        aux(())
        return valid_selections
    ```


=== "BFS"
    ```python
    from collections import deque

    def permutations_with_replacements_v2[T](lst: list[T], num_of_items: int) -> list[tuple[T]]:
        if len(lst) == 0: return []
        if num_of_items == 0: return [()]

        valid_selections = []
        nodes = deque([()])

        while nodes:
            selected = nodes.popleft()

            for val in lst:
                new_selected = selected + (val,)

                if len(new_selected) == num_of_items:
                    valid_selections.append(new_selected)
                else:
                    nodes.append(new_selected)
        
        return valid_selections
    ```


=== "Generator/Recursive"
    ```python
    from typing import Generator

    def permutations_with_replacements_v3[T](lst: list[T], num_of_items: int) -> list[tuple[T]]:
        def permutations_iter(lst: list[T], num_of_items: int) -> Generator[tuple[T]]:
            if len(lst) == 0:
                return

            if num_of_items == 0:
                yield ()
                return

            yield from ((val,) + perm
                        for val in lst
                        for perm in permutations_iter(lst, num_of_items - 1))
        
        return list(permutations_iter(lst, num_of_items))
    ```


=== "Direct"
    ```python
    from itertools import product
    
    def permutations_with_replacements_v4[T](lst: list[T], num_of_items: int) -> list[tuple[T]]:
        return list(product(lst, repeat=num_of_items))
    ```