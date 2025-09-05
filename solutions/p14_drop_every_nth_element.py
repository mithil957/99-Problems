# Drop every Nth element

from functools import reduce

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
                     if idx % n != 0
                     )
    
    return list(generator_exp)
    