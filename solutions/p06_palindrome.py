# Check if list is a palindrome

def check_palindrome_v1[T](lst: list[T]) -> bool:
    return lst == lst[::-1]

def check_palindrome_v2[T](lst: list[T]) -> bool:
    match lst:
        case []: return True
        case [a]: return True
        case [first, *body, last]: 
            return (first == last) and check_palindrome_v2(body)