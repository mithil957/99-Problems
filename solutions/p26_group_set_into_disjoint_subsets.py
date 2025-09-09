# Ordered Partitions
# Group the elements of a set into disjoint sets
# Given elements and the group sizes, generate all the possible list of groups

from itertools import combinations
from collections import deque
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