import pytest
from solutions.p35_calculate_truth_table import *

implementations = [calculate_truth_table_v1]
ids = ["recursive"]

@pytest.mark.parametrize("solution", implementations, ids=ids)
def test_calculate_truth_table(solution):
    assert set(solution(['a', 'b'], And(Var('a'), Or(Var('a'), Var('b'))))) == set((
        ((('a', 0), ('b', 0)), 0),
        ((('a', 0), ('b', 1)), 0),
        ((('a', 1), ('b', 0)), 1),
        ((('a', 1), ('b', 1)), 1)
    ))

    assert set(solution(['a', 'b'], Not(And(Var('a'), Var('b'))))) == set((
        ((('a', 0), ('b', 0)), 1),
        ((('a', 0), ('b', 1)), 1),
        ((('a', 1), ('b', 0)), 1),
        ((('a', 1), ('b', 1)), 0)
    ))


    assert set(solution(['a'], Not(Var('a')))) == set((
        ((('a', 0),), 1),
        ((('a', 1),), 0),
    ))


    assert set(solution(['a', 'b', 'c'], Or(Var('c'), Not(And(Var('a'), Var('b')))))) == set((
        ((('a', 0), ('b', 0), ('c', 0)), 1),
        ((('a', 0), ('b', 0), ('c', 1)), 1),
        ((('a', 0), ('b', 1), ('c', 0)), 1),
        ((('a', 0), ('b', 1), ('c', 1)), 1),
        ((('a', 1), ('b', 0), ('c', 0)), 1),
        ((('a', 1), ('b', 0), ('c', 1)), 1),
        ((('a', 1), ('b', 1), ('c', 0)), 0),
        ((('a', 1), ('b', 1), ('c', 1)), 1)
    ))


def test_discover_vars():
    assert discover_vars(Or(Var('c'), Not(And(Var('a'), Var('b'))))) == {'a', 'b', 'c'}