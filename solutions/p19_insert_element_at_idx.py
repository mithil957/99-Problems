# Start counting list elements with 0. Insert the element at the index
# If out of bounds (postive direction), add to the end
# If negative, return input


def insert_element_v1[T](lst: list[T], value: T, insert_at: int) -> list[T]:
    def aux(accumulated: list[T], current_index: int) -> list[T]:
        at_insert_indx = current_index == insert_at
        reached_end = current_index >= len(lst)

        match (at_insert_indx, reached_end):
            case (_, True): 
                return accumulated
            case (True, _): 
                return aux(accumulated + [value, lst[current_index]], current_index + 1)
            case (False, _):
                return aux(accumulated + [lst[current_index]], current_index + 1)
    
    if insert_at >= len(lst) or lst == []: return lst + [value]
    elif insert_at < 0: return lst
    else: return aux([], 0)


def insert_element_v2[T](lst: list[T], value: T, insert_at: int) -> list[T]:
    if insert_at > len(lst): 
        return lst + [value]
    elif insert_at < 0: 
        return lst
    else:
        lst.insert(insert_at, value)
        return lst
    

def insert_element_v3[T](lst: list[T], value: T, insert_at: int) -> list[T]:
    if insert_at < 0: return lst
    else: return lst[:insert_at] + [value] + lst[insert_at:]