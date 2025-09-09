---
tags:
    - Arithmetic
    - Intermediate
---

# Totient Function

[Euler's Totient Function φ(m)](https://en.wikipedia.org/wiki/Euler%27s_totient_function) -> number of positive integers that are coprime to m.
Two numbers are coprime if their GCD is 1. 

If we know the prime factors and the multiplicities -> [(p1, m1), (p2, m2), (p3, m3), ...]

φ(m) = (p1 - 1) × p1^(m1 - 1) × (p2 - 1) × p2^(m2 - 1) × (p3 - 1) × p3^(m3 - 1) × ⋯

=== "Test"
    ```python
    def test_totient_fn(solution):
        assert solution(10) == 4
        assert solution(20) == 8
        assert solution(40) == 16
        assert solution(99) == 60
        assert solution(33) == 20
        assert solution(1) == 1
    ```

=== "Direct"
    ```python
    from math import gcd

    def totient_fn_v1(m: int) -> int:
        if m == 1: return 1

        return sum(1 if gcd(m, curr_num) == 1 else 0
                   for curr_num in range(1, m))
    ```

=== "Formula"
    ```python
    from functools import reduce
    from operator import mul
    from solutions.p32_prime_factor_multiplicity import prime_factor_counts_v2

    def totient_fn_v2(m: int) -> int:
        if m == 1: return 1
        
        prime_counts = prime_factor_counts_v2(m)
        return reduce(mul, [(p - 1) * p**(c - 1) 
                            for p, c in prime_counts])
    ```