---
tags:
    - List
    - Beginner
---

# Create a List Containing All Integers Within a Given Range

Create a list containing all integers within a given range. If first argument is greater than second, produce a list in decreasing order. 

=== "Test"
    ```python
    def test_create_range(solution):
        assert solution(0, 0) == [0]
        assert solution(1, 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        assert solution(5, 3) == [5, 4, 3]
        assert solution(-2, 2) == [-2, -1, 0, 1, 2]
    ```

=== "Recursive"
    ```python
    def create_range_v1(start: int, end: int) -> list[int]:
        def aux(accumulated: list[int], direction: int, remaining: int) -> list[int]:
            if remaining == 0: 
                return accumulated
            else: 
                return aux(accumulated + [accumulated[-1] + direction], direction, remaining - 1)
        
        direction = 1 if end >= start else -1
        return aux([start], direction, abs(start - end))
    ```

=== "Direct"
    ```python
    def create_range_v2(start: int, end: int) -> list[int]:
        direction = 1 if end >= start else -1
        return list(range(start, end + direction, direction))
    ```

=== "Itertools"
    ```python
    from itertools import count, takewhile
    
    def create_range_v3(start: int, end: int) -> list[int]:
        if start <= end:
            direction = 1
            stop_condition = lambda x: x <= end
        else:
            direction = -1
            stop_condition = lambda x: x >= end
        
        counter = count(start, direction)
        bounded_counter = takewhile(stop_condition, counter)
        return list(bounded_counter)
    ```