---
tags:
    - List
    - Intermediate
---

# Drop Every Nth Element From a List

Drop every Nth element from a list. If N is 2, then every second element should be dropped.

=== "Test"
    ```python
    def test_drop_every_nth_element(solution):
        assert solution([], 0) == []
        assert solution([], 5) == []
        
        assert solution([1], 0) == [1]
        assert solution([1], 1) == []
        assert solution([1], 3) == [1]
        
        assert solution([1, 2, 3], 0) == [1, 2, 3]
        assert solution([1, 2, 2], 1) == []
        assert solution([1, 2, 2], 3) == [1, 2]

        assert solution(['a', 'b', 'b', 'c', 'c', 'd', 'a', 'd'], 4) == \
            ['a', 'b', 'b', 'c', 'd', 'a']
    ```

=== "Recursive"
    ```python
    def drop_every_nth_element_v1[T](lst: list[T], n: int) -> list[T]:
        if n == 0: 
            return lst

        def aux(left: tuple[list[T], int], right: T) -> tuple[list[T], int]:
            acummulated, index_tracker = left
            if index_tracker % n != 0: 
                acummulated.append(right)
            return (acummulated, index_tracker + 1)

        acummulated, _ = reduce(aux, lst, ([], 1))
        return acummulated
    ```

=== "Generator/Comprehension"
    ```python
    def drop_every_nth_element_v2[T](lst: list[T], n: int) -> list[T]:
        if n == 0: 
            return lst
        
        generator_exp = (value 
                         for idx, value in enumerate(lst, 1)
                         if idx % n != 0)
        
        return list(generator_exp)
    ```

=== "Chain"
    ```python
    from itertools import chain

    def drop_every_nth_element_v3[T](lst: list[T], n: int) -> list[T]:
        if n == 0:
            return lst
        
        step = n
        return list(chain.from_iterable(
            lst[idx: idx + step - 1] 
            for idx in range(0, len(lst), step)
        ))
    ```

=== "Mask"
    ```python
    from itertools import compress, cycle

    def drop_every_nth_element_v4[T](lst: list[T], n: int) -> list[T]:
        if n == 0:
            return lst
        
        mask = [True] * (n - 1) + [False]
        repeated_mask = cycle(mask)
        return list(compress(lst, repeated_mask))
    ```