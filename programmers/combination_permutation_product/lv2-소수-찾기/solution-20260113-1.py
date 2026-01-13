from itertools import permutations
from math import isqrt

def is_prime(n):
    if n == 1 or n == 0:
        return False
    
    for curr in range(2, isqrt(n)+1):
        if n % curr == 0:
            return False
    return True
        

def solution(numbers):
    prime_numbers = set()
    
    for window_size in range(1, len(numbers)+1):
        for curr_perm in permutations(numbers, window_size):
            curr_number = int("".join(curr_perm))
            
            if is_prime(curr_number):
                prime_numbers.add(curr_number)
    
    return len(prime_numbers)

print(solution("17"))
print(solution("011"))