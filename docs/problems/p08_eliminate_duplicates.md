---
tags:
    - List
    - Intermediate
---

# Eliminate Duplicates

Eliminate consecutive duplicates of list elements.

=== "Test"
    ```python
    def test_eliminate_duplicates(solution):
        assert solution([]) == []
        assert solution([1]) == [1]
        
        assert solution([1, 2, 3]) == [1, 2, 3]
        assert solution([1, 1, 2]) == [1, 2]
        assert solution([1, 2, 2]) == [1, 2]

        assert solution(['a', 'b', 'b', 'c', 'c', 'd', 'a', 'd']) == ['a', 'b', 'c', 'd', 'a', 'd']
    ```

=== "Recursive"
    ```python
    def eliminate_consecutive_duplicates_v1[T](lst: list[T]) -> list[T]:
        match lst:
            case []: return []
            case [a]: return [a]
            case [a, b, *tail]:
                if a != b: 
                    return [a] + eliminate_consecutive_duplicates_v1(lst[1:])
                else: 
                    return eliminate_consecutive_duplicates_v1(lst[1:])

    ```

=== "Iterative"
    ```python
    from copy import deepcopy

    def eliminate_consecutive_duplicates_v2[T](lst: list[T]) -> list[T]:
        accumulated: list[T] = []
        working_list: list[T] = deepcopy(lst)
        
        while working_list:
            match working_list:
                case []: 
                    return accumulated
                
                case [a]: 
                    return accumulated + [a]
                
                case [first, second, *body] if first == second: 
                    working_list.pop(0)

                case [first, second, *body]:
                    accumulated.append(first)
                    working_list.pop(0)
                    
        return accumulated
    ```

=== "Direct"
    ```python
    from itertools import groupby

    def eliminate_consecutive_duplicates_v3[T](lst: list[T]) -> list[T]:
        return [key for key, group in groupby(lst)]
    ```