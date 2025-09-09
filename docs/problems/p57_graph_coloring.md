---
tags:
    - Graph
    - Intermediate
---

# Graph Coloring

Given a graph $G$, find the [minimum number of colors](https://en.wikipedia.org/wiki/Graph_coloring) needed such that each node can be painted a color
and any of its adjacent nodes are a different color. In other words, no adjacent nodes can be 
the same color. How many colors would we need?


=== "Test"
    ```python
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
    ```

=== "Recursive"
    ```python
    from __future__ import annotations
    from dataclasses import dataclass, field
    from collections import namedtuple

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

    type Color = int
    type ColorMapping = dict[Node, Color]
    type Palette = set[Color]
    type AdjacencyGraph = dict[Node, set[Edge]]

    def color_graph_v1(graph: Graph) -> ColorMapping:
        def get_adjacency_form(graph: Graph) -> AdjacencyGraph:
            lookup = {n: set() for n in graph.nodes}
            for edge in graph.edges:
                lookup[edge.start].add(edge)
                lookup[edge.end].add(edge.flip())

            # Hueristic (Welsh-Powell) - color node with highest degree
            nodes_sorted_by_degree = dict(sorted(lookup.items(), key=lambda item: len(item[1]), reverse=True))
            return nodes_sorted_by_degree

        def get_larger_palette(p: Palette) -> Palette:
            return set(range(0, len(p) + 1))
        
        def color_graph_with_palette(color_f: ColorMapping, p: Palette, adjacency_g: AdjacencyGraph) -> ColorMapping | None:
            if len(color_f) == len(graph.nodes):
                return color_f
            
            uncolored_node = next((node for node in adjacency_g.keys() if node not in color_f), None)
            neighbor_colors = {color_f.get(edge.end, None) for edge in adjacency_g[uncolored_node]}
            possible_colors = p - neighbor_colors

            for color in possible_colors:
                color_f[uncolored_node] = color
                if color_graph_with_palette(color_f, p, adjacency_g) is not None:
                    return color_f
                color_f.pop(uncolored_node)
            
            return None
        
        if len(graph.nodes) == 0: 
            return {}

        curr_palette = {0}
        lookup_g = get_adjacency_form(graph)

        while (mapping := color_graph_with_palette({}, curr_palette, lookup_g)) is None:
            curr_palette = get_larger_palette(curr_palette)

        return mapping
    ```