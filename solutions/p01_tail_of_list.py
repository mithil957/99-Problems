# Returns the last element of a list

def tail_of_list_v1[T](lst: list[T]) -> T | None:
    match lst:
        case []: return None
        case [a]: return a
        case [*front, last]: return last # OR return tail_of_list(lst[1:])

def tail_of_list_v2[T](lst: list[T]) -> T | None:
    match lst:
        case []: return None
        case [a]: return a
        case [head, *tail]: return tail_of_list_v2(tail)

def tail_of_list_v3[T](lst: list[T]) -> T | None:
    return lst[-1] if len(lst) > 0 else None