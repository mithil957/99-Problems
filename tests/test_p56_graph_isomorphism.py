import pytest
from solutions.p56_graph_isomorphism import *

implementations = [find_isomorph_v1]
ids = ["recursive/backtracking"]

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
    Edge(Node(1), Node(3)) # The extra diagonal edge
}
g3 = Graph(nodes3, edges3)


@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_isomorphic_graphs(solution):
    mappings = solution(g1, g2)
    
    assert len(mappings) == 8
    
    expected_mapping = bidict({
        Node(1): Node('A'),
        Node(2): Node('B'),
        Node(3): Node('C'),
        Node(4): Node('D')
    })
    assert expected_mapping in mappings


@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_non_isomorphic_graphs(solution):
    mappings = solution(g1, g3)
    assert mappings == []