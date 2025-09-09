# Drop every Nth element

from functools import reduce
from itertools import chain, compress, cycle

def drop_every_nth_element_v1[T](lst: list[T], n: int) -> list[T]:
    if n == 0: 
        return lst

    def aux(left: tuple[list[T], int], right: T) -> tuple[list[T], int]:
        acummulated, index_tracker = left
        if index_tracker % n != 0: 
            acummulated.append(right)
        return (acummulated, index_tracker + 1)

    acummulated, _ = reduce(aux, lst, ([], 1))
    return acummulated


def drop_every_nth_element_v2[T](lst: list[T], n: int) -> list[T]:
    if n == 0: 
        return lst
    
    generator_exp = (value 
                     for idx, value in enumerate(lst, 1)
                     if idx % n != 0)
    
    return list(generator_exp)


def drop_every_nth_element_v3[T](lst: list[T], n: int) -> list[T]:
    if n == 0:
        return lst
    
    step = n
    return list(chain.from_iterable(
        lst[idx: idx + step - 1] 
        for idx in range(0, len(lst), step)
    ))


def drop_every_nth_element_v4[T](lst: list[T], n: int) -> list[T]:
    if n == 0:
        return lst
    
    mask = [True] * (n - 1) + [False]
    repeated_mask = cycle(mask)
    return list(compress(lst, repeated_mask))