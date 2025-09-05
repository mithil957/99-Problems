# Given a tree T, convert it into string format and write the inverse function
# ∅ -> '', N(∅, ∅, a) -> 'a', N(N(∅, ∅, b), ∅, a) -> a(b,), N(∅, N(∅, ∅, c), a) -> a(,c)

from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:
    value: str
    left: Tree
    right: Tree

type Tree = Node | None

def tree_to_string_v1(tree: Tree) -> str:
    match tree:
        case None: return ''
        case Node(value, None, None): return f'{value}'
        case Node(value, left, right):
            left_str = tree_to_string_v1(left)
            right_str = tree_to_string_v1(right)
            return f'{value}({left_str},{right_str})'

