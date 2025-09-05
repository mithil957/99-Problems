# Encode list using RLE (run length encoding)
# [(elem1, # of consecutive terms), (elem2, # of consecutive terms), ...]

from functools import reduce
from itertools import groupby

type RleTerm[T] = tuple[T, int]

def rle_encode_v1[T](lst: list[T]) -> list[RleTerm]:
    def aux(working_list: list[T], groups: list[list[T]]) -> list[list[T]]:
        match working_list:
            case []: 
                return groups
            
            case [first, *tail] if first == groups[-1][0]:
                groups[-1].append(first)
                return aux(working_list[1:], groups)
            
            case [first, *tail]:
                groups.append([first])
                return aux(working_list[1:], groups)
    
    if len(lst) == 0: return []
    groups = aux(lst[1:], [[lst[0]]])
    return [(group[0], len(group)) for group in groups]


def rle_encode_v2[T](lst: list[T]) -> list[RleTerm]:
    def helper(left: list[RleTerm], right: T) -> list[RleTerm]:
        match left[-1]:
            case (item, count) if item == right:
                left[-1] = (item, count + 1)
            case _:
                left.append((right, 1))

        return left
    
    if len(lst) == 0: return []
    return reduce(helper, lst[1:], [(lst[0], 1)])


def rle_encode_v3[T](lst: list[T]) -> list[RleTerm]:
    return [(key, len(list(group))) 
            for key, group in groupby(lst)]