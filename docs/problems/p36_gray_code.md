---
tags:
    - Logic
    - Intermediate
---

# Gray Code

An n-bit [gray code](https://www.youtube.com/watch?v=RURnaoPTEMI) is a sequence of n-bit strings where each string differs by only 1 bit as the sequence carries on.

There is an exact [formula](https://mathworld.wolfram.com/GrayCode.html) as well.

=== "Test"
    ```python
    def test_generate_gray_code(solution):
        assert solution(1) == ['0', '1']
        assert solution(2) == ['00', '01', '11', '10']
        assert solution(3) == ['000', '001', '011', '010', '110', '111', '101', '100']
    ```

=== "Recursive"
    ```python
    def generate_gray_code_v1(bit_str_size: int) -> list[str]:
        match bit_str_size:
            case 1: return ['0', '1']
            case _:
                prev_level_codes = generate_gray_code_v1(bit_str_size - 1)
                p1 = (f'{a}{b}' for a,b in zip(repeat('0'), prev_level_codes))
                p2 = (f'{a}{b}' for a,b in zip(repeat('1'), reversed(prev_level_codes)))
                return list(chain(p1, p2))
    ```


=== "Formula"
    ```python
    def generate_gray_code_v2(bit_str_size: int) -> list[str]:
        return [(bin(i ^ (i >> 1))[2:]).rjust(bit_str_size, "0")
                 for i in range(2**bit_str_size)]
    ```