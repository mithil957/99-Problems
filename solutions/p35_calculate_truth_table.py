# Construct a function which returns the truth table of a given expression in 2 variables (a, b)
# the outputs is a list[TableRow] where TableRow is (value of a, value of b, expression value)
# *Learning - ADTs can be implemented with dataclass and union types
# recursive types can be also be stated in the same way

from __future__ import annotations
from dataclasses import dataclass
from itertools import product, repeat

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
    for var_values in product(*repeat([0, 1], len(vars))):
        var_table = {var: val for var, val in zip(vars, var_values)}
        res.append((tuple(var_table.items()), 
                    eval_expr(expr, var_table)))
    
    return tuple(res)


def discover_vars(expr: BoolExpr) -> set[str]:
    match expr:
        case Var(a): return {a}
        case Not(a): return discover_vars(a)
        case And(a, b) | Or(a, b): return discover_vars(a) | discover_vars(b)