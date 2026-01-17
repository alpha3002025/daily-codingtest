def solution(A,B):
    A.sort(reverse = True)
    B.sort()
    
    total = 0
    for a,b in zip (A, B):
        total +=  a*b

    return total