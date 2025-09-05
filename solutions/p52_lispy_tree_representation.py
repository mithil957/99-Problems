# Given a multiway tree T output its lisp-like representation
# A node with children is always the first in a list, followed by its children
# The lispy repr is a sequence of values | "(" | ")"
# Ex. Node(a, []) -> a
# Ex. Node(a, [Node(b, [])]) -> (a b)
# Ex. Node(a, [Node(b, [Node(c, [])])]) -> (a (b c))
# Ex. Node(a, [Node(b, []), Node(c, [])]) -> (a b c)

from solutions.p50_multiway_tree_to_string import *

def lispy_tree_repr_v1(tree: Tree) -> str:
    match tree:
        case Node(val, []): 
            return val
        
        case Node(val, children):
            children_repr = ' '.join(lispy_tree_repr_v1(child) for child in children)
            return f'({val} {children_repr})'