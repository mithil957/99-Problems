# Given a string representation of a multiway tree, parse it and output a tree
# *MARK - Review

from solutions.p50_multiway_tree_to_string import *

def tree_to_string_v1(tree_str: str) -> Tree | None:
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