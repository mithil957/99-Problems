import pytest
from solutions.p59_is_bipartite import *

implementations = [is_bipartite_v1]
ids = ["recursive_dfs"]

N = Node

# Graph 1: A triangle (3-node odd cycle)
n_a, n_b, n_c = N('A'), N('B'), N('C')
g_triangle = Graph(
    nodes={n_a, n_b, n_c},
    edges={Edge(n_a, n_b), Edge(n_b, n_c), Edge(n_c, n_a)}
)

# Graph 2: A square (4-node even cycle)
n_d = N('D')
g_square = Graph(
    nodes={n_a, n_b, n_c, n_d},
    edges={Edge(n_a, n_b), Edge(n_b, n_c), Edge(n_c, n_d), Edge(n_d, n_a)}
)

# Graph 3: A line graph
g_line = Graph(
    nodes={n_a, n_b, n_c, n_d},
    edges={Edge(n_a, n_b), Edge(n_b, n_c), Edge(n_c, n_d)}
)

# Graph 4: A disconnected graph where all components are bipartite
n_e, n_f, n_g, n_h = N('E'), N('F'), N('G'), N('H')
g_disconnected_bipartite = Graph(
    nodes={n_a, n_b, n_c, n_d, n_e, n_f, n_g, n_h},
    edges={
        Edge(n_a, n_b), Edge(n_b, n_c),
        Edge(n_e, n_f),
    }
)

# Graph 5: A disconnected graph with a non-bipartite component
g_disconnected_non_bipartite = Graph(
    nodes={n_a, n_b, n_c, n_d, n_e},
    edges={
        Edge(n_a, n_b), Edge(n_b, n_c), Edge(n_c, n_a),
        Edge(n_d, n_e)
    }
)

# Graph 6: A "star" graph
g_star = Graph(
    nodes={n_a, n_b, n_c, n_d},
    edges={Edge(n_a, n_b), Edge(n_a, n_c), Edge(n_a, n_d)}
)

test_cases = [
    pytest.param(g_triangle, False, id="non-bipartite (triangle)"),
    pytest.param(g_square, True, id="bipartite (square)"),
    pytest.param(g_line, True, id="bipartite (line)"),
    pytest.param(g_star, True, id="bipartite (star graph)"),
    pytest.param(g_disconnected_bipartite, True, id="bipartite (disconnected)"),
    pytest.param(g_disconnected_non_bipartite, False, id="non-bipartite (disconnected)"),
    pytest.param(Graph(set(), set()), True, id="bipartite (empty graph)"),
]


@pytest.mark.parametrize("graph, expected_result", test_cases)
@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_is_bipartite(solution, graph, expected_result):
    assert solution(graph) == expected_result