---
tags:
    - Arithmetic
    - Intermediate
---

# Prime Factor Multiplicity

Same as find the prime factors but instead return their counts. 


=== "Test"
    ```python
    def test_prime_factor_multiplicity(solution):
        assert solution(1) == []
        assert solution(315) == [(3, 2), (5, 1), (7, 1)]
        assert solution(9999) == [(3, 2), (11, 1), (101, 1)]
        assert solution(1009899) == [(3, 2), (11, 1), (101, 2)]
        assert solution(99999) == [(3, 2), (41, 1), (271, 1)]
    ```

=== "Recursive"
    ```python
    from math import isqrt
    from itertools import chain

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
    ```

=== "Compounding Previous Solutions"
    ```python
    from solutions.p31_prime_factors import prime_factors_v4
    from solutions.p09_run_length_encoding import rle_encode_v3

    def prime_factor_counts_v2(m: int) -> list[FactorCount]:
        factors = prime_factors_v4(m)
        return rle_encode_v3(factors)
    ```