---
tags:
    - Graph
    - Intermediate
---

# Graph Isomorphism

Find the function $F$ if it exists that makes two graphs $G_i$ and $G_j\;$ [isomorphic](https://en.wikipedia.org/wiki/Graph_isomorphism_problem).


We have two graphs $G_i$ and $G_j\;$. 

A function $F$ defines a mapping between a node $N_0 ∈ G_i \;$ and a node $M_0 ∈ G_j \;$ so this means $F(N_0) → M_0$. 

In other words, $F$ can be thought of as a dictionary where the keys are nodes from $G_i$ and the values are nodes from $G_j$.

$F$ is not allowed to map 2 nodes from $G_i$ to the same node in $G_j \;$ so $F(N_0) ≠ F(N_1)$

$F$ must map all nodes from $G_i$ to all nodes from $G_j \;$ so this means the number of nodes in $G_i$ must equal the number of nodes in $G_j$. 

$Adj(N_0) → A_0 \;$ is the set of nodes adjacent to $N_0$

$Adj(M_0) → B_0 \;$ is the set of nodes adjacent to $M_0$

If $\; F(Adj(N_0)) = Adj(F(N_0))$ for all nodes $N_0 \;$ from $G_i\;$ then $G_i\;$ and $G_j\;$ are isomorphic. This means that the structure of $G_i$ and $G_j\;$ is identical under the mapping $F$.


=== "Test"
    ```python
    # Graph 1: A simple square with number nodes
    nodes1 = {Node(i) for i in range(1, 5)}
    edges1 = {
        Edge(Node(1), Node(2)), Edge(Node(2), Node(3)),
        Edge(Node(3), Node(4)), Edge(Node(4), Node(1))
    }
    g1 = Graph(nodes1, edges1)

    # Graph 2: A simple square with letter nodes
    nodes2 = {Node(c) for c in "ABCD"}
    edges2 = {
        Edge(Node('A'), Node('B')), Edge(Node('B'), Node('C')),
        Edge(Node('C'), Node('D')), Edge(Node('D'), Node('A'))
    }
    g2 = Graph(nodes2, edges2)

    # Graph 3: A "kite" graph
    nodes3 = {Node(i) for i in range(1, 5)}
    edges3 = {
        Edge(Node(1), Node(2)), Edge(Node(2), Node(3)),
        Edge(Node(3), Node(4)), Edge(Node(4), Node(1)),
        Edge(Node(1), Node(3))
    }
    g3 = Graph(nodes3, edges3)

    def test_isomorphic_graphs(solution):
        mappings = solution(g1, g2)
        
        assert len(mappings) == 8
        
        expected_mapping = {
            Node(1): Node('A'),
            Node(2): Node('B'),
            Node(3): Node('C'),
            Node(4): Node('D')
        }
        assert expected_mapping in mappings

    def test_non_isomorphic_graphs(solution):
        mappings = solution(g1, g3)
        assert mappings == []
    ```

=== "Recursive"
    ```python
    from __future__ import annotations
    from dataclasses import dataclass, field
    from bidict import bidict
    from collections import namedtuple, defaultdict

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

        def add(self, node: Node, edges: iter[Edge]):
            self.nodes.add(node)
            self.edges.update(edges)

        def remove(self, node: Node, edges: iter[Edge]):
            self.nodes.difference_update((node,))
            self.edges.difference_update(edges)


    type Mapping = bidict[Node, Node]
    type AdjacencyGraph = defaultdict[Node, set[Edge]]

    def find_isomorph_v1(gi: Graph, gj: Graph) -> Mapping:

        def get_adjacency_form(graph: Graph) -> AdjacencyGraph:
            lookup = defaultdict(set)
            for edge in graph.edges:
                lookup[edge.start].add(edge)
                lookup[edge.end].add(edge.flip())

            return lookup

        def find_edges_that_terminate_within_graph(node: Node, mapped_nodes: set[Node], lookup_g: AdjacencyGraph) -> set[Edge]:
            return {terminating_edge 
                    for terminating_edge in lookup_g[node] 
                    if terminating_edge.end in mapped_nodes}
        
        def is_possible_candidate(n_0: Node, n_0_edges: set[Edge], working_f: Mapping, m_0: Node) -> bool:
            is_mapped = m_0 in working_f.inverse.keys()
            if is_mapped:
                return False
            
            degree_matches = len(lookup_gi[n_0]) == len(lookup_gj[m_0])
            if not degree_matches:
                return False
            
            m_0_edges = find_edges_that_terminate_within_graph(m_0, working_f.inverse.keys(), lookup_gj)
            size_matches = len(n_0_edges) == len(m_0_edges)
            if not size_matches:
                return False
            
            edges_match = {working_f[edge.end] for edge in n_0_edges} == {edge.end for edge in m_0_edges}
            if not edges_match:
                return False
            
            return True
            
        def aux(working_f: Mapping):
            if len(working_f) == len(gi.nodes):
                valid_mappings.append(working_f.copy())
                return
            
            n_0 = next((node for node in gi.nodes 
                        if node not in working_f))
            respective_n_0_edges = find_edges_that_terminate_within_graph(n_0, working_f.keys(), lookup_gi)
            
            candidates = (m_0 for m_0 in gj.nodes
                          if is_possible_candidate(n_0, respective_n_0_edges, working_f, m_0))
            
            for m_0 in candidates:
                working_f[n_0] = m_0
                aux(working_f)
                working_f.pop(n_0)


        valid_mappings = []
        if len(gi.nodes) != len(gj.nodes): return valid_mappings

        lookup_gi = get_adjacency_form(gi)
        lookup_gj = get_adjacency_form(gj)
        
        aux(bidict())

        return valid_mappings
    ```