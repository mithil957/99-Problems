---
tags:
    - List
    - Intermediate
---

# Rotate a List N Places to the Left

Rotate a list N places to the left. 


=== "Test"
    ```python
    def test_rotate_left(solution):
        assert solution([], 0) == []
        assert solution([], 1) == []
        assert solution([], 5) == []
        
        assert solution([1], 0) == [1]
        assert solution([1], 1) == [1]
        assert solution([1], 100) == [1]
        
        assert solution([1, 2, 3], 0) == [1, 2, 3]
        assert solution([1, 2, 3], 1) == [2, 3, 1]
        assert solution([1, 2, 3], 2) == [3, 1, 2]
        assert solution([1, 2, 3], 3) == [1, 2, 3]
        assert solution([1, 2, 3], 4) == [2, 3, 1]
        assert solution([1, 2, 3], 100) == [2, 3, 1]

        assert solution(['a', 'b', 'b', 'c', 'c', 'd', 'a', 'd'], 4) == \
            ['c', 'd', 'a', 'd', 'a', 'b', 'b', 'c']
    ```

=== "Recursive"
    ```python
    def rotate_left_v1[T](lst: list[T], times: int) -> list[T]:
        if len(lst) <= 1: return lst

        match times % len(lst):
            case 0: return lst
            case _: return rotate_left_v1(lst[1:] + lst[:1], times - 1)
    ```


=== "Slice"
    ```python
    def rotate_left_v2[T](lst: list[T], times: int) -> list[T]:
        if len(lst) <= 1: return lst
        times = times % len(lst)
        return lst[times:] + lst[:times]
    ```


=== "Chain"
    ```python
    from itertools import chain

    def rotate_left_v3[T](lst: list[T], times: int) -> list[T]:
        if len(lst) <= 1: return lst
        times = times % len(lst)
        path = chain(range(times, len(lst)), 
                     range(0, times))
        return [lst[idx] for idx in path]
    ```


=== "Deque"
    ```python
    from collections import deque

    def rotate_left_v4[T](lst: list[T], times: int) -> list[T]:
        d = deque(lst)
        d.rotate(-times)
        return list(d)
    ```