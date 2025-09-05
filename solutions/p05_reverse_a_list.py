# Reverse a list

def reverse_list_v1[T](lst: list[T]) -> list[T]:
    return lst[::-1]

def reverse_list_v2[T](lst: list[T]) -> list[T]:
    match lst:
        case []: return []
        case [a]: return [a]
        case [head, *tail]: return reverse_list_v2(tail) + [head]

