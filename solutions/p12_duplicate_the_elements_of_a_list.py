# Duplicate the elements of a 

from itertools import chain
from functools import reduce

def duplicate_elements_v1[T](lst: list[T]) -> list[T]:
    match lst:
        case []: return []
        case [head, *tail]: return [head, head] + duplicate_elements_v1(lst[1:])


def duplicate_elements_v2[T](lst: list[T]) -> list[T]:
    return sum(map(lambda x: [x, x], lst), [])


def duplicate_elements_v3[T](lst: list[T]) -> list[T]:
    return list(sum(chain(zip(lst, lst)), ()))


def duplicate_elements_v4[T](lst: list[T]) -> list[T]:
    return reduce(lambda l, r: l + [r, r], lst, [])


def duplicate_elements_v5[T](lst: list[T]) -> list[T]:
    return [elem for elem in lst for _ in range(2)]