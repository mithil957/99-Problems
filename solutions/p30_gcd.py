# Determine the greatest common divisor of 2 positive integer numbers

def gcd_v1(a: int, b: int) -> int:
    return a if b == 0 else gcd_v1(b, a % b)
     