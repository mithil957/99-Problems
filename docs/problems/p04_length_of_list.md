---
tags:
    - List
    - Beginner
---

# Length of a List

Find the number of elements in a list.

=== "Test"
    ```python
    def test_length_of_list(solution):
        assert solution([]) == 0
        assert solution([1]) == 1
        assert solution([1, 2, 3]) == 3
        assert solution(['a', 'b', 'c', 'd']) == 4
    ```

=== "Direct"
    ```python
    def number_of_elements_in_list_v1[T](lst: list[T]) -> int:
        return len(lst)
    ```

=== "Recursive"
    ```python
    def number_of_elements_in_list_v2[T](lst: list[T]) -> int:
        match lst:
            case []: return 0
            case [a]: return 1
            case [a, *tail]: return 1 + number_of_elements_in_list_v2(tail)
    ```

=== "Tail Recursive"
    ```python
    def number_of_elements_in_list_v3[T](lst: list[T]) -> int:
        def aux(current_lst: list[T], accumulated: int) -> int:
            match current_lst:
                case []: return accumulated
                case [a]: return 1 + accumulated
                case [a, *tail]: return aux(tail, accumulated + 1)
        
        return aux(lst, 0)
    ```