---
tags:
    - List
    - Beginner
---

# Split a List Into Two Parts

Split a list into two parts. The lenght of the first part is given. If the length of the first part is longer than the entire list, then the first part is the list and the second list is empty.

=== "Test"
    ```python
    def test_split_list(solution):
        assert solution([], 0) == ([], [])
        assert solution([], 5) == ([], [])
        
        assert solution([1], 0) == ([], [1])
        assert solution([1], 1) == ([1], [])
        assert solution([1], 3) == ([1], [])
        
        assert solution([1, 2, 3], 0) == ([], [1, 2, 3])
        assert solution([1, 2, 2], 1) == ([1], [2, 2])
        assert solution([1, 2, 2], 3) == ([1, 2, 2], [])

        assert solution(['a', 'b', 'b', 'c', 'c', 'd', 'a', 'd'], 4) == \
            (['a', 'b', 'b', 'c'], ['c', 'd', 'a', 'd'])
    ```

=== "Recursive"
    ```python
    def split_list_v1[T](lst: list[T], split_point: int) -> tuple[list[T], list[T]]:
        def aux[T](p1: list[T], p2:list[T], idx: int) -> tuple[list[T], list[T]]:
            match (idx < split_point, idx >= len(lst)):
                case (_, True): 
                    return p1, p2
                case (True, _): 
                    return aux(p1 + [lst[idx]], p2, idx + 1)
                case (False, _): 
                    return aux(p1, p2 + [lst[idx]], idx + 1)
        
        return aux([], [], 0)
    ```

=== "Slice"
    ```python
    def split_list_v2[T](lst: list[T], split_point: int) -> tuple[list[T], list[T]]:
        return lst[:split_point], lst[split_point:]
    ```

=== "Iterative"
    ```python
    def split_list_v3[T](lst: list[T], split_point: int) -> tuple[list[T], list[T]]:
        p1, p2 = [], []
        for idx, value in enumerate(lst, 1):
            if idx <= split_point: p1.append(value)
            else: p2.append(value)
        
        return p1, p2
    ```


=== "islice"
    ```python
    def split_list_v4[T](lst: list[T], split_point: int) -> tuple[list[T], list[T]]:
        p1 = islice(lst, split_point)
        p2 = islice(lst, split_point, None)
        return list(p1), list(p2)
    ```

=== "Deque"
    ```python
    def split_list_v5[T](lst: list[T], split_point: int) -> tuple[list[T], list[T]]:
        split_point = min(split_point, len(lst))
        queue = deque(lst)

        p1 = [queue.popleft() for _ in range(split_point)]
        p2 = list(queue)
        return p1, p2
    ```