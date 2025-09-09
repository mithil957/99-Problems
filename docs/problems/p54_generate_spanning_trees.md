---
tags:
    - Tree
    - Intermediate
---

# Generate all Spanning Trees

Generate all the [spanning trees](https://en.wikipedia.org/wiki/Spanning_tree) of a given graph $G$. A spanning tree contains all the nodes of $G$ and a minimal set of edges from $G$ without creating cycles.

=== "Test"
    ```python
    def test_generate_spanning_trees(solution):
        g = Graph(nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
                  edges = [Edge('a', 'b'), Edge('a', 'd'), Edge('b', 'c'), Edge('b', 'e'),
                           Edge('c', 'e'), Edge('d', 'e'), Edge('d', 'f'), Edge('d', 'g'),
                           Edge('e', 'h'), Edge('f', 'g'), Edge('g', 'h')])
        
        assert len(solution(g)) == 112

        g = Graph(nodes = ['a', 'b', 'c'],
                  edges = [Edge('a', 'b'), Edge('a', 'c'), Edge('b', 'c')])
        
        assert len(solution(g)) == 3

        g = Graph(nodes = ['1', '2', '3', '4'], 
                  edges = [Edge('1', '2'), Edge('1', '3'), Edge('1', '4'), Edge('4', '3')])
        
        assert len(solution(g)) == 3
    ```

=== "Recursive"
    ```python
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
    ```