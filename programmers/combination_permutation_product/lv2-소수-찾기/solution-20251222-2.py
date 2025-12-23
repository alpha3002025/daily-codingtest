import math
from itertools import permutations

def is_prime(number):
    if number < 2:
        return False
    
    for div in range(2, int(math.sqrt(number))+1):
        if number % div == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    number_list = list(numbers)
    
    prime_set = set()
    
    for curr_len in range(1, len(number_list)+1):
        for curr_perm in permutations(number_list, curr_len):
            curr_number = int("".join(curr_perm))
            if is_prime(int(curr_number)):
                prime_set.add(int(curr_number))
    
    return len(prime_set)