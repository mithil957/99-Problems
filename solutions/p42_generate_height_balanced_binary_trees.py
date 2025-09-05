# In a height balanced tree, the height of the left subtree (LT) and the height of the right subtree (RT)
# differ by no more than 1 -> | HL - HR | <= 1
# Generate all the possible hight balanced trees for a hight H
# *Very similar to how we approached 'generate completely balanced binary trees'
# F(0) -> [Ø] b/c with 0 nodes, we can only make an "empty" tree
# F(1) -> [Node] b/c with 1 node, we can only make a tree with a single node (being the root node)
# F(h) -> w/ the root node we have h - 1 height left -> k
#         this means (HL, HR) can be (k, k) | (k, k-1) | (k-1, k)
#         k-2 would make the difference too big and k+1 would put us above the height requirement 
#         we find f(k) gives us all height balanced trees with height k
#         we find f(k-1) gives us all height balanced trees with heigh k - 1
#         LT, RT = f(k) cross_prod f(k)  
#           *means LT can be any tree from f(k) and RT can be any tree from f(k)
#           *if we make a tree using LT and RT then it will be height balanced
#         Repeat for LT, RT = f(k) cross f(k-1) AND LT, RT = f(k-1) cross f(k)


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