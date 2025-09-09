# Implement fold which takes a state S, a function F, and elements E
# It applies F(S, Eₕ) -> Sₙ where Eₕ is the head of E and Sₙ is the new state
# Then we move "forward" along E and apply again
# Repeat this until we run out of elements and return the final state

from typing import Callable, Generator
from functools import reduce

def fold_v1[T](state: T, func: Callable[[T, T], T], elements: Generator[T]) -> T:
    if (head := next(elements, None)) is not None:
        next_state = func(state, head)
        return fold_v1(next_state, func, elements)
    
    return state


def fold_v2[T](state: T, func: Callable[[T, T], T], elements: Generator[T]) -> T:
    current_state = state
    while (head := next(elements, None)) is not None:
        current_state = func(current_state, head)
    
    return current_state


def fold_v3[T](state: T, func: Callable[[T, T], T], elements: Generator[T]) -> T:
    return reduce(func, elements, state)