import pytest
from solutions.p53_path_from_one_node_to_another import *

implementations = [find_paths_v1, find_paths_v2]
ids = ["recursive", "generator"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_find_paths(solution):
    g = Graph(['b', 'c', 'd', 'f', 'g', 'h', 'k'],
              [Edge('h', 'g'), Edge('k', 'f'), Edge('f', 'b'), Edge('f', 'c'), Edge('c', 'b')])
    
    assert set(solution(g, 'f', 'b')) == set([('f', 'c', 'b'), ('f', 'b')])
    assert set(solution(g, 'd', 'h')) == set([])
    assert set(solution(g, 'h', 'g')) == set([('h', 'g')])