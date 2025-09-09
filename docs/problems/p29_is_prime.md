---
tags:
    - Arithmetic
    - Intermediate
---

# Is Prime

Determine if a given integer number is prime


=== "Test"
    ```python
    def test_is_prime(solution):
        assert solution(0) == False
        assert solution(1) == False
        assert solution(2) == True
        assert solution(3) == True
        assert solution(5) == True
        assert solution(7) == True
        assert solution(13) == True
        assert solution(1299827) == True
        assert solution(6) == False
        assert solution(1000000) == False
    ```

=== "Direct"
    ```python
    def is_prime_v1(num: int) -> bool:
        if num <= 1: return False
        if num == 2: return True
        if num % 2 == 0: return False

        upper_limit = isqrt(num)
        odd_numbers = range(3, upper_limit + 1, 2)
        return all((num % i != 0 for i in odd_numbers))
    ```