# Returns the last element of a list

def tail_of_list[T](lst: list[T]) -> T | None:
    match lst:
        case []: return None
        case [a]: return a
        case [*front, last]: return last # OR return tail_of_list(lst[1:])