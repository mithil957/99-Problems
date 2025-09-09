---
tags:
    - Tree
    - Intermediate
---

# String to Multiway Tree

Given a string representation of a multiway tree, parse it and output a tree.

=== "Test"
    ```python
    def test_tree_from_string(solution):
        assert tree_to_string(solution('afg^^c^^')) == 'afg^^c^^'
    ```

=== "Recursive"
    ```python
    from __future__ import annotations
    from dataclasses import dataclass

    @dataclass
    class Node:
        value: str
        successors: list[Tree]

    type Tree = Node

    def string_to_tree_v1(tree_str: str) -> Tree | None:
        def parse_node(idx: int) -> tuple[Tree, int]:
            val = tree_str[idx]
            children, final_idx = parse_children(idx + 1)
            return Node(val, children), final_idx

        def parse_children(idx: int) -> tuple[list[Tree], int]:
            if idx >= len(tree_str) or tree_str[idx] == '^':
                return [], idx + 1
            
            tree, next_idx = parse_node(idx)
            children, final_idx = parse_children(next_idx)
            return [tree] + children, final_idx
        
        if len(tree_str) == 0: return None
        tree, _ = parse_node(0)
        return tree
    ```