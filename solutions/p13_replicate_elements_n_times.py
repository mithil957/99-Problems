# Replicate the elements of a list a given number of times

from functools import reduce

def replicate_elements_v1[T](lst: list[T], times: int) -> list[T]:
    match (lst, times):
        case ([], _) | (_, 0): 
            return []
        case (_, 1): 
            return lst
        case ([head, *tail], times): 
            return ([head] * times) + replicate_elements_v1(lst[1:], times)


def replicate_elements_v2[T](lst: list[T], times: int) -> list[T]:
    return reduce(lambda l, r: l + [r] * times, lst, [])


def replicate_elements_v3[T](lst: list[T], times: int) -> list[T]:
    return [elem for elem in lst for _ in range(times)]

