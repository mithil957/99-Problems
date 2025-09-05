# Same as find the prime factors but instead return their counts
# [3, 3, 7] -> [(3, 2), (7, 1)]

from math import isqrt
from itertools import chain

from solutions.p32_prime_factors import prime_factors_v3
from solutions.p09_run_length_encoding import rle_encode_v3

type FactorCount = tuple[int, int]

def prime_factor_counts_v1(target: int) -> list[FactorCount]:
    if target <= 1: return []

    accumulated = []
    for curr_num in chain([2], range(3, isqrt(target) + 1, 2)):
        curr_count = 0
        while target % curr_num == 0:
            curr_count += 1
            target //= curr_num

        if curr_count != 0:
            accumulated.append((curr_num, curr_count))
    
    if target != 1: 
        last_num, last_count = accumulated[-1]
        if last_num != target:
            accumulated.append((target, 1))
        else:
            accumulated[-1] = (last_num, last_count + 1)

    return accumulated


def prime_factor_counts_v2(m: int) -> list[FactorCount]:
    factors = prime_factors_v3(m)
    return rle_encode_v3(factors)