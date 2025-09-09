---
tags:
    - Logic
    - Intermediate
---

# Shannon Fano Encoding

Given an alphabet (a, b, c, d, ...) and their respective frequencies (45, 13, 12, ...).
Construct a code C for every symbol S in the alphabet, [(symbol, code), ...] using Shannon Fano Encoding. 

[Includes Shannon Fano encoding explanation](https://www.youtube.com/watch?v=B3y0RsVCyrw)

[Encoding calculator](https://planetcalc.com/8168/)

=== "Test"
    ```python
    def test_generate_shannon_fano_encoding(solution):
        assert solution([
            ("a", 45), ("b", 13), ("c", 12), 
            ("d", 16), ("e", 9), ("f", 5)
        ]) == [
            ('a', '0'), ('d', '100'), ('b', '101'),
            ('c', '110'), ('e', '1110'), ('f', '1111')]
        
        assert solution([
            ('a', 100), ('b', 1), ('c', 1)
        ]) == [
            ('a', '0'), ('b', '10'), ('c', '11')]
    ```

=== "Recursive"
    ```python
    from __future__ import annotations
    from dataclasses import dataclass
    from bisect import bisect
    from itertools import accumulate

    @dataclass
    class Leaf:
        symbol: str

    @dataclass
    class Branch:
        left: Tree
        right: Tree

    type Tree = Branch | Leaf | None
    type SymbolFrequency = tuple[str, int]
    type Code = tuple[str, str]


    def generate_shannon_fano_encoding_v1(alphabet: list[SymbolFrequency]) -> list[Code]:
        def find_best_split_point(alphabet: list[SymbolFrequency]) -> int:
            cumulative_sums = [0] + list(accumulate(elem[1] for elem in alphabet))
            ideal_midpoint = cumulative_sums[-1] / 2.0
            insertion_point = bisect(cumulative_sums, ideal_midpoint)

            diff_at = abs(cumulative_sums[insertion_point] - ideal_midpoint)
            diff_right_before = abs(cumulative_sums[insertion_point - 1] - ideal_midpoint)
            
            if diff_at < diff_right_before: return insertion_point
            else: return insertion_point - 1

        def contruct_tree(alphabet: list[SymbolFrequency]) -> Tree:
            match alphabet:
                case []: return None
                case [a]: return Leaf(a[0])
                case _:
                    split_point = find_best_split_point(alphabet)
                    left, right = alphabet[:split_point], alphabet[split_point:]
                    return Branch(contruct_tree(left), contruct_tree(right))
        
        def calculate_codes(tree: Tree, current_path: str) -> list[Code]:
            match tree:
                case None: return []
                case Leaf(symbol): return [(symbol, current_path)]
                case Branch(left, right):
                    return calculate_codes(left, current_path + "0") + calculate_codes(right, current_path + "1")
        
        sorted_alphabet = sorted(alphabet, key=lambda elem: elem[1], reverse=True)
        encoding_tree = contruct_tree(sorted_alphabet)
        return calculate_codes(encoding_tree, "")
    ```