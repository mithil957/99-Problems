import pytest
from solutions.p58_connected_components import *

implementations = [find_connected_components_v1, find_connected_components_v2]
ids = ["dfs", "recursive"]

# Graph 1: A empty graph
g1 = Graph(set(), set())

# Graph 2: A single node
g2 = Graph(nodes={Node('a')}, edges=set())

# Graph 3: All connected nodes
g3 = Graph({Node('a'), Node('b'), Node('c'), Node('d')}, 
           {Edge(Node('a'), Node('b')), 
            Edge(Node('b'), Node('c')), Edge(Node('a'), Node('d'))})

# Graph 4: Several components
g4 = Graph({Node('a'), Node('b'), Node('c'), Node('d'), 
            Node('e'), Node('f'), Node('g')}, 
           {Edge(Node('a'), Node('b')),
            Edge(Node('c'), Node('d')), Edge(Node('d'), Node('e'))})

test_cases = [
    pytest.param(g1, 0, id="empty"),
    pytest.param(g2, 1, id="single"),
    pytest.param(g3, 1, id="fully connected"),
    pytest.param(g4, 4, id="several groups"),
]

@pytest.mark.parametrize("graph, expected_num_components", test_cases)
@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_connected_components(solution, graph, expected_num_components):
    components = solution(graph)
    assert len(components) == expected_num_components