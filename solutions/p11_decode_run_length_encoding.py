# Given a run-length code list, construct its uncompressed version

from typing import Generator

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
    def aux() -> Generator[T]:
        for term in rle_lst:
            match term:
                case (element, count): yield from (element for _ in range(count))
                case element: yield element
    
    return list(aux())