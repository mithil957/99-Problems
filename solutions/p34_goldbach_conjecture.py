# Goldbach's conjecture says that every postive even number > 2 
# is the sum of two primes

from solutions.p29_is_prime import is_prime_v1


def goldbach_v1(target: int) -> tuple[int, int] | None:
    if target < 2 or target % 2 != 0:
        return None
    
    def aux(current_num: int) -> tuple[int, int]:
        if is_prime_v1(current_num) and is_prime_v1(target - current_num):
            return (current_num, target - current_num)
        else:
            return aux(current_num + 1)
    
    return aux(2)


def goldbach_v2(target: int) -> tuple[int, int] | None:
    if target < 2 or target % 2 != 0:
        return None
    
    def sieve(target: int) -> list[int]:
        possible_primes = dict.fromkeys(range(3, target + 1, 2))
        primes = [2]
        while possible_primes:
            curr_prime = next(iter(possible_primes))
            primes.append(curr_prime)
            possible_primes.pop(curr_prime)

            k = 1
            while (eliminated := curr_prime * (2 * k + 1)) < target:
                possible_primes.pop(eliminated, None)
                k += 1
        
        return primes

    def twosum(target: int, items: list[int]) -> tuple[int, int] | None:
        left, right = 0, len(items) - 1
        while left <= right:
            left_item, right_item = items[left], items[right]
            curr_sum = left_item + right_item
            if curr_sum == target: return (left_item, right_item)
            elif curr_sum < target: left += 1
            else: right -= 1
        
        return None
    
    primes = sieve(target)
    return twosum(target, primes)
    



        
