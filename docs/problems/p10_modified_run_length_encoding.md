---
tags:
    - List
    - Beginner
---

# Modified Run-Length Encoding

RLE but for elements with 1 count just append the element only. 


=== "Test"
    ```python
    def test_modifed_run_length_encoding(solution):
        assert solution([]) == []
        assert solution([1]) == [1]
        
        assert solution([1, 2, 3]) == [1, 2, 3]
        assert solution([1, 1, 2]) == [(1, 2), 2]
        assert solution([1, 2, 2]) == [1, (2, 2)]

        assert solution(['a', 'b', 'b', 'c', 'c', 'd', 'a', 'd']) == \
            ['a', ('b', 2), ('c', 2), 'd', 'a', 'd']
    ```

=== "4fun/DSL"
    ```python
    from __future__ import annotations
    from functools import reduce

    type RleTerm[T] = tuple[T, int] | T

    class RleList:
        working_list: list[RleTerm]

        def __init__(self, init_element: RleTerm):
            self.working_list = [init_element]
        
        def __or__[T](self, value: T) -> RleList:
            match self.working_list[-1]:
                case (elem, count) if elem == value:
                    self.working_list[-1] = (elem, count + 1)
                case (elem, count):
                    self.working_list.append(value)
                
                case elem if elem == value:
                    self.working_list[-1] = (elem, 2)
                case elem:
                    self.working_list.append(value)
            
            return self
    
    def modded_rle_encode_v1[T](lst: list[T]) -> list[RleTerm]:
        if len(lst) == 0: return []
        return reduce(lambda l, r: l | r, 
                      lst[1:], 
                      RleList(lst[0])).working_list
    ```


=== "Direct"
    ```python
    
    from itertools import groupby
    
    type RleTerm[T] = tuple[T, int] | T

    def modded_rle_encode_v2[T](lst: list[T]) -> list[RleTerm]:
        def aux(key, group):
            if len(group) == 1: return key
            else: return (key, len(group))
        
        return [aux(key, list(group)) for key, group in groupby(lst)]
    ```