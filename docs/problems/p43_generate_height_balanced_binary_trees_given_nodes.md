---
tags:
    - Tree
    - Intermediate
---

# Generate Height Balanced Trees With a Given Number of Nodes

Given $N$ nodes, generate all height balanced trees with exactly $N$ nodes.

=== "Test"
    ```python
    def test_generate_height_balanced_binary_trees_given_nodes(solution):
        assert len(solution(0)) == 1
        assert len(solution(1)) == 1
        assert len(solution(2)) == 2
        assert len(solution(3)) == 1
        assert len(solution(4)) == 4
        assert len(solution(5)) == 6
        assert len(solution(15)) == 1553
    ```

=== "Recursive"
    ```python
    from __future__ import annotations
    from dataclasses import dataclass
    from functools import cache
    from math import log2, ceil, floor
    from itertools import product, chain

    @dataclass(frozen=True)
    class Node:
        left: Tree
        right: Tree
        value: str = 'x'

    type Tree = Node | None

    def generate_height_balanced_trees_given_nodes_v1(nodes: int) -> list[Tree]:

        @cache
        def minimum_nodes(height: int) -> int:
            if height == 0: return 0
            if height == 1: return 1
            return minimum_nodes(height - 1) + minimum_nodes(height - 2) + 1

        def maximum_nodes(height: int) -> int:
            return 2**height - 1
        
        def minimum_height(nodes: int) -> float:
            return log2(nodes + 1)
        
        def maximum_height(n: int) -> int:
            h = 0
            while minimum_nodes(h + 1) <= n:
                h += 1
            return h
        
        @cache
        def generate_trees(nodes: int, height: int) -> list[Tree]:
            match (nodes, height):
                case (0, 0): return [None]
                case (1, 1): return [Node(None, None)]
                case (0, _) | (_, 0): return []
                case (n, h) if (n < minimum_nodes(h)): return []
                case (n, h) if (n > maximum_nodes(h)): return []
                case _:
                    k = height - 1 # Remaining height excluding the root
                    n = nodes - 1  # Remaining nodes excluding the root

                    partitions = [(k, k), (k - 1, k), (k, k - 1)]
                    total_trees = []

                    for left_height, right_height in partitions:
                        min_nodes = minimum_nodes(left_height)
                        max_nodes = maximum_nodes(left_height)

                        for curr_node_amount in range(min_nodes, max_nodes + 1):
                            left_tree_node_amount = curr_node_amount
                            right_tree_node_amount = n - curr_node_amount # The total number of nodes must add up across the subtrees

                            left_trees = generate_trees(left_tree_node_amount, left_height)
                            right_trees = generate_trees(right_tree_node_amount, right_height)

                            cross_trees = (Node(left, right) for left, right in product(left_trees, right_trees))
                            total_trees.append(cross_trees)

                    return list(chain(*total_trees))
        
        min_height = ceil(minimum_height(nodes))
        max_height = floor(maximum_height(nodes))

        return list(chain(*(generate_trees(nodes, h) 
                            for h in range(min_height, max_height + 1))))
    ```