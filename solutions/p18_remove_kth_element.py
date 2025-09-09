# Remove the kth element from a list
# Out of bounds 'idx' returns the input

def remove_kth_element_v1[T](lst: list[T], remove_at: int) -> list[T]:
    def aux(working_lst: list[T], current_idx: int) -> list[T]:
        match (current_idx == remove_at, current_idx >= len(lst)):
            case (_, True): 
                return working_lst
            case (True, _): 
                return aux(working_lst, current_idx + 1)
            case (False, _): 
                return aux(working_lst + [lst[current_idx]], current_idx + 1)
            
    return aux([], 0) if 0 <= remove_at < len(lst) else lst


def remove_kth_element_v2[T](lst: list[T], remove_at: int) -> list[T]:
    if 0 <= remove_at < len(lst): 
        lst.pop(remove_at)
    return lst


def remove_kth_element_v3[T](lst: list[T], remove_at: int) -> list[T]:
    return [elem for idx, elem in enumerate(lst) if idx != remove_at]


def remove_kth_element_v4[T](lst: list[T], remove_at: int) -> list[T]:
    if 0 <= remove_at < len(lst): 
        return lst[:remove_at] + lst[remove_at+1:]
    return lst