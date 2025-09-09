---
tags:
  - List
  - Beginner
---

# Tail of a List

Write a function that returns the last element of a list.



=== "Test"
    ```python 
    def test_tail_of_list(solution):
        assert solution([]) is None
        assert solution([1]) == 1
        assert solution([1, 2, 3]) == 3
        assert solution(['a', 'b', 'c']) == 'c'
    ```

=== "Pattern Matching"
    ```python
    def tail_of_list_v1[T](lst: list[T]) -> T | None:
        match lst:
            case []: return None
            case [a]: return a
            case [*front, last]: return last
    ```

=== "Recursive"
    ```python
    def tail_of_list_v2[T](lst: list[T]) -> T | None:
        match lst:
            case []: return None
            case [a]: return a
            case [head, *tail]: return tail_of_list_v2(tail)
    ```
=== "Direct"
    ```python
    def tail_of_list_v3[T](lst: list[T]) -> T | None:
        return lst[-1] if len(lst) > 0 else None
    ```