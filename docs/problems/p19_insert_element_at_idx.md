---
tags:
    - List
    - Beginner
---

# Insert an Element at a Given Position Into a List

Start counting list elements with 0. Insert the element at the __index__.

If __index__ >= length of the list, add to the end. Otherwise, return the list unchanged. 

=== "Test"
    ```python
    def test_insert_element(solution):
        elem = 42

        assert solution([], elem, 0) == [elem]
        assert solution([], elem, 1) == [elem]
        assert solution([], elem, 5) == [elem]
        
        assert solution([1], elem, 0) == [elem, 1]
        assert solution([1], elem, 1) == [1, elem]
        assert solution([1], elem, 100) == [1, elem]
        assert solution([1], elem, -37) == [1]
        
        assert solution([1, 2, 3], elem, 0) == [elem, 1, 2, 3]
        assert solution([1, 2, 3], elem, 1) == [1, elem, 2, 3]
        assert solution([1, 2, 3], elem, 2) == [1, 2, elem, 3]
        assert solution([1, 2, 3], elem, 3) == [1, 2, 3, elem]
        assert solution([1, 2, 3], elem, 4) == [1, 2, 3, elem]
        assert solution([1, 2, 3], elem, -44) == [1, 2, 3]

        elem = '42'

        assert solution(['a', 'b', 'b', 'c', 'c', 'd', 'a', 'd'], elem, 4) == \
            ['a', 'b', 'b', 'c', elem, 'c', 'd', 'a', 'd']
    ```

=== "Recursive"
    ```python
    def insert_element_v1[T](lst: list[T], value: T, insert_at: int) -> list[T]:
        def aux(accumulated: list[T], current_index: int) -> list[T]:
            at_insert_indx = current_index == insert_at
            reached_end = current_index >= len(lst)

            match (at_insert_indx, reached_end):
                case (_, True): 
                    return accumulated
                    
                case (True, _): 
                    return aux(accumulated + [value, lst[current_index]],
                               current_index + 1)

                case (False, _):
                    return aux(accumulated + [lst[current_index]], 
                               current_index + 1)
        
        if insert_at >= len(lst) or lst == []: return lst + [value]
        elif insert_at < 0: return lst
        else: return aux([], 0)
    ```

=== "Direct"
    ```python
    def insert_element_v2[T](lst: list[T], value: T, insert_at: int) -> list[T]:
        if insert_at > len(lst): 
            return lst + [value]
        elif insert_at < 0: 
            return lst
        else:
            lst.insert(insert_at, value)
            return lst
    ```

=== "Slice"
    ```python
    def insert_element_v3[T](lst: list[T], value: T, insert_at: int) -> list[T]:
        if insert_at < 0: return lst
        else: return lst[:insert_at] + [value] + lst[insert_at:]
    ```