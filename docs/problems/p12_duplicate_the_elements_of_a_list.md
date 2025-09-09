---
tags:
    - List
    - Beginner
---

# Duplicate the Elements of a List

Duplicate the elements of a list.

=== "Test"
    ```python
    def test_duplicate_elements(solution):
        assert solution([]) == []
        assert solution([1]) == [1, 1]
        
        assert solution([1, 2, 3]) == [1, 1, 2, 2, 3, 3]
        assert solution([1, 2, 2]) == [1, 1, 2, 2, 2, 2]

        assert solution(['a', 'b', 'b', 'c', 'c', 'd', 'a', 'd']) == \
            ['a', 'a', 
             'b', 'b', 'b', 'b', 
             'c', 'c', 'c', 'c', 
             'd', 'd',
             'a', 'a',
             'd', 'd']
    ```

=== "Recursive"
    ```python
    def duplicate_elements_v1[T](lst: list[T]) -> list[T]:
        match lst:
            case []: return []
            case [head, *tail]: return [head, head] + duplicate_elements_v1(lst[1:])
    ```

=== "Map/Sum"
    ```python
    def duplicate_elements_v2[T](lst: list[T]) -> list[T]:
        return sum(map(lambda x: [x, x], lst), [])
    ```

=== "Zip"
    ```python
    from itertools import chain

    def duplicate_elements_v3[T](lst: list[T]) -> list[T]:
        return list(chain(*zip(lst, lst)))
    ```

=== "Reduce"
    ```python
    from functools import reduce

    def duplicate_elements_v4[T](lst: list[T]) -> list[T]:
        return reduce(lambda l, r: l + [r, r], lst, [])
    ```

=== "Comprehension"
    ```python
    def duplicate_elements_v5[T](lst: list[T]) -> list[T]:
        return [elem for elem in lst 
                     for _ in range(2)]
    ```