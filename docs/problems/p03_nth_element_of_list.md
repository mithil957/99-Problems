---
tags:
    - List
    - Beginner
---

# Nth Element of a List

Find the Nth element of a list.

=== "Test"
    ```python
    def test_nth_element_of_list(solution):
        assert solution([], 5) is None
        assert solution([1], 5) is None
        assert solution([1], 0) is 1
        assert solution([1, 2, 3], 2) == 3
        assert solution(['a', 'b', 'c', 'd'], 2) == 'c'
        assert solution(['a', 'b', 'c', 'd'], 89) is None
    ```

=== "Recursive"
    ```python
    def nth_element_of_list_v1[T](lst: list[T], n: int) -> T | None:
        match (lst, n):
            case ([], _): return None
            case ([a, *tail], 0): return a
            case _: return nth_element_of_list_v1(lst[1:], n - 1)
    ```

=== "Direct"
    ```python
    def nth_element_of_list_v2[T](lst: list[T], n: int) -> T | None:
        match 0 <= n < len(lst):
            case True: return lst[n]
            case False: return None
    ```