# Encode list using RLE (run length encoding)
# [(elem1, # of consecutive terms), (elem2, # of consecutive terms), ...]

from functools import reduce
from itertools import groupby
from collections import namedtuple

RleTerm = namedtuple("RleTerm", ["elem", "count"])


def rle_encode_v1[T](lst: list[T]) -> list[RleTerm]:
    def aux(working_list: list[T], encoding: list[RleTerm]) -> list[RleTerm]:
        match working_list:
            case []: 
                return encoding
            
            case [head, *tail] if (last_term := encoding[-1]).elem == head:
                updated_term = RleTerm(last_term.elem, last_term.count + 1)
                encoding[-1] = updated_term
                return aux(tail, encoding)
            
            case [head, *tail]:
                encoding.append(RleTerm(head, 1))
                return aux(tail, encoding)

    if len(lst) == 0: return []
    return aux(lst[1:], [RleTerm(lst[0], 1)])


def rle_encode_v2[T](lst: list[T]) -> list[RleTerm]:
    def helper(left: list[RleTerm], right: T) -> list[RleTerm]:
        match left[-1]:
            case RleTerm(item, count) if item == right:
                left[-1] = RleTerm(item, count + 1)

            case _:
                left.append(RleTerm(right, 1))

        return left
    
    if len(lst) == 0: return []
    return reduce(helper, lst[1:], [RleTerm(lst[0], 1)])


def rle_encode_v3[T](lst: list[T]) -> list[RleTerm]:
    return [RleTerm(key, len(list(group))) 
            for key, group in groupby(lst)]