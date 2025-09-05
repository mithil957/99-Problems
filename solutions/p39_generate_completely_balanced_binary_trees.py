# A binary tree is either empty or it is made of a root element and 2 successors
# The successors are binary trees
# A completely balanced binary tree is tree where the number of nodes on the left - NL
# and the number of nodes on the right - NR differ by at most 1 so | NL - NR | <= 1
# Generate all completely balanced binary trees for a given number of nodes
# Put the letter 'x' as information into all nodes of the tree
# *Learning
# Let NL be the number of nodes on the left subtree (LT)
# Let NR be the number of nodes on the right subtree (RT)
# NL + NR + 1 = n (+1 b/c we can't have subtrees w/o a root node)
# | NL - NR | <= 1 (this means either NL and NR can equal each other or differ by 1) 
# F(n) -> generates all the completely balanced binary trees using N nodes
# F(0) -> [Ø] b/c with 0 nodes, we can only make an "empty" tree
# F(1) -> [Node] b/c with 1 node, we can only make a tree with a single node (being the root node)
# F(n) -> we would have n - 1 nodes left to distribute over our subtrees (-1 b/c we need a root node)
#         if n - 1 is EVEN so n - 1 = 2k, then NL has to be k and NR has to be k
#         we need to find F(k) which gives us all the subtrees we can make using k nodes
#         LT can be any tree (ti) from F(k) and RT can be any tree (tj) from F(k)
#         so Node(ti, tj) would give us a tree with k + k + 1 nodes which is n nodes
# F(n) -> we would have n - 1 nodes left to distribute over our subtrees
#         if n - 1 is ODD so n - 1 = 2k + 1, then NL=k, NR=k+1 OR NL=k+1, NR=k
#         we need to find F(k) and F(k+1) which gives all the subtrees we can make using k and k + 1 nodes
#         LT can be any tree (ti) from F(k) and RT can be any tree (tj) from F(k+1)
#         so Node(ti, tj) would give us a tree with k + k + 1 + 1 nodes which is n nodes
#         likewise, we can give LT k+1 nodes and RT k nodes and contruct the trees
#         add these sets together and we get all the tree we can make


from __future__ import annotations
from dataclasses import dataclass
from itertools import product
from functools import cache


@dataclass
class Node:
    left: Tree
    right: Tree
    value: str = 'x'

type Tree = Node | None

@cache
def generate_completely_balanced_binary_trees_v1(nodes: int) -> list[Tree]:
    match nodes:
        case 0: 
            return [None]
        
        case 1: 
            return [Node(None, None)]
        
        case n if (remaining_nodes := n - 1) % 2 == 0:
            subtrees = generate_completely_balanced_binary_trees_v1(remaining_nodes // 2)
            return [Node(left, right) for left, right in product(subtrees, subtrees)]
        
        case n if (remaining_nodes := n - 1) % 2 == 1:
            smaller_subtrees = generate_completely_balanced_binary_trees_v1(remaining_nodes // 2)
            larger_subtrees = generate_completely_balanced_binary_trees_v1(remaining_nodes // 2 + 1)

            p1_trees = [Node(left, right) for left, right in product(smaller_subtrees, larger_subtrees)]
            p2_trees = [Node(left, right) for left, right in product(larger_subtrees, smaller_subtrees)]
            
            return p1_trees + p2_trees