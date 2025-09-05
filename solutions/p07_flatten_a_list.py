# Flatten a nested list structure
# The list is allowed to be arbitrarily deep

from copy import deepcopy

def flatten_list_v1[T](lst: list[T]) -> list[T]:
    def aux(accumulated: list[T], working_lst: list[T]) -> list[T]:
        match working_lst:
            case []: 
                return accumulated
            
            case [nested_list, *tail] if type(nested_list) is list:
                flatten_nested_list = aux([], nested_list)
                return aux(accumulated + flatten_nested_list, tail)

            case [single_element, *tail]: 
                return aux(accumulated + [single_element], tail)
    
    return aux([], lst)


def flatten_list_v2[T](lst: list[T]) -> list[T]:
    accumulated = []
    stack = [deepcopy(lst)]

    while stack:
        print(stack)
        match stack[-1]:
            case []:
                stack.pop()

            case nested_list if type(nested_list) is list:
                stack.append(nested_list.pop(0))

            case single_element:
                stack.pop() 
                accumulated.append(single_element)
    
    return accumulated