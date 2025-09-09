---
tags:
    - List
    - Intermediate
---

# Extract a Given Number of Randomly Selected Elements From a List

Select K items from a list and return them. If K is bigger than length of list, return None. The items should be unique, not allowed to select the same index twice.

<description>

=== "Test"
    ```python
    def test_extract_elements(solution):
        assert solution([1, 2, 3], 0) == []
        assert solution([1, 2, 3], 4) is None
        assert solution([1, 2, 3], 10) is None
        assert len(solution([1, 2, 3], 3)) == 3
        assert len(solution([1, 2, 3], 2)) == 2
    ```

=== "Sample"
    ```python
    from random import sample

    def extract_elements_v1[T](lst: list[T], k: int) -> list[T] | None:
        if k > len(lst): return None
        return sample(lst, k)
    ```

=== "Shuffle"
    ```python
    from random import shuffle

    def extract_elements_v2[T](lst: list[T], k: int) -> list[T] | None:
        if k > len(lst): return None
        copy_lst = lst[:]
        shuffle(copy_lst)
        return copy_lst[:k]
    ```