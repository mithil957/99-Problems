# Generate the permutations of K objects from the N elements of a list

from collections import deque
from collections.abc import Iterator


def generate_permutations_v1[T](lst: list[T], num_of_items: int) -> list[tuple[T]]:
    accumulated = []
    def aux(selected: tuple[T], remaining_choices: list[T]):
        if len(selected) + len(remaining_choices) < num_of_items:
            return
        
        if len(selected) == num_of_items:
            accumulated.append(selected)
            return
        
        for idx, choice in enumerate(remaining_choices):
            aux(selected + (choice,), remaining_choices[:idx] + remaining_choices[idx + 1:])
    
    aux((), lst)
    return accumulated


def generate_permutations_v2[T](lst: list[T], num_of_items: int) -> list[tuple[T]]:
    accumulated = []
    nodes = deque([((), lst)])

    while nodes:
        selected, remaining_choices = nodes.popleft()

        for idx, choice in enumerate(remaining_choices):
            new_selected = selected + (choice,)
            new_remaining_choices = remaining_choices[:idx] + remaining_choices[idx + 1:]

            if len(new_selected) == num_of_items:
                accumulated.append(new_selected)
            elif len(new_selected) + len(new_remaining_choices) >= num_of_items:
                nodes.append((new_selected, new_remaining_choices))
    
    return accumulated


def generate_permutations_v3[T](lst: list[T], num_of_items: int) -> list[tuple[T]]:
    def permutations_iter(lst: list[T], num_of_items: int) -> Iterator[tuple[T]]:
        if len(lst) == 0 or num_of_items > len(lst):
            return
        
        if num_of_items == 0:
            yield ()
            return

        yield from ((val,) + perm
                    for val in lst
                    for perm in permutations_iter(set(lst) - {val}, num_of_items - 1))
    
    return list(permutations_iter(lst, num_of_items))
        