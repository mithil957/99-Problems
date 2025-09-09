---
tags:
    - List
    - Beginner
---

# Last Two Elements of a List

Find the last two elements of a list.

=== "Test"
    ```python
    def test_last_two_elements_of_a_list(solution):
        assert solution([]) is None
        assert solution([1]) is None
        assert solution([1, 2, 3]) == (2, 3)
        assert solution(['a', 'b', 'c', 'd']) == ('c', 'd')
    ```

=== "Pattern Matching"
    ```python
    def last_two_elements_of_a_list_v1[T](lst: list[T]) -> tuple[T, T] | None:
        match lst:
            case [] | [_]: return None
            case [a, b]: return (a, b)
            case [*front, penultimate, last]: return (penultimate, last)
    ```

=== "Recursive"
    ```python
    def last_two_elements_of_a_list_v2[T](lst: list[T]) -> tuple[T, T] | None:
        match lst:
            case [] | [_]: return None
            case [a, b]: return (a, b)
            case _: return last_two_elements_of_a_list_v2(lst[1:])
    ```

=== "Direct"
    ```python
    def last_two_elements_of_a_list_v3[T](lst: list[T]) -> tuple[T, T] | None:
        return (lst[-2], lst[-1]) if len(lst) >= 2 else None
    ```