# Find the last two elements of a list

def last_two_elements_of_a_list_v1[T](lst: list[T]) -> tuple[T, T] | None:
    match lst:
        case [] | [_]: return None
        case [a, b]: return (a, b)
        case [*front, penultimate, last]: return (penultimate, last)


def last_two_elements_of_a_list_v2[T](lst: list[T]) -> tuple[T, T] | None:
    match lst:
        case [] | [_]: return None
        case [a, b]: return (a, b)
        case _: return last_two_elements_of_a_list_v2(lst[1:])
        