---
tags:
    - List
    - Beginner
---

# Reverse a List

Reverse a list.

=== "Test"
    ```python
    def test_reverse_a_list(solution):
        assert solution([]) == []
        assert solution([1]) == [1]
        assert solution([1, 2, 3]) == [3, 2, 1]
        assert solution(['a', 'b', 'c', 'd']) == ['d', 'c', 'b', 'a']
    ```

=== "Direct"
    ```python
    def reverse_list_v1[T](lst: list[T]) -> list[T]:
        return lst[::-1]
    ```

=== "Recursive"
    ```python
    def reverse_list_v2[T](lst: list[T]) -> list[T]:
        match lst:
            case []: return []
            case [a]: return [a]
            case [head, *tail]: return reverse_list_v2(tail) + [head]
    ```

=== "Tail Recursive"
    ```python
    def reverse_list_v3[T](lst: list[T]) -> list[T]:
        def aux(current_lst: list[T], accumlated: list[T]) -> list[T]:
            match current_lst:
                case []: return accumlated
                case [a]: return accumlated + [a]
                case [head, *tail]: return aux(tail, accumlated + [head])
        
        return aux(lst, [])
    ```
