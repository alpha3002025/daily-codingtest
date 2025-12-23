import math
from itertools import permutations

def is_prime(number):
    if number < 2:
        return False
    
    limit = int(math.sqrt(number))
    for n in range(2, limit+1):
        if number % n == 0:
            return False
    return True


def solution(numbers):
    number_list = list(numbers)
    number_set = set()
    
    for curr_len in range(1,len(numbers)+1):
        for perm in permutations(number_list, curr_len):
            number_set.add(int("".join(perm)))
    
    cnt = 0
    for number in number_set:
        if is_prime(number):
            cnt+=1
    
    return cnt


print(solution("17"))
print(solution("011"))