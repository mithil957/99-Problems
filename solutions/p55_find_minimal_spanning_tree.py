# Find the minimal spanning tree for a weighted/labelled graph
# We have a graph G with weighted edges. If we have a function M(G₀) which gives us the minimal spanning
# tree T₀. Now if we add an edge to E₁ to G₀ and M(G₀ ∪ E₁) which gives us the minimal spanning tree T₁
# What can we say about T₁ in terms of T₀? 
# 1) If E₁ connects to a new node from any existing node in T₀ then its a linear add so T₀ ∪ E₁ -> T₁. 
# 2) If E₁ is an edge between two already connected nodes N1 and N2, we consider how
# N1 and N2 are connected by a single path P in T₀ b/c it is a spanning tree and there are no loops, there can only
# be one path. So if we cut the path P at any point from T₀, we get two disjoint trees and if we add E₁ 
# then its connected again and becomes a new spanning tree T₁. We find the higest cost edge along P and replace it.
# 3) If E₁ connects 2 never seen before nodes, then what? 
# If we only consider edges from nodes we have seen then we don't need to worry about case 3. And if we keep a sorted
# list of edges based on cost and track only edges stemmming out from nodes in T₀ then we don't need to worry about case 2.
# So it reduces to only case 1 but we make sure an added edge doesn't create a loop.

from __future__ import annotations
from dataclasses import dataclass
from sortedcontainers import SortedList
from collections import defaultdict

@dataclass(frozen=True)
class Edge[T]:
    start: T
    end: T
    value: int

@dataclass
class Graph[T]:
    nodes: list[T]
    edges: list[Edge]

type SpanningTree = set[Edge]
type Cost = int    


def find_minimal_spanning_tree_v1(graph: Graph) -> tuple[SpanningTree, Cost]:
    def get_adjacency_form[T](graph: Graph) -> defaultdict[T, set[Edge]]:
        lookup = defaultdict(set)
        for edge in graph.edges:
            lookup[edge.start].add(edge)
            lookup[edge.end].add(Edge(edge.end, edge.start, edge.value))

        return lookup

    def get_next_valid_edge(pq: SortedList, seen_nodes: set) -> iter[Edge]:
        while pq and (cheapest_edge := pq.pop(0)):
            if cheapest_edge.end not in seen_nodes:
                yield cheapest_edge

    lookup = get_adjacency_form(graph)
    edges_to_consider = SortedList([], key=lambda elem: elem.value)
    working_tree = set()
    seen_nodes = set()
    cost = 0
    required_size = len(graph.nodes) - 1

    seen_nodes.add(graph.nodes[0])
    edges_to_consider.update(lookup[graph.nodes[0]])

    for edge in get_next_valid_edge(edges_to_consider, seen_nodes):
        if len(working_tree) == required_size:
            break
        
        working_tree.add(edge)
        seen_nodes.add(edge.end)
        cost += edge.value
        edges_to_consider.update(lookup[edge.end])

    return working_tree, cost