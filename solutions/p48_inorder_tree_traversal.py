# Given a tree T, output a string of its values via inorder traversal

from solutions.p46_string_to_tree import *

def inorder_tree_traversal_v1(tree: Tree) -> str:
    match tree:
        case None: 
            return ''
        case Node(val, left, right): 
            return inorder_tree_traversal_v1(left) + val + inorder_tree_traversal_v1(right)
