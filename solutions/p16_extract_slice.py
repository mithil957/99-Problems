# Given two indices, i and k, the slice is the list containing the elements
# between the ith and kth element of the original list (inclusive)
# *No negative slices


def extract_slice_v1[T](lst: list[T], start: int, stop: int) -> list[T]:
    def aux(accumlated: list[T], idx: int) -> list[T]:
        match (start <= idx <= stop, idx >= len(lst)):
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
    
    