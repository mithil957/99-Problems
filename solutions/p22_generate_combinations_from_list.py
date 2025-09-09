# Generate the combinations of K objects from the N elements of a list

from collections import deque
from typing import Generator
from itertools import combinations

def generate_combinations_v1[T](lst: list[T], num_of_items: int) -> list[tuple[T]]:
    valid_selections = []

    def aux(selected: tuple[T], remaining_choices: list[T]):
        if len(selected) + len(remaining_choices) < num_of_items:
            return
        
        if len(selected) == num_of_items:
            valid_selections.append(selected)
            return
        
        for idx, choice in enumerate(remaining_choices):
            aux(selected + (choice,), remaining_choices[idx + 1:])
    
    aux((), lst)
    return valid_selections


def generate_combinations_v2[T](lst: list[T], num_of_items: int) -> list[tuple[T]]:
    valid_selections = []
    nodes = deque([((), lst)])

    while nodes:
        selected, remaining_choices = nodes.popleft()
        
        for idx, choice in enumerate(remaining_choices):
            new_selection = selected + (choice,)
            new_remaining_choices = remaining_choices[idx+1:]

            if len(new_selection) == num_of_items:
                valid_selections.append(new_selection)

            elif len(selected) + len(remaining_choices) >= num_of_items:
                nodes.append((new_selection, new_remaining_choices))
    
    return valid_selections


def generate_combinations_v3[T](lst: list[T], num_of_items: int) -> list[tuple[T]]:
    def combinations_iter(lst: list[T], num_of_items: int) -> Generator[tuple[T]]:
        if len(lst) == 0 or num_of_items > len(lst):
            return
        
        if num_of_items == 0:
            yield ()
            return
        
        if len(lst) == num_of_items:
            yield tuple(lst)
            return

        head, *tail = lst
        
        yield from ((head,) + selection for selection in combinations_iter(tail, num_of_items - 1))
        yield from combinations_iter(tail, num_of_items)
    
    return list(combinations_iter(lst, num_of_items))


def generate_combinations_v4[T](lst: list[T], num_of_items: int) -> list[tuple[T]]:
    return list(combinations(lst, num_of_items))