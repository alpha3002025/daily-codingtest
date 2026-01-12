from itertools import permutations
from math import isqrt

def is_prime(n):
    if n == 0 or n == 1:
        return False
    
    for div in range(2, isqrt(n)+1):
        if n % div == 0:
            return False
    return True


def solution(numbers):
    total_size = len(numbers)
    prime_set = set()
    
    for window_size in range(1, total_size+1):
        for p in permutations(numbers, window_size):
            curr = int("".join(p))
            if is_prime(curr):
                prime_set.add(curr)
    
    return len(prime_set)


print(solution("17"))
print(solution("011"))
