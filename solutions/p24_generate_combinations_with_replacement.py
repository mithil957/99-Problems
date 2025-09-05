# Generate the combinations of K objects from the N elements of a list 
# Repeats are allowed

from collections import deque
from collections.abc import Iterator

def combinations_with_replacement_v1[T](lst: list[T], num_of_items: int) -> list[tuple[T]]:
    if num_of_items == 0: return [()]
    valid_selections = []

    def aux(selected: tuple[T], remaining_choices: list[T]):
        if len(selected) == num_of_items:
            valid_selections.append(selected)
            return

        for idx, choice in enumerate(remaining_choices):
            aux(selected + (choice,), remaining_choices[idx:])
    
    aux((), lst)
    return valid_selections


def combinations_with_replacement_v2[T](lst: list[T], num_of_items: int) -> list[tuple[T]]:
    if num_of_items == 0: return [()]
    valid_selections = []
    nodes = deque([((), lst)])

    while nodes:
        selected, remaining_choices = nodes.popleft()

        for idx, val in enumerate(remaining_choices):
            new_selected = selected + (val,)
            new_remaining_choices = remaining_choices[idx:]

            if len(new_selected) == num_of_items:
                valid_selections.append(new_selected)
            else:
                nodes.append((new_selected, new_remaining_choices))
    
    return valid_selections


def combinations_with_replacement_v3[T](lst: list[T], num_of_items: int) -> list[tuple[T]]:
    def combinations_iter(lst: list[T], num_of_items: int) -> Iterator[tuple[T]]:
        if len(lst) == 0:
            return
        
        if num_of_items == 0:
            yield ()
            return
        
        head, *tail = lst
        yield from ((head,) + combo for combo in combinations_iter(lst, num_of_items - 1))
        yield from combinations_iter(tail, num_of_items)
    
    return list(combinations_iter(lst, num_of_items))