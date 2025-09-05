# Given a graph G, find all the connected components of G
# Connected component is a subgraph where nodes of the subgraph have a path to each other
# It is possible for a connected component to be exactly G, this would happen when
# every node has a path to every other node.

from __future__ import annotations
from dataclasses import dataclass
from collections import namedtuple

Node = namedtuple('Node', ['name'])

@dataclass(frozen=True)
class Edge:
    start: Node
    end: Node

    def flip(self) -> Edge:
        return Edge(self.end, self.start)

@dataclass(frozen=True)
class Graph:
    nodes: set[Node]
    edges: set[Edge]


type Component = set[Node]
type AdjacencyGraph = dict[Node, set[Edge]]

def get_adjacency_form(graph: Graph) -> AdjacencyGraph:
    lookup = {node: set() for node in graph.nodes}
    for edge in graph.edges:
        lookup[edge.start].add(edge)
        lookup[edge.end].add(edge.flip())
    
    return lookup

def find_connected_components_v1(graph: Graph) -> list[Component]:
    def dfs(curr_node: Node, working_component: Component, adjacency_graph: AdjacencyGraph) -> Component:
        working_component.add(curr_node)

        neighbors = (edge.end 
                     for edge in adjacency_graph[curr_node] 
                     if edge.end not in working_component)
        
        for next_node in neighbors:
            dfs(next_node, working_component, adjacency_graph)
        
        return working_component

    connected_components = []
    remaining_nodes = graph.nodes.copy()
    lookup_g = get_adjacency_form(graph)

    while len(remaining_nodes) > 0:
        seed_node = next(iter(remaining_nodes))
        component = dfs(seed_node, set(), lookup_g)
        remaining_nodes -= component
        connected_components.append(component)
    
    return connected_components


def find_connected_components_v2(graph: Graph) -> list[Component]:
    def dfs(curr_node: Node, working_component: set[Node]) -> Component:
        working_component.add(curr_node)

        neighbors = (edge.end for edge in lookup_g[curr_node] 
                     if edge.end not in working_component)
        
        for next_node in neighbors:
            dfs(next_node, working_component)
        
        return working_component
    
    def find_components(visited: set[Node]) -> list[Component]:
        unseen_node = next(iter(graph.nodes - visited), None)
        if unseen_node is None: 
            return []
        
        component = dfs(unseen_node, set())
        return [component] + find_components(visited | component)
    
    lookup_g = get_adjacency_form(graph)
    return find_components(set())

    

        



