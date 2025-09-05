# Sorting a list of lists according to length of sublists

from typing import Callable

type Comparison[T] = Callable[[T, T], bool]

def merge_sort[T](lst: list[T], less_than: Comparison) -> list[T]:
    def merge_sorted_lists(left_list: list[T], right_list: list[T]) -> list[T]:
        match (left_list, right_list):
            case ([], _) | (_, []):
                return left_list + right_list

            case ([left_head, *left_tail], [right_head, *right_tail]):
                if less_than(left_head, right_head):
                    return [left_head] + merge_sorted_lists(left_tail, right_list)
                else:
                    return [right_head] + merge_sorted_lists(left_list, right_tail)
    
    match lst:
        case [] | [_]: 
            return lst
        case _: 
            mid_point = len(lst) // 2
            left, right = lst[:mid_point], lst[mid_point:]
            sorted_left, sorted_right = merge_sort(left, less_than), merge_sort(right, less_than) 
            return merge_sorted_lists(sorted_left, sorted_right)
    

def sort_sublists_by_length_v1[T](lst: list[list[T]]) -> list[list[T]]:
    return merge_sort(lst, lambda l, r: len(l) < len(r))


def sort_sublists_by_length_v2[T](lst: list[list[T]]) -> list[list[T]]:
    return sorted(lst, key=lambda l: len(l))
