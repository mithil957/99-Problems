---
tags:
    - Logic
    - Intermediate
---

# Calculate Truth Table

Construct a function which returns the [truth table](https://www.bucks.edu/media/bcccmedialibrary/tutoring/documents/math/Truth-Tables.pdf) of a given expression. The expression may contain any number of logical variables. The output is a list of __TableRow__ where __TableRow__ is 
    ((A, value of A), (B, value of B), (C, value of C), ..., expression value)

=== "Test"
    ```python
    def test_calculate_truth_table(solution):
        # A ∩ (A ∪ B )
        assert set(solution(['a', 'b'], And(Var('a'), Or(Var('a'), Var('b'))))) == set((
            ((('a', 0), ('b', 0)), 0),
            ((('a', 0), ('b', 1)), 0),
            ((('a', 1), ('b', 0)), 1),
            ((('a', 1), ('b', 1)), 1)
        ))

        # ¬(A ∩ B)
        assert set(solution(['a', 'b'], Not(And(Var('a'), Var('b'))))) == set((
            ((('a', 0), ('b', 0)), 1),
            ((('a', 0), ('b', 1)), 1),
            ((('a', 1), ('b', 0)), 1),
            ((('a', 1), ('b', 1)), 0)
        ))

        # ¬A
        assert set(solution(['a'], Not(Var('a')))) == set((
            ((('a', 0),), 1),
            ((('a', 1),), 0),
        ))

        # C ∪ (A ∩ B)
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
        # C ∪ (A ∩ B) has 3 variables A, B, C
        assert discover_vars(Or(Var('c'), Not(And(Var('a'), Var('b'))))) == {'a', 'b', 'c'}
    ```

=== "Recursive"
    ```python
    from __future__ import annotations
    from dataclasses import dataclass
    from itertools import product

    @dataclass
    class Var:
        name: str

    @dataclass
    class Not:
        expr: BoolExpr

    @dataclass
    class And:
        left: BoolExpr
        right: BoolExpr

    @dataclass
    class Or:
        left: BoolExpr
        right: BoolExpr

    type BoolExpr = Var | Not | And | Or
    type TableVar = tuple[str, bool]
    type TableRow = tuple[tuple[TableVar], bool]

    def calculate_truth_table_v1(vars: list[str], expr: BoolExpr) -> tuple[TableRow]:
        def eval_expr(expr: BoolExpr, values: dict[Var, bool]) -> bool:
            match expr:
                case Var(name):
                    return values[name]
                case Not(subexpr):
                    return not eval_expr(subexpr, values)
                case And(left, right):
                    return eval_expr(left, values) and eval_expr(right, values)
                case Or(left, right):
                    return eval_expr(left, values) or eval_expr(right, values)
        
        res = []
        for var_values in product([0, 1], repeat=len(vars)):
            var_table = {var: val for var, val in zip(vars, var_values)}
            res.append((tuple(var_table.items()), 
                        eval_expr(expr, var_table)))
        
        return tuple(res)


    def discover_vars(expr: BoolExpr) -> set[str]:
        match expr:
            case Var(a): return {a}
            case Not(a): return discover_vars(a)
            case And(a, b) | Or(a, b): return discover_vars(a) | discover_vars(b)
    ```