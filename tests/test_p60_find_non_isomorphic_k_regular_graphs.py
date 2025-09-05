import pytest
from solutions.p60_find_non_isomorphic_k_regular_graphs import *

implementations = [find_non_isomorophic_graphs_v1, find_non_isomorphic_graphs_v2]
ids = ["generate/canonical label", "mismatch based hueristic"]

def graph_from_str(g_str, num_nodes) -> Graph:
    nodes = [Node(str(i)) for i in range(1, num_nodes + 1)]
    edge_set = set()
    for pair in g_str.split(', '):
        start, end = pair.split('-')
        start_node = nodes[int(start) - 1]
        end_node = nodes[int(end) - 1]
        edge_set.add(Edge(start_node, end_node))
    
    return Graph(nodes, edge_set)

r2n3_str = "1-2, 1-3, 2-3"
r2n3 = graph_from_str(r2n3_str, 3)

r3n6_str = "1-2, 1-3, 1-4, 2-3, 2-5, 3-6, 4-5, 4-6, 5-6"
r3n6 = graph_from_str(r3n6_str, 6)

r5n8_str = "1-2, 1-3, 1-4, 1-5, 1-6, 2-3, 2-4, 2-5, 2-6, 3-4, 3-7, 3-8, 4-7, 4-8, 5-6, 5-7, 5-8, 6-7, 6-8, 7-8"
r5n8 = graph_from_str(r5n8_str, 8)


test_cases = [
    pytest.param(r2n3, 1, id="2 Regular 3 Node"),
    pytest.param(r3n6, 2, id="3 Regular 6 Node"),
    # pytest.param(r5n8, 3, id="5-regular-8-node"), # too slow for v1
]

@pytest.mark.parametrize("graph, expected_result", test_cases)
@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_find_non_isomorphic_k_regular_graphs(solution, graph, expected_result):
    assert len(solution(graph)) == expected_result