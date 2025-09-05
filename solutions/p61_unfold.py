# Implement unfold which applies a function F to a starting value S until a predicate P is true

from typing import Callable
from collections.abc import Iterator

def unfold_v1[T](seed: T, func: Callable[[T], T], stop_condition: Callable[[T], bool]) -> Iterator[T]:
    if stop_condition(seed):
        return
    
    yield seed
    yield from unfold_v1(func(seed), func, stop_condition)


def unfold_v2[T](seed: T, func: Callable[[T], T], stop_condition: Callable[[T], bool]) -> Iterator[T]:
    current_state = seed
    while not stop_condition(current_state):
        yield current_state
        current_state = func(current_state)