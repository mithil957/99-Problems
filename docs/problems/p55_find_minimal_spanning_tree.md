---
tags:
    - Graph
    - Intermediate
---

# Find the Minimal Spanning Tree

Find the [minimal spanning tree](https://www.youtube.com/watch?v=Yldkh0aOEcg) for a weighted/labelled graph.

=== "Test"
    ```python
    def test_final_minimal_spanning_tree(solution):
        g = Graph(nodes = ['a', 'b', 'c'],
                  edges = [Edge('a', 'b', 2), Edge('a', 'c', 1), Edge('b', 'c', 1)])
        
        assert solution(g)[1] == 2
    ```

=== "Prim"
    ```python
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
    ```