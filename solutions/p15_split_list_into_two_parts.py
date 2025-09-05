# Split a list into two parts, the length of the first part is given

from functools import reduce

def split_list_v1[T](lst: list[T], split_point: int) -> tuple[list[T], list[T]]:
    def aux[T](p1: list[T], p2:list[T], idx: int) -> tuple[list[T], list[T]]:
        match (idx <= split_point, idx > len(lst)):
            case (_, True): 
                return p1, p2
            case (True, _): 
                return aux(p1 + [lst[idx - 1]], p2, idx + 1)
            case (False, _): 
                return aux(p1, p2 + [lst[idx - 1]], idx + 1)
    
    return aux([], [], 1)


def split_list_v2[T](lst: list[T], split_point: int) -> tuple[list[T], list[T]]:
    return lst[:split_point], lst[split_point:]


def split_list_v3[T](lst: list[T], split_point: int) -> tuple[list[T], list[T]]:
    p1, p2 = [], []
    for idx, value in enumerate(lst, 1):
        if idx <= split_point: p1.append(value)
        else: p2.append(value)
    
    return p1, p2