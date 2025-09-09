# Determine if a given integer number is prime

from math import isqrt

def is_prime_v1(num: int) -> bool:
    if num <= 1: return False
    if num == 2: return True
    if num % 2 == 0: return False

    upper_limit = isqrt(num)
    odd_numbers = range(3, upper_limit + 1, 2)
    return all((num % i != 0 for i in odd_numbers))