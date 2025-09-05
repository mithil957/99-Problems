# A multiway tree has a root element and a set of multiway trees
# The nodes contain a single characters. A special characer ^ has
# been inserted during depth-first order traversal. ^ means to backtrack
# to the previous level
# Ex. afg^^c^ represents the multiway tree MT
#     MT → T(a, {T(f, {T(g, {∅})}), T(c, {∅})})


from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:
    value: str
    successors: list[Tree]

type Tree = Node


def tree_to_string(tree: Tree) -> str:
    successors_str = ''.join(tree_to_string(st) for st in tree.successors)
    return tree.value + successors_str + '^'
