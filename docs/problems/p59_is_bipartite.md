---
tags:
    - Graph
    - Intermediate
---

# Is Bipartite

Check if a graph $G$ is [bipartite](https://en.wikipedia.org/wiki/Bipartite_graph) (is it 2 colorable).


=== "Test"
    ```python
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
    ```

=== "Recursive"
    ```python
    from __future__ import annotations
    from dataclasses import dataclass
    from collections import namedtuple

    type AdjacencyGraph = dict[Node, set[Edge]]
    type Color = int
    type Palette = set[Color]
    type ColorMapping = dict[Node, Color]

    Node = namedtuple('Node', ['name'])

    @dataclass(frozen=True)
    class Edge:
        start: Node
        end: Node

        def flip(self) -> Edge:
            return Edge(self.end, self.start)

    @dataclass
    class Graph:
        nodes: set[Node]
        edges: set[Edge]

        def get_adacencey_form(self) -> AdjacencyGraph:
            lookup = {node: set() for node in self.nodes}
            for edge in self.edges:
                lookup[edge.start].add(edge)
                lookup[edge.end].add(edge.flip())
            
            return lookup


    def is_bipartite_v1(graph: Graph) -> bool:
        def dfs(curr_node: Node, color_f: ColorMapping) -> ColorMapping | None:
            neighbors = (edge.end for edge in lookup_g[curr_node])
            curr_node_color = color_f[curr_node]

            for neighbor_node in neighbors:
                match color_f.get(neighbor_node, None):
                    case None:
                        color_f[neighbor_node] = (curr_node_color + 1) % 2
                        if dfs(neighbor_node, color_f) is None: 
                            return None

                    case neighbor_color if curr_node_color == neighbor_color:
                        return None
            
            return color_f
        

        def jump_and_color(color_f: ColorMapping) -> ColorMapping | None:
            unseen_node = next(iter(graph.nodes - color_f.keys()), None)
            if unseen_node is None:
                return color_f
            
            color_f[unseen_node] = 0
            if dfs(unseen_node, color_f) is None:
                return None
            
            return jump_and_color(color_f)

        lookup_g = graph.get_adacencey_form()
        coloring = jump_and_color({})
        return coloring is not None
    ```