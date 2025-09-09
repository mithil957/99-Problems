---
tags:
    - Tree
    - Intermediate
---

# Generate Height Balanced Trees

In a height balanced tree, the height of the left subtree $T_L$ and the height of the right subtree differe by no more than 1. 

$H_L$ and $H_R$ are the heights of $T_L$ and $T_R$ respectively. $|H_L - H_R| ≤ 1$

Generate all possible height balanced trees for height $H$

=== "Test"
    ```python
    def test_generate_height_balanced_binary_trees(solution):
        assert len(solution(2)) == 3
        assert len(solution(3)) == 15
        assert len(solution(4)) == 315
        assert len(solution(5)) == 108675
    ```

=== "Recursive"
    ```python
    from __future__ import annotations
    from dataclasses import dataclass
    from itertools import product
    from functools import cache

    @dataclass(frozen=True)
    class Node:
        left: Tree
        right: Tree
        value: str = 'x'

    type Tree = Node | None

    @cache
    def generate_height_balanced_trees_v1(height: int) -> list[Tree]:
        match height:
            case 0: return [None]
            case 1: return [Node(None, None)]
            case h:
                k = h - 1
                subtrees = generate_height_balanced_trees_v1(k)
                shorter_subtrees = generate_height_balanced_trees_v1(k - 1)

                p1 = [Node(left, right) for left, right in product(subtrees, subtrees)]
                p2 = [Node(left, right) for left, right in product(subtrees, shorter_subtrees)]
                p3 = [Node(left, right) for left, right in product(shorter_subtrees, subtrees)]

                return p1 + p2 + p3
    ```