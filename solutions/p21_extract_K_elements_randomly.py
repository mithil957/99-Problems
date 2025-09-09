# Select K items from a list and return them
# If K is bigger than number of items from list, return None
# The items should come from the list, should be unique

from random import sample, shuffle


def extract_elements_v1[T](lst: list[T], k: int) -> list[T] | None:
    if k > len(lst): return None
    return sample(lst, k)


def extract_elements_v2[T](lst: list[T], k: int) -> list[T] | None:
    if k > len(lst): return None
    copy_lst = lst[:]
    shuffle(copy_lst)
    return copy_lst[:k]