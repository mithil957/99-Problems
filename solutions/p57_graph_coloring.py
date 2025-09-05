# Given a graph G find the minimum number of colors needed such that each node can be painted a
# color and any of its adjacent nodes are a different color. In other words, no adjacent nodes can be the same 
# color. How many colors would we need?
# Assume we have a function L(G) which gives us the minimum number of colors C₀ needed for G. We add an
# edge Eᵢ to G so L(G + Eᵢ) gives us C₁. What can we say about C₁ in terms of C₀?
# If Eᵢ is a linear add, meaning it starts from a node Nₛ ∈ G and terminates at node Nₑ ∉ G. 
# If P is our palette whose size would be Cₒ then P - {color of Nₛ} -> C₀ - 1
#   Case 1) If this is ∅ or 0 then we need a new color C₁ = C₀ + 1
#   Case 2) If not then it can be painted any color and C₁ is C₀
# If Eᵢ connects 2 nodes Nₛ and Nₑ in G, what can we say about the possible states?
# If the color of Nₛ and Nₑ are different then we don't do anything b/c we added an edge w/o breaking
# the constraint. C₁ is C₀
# If the color of Nₛ and Nₑ are same. Then at least Nₛ or Nₑ would have to change colors. 
# What color can it change to?
# Either its a new color not in P or its an existing color from P
# 1) If new color, then set Nₛ or Nₑ to this new color and now they are different and the constraint isn't broken. C₁ = C₀ + 1
# 2) If an existing color from P then can we "rotate" the colors of the nodes in G such that the constraint is no longer broken.
#    Before Eᵢ is connects Nₛ and Nₑ there must have existed a node Mₛ and Mₑ which connected to Nₛ and Nₑ respectively.
#    *There are multiple cases here, Mₛ could equal Mₑ OR we could have multiple connecting nodes (Mₛ, Oₛ, Pₛ, ...) (Mₑ, Oₑ, Pₑ, ...)
#    Let's keep it simple and focus on Mₛ ≠ Mₑ and we only have Mₛ and Mₑ and Mₛ is connected to Mₑ
# Before Eᵢ, Mₛ must have a different color than Nₛ and Mₑ must have a different color than Nₑ and Nₛ and Nₑ have the same color. We will use numbers
# to represent colors.
# This is the state before (the coloring before)
# Nₛ → ¬(Mₛ)          1 = ¬(2)    
# Mₛ → ¬(Nₛ ∪ Mₑ)     2 = ¬(1 ∪ 1)  
# Nₑ → ¬(Mₑ)         1 = ¬(2)
# Mₑ → ¬(Nₑ ∪ Mₛ)     2 = ¬(1 ∪ 1) 
# ¬ is not and (X ∪ X) reduces to just X so for example 2 = ¬1 which is true
# P = {1, 2}
# After adding Eᵢ to G, the equations change.
# Nₛ → ¬(Mₛ ∪ Nₑ)     1 = ¬(2 ∪ 1)    
# Mₛ → ¬(Nₛ ∪ Mₑ)     2 = ¬(1 ∪ 1)  
# Nₑ → ¬(Mₑ ∪ Mₛ)     1 = ¬(2 ∪ 1)
# Mₑ → ¬(Nₑ ∪ Mₛ)     2 = ¬(1 ∪ 1)
# We need to detect a "bad" state. We only need to look at the nodes involved with edge Eᵢ to see
# if they caused a "bad" state. For example, 1 = ¬(2 ∪ 1) → 1 = not 2 or 1 = {∅} b/c all colors from P have been eliminated
# The right side is a bad state so we add a new color or rotate colors. If we change any number in the equation to a number outside of
# P (prob successor of the max number) then this is like adding a new color. If we change any number in the equation to
# a number inside P, this is like rotating colors. In order to rotate, go through each var on right side. If var equals left side, we rotate it
# to "lowest possibility/drop to lowest potential". If fixed then check other equations. 
# This has a cascade effect b/c other equations will be effected. Repeat for them. If we cycle then maybe its not possible? 
# Nₛ → ¬(Mₛ ∪ Nₑ)     1 = ¬(2 ∪ 1)  ↻  1 → ¬(2 ∪ 2) *Nₛ got set to 2
# Mₛ → ¬(Nₛ ∪ Mₑ)     2 = ¬(1 ∪ 1)     
# Nₑ → ¬(Mₑ ∪ Mₛ)     1 = ¬(2 ∪ 1)  ⇒ 2 → ¬(2 ∪ 1)  ↻  2 → ¬(1 ∪ 1)  *Mₑ got set to 1
# Mₑ → ¬(Nₑ ∪ Mₛ)     2 = ¬(1 ∪ 1)  ⇒ 1 → ¬(2 ∪ 2)
# This means we could rotate and cascade until bad state is gone. Although this is just one example
# maybe it can work for bigger examples? One thing to note, G in this case could be consider "not packed"
# b/c we could add an edge to it w/o needing a new color. There is a point where if we add enough edges, we are required
# to generate a new color. There are multiple valid colorings possible depending on if we set Nₛ to 1 or Nₑ to 1. 

from __future__ import annotations
from dataclasses import dataclass, field
from collections import namedtuple

Node = namedtuple('Node', ['name'])

@dataclass(frozen=True)
class Edge:
    start: Node
    end: Node

    def flip(self) -> Edge:
        return Edge(self.end, self.start)

@dataclass
class Graph:
    nodes: set[Node] = field(default_factory=set)
    edges: set[Edge] = field(default_factory=set)

type Color = int
type ColorMapping = dict[Node, Color]
type Palette = set[Color]
type AdjacencyGraph = dict[Node, set[Edge]]

def color_graph_v1(graph: Graph) -> ColorMapping:
    def get_adjacency_form(graph: Graph) -> AdjacencyGraph:
        lookup = {n: set() for n in graph.nodes}
        for edge in graph.edges:
            lookup[edge.start].add(edge)
            lookup[edge.end].add(edge.flip())

        # Hueristic (Welsh-Powell) - color node with highest degree
        nodes_sorted_by_degree = dict(sorted(lookup.items(), key=lambda item: len(item[1]), reverse=True))
        return nodes_sorted_by_degree

    def get_larger_palette(p: Palette) -> Palette:
        return set(range(0, len(p) + 1))
    
    def color_graph_with_palette(color_f: ColorMapping, p: Palette, adjacency_g: AdjacencyGraph) -> ColorMapping | None:
        if len(color_f) == len(graph.nodes):
            return color_f
        
        uncolored_node = next((node for node in adjacency_g.keys() if node not in color_f), None)
        neighbor_colors = {color_f.get(edge.end, None) for edge in adjacency_g[uncolored_node]}
        possible_colors = p - neighbor_colors

        for color in possible_colors:
            color_f[uncolored_node] = color
            if color_graph_with_palette(color_f, p, adjacency_g) is not None:
                return color_f
            color_f.pop(uncolored_node)
        
        return None
    
    if len(graph.nodes) == 0: 
        return {}

    curr_palette = {0}
    lookup_g = get_adjacency_form(graph)

    while (mapping := color_graph_with_palette({}, curr_palette, lookup_g)) is None:
        curr_palette = get_larger_palette(curr_palette)

    return mapping