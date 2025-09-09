# Construct a flat list containing the prime factors in ascending order
# *Lesson - Don't need a primality test b/c a prime number (P) 
# appears before any composite number (C) that has P as a factor

from math import isqrt
from itertools import chain, cycle
from typing import Generator

def prime_factors_v1(m: int) -> list[int]:
    def aux(factors: list[int], curr_num: int, target: int) -> list[int]:
        if target == 1:
            return factors
        elif target % curr_num == 0:
            return aux(factors + [curr_num], curr_num, target // curr_num)
        else:
            return aux(factors, curr_num + 1, target)

    if m <= 1: return []
    return aux([], 2, m)


def prime_factors_v2(m: int) -> list[int]:
    def prime_factors_iter(target: int) -> Generator[int]:
        if target <= 1:
            return
        
        nums_range = chain([2], range(3, isqrt(m) + 1, 2))
        while curr_num := next(nums_range, None):
            while target % curr_num == 0:
                target //= curr_num
                yield curr_num
            
        if target != 1: yield target
    
    return list(prime_factors_iter(m))


def prime_factors_v3(m: int) -> list[int]:
    if m <= 1: return []

    factors = []

    for curr_num in chain([2], range(3, isqrt(m) + 1, 2)):
        while m % curr_num == 0:
            factors.append(curr_num)
            m //= curr_num
    
    if m != 1: factors.append(m)
    return factors


def prime_factors_v4(m: int) -> list[int]:
    if m <= 1: return []

    def tiny_wheel() -> Generator[int]:
        candiate = 5
        gap_cycle = cycle([2, 4])

        while True:
            yield candiate
            candiate += next(gap_cycle)

    factors = []
    all_candiates = chain([2, 3], tiny_wheel())

    while (curr_num := next(all_candiates)) <= isqrt(m):
        while m % curr_num == 0:
            factors.append(curr_num)
            m //= curr_num
    
    if m != 1: factors.append(m)
    return factors