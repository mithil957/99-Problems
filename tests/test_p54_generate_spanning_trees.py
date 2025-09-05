import pytest
from solutions.p54_generate_spanning_trees import *

implementations = [generate_spanning_trees_v1]
ids = ["recursive"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_generate_spanning_trees(solution):
    g = Graph(nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
                edges = [Edge('a', 'b'), Edge('a', 'd'), Edge('b', 'c'), Edge('b', 'e'),
                            Edge('c', 'e'), Edge('d', 'e'), Edge('d', 'f'), Edge('d', 'g'),
                            Edge('e', 'h'), Edge('f', 'g'), Edge('g', 'h')])
    
    assert len(solution(g)) == 112

    g = Graph(nodes = ['a', 'b', 'c'],
                edges = [Edge('a', 'b'), Edge('a', 'c'), Edge('b', 'c')])
    
    assert len(solution(g)) == 3

    g = Graph(nodes = ['1', '2', '3', '4'], 
              edges = [Edge('1', '2'), Edge('1', '3'), Edge('1', '4'), Edge('4', '3')])
    
    assert len(solution(g)) == 3