---
tags:
    - List
    - Beginner
---

# Remove the Kth Element From a List

Remove the kth element from a list and return the list. Out of bounds index returns the list with no changes.

=== "Test"
    ```python
    def test_remove_kth_element(solution):
        assert solution([], 0) == []
        assert solution([], 1) == []
        assert solution([], 5) == []
        
        assert solution([1], 0) == []
        assert solution([1], 1) == [1]
        assert solution([1], 100) == [1]
        
        assert solution([1, 2, 3], 0) == [2, 3]
        assert solution([1, 2, 3], 1) == [1, 3]
        assert solution([1, 2, 3], 2) == [1, 2]
        assert solution([1, 2, 3], 3) == [1, 2, 3]
        assert solution([1, 2, 3], 4) == [1, 2, 3]

        assert solution(['a', 'b', 'b', 'c', 'c', 'd', 'a', 'd'], 4) == \
            ['a', 'b', 'b', 'c', 'd', 'a', 'd']
    ```

=== "Recursive"
    ```python
    def remove_kth_element_v1[T](lst: list[T], remove_at: int) -> list[T]:
        def aux(working_lst: list[T], current_idx: int) -> list[T]:
            match (current_idx == remove_at, current_idx >= len(lst)):
                case (_, True): 
                    return working_lst
                case (True, _): 
                    return aux(working_lst, current_idx + 1)
                case (False, _): 
                    return aux(working_lst + [lst[current_idx]], current_idx + 1)
                
        return aux([], 0) if 0 <= remove_at < len(lst) else lst
    ```

=== "Direct"
    ```python
    def remove_kth_element_v2[T](lst: list[T], remove_at: int) -> list[T]:
        if 0 <= remove_at < len(lst): 
            lst.pop(remove_at)
        return lst
    ```

=== "Comprehension"
    ```python
    def remove_kth_element_v3[T](lst: list[T], remove_at: int) -> list[T]:
        return [elem for idx, elem in enumerate(lst) if idx != remove_at]
    ```

=== "Slice"
    ```python
    def remove_kth_element_v4[T](lst: list[T], remove_at: int) -> list[T]:
        if 0 <= remove_at < len(lst): 
            return lst[:remove_at] + lst[remove_at+1:]
        return lst
    ```