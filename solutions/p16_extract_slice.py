# Given two indices, i and k, the slice is the list containing the elements
# between the ith and kth element of the original list (inclusive)
# *No negative slices

from itertools import repeat, compress, chain

def extract_slice_v1[T](lst: list[T], start: int, stop: int) -> list[T]:
    terminal_point = min(stop + 1, len(lst))
    
    def aux(accumlated: list[T], idx: int) -> list[T]:
        match (start <= idx <= stop, idx >= terminal_point):
            case (_, True): return accumlated
            case (False, _): return aux(accumlated, idx + 1)
            case (True, _): return aux(accumlated + [lst[idx]], idx + 1)
    
    return aux([], 0)


def extract_slice_v2[T](lst: list[T], start: int, stop: int) -> list[T]:
    return lst[start:stop+1]


def extract_slice_v3[T](lst: list[T], start: int, stop: int) -> list[T]:
    return list(elem 
                for idx, elem in enumerate(lst) 
                if start <= idx <= stop)
    

def extract_slice_v4[T](lst: list[T], start: int, stop: int) -> list[T]:
    falses_at_start = repeat(False, start)
    trues_for_slice = repeat(True, stop - start + 1)
    mask = chain(falses_at_start, trues_for_slice)
    return list(compress(lst, mask))