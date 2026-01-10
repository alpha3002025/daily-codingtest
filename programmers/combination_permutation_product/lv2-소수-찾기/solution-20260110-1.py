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
    answer = 0
    number_list = list(numbers)
    prime_set = set()
    
    for window_size in range(1, len(number_list)+1):
        for p in permutations(number_list, window_size):
            n = int("".join(p))
    
            if is_prime(n):
                ## answer += 1 ## 1 만 계속 나오는 경우도 있다. 
                ##    (e.g. 1115 의 순열은 1, 1, 1, 5, ... 으로 시작된다.)
                ## 따라서 set 으로 prime 의 종류 수를 체크한다.
                prime_set.add(n)
    
    return len(prime_set)


print(solution("17"))
print(solution("011"))