# Reverse a list

def reverse_list_v1[T](lst: list[T]) -> list[T]:
    return lst[::-1]

def reverse_list_v2[T](lst: list[T]) -> list[T]:
    match lst:
        case []: return []
        case [a]: return [a]
        case [head, *tail]: return reverse_list_v2(tail) + [head]

def reverse_list_v3[T](lst: list[T]) -> list[T]:
    def aux(current_lst: list[T], accumlated: list[T]) -> list[T]:
        match current_lst:
            case []: return accumlated
            case [a]: return accumlated + [a]
            case [head, *tail]: return aux(tail, accumlated + [head])
    
    return aux(lst, [])