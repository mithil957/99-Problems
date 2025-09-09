---
tags:
    - Tree
    - Intermediate
---

# String to Tree

Given a string like __'a(b, c)'__ parse it into a tree.

=== "Test"
    ```python
    def test_string_to_tree(solution):
        tree = Node('a', Node ('b', Node ('d', None, None), Node ('e', None, None)),
                            Node ('c', None, Node ('f', Node ('g', None, None), None)))
        assert solution('a(b(d,e),c(,f(g,)))') == tree
    ```

=== "Recursive"
    ```python
    from __future__ import annotations
    from dataclasses import dataclass

    @dataclass
    class Node:
        value: str
        left: Tree
        right: Tree

    type Tree = Node | None

    def string_to_tree_v1(tree_str: str) -> Tree:
        def aux(idx: int) -> tuple[Tree, int]:
            if idx >= len(tree_str) or tree_str[idx] in [',', ')']:
                return None, idx
            
            current_char = tree_str[idx]
            next_char = tree_str[idx + 1]

            match (current_char, next_char):
                case (val, "("):
                    left, left_final_idx = aux(idx + 2)
                    right, right_final_idx = aux(left_final_idx + 1)
                    return Node(val, left, right), right_final_idx + 1
                
                case ("(", ","):
                    return None, idx
                
                case (val, ",") | (val, ")"):
                    return Node(val, None, None), idx + 1

        tree, _ = aux(0)    
        return tree
    ```