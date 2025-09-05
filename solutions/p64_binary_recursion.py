# Implement binary recursion which has 4 parts
# A function BC which tells us if we reached the base case
# A function VBC which calculates the value when we reach the base case
# A function B which outputs 2 values given a state
# A function C which combines the results of the recursive calls

from __future__ import annotations
from typing import Callable
from dataclasses import dataclass

type State[T] = T
type Result[V] = V

def binary_recursion_v1(state: State,
                        at_base_case: Callable[[State], bool],
                        calculate_base_case: Callable[[State], Result],
                        transform: Callable[[State], tuple[State, State]],
                        combine: Callable[[State, Result, Result], Result]) -> Result:
    
    if at_base_case(state):
        return calculate_base_case(state)
    
    next_state_1, next_state_2 = transform(state)

    result_from_1 = binary_recursion_v1(next_state_1,
                                        at_base_case, calculate_base_case,
                                        transform, combine)
    
    result_from_2 = binary_recursion_v1(next_state_2,
                                        at_base_case, calculate_base_case,
                                        transform, combine)
    
    return combine(state, result_from_1, result_from_2)