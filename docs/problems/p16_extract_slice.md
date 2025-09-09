---
tags:
    - List
    - Intermediate
---

# Extract a Slice From a List

Given two indices, i and k, the slice is the list containing the elements between the ith and kth element of the original list (inclusive). No negative slices.

=== "Test"
    ```python
    def test_extract_slice(solution):
        assert solution([], 0, 0) == []
        assert solution([], 0, 1) == []
        assert solution([], 0, 5) == []
        assert solution([], 3, 5) == []
        
        assert solution([1], 0, 0) == [1]
        assert solution([1], 0, 1) == [1]
        assert solution([1], 1, 1) == []
        assert solution([1], 0, 5) == [1]
        assert solution([1], 3, 5) == []
        
        assert solution([1, 2, 3], 0, 0) == [1]
        assert solution([1, 2, 3], 0, 1) == [1, 2]
        assert solution([1, 2, 3], 0, 2) == [1, 2, 3]
        assert solution([1, 2, 3], 1, 2) == [2, 3]
        assert solution([1, 2, 3], 2, 3) == [3]
        assert solution([1, 2, 3], 4, 7) == []

        assert solution(['a', 'b', 'b', 'c', 'c', 'd', 'a', 'd'], 4, 6) == \
            ['c', 'd', 'a']
    ```

=== "Recursive"
    ```python
    def extract_slice_v1[T](lst: list[T], start: int, stop: int) -> list[T]:
        terminal_point = min(stop + 1, len(lst))
        
        def aux(accumlated: list[T], idx: int) -> list[T]:
            match (start <= idx <= stop, idx >= terminal_point):
                case (_, True): return accumlated
                case (False, _): return aux(accumlated, idx + 1)
                case (True, _): return aux(accumlated + [lst[idx]], idx + 1)
        
        return aux([], 0)
    ```


=== "Slice"
    ```python
    def extract_slice_v2[T](lst: list[T], start: int, stop: int) -> list[T]:
        return lst[start:stop+1]
    ```

=== "Comprehension"
    ```python
    def extract_slice_v3[T](lst: list[T], start: int, stop: int) -> list[T]:
        return list(elem 
                    for idx, elem in enumerate(lst) 
                    if start <= idx <= stop)
    ```

=== "Mask"
    ```python
    from itertools import repeat, compress, chain

    def extract_slice_v4[T](lst: list[T], start: int, stop: int) -> list[T]:
        falses_at_start = repeat(False, start)
        trues_for_slice = repeat(True, stop - start + 1)
        mask = chain(falses_at_start, trues_for_slice)
        return list(compress(lst, mask))
    ```