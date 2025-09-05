# Given a run-length code list, construct its uncomprssed version
from functools import reduce

type RleTerm[T] = tuple[T, int] | T 

def decode_rle_list_v1[T](rle_lst: list[RleTerm]) -> list[T]:
    match rle_lst:
        case []: 
            return []
        case [(element, count), *tail]:
            return [element] * count + decode_rle_list_v1(rle_lst[1:])
        case [element, *tail]:
            return [element] + decode_rle_list_v1(rle_lst[1:])


def decode_rle_list_v2[T](rle_lst: list[RleTerm]) -> list[T]:
    def aux(term: RleTerm) -> list[T]:
        match term:
            case (element, count): return [element] * count
            case element: return [element]
    
    return sum(map(aux, rle_lst), [])