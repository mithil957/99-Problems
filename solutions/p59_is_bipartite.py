# Check if a graph G is bipartite means if it is 2 colorable

from __future__ import annotations
from dataclasses import dataclass
from collections import namedtuple

type AdjacencyGraph = dict[Node, set[Edge]]
type Color = int
type Palette = set[Color]
type ColorMapping = dict[Node, Color]

Node = namedtuple('Node', ['name'])

@dataclass(frozen=True)
class Edge:
    start: Node
    end: Node

    def flip(self) -> Edge:
        return Edge(self.end, self.start)

@dataclass
class Graph:
    nodes: set[Node]
    edges: set[Edge]

    def get_adacencey_form(self) -> AdjacencyGraph:
        lookup = {node: set() for node in self.nodes}
        for edge in self.edges:
            lookup[edge.start].add(edge)
            lookup[edge.end].add(edge.flip())
        
        return lookup


def is_bipartite_v1(graph: Graph) -> bool:
    def dfs(curr_node: Node, color_f: ColorMapping) -> ColorMapping | None:
        neighbors = (edge.end for edge in lookup_g[curr_node])
        curr_node_color = color_f[curr_node]

        for neighbor_node in neighbors:
            match color_f.get(neighbor_node, None):
                case None:
                    color_f[neighbor_node] = (curr_node_color + 1) % 2
                    if dfs(neighbor_node, color_f) is None: 
                        return None

                case neighbor_color if curr_node_color == neighbor_color:
                    return None
        
        return color_f
    

    def jump_and_color(color_f: ColorMapping) -> ColorMapping | None:
        unseen_node = next(iter(graph.nodes - color_f.keys()), None)
        if unseen_node is None:
            return color_f
        
        color_f[unseen_node] = 0
        if dfs(unseen_node, color_f) is None:
            return None
        
        return jump_and_color(color_f)

    lookup_g = graph.get_adacencey_form()
    coloring = jump_and_color({})
    return coloring is not None


    
    

    

        
