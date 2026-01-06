from itertools import permutations
from math import isqrt


def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    number_list = list(numbers)
    
    prime_set = set()
    ## 순열의 길이 순회
    for curr_length in range(1, len(number_list)+1):
        for curr_perm in permutations(number_list ,curr_length):
            n = int("".join(curr_perm))
            if is_prime(n):
                prime_set.add(n)
    
    return len(prime_set)

print(solution("17"))
print(solution("011"))