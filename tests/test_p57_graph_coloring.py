import pytest
from solutions.p57_graph_coloring import *

implementations = [color_graph_v1]
ids = ["backtracking/check chromatic number"]

# Graph 1: A triangle
n_a, n_b, n_c = Node('A'), Node('B'), Node('C')
g_triangle = Graph(
    nodes={n_a, n_b, n_c},
    edges={Edge(n_a, n_b), Edge(n_b, n_c), Edge(n_c, n_a)}
)

# Graph 2: A square
n_d = Node('D')
g_square = Graph(
    nodes={n_a, n_b, n_c, n_d},
    edges={Edge(n_a, n_b), Edge(n_b, n_c), Edge(n_c, n_d), Edge(n_d, n_a)}
)

# Graph 3: A line graph
g_line = Graph(
    nodes={n_a, n_b, n_c, n_d},
    edges={Edge(n_a, n_b), Edge(n_b, n_c), Edge(n_c, n_d)}
)

# Graph 4: A disconnected graph
n_e, n_f = Node('E'), Node('F')
g_disconnected = Graph(
    nodes={n_a, n_b, n_c, n_d, n_e, n_f},
    edges={
        # Component 1: A triangle (requires 3 colors)
        Edge(n_a, n_b), Edge(n_b, n_c), Edge(n_c, n_a),
        # Component 2: A single edge (requires 2 colors)
        Edge(n_d, n_e)
    }
)

# Graph 5: A graph with nodes but no edges
g_no_edges = Graph(
    nodes={n_a, n_b, n_c}
)

test_cases = [
    pytest.param(g_triangle, 3, id="3-colorable triangle"),
    pytest.param(g_square, 2, id="2-colorable square"),
    pytest.param(g_line, 2, id="2-colorable line"),
    pytest.param(g_disconnected, 3, id="disconnected"),
    pytest.param(g_no_edges, 1, id="1-colorable (no edges)"),
    pytest.param(Graph(), 0, id="empty graph"),
]

@pytest.mark.parametrize("graph, expected_num_colors", test_cases)
@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_color_graph(solution, graph, expected_num_colors):
    coloring = solution(graph)
    colors_used = set(coloring.values())
    assert len(colors_used) == expected_num_colors