# Implement linear recursion which has 4 parts
# A function BC which tells us if we reached the base case
# A function VBC which calculates the value when we reach the base case
# A function A which we apply to state before the recursive call
# A function C which combines the state with the result of the recursive call


from typing import Callable


type State[T] = T
type Result[V] = V

def linear_recursion_v1(state: State,
                        at_base_case: Callable[[State], bool],
                        calculate_base_case: Callable[[State], Result],
                        transform: Callable[[State], State],
                        combine: Callable[[State, Result], Result]) -> Result:
    
    if at_base_case(state):
        return calculate_base_case(state)
    
    recursive_result = linear_recursion_v1(transform(state), 
                                           at_base_case, 
                                           calculate_base_case, 
                                           transform, 
                                           combine)

    return combine(state, recursive_result)


def linear_recursion_v2(state: State,
                        at_base_case: Callable[[State], bool],
                        calculate_base_case: Callable[[State], Result],
                        transform: Callable[[State], State],
                        combine: Callable[[State, Result], Result]) -> Result:
    
    stack = [state]

    while not at_base_case((current_state := transform(stack[-1]))):
        stack.append(current_state)

    result = calculate_base_case(current_state)

    while stack:
        last_state = stack.pop()
        result = combine(last_state, result)

    return result