# Given a tree T, output a string of its values via preorder traversal

from solutions.p46_string_to_tree import *

def preorder_tree_traversal_v1(tree: Tree) -> str:
    match tree:
        case None: 
            return ''
        case Node(val, left, right): 
            return val + preorder_tree_traversal_v1(left) + preorder_tree_traversal_v1(right)
