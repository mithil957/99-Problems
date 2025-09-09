---
tags:
    - List
    - Beginner
---

# Palindrome

Find out whether a list is a palindrome. A palindrome is its own reverse.

=== "Test"
    ```python
        def test_palindrome(solution):
            assert solution([]) == True
            assert solution([1]) == True
            assert solution([1, 1]) == True
            assert solution([1, 2]) == False
            assert solution([1, 2, 3]) == False
            assert solution(['a', 'b', 'b', 'a']) == True
            assert solution(['a', 'b', 'c', 'b', 'a']) == True
            assert solution(['r', 'a', 'c', 'e', 'c', 'a', 'r']) == True
    
    ```

=== "Direct"
    ```python
    def check_palindrome_v1[T](lst: list[T]) -> bool:
        return lst == lst[::-1]
    ```

=== "Recursive"
    ```python
    def check_palindrome_v2[T](lst: list[T]) -> bool:
        match lst:
            case []: return True
            case [a]: return True
            case [first, *body, last]: 
                return (first == last) and check_palindrome_v2(body)
    ```

=== "Tail Recursive"
    ```python
    def check_palindrome_v3[T](lst: list[T]) -> bool:
        def aux(current_lst: list[T], same_so_far: bool) -> bool:
            if not same_so_far: return False
            
            match current_lst:
                case []: return True
                case [a]: return True
                case [first, *body, last]: 
                    return aux(body, first == last)
    
        return aux(lst, True)
    ```

