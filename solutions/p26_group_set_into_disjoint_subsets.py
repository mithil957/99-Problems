# Ordered Partitions
# Group the elements of a set into disjoint sets
# Given elements and the group sizes, generate all the possible list of groups

from itertools import combinations
from collections import deque
from collections.abc import Iterator

type Partition[T] = list[tuple[T]] # Ex. [1,2,3,4] -> [(1,2), (3), (4)]

def generate_ordered_partitions_v1[T](lst: list[T], group_sizes: list[int]) -> list[Partition]:
    def disjoint_subsets_iter(lst: list[T], group_sizes: list[int]) -> Iterator[Partition]:
        if len(group_sizes) == 0 or group_sizes[0] > len(lst):
            yield [] 
            return
        
        yield from ([combo] + partition
                    for combo in combinations(lst, group_sizes[0])
                    for partition in disjoint_subsets_iter(set(lst) - set(combo), group_sizes[1:]))
    
    return list(disjoint_subsets_iter(lst, group_sizes))


def generate_ordered_partitions_v2[T](lst: list[T], group_sizes: list[int]) -> list[Partition]:
    valid_partitions = []
    nodes = deque([(lst, 0, [])])

    while nodes:
        remaining_choices, group_size_idx, partition = nodes.popleft()

        for combo in combinations(remaining_choices, group_sizes[group_size_idx]):
            new_remaining_choices = set(remaining_choices) - set(combo)
            next_group_size_idx = group_size_idx + 1
            updated_partition = partition + [combo]

            if next_group_size_idx >= len(group_sizes):
                valid_partitions.append(updated_partition)

            elif len(new_remaining_choices) >= group_sizes[next_group_size_idx]:
                nodes.append([new_remaining_choices, next_group_size_idx, updated_partition])
    
    return valid_partitions