# Select K items from a list and return them
# If K is bigger than number of items from list, return None
# The items should come from the list, should be unique

import random
from copy import deepcopy

random.seed(0)

def extract_elements_v1[T](lst: list[T], k: int) -> list[T] | None:
    if k > len(lst): return None
    return random.sample(lst, k)


def extract_elements_v2[T](lst: list[T], k: int) -> list[T] | None:
    def aux(possibilities: list[T], accumulated: list[T], current_idx: int) -> list[T]:
        if len(accumulated) == k or len(possibilities) == 0: 
            return accumulated

        match (1/len(lst)) <= random.random():
            case True:
                selected = possibilities.pop(current_idx % len(possibilities))
                return aux(possibilities, accumulated + [selected], current_idx + 1)
            
            case False: 
                return aux(possibilities, accumulated, current_idx + 1)

    if k > len(lst): return None 
    return aux(deepcopy(lst), [], 0)