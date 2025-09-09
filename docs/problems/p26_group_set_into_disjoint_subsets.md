---
tags:
    - List
    - Intermediate
---

# Ordered Partitions

Group the elements of a set into disjoint subsets. Given elements and the group sizes, generate all possible groups.


=== "Test"
    ```python
    def test_disjoint_subsets(solution):
        assert len(solution(['a','b', 'c', 'd'], [2, 1])) == len([
            [("a", "b"), ("c")], [("a", "c"),("b")], [("b", "c"), ("a")],
            [("a", "b"), ("d")], [("a", "c"),("d")], [("b", "c"), ("d")],
            [("a", "d"), ("b")], [("b", "d"),("a")], [("a", "d"), ("c")],
            [("b", "d"), ("c")], [("c", "d"),("a")], [("c", "d"), ("b")]
        ])

        assert len(solution(['a','b', 'b'], [2, 1])) == len([
            [("a", "b"), ("b")], [("a", "b"),("b")], [("b", "b"), ("a")],
        ])

        assert len(solution([1, 2, 3, 4, 5], [1, 3, 1])) == len([
            [(1), (2, 3, 4), (5)], [(1), (2, 3, 5), (4)], [(1), (2, 4, 5), (3)], [(1), (3, 4, 5), (2)],
            [(2), (1, 3, 4), (5)], [(2), (1, 3, 5), (4)], [(2), (1, 4, 5), (3)], [(2), (3, 4, 5), (1)],
            [(3), (1, 2, 4), (5)], [(3), (1, 2, 5), (4)], [(3), (1, 4, 5), (2)], [(3), (2, 4, 5), (1)],
            [(4), (1, 2, 3), (5)], [(4), (1, 2, 5), (3)], [(4), (1, 3, 5), (2)], [(4), (2, 3, 5), (1)],
            [(5), (1, 2, 3), (4)], [(5), (1, 2, 4), (3)], [(5), (1, 3, 4), (2)], [(5), (2, 3, 4), (1)]
        ])

        assert len(solution(['a', 'b', 'c', 'd'], [2, 2])) == len([
            [('a', 'b'), ('c', 'd')],
            [('a', 'c'), ('b', 'd')],
            [('a', 'd'), ('b', 'c')],
            [('b', 'c'), ('a', 'd')],
            [('b', 'd'), ('a', 'c')],
            [('c', 'd'), ('a', 'b')]
        ])
    ```

=== "Generator/Recursive"
    ```python
    from itertools import combinations
    from typing import Generator

    type Partition[T] = list[tuple[T]] # Ex. [1,2,3,4] -> [(1,2), (3), (4)]

    def generate_ordered_partitions_v1[T](lst: list[T], group_sizes: list[int]) -> list[Partition]:
        def disjoint_subsets_iter(remaining_idxs: list[int], group_sizes: list[int]) -> Generator[Partition]:
            if len(group_sizes) == 0:
                yield [] 
                return
            
            if group_sizes[0] > len(lst):
                return
            
            yield from ([tuple(lst[selected] for selected in combo_idxs)] + partition
                        for combo_idxs in combinations(remaining_idxs, group_sizes[0])
                        for partition in disjoint_subsets_iter(remaining_idxs - set(combo_idxs), group_sizes[1:]))
        
        idxs = set(range(len(lst)))
        return list(disjoint_subsets_iter(idxs, group_sizes))
    ```

=== "BFS"
    ```python
    from itertools import combinations
    from collections import deque

    type Partition[T] = list[tuple[T]] # Ex. [1,2,3,4] -> [(1,2), (3), (4)]

    def generate_ordered_partitions_v2[T](lst: list[T], group_sizes: list[int]) -> list[Partition]:
        valid_partitions = []
        idxs = set(range(len(lst)))
        nodes = deque([(idxs, 0, [])])

        while nodes:
            remaining_idxs, group_size_idx, partition = nodes.popleft()

            for combo_idxs in combinations(remaining_idxs, group_sizes[group_size_idx]):
                new_remaining_idxs = remaining_idxs - set(combo_idxs)
                next_group_size_idx = group_size_idx + 1
                updated_partition = partition + [tuple(lst[selected] for selected in combo_idxs)]

                if next_group_size_idx >= len(group_sizes):
                    valid_partitions.append(updated_partition)

                elif len(new_remaining_idxs) >= group_sizes[next_group_size_idx]:
                    nodes.append((new_remaining_idxs, next_group_size_idx, updated_partition))
        
        return valid_partitions
    ```