# Rotate a list N places to the left

from itertools import chain
from collections import deque

def rotate_left_v1[T](lst: list[T], times: int) -> list[T]:
    if len(lst) <= 1: return lst

    match times % len(lst):
        case 0: return lst
        case _: return rotate_left_v1(lst[1:] + lst[:1], times - 1)


def rotate_left_v2[T](lst: list[T], times: int) -> list[T]:
    if len(lst) <= 1: return lst
    times = times % len(lst)
    return lst[times:] + lst[:times]


def rotate_left_v3[T](lst: list[T], times: int) -> list[T]:
    if len(lst) <= 1: return lst
    times = times % len(lst)
    path = chain(range(times, len(lst)), 
                 range(0, times))
    return [lst[idx] for idx in path]


def rotate_left_v4[T](lst: list[T], times: int) -> list[T]:
    d = deque(lst)
    d.rotate(-times)
    return list(d)