---
tags:
    - List
    - Intermediate
---

# Decode a Run-Length Encoded List

Given a run-length encoded list, construct its uncompressed version.

=== "Test"
    ```python
    def test_decode_rle_list(solution):
        assert solution([]) == []
        assert solution([1]) == [1]
        
        assert solution([1, 2, 3]) == [1, 2, 3]
        assert solution([(1, 2), 2]) == [1, 1, 2]
        assert solution([1, (2, 2)]) == [1, 2, 2]

        assert solution(['a', ('b', 2), ('c', 2), 'd', 'a', 'd']) == \
            ['a', 'b', 'b', 'c', 'c', 'd', 'a', 'd']
    ```

=== "Recursive"
    ```python
    type RleTerm[T] = tuple[T, int] | T 

    def decode_rle_list_v1[T](rle_lst: list[RleTerm]) -> list[T]:
        match rle_lst:
            case []: 
                return []
            case [(element, count), *tail]:
                return [element] * count + decode_rle_list_v1(rle_lst[1:])
            case [element, *tail]:
                return [element] + decode_rle_list_v1(rle_lst[1:])
    ```

=== "Generator"
    ```python
    from typing import Generator

    type RleTerm[T] = tuple[T, int] | T 

    def decode_rle_list_v2[T](rle_lst: list[RleTerm]) -> list[T]:
        def aux() -> Generator[T]:
            for term in rle_lst:
                match term:
                    case (element, count): yield from (element for _ in range(count))
                    case element: yield element
        
        return list(aux())
    ```