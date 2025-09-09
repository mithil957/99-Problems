# Determine the greatest common divisor of 2 positive integer numbers

from math import gcd

def gcd_v1(a: int, b: int) -> int:
    return a if b == 0 else gcd_v1(b, a % b)


def gcd_v2(a: int, b: int) -> int:
    target, divider = a, b
    
    while (remaining := target % divider) != 0:
        target = divider
        divider = remaining
    
    return divider


def gcd_v3(a: int, b: int) -> int:
    return gcd(a, b)