---
tags:
    - List
    - Intermediate
---

# Replicate the Elements of a List a Given Number of Times

Replicate the elements of a list a given number of times.

=== "Test"
    ```python
    def test_replicate_elements(solution):
        assert solution([], 0) == []
        assert solution([], 5) == []
        
        assert solution([1], 0) == []
        assert solution([1], 1) == [1]
        assert solution([1], 3) == [1, 1, 1]
        
        assert solution([1, 2, 3], 0) == []
        assert solution([1, 2, 2], 1) == [1, 2, 2]
        assert solution([1, 2, 2], 3) == [1, 1, 1, 2, 2, 2, 2, 2, 2]

        assert solution(['a', 'b', 'b', 'c', 'c', 'd', 'a', 'd'], 4) == \
            ['a', 'a', 'a', 'a',
            'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b',
            'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c',
            'd', 'd', 'd', 'd',
            'a', 'a', 'a', 'a',
            'd', 'd', 'd', 'd']
    ```

=== "Recursive"
    ```python
    def replicate_elements_v1[T](lst: list[T], times: int) -> list[T]:
        match (lst, times):
            case ([], _) | (_, 0): 
                return []
            case (_, 1): 
                return lst
            case ([head, *tail], times): 
                return ([head] * times) + replicate_elements_v1(tail, times)
    ```

=== "Matrix Like"
    ```python
    from itertools import chain, repeat

    def replicate_elements_v2[T](lst: list[T], times: int) -> list[T]:
        return list(chain(*zip(*repeat(lst, times))))
    ```

=== "Chain/Repeat"
    ```python
    from itertools import chain

    def replicate_elements_v3[T](lst: list[T], times: int) -> list[T]:
        return list(chain(*(repeat(elem, times) for elem in lst)))
    ```

=== "Reduce"
    ```python
    from functools import reduce
    
    def replicate_elements_v4[T](lst: list[T], times: int) -> list[T]:
        return reduce(lambda l, r: l + [r] * times, lst, [])
    ```

=== "Comprehension"
    ```python
    def replicate_elements_v5[T](lst: list[T], times: int) -> list[T]:
        return [elem for elem in lst 
                     for _ in range(times)]
    ```