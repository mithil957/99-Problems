# Find the nth element of a list

def nth_element_of_list_v1[T](lst: list[T], n: int) -> T | None:
    match (lst, n):
        case ([], _): return None
        case ([a, *tail], 0): return a
        case _: return nth_element_of_list_v1(lst[1:], n - 1)


def nth_element_of_list_v2[T](lst: list[T], n: int) -> T | None:
    match 0 <= n < len(lst):
        case True: return lst[n]
        case False: return None