from math import gcd

def gcd_from_list(numbers):
    curr = numbers[0]
    for i in range(len(numbers)):
        curr = gcd(curr, numbers[i])
    return curr

def solution(arrayA, arrayB):
    gcd_A = gcd_from_list(arrayA)
    gcd_B = gcd_from_list(arrayB)
    
    is_useless_a = False
    for num in arrayB:
        if num % gcd_A == 0:
            is_useless_a = True
            break
    
    is_useless_b = False
    for num in arrayA:
        if num % gcd_B == 0:
            is_useless_b = True
            break
    
    return 0 if is_useless_a and is_useless_b else max(gcd_A, gcd_B)


print(solution([10, 17], [5, 20]))
print(solution([10, 20], [5, 17]))
print(solution([14, 35, 119], [18, 30, 102]))