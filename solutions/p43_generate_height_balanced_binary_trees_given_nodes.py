# Given n nodes, generate all the height balanced trees with exactly n nodes
# *Learning - When multiple answers are possible, look for bounds.
#             When many variables are present, lock them one by one and eventually the problem can be solved.
#             This problem requires finding the relationship between the number of nodes (N) and the height (H) for a height balanced tree (T)
#             Sometimes finding the direct relationship like nodes of a tree N(H) in terms of its height would be messy and maybe narrow-sighted
#             In those cases, try searching for bounds -> Nmin(H) - what is the minimum number of nodes T must have if it has height H?
#                                                         Nmax(H) - what is the maximum number of nodes T can have if it has height H?
#             Nmax(H) turns out to be 2ᴴ-1 
#                     b/c we are trying to fill all the possible spots in T w/o needing additional depth
#             Nmin(H) turns out to be Nmin(H - 1) + Nmin(H - 2) + 1 (*Fib variant, Nmin equals Fₕ₊₂ - 1) 
#                     b/c we are trying to use the least amount of space in T while still preserving the height balance constraint
#             If we invert Nmax⁻¹(H) = Hmin(N) and Nmin⁻¹(H) = Hmax(N), this gives us a bounds on possible heights T -> Hmin(N) <= H <= Hmax(N)
#             For each possible height (Hᵢ) -> we just need to make sure we generate only trees that use N nodes for given height so we need a function G(N, Hᵢ)
#             Bases cases for G(N, Hᵢ) are (0 nodes, 0 height) -> [∅], (1 node, 1 height) -> [Node(∅, ∅)]  
#                                          (0 nodes, >0 height) not possible so [],  (>0 nodes, 0 height) not possible so [] (not enough resources to make a tree)
#                                          (N nodes, Hᵢ height) not possible if N < Nmin(Hᵢ) OR N > Nmax(Hᵢ) (not enough/too many resources to make a tree)
#             If N and Hᵢ are good then what are the possible for heights for left subtree (LT) and right subtree (RT) such that we have a height balanced tree T?
#             T has height Hᵢ so the remaining height is Hᵢ - 1 = k, so the heights LTₕ and RTₕ would be either (k, k) OR (k, k - 1) OR (k - 1, k)
#             So now we go through each possibility -> LTₕ, RTₕ -> How do we allocate the nodes across LT and RT?
#             LTₙ + RTₙ + 1 = N (*N from G(N, Hᵢ), 1 from root node), we can again set up bounds since LTᵢ can have a range of nodes while still having height LTₕ 
#             Nmin(LTₕ) <= LTₙ <= Nmax(LTₕ) this means that RTₙ = N - 1 - LTₙ, with that we have fixed all the variables, so we go through each possibility
#             G(LTₙ, LTₕ) -> All possible left subtrees L and G(RTₙ, RTₕ) -> All possible right subtrees R, so we cross every tree from L with one from R
#             Repeat until we go out of bounds


from __future__ import annotations
from dataclasses import dataclass
from functools import cache
from math import log2, ceil, floor
from itertools import product, chain

@dataclass(frozen=True)
class Node:
    left: Tree
    right: Tree
    value: str = 'x'

type Tree = Node | None

def generate_height_balanced_trees(nodes: int) -> list[Tree]:

    @cache
    def minimum_nodes(height: int) -> int:
        if height == 0: return 0
        if height == 1: return 1
        return minimum_nodes(height - 1) + minimum_nodes(height - 2) + 1

    def maximum_nodes(height: int) -> int:
        return 2**height - 1
    
    def minimum_height(nodes: int) -> float:
        return log2(nodes + 1)
    
    def maximum_height(n: int) -> int:
        h = 0
        while minimum_nodes(h + 1) <= n:
            h += 1
        return h
    
    @cache
    def generate_trees(nodes: int, height: int) -> list[Tree]:
        match (nodes, height):
            case (0, 0): return [None]
            case (1, 1): return [Node(None, None)]
            case (0, _) | (_, 0): return []
            case (n, h) if (n < minimum_nodes(h)): return []
            case (n, h) if (n > maximum_nodes(h)): return []
            case _:
                k = height - 1 # Remaining height excluding the root
                n = nodes - 1  # Remaining nodes excluding the root

                partitions = [(k, k), (k - 1, k), (k, k - 1)]
                total_trees = []

                for left_height, right_height in partitions:
                    min_nodes = minimum_nodes(left_height)
                    max_nodes = maximum_nodes(left_height)

                    for curr_node_amount in range(min_nodes, max_nodes + 1):
                        left_tree_node_amount = curr_node_amount
                        right_tree_node_amount = n - curr_node_amount # The total number of nodes must add up across the subtrees

                        left_trees = generate_trees(left_tree_node_amount, left_height)
                        right_trees = generate_trees(right_tree_node_amount, right_height)

                        cross_trees = (Node(left, right) for left, right in product(left_trees, right_trees))
                        total_trees.append(cross_trees)

                return list(chain(*total_trees))
    
    min_height = ceil(minimum_height(nodes))
    max_height = floor(maximum_height(nodes))

    return list(chain(*(generate_trees(nodes, h) 
                        for h in range(min_height, max_height + 1))))