# Find the number of elements of a list

def number_of_elements_in_list_v1[T](lst: list[T]) -> int:
    return len(lst)

def number_of_elements_in_list_v2[T](lst: list[T]) -> int:
    match lst:
        case []: return 0
        case [a]: return 1
        case [a, *tail]: return 1 + number_of_elements_in_list_v2(tail)

def number_of_elements_in_list_v3[T](lst: list[T]) -> int:
    def aux(current_lst: list[T], accumulated: int) -> int:
        match current_lst:
            case []: return accumulated
            case [a]: return 1 + accumulated
            case [a, *tail]: return aux(tail, accumulated + 1)
    
    return aux(lst, 0)