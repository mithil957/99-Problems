---
tags:
    - Arithmetic
    - Intermediate
---

# GCD

Determine the greatest common divisor of 2 positive integer numbers

<description>

=== "Test"
    ```python
    def test_gcd(solution):
        assert solution(13, 27) == 1
        assert solution(24, 18) == 6
        assert solution(20536, 7826) == 2
    ```

=== "Recursive"
    ```python
    def gcd_v1(a: int, b: int) -> int:
        return a if b == 0 else gcd_v1(b, a % b)
    ```

=== "Iterative"
    ```python
    def gcd_v2(a: int, b: int) -> int:
        target, divider = a, b
        
        while (remaining := target % divider) != 0:
            target = divider
            divider = remaining
        
        return divider
    ```

=== "Direct"
    ```python
    from math import gcd

    def gcd_v3(a: int, b: int) -> int:
        return gcd(a, b)
    ```