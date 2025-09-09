# Generate all the spanning trees of a given graph G
# A spanning tree contains all the nodes of G and a minimal set of edges from G w/o creating cycles 
# The set of all spanning trees for G is the union of two sets. The set containing all spanning trees which
# include an edge Ei from G and the set containing all spanning trees that don't include edge Ei from G
# This becomes a combination problem where the objects we are picking are edges from G
# We can't pick all the edges. The order in which we pick edges doesn't matter. 
# We can't have cycles o/w it wouldn't be a tree. We must connect all the nodes of G
# Learning - Use Disjoint Set Union and Matrix Tree Theorm is a very interesting way to
# calculate the number of spanning trees for G. If we pick edges such that they don't create loops
# we are guaranteed a spanning tree after picking N - 1 edges where V is the number of nodes in G

from __future__ import annotations
from dataclasses import dataclass, field
from collections import namedtuple


Edge = namedtuple('Edge', ['start', 'end'])
type SpanningTree = set[Edge]

@dataclass
class Graph[T]:
    nodes: list[T]
    edges: list[Edge]

Merges = namedtuple('Merges', ['index_start', 'index_end', 'popped_values'])

@dataclass
class EdgeSet[T]:
    edges: list[Edge] = field(default_factory=list)
    connected_nodes: list[set[T]] = field(default_factory=list)
    history: list[Merges] = field(default_factory=list)

    def find_node(self, node: T) -> int:
        return next((idx 
                     for idx, nodes in enumerate(self.connected_nodes) 
                     if node in nodes))
    
    def creates_loop(self, edge: Edge) -> bool:
        # If both nodes are in the same connected set of nodes, that would create a loop
        return self.find_node(edge.start) == self.find_node(edge.end)

    def add_edge(self, edge: Edge) -> None:
        self.edges.append(edge)

        idx_start = self.find_node(edge.start)
        idx_end = self.find_node(edge.end)

        self.connected_nodes[idx_start] |= self.connected_nodes[idx_end]
        self.history.append(Merges(idx_start, idx_end, self.connected_nodes[idx_end]))    
        self.connected_nodes[idx_end] = set()
                

    def undo_action(self) -> None:
        self.edges.pop()
        idx_start, idx_end, popped = self.history.pop()
        self.connected_nodes[idx_start].difference_update(popped)
        self.connected_nodes[idx_end] = set(popped)


def generate_spanning_trees_v1(graph: Graph) -> list[SpanningTree]:
    valid_choices = []
    required_edges = len(graph.nodes) - 1

    def aux(accumulated_edges: EdgeSet, possible_edges: list[Edge]):
        if len(accumulated_edges.edges) == required_edges:
            valid_choices.append(tuple(accumulated_edges.edges))
            return
        
        if not possible_edges or len(accumulated_edges.edges) + len(possible_edges) < required_edges:
            return
        
        head, *tail = possible_edges
        creates_loop = accumulated_edges.creates_loop(head)

        if not creates_loop:
            accumulated_edges.add_edge(head)
            aux(accumulated_edges, tail)
            accumulated_edges.undo_action()
            
        aux(accumulated_edges, tail)


    aux(EdgeSet([], [{node} for node in graph.nodes], []), graph.edges)
    return valid_choices