# Generate the permutations of K objects from the N elements of a list 
# Repeats are allowed

from collections import deque
from collections.abc import Iterator


def permutations_with_replacement_v1[T](lst: list[T], num_of_items: int) -> list[tuple[T]]:
    if len(lst) == 0: return []
    if num_of_items == 0: return [()]

    valid_selections = []

    def aux(selection: tuple[T]):
        if len(selection) == num_of_items:
            valid_selections.append(selection)
            return
        
        for val in lst:
            aux(selection + (val,))
    
    aux(())
    return valid_selections


def permutations_with_replacements_v2[T](lst: list[T], num_of_items: int) -> list[tuple[T]]:
    if len(lst) == 0: return []
    if num_of_items == 0: return [()]

    valid_selections = []
    nodes = deque([()])

    while nodes:
        selected = nodes.popleft()

        for val in lst:
            new_selected = selected + (val,)
            if len(new_selected) == num_of_items:
                valid_selections.append(new_selected)
            else:
                nodes.append(new_selected)
    
    return valid_selections


def permutations_with_replacements_v3[T](lst: list[T], num_of_items: int) -> list[tuple[T]]:
    def permutations_iter(lst: list[T], num_of_items: int) -> Iterator[tuple[T]]:
        if len(lst) == 0:
            return

        if num_of_items == 0:
            yield ()
            return

        yield from ((val,) + perm
                    for perm in permutations_iter(lst, num_of_items - 1)
                    for val in lst)
    
    return list(permutations_iter(lst, num_of_items))