# Create a list containing all integers within a given range
# if the first argument is greater than the second, return the list in decreasing order

from itertools import count, takewhile

def create_range_v1(start: int, end: int) -> list[int]:
    def aux(accumulated: list[int], direction: int, remaining: int) -> list[int]:
        if remaining == 0: 
            return accumulated
        else: 
            return aux(accumulated + [accumulated[-1] + direction], direction, remaining - 1)
    
    direction = 1 if end >= start else -1
    return aux([start], direction, abs(start - end))


def create_range_v2(start: int, end: int) -> list[int]:
    direction = 1 if end >= start else -1
    return list(range(start, end + direction, direction))


def create_range_v3(start: int, end: int) -> list[int]:
    if start <= end:
        direction = 1
        stop_condition = lambda x: x <= end
    else:
        direction = -1
        stop_condition = lambda x: x >= end
    
    counter = count(start, direction)
    bounded_counter = takewhile(stop_condition, counter)
    return list(bounded_counter)