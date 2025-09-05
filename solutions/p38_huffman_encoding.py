# Given an alphabet (a, b, c, d, ...) and their respective frequencies (45, 13, 12, ...)
# Construct a code C for every symbol S in the alphabet, [(symbol, code), ...] 
# Use Huffman Encoding
# https://www.youtube.com/watch?v=B3y0RsVCyrw&t=1458s
# Learning - Shannon Fano uses top down approach while Huffman uses bottom up approach
#          - Even though the tree built isn't the same, we are still creating a tree so there is
#          - 2 simple ways to approach building trees like there are 2 simple ways to explore/create 
#          - a graph (DFS and BFS)

from __future__ import annotations
from dataclasses import dataclass
from sortedcontainers import SortedList

@dataclass
class Leaf:
    symbol: str
    value: int

@dataclass
class Branch:
    value: int
    left: Tree
    right: Tree

type Tree = Leaf | Branch | None

type SymbolFrequency = tuple[str, int]
type Code = tuple[str, str]

def generate_huffman_codes_v1(alphabet: list[SymbolFrequency]) -> list[Code]:
    def contruct_encoding_tree(alphabet: list[SymbolFrequency]) -> Tree:
        if len(alphabet) == 0: return None
        if len(alphabet) == 1: return Leaf(alphabet[0][0], alphabet[0][1])
        
        leaves = [Leaf(sym, val) for sym, val in alphabet]
        trees = SortedList(leaves, key=lambda t: t.value)

        while len(trees) > 1:
            lowest_occurring = trees.pop(0)
            next_lowest_occurring = trees.pop(0)
            new_tree = Branch(lowest_occurring.value + next_lowest_occurring.value, 
                              lowest_occurring,
                              next_lowest_occurring)
            trees.add(new_tree)
        
        return trees.pop(0)

    def calculate_codes(encoding_tree: Tree, current_path: str) -> list[Code]:
        match encoding_tree:
            case None: return []
            case Leaf(sym, _): return [(sym, current_path)]
            case Branch(_, left, right):
                return calculate_codes(left, current_path + "0") + calculate_codes(right, current_path + "1")
    
    encoding_tree = contruct_encoding_tree(alphabet)
    return calculate_codes(encoding_tree, "")