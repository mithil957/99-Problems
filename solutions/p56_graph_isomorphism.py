# Find the function F if it exists that makes two graphs Gi and Gj isomorphic
# We have two graphs Gi and Gj. A function F is defining a mapping between
# a node N₀ ∈ Gi and a node M₀ ∈ Gj, so F(N₀) -> M₀
# F is not allowed to map 2 nodes from Gi to the same node in Gj -> F(N₀) ≠ F(N₁)
# F must map all nodes from Gi to all nodes from Gj -> number of nodes in Gi must equal number of nodes in Gj
# Adj(N₀) -> A₀ is the set of nodes adjacent to N₀
# Adj(M₀) -> B₀ is the set of nodes adjacent to M₀
# If F(Adj(N₀)) == Adj(F(N₀)) for all nodes N₀ from Gi then Gi and Gj are isomorphic
# This means that the structure of Gi and Gj is identical under the mapping F
# We need to generate F and we have constraints. It is possible that more than 1 valid F exists.
# We could generate all permutations for nodes in Gj and make each selection F and check for isomorphism? 
# Maybe we can avoid certain searches?
# If we have a function I(Gi, Gj) which gives us a F₀ that makes Gi and Gj isomorphic, then we 
# add a node N₀ to Gi along with its edges to Gi & and we add a node M₀ to Gj along with its edges.
# So I(Gi + N₀, Gj + Mₒ) -> F₁, what can we say about F₁ in terms of F₀? F₁ is F₀ + (N₀ -> M₀). N₀ $ M₀ had
# a similar structure b/c we were able to get F₁
# How do we pick a M₀ from Gj which has a similar structure to some selected N₀ from Gi? 
# Adj(N₀) -> A₀ and Adj(M₀) -> B₀
# For our current graph (working graph) Gi we might not see every node so we need to filter edges from A₀
# Only keep edges of N₀ with terminal points to a node in Gi. Then any B₀ after filtering also needs to have
# the same number of edges |A₀| == |B₀| and f(A₀) == B₀. If this is true, then N₀ -> M₀ could be a mapping
# of F. There might exist multiple "candidate" mappings for a selected N₀ so we can consider those and play
# it out assuming the mapping IS part of F until we reach a point where no mapping can be found OR until we
# have a mapping for every node.  


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