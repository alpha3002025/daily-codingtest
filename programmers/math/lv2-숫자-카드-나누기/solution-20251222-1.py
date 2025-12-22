from math import gcd

def gcd_from_list(numbers):
    curr = numbers[0]
    for i in range(1, len(numbers)):
        curr = gcd(curr, numbers[i])
    return curr

def solution(arrayA, arrayB):
    gcd_a = gcd_from_list(arrayA)
    gcd_b = gcd_from_list(arrayB)
    
    foundA = False
    for n in arrayB:
        if n % gcd_a == 0:
            foundA = True
            break
    
    
    foundB = False
    for n in arrayA:
        if n % gcd_b == 0:
            foundB = True
            break
    
    return 0 if foundA and foundB else max(gcd_a, gcd_b)