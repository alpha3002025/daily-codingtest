DIGITS = "0123456789ABCDEF"

def to_base_n(num, n):
    if num == 0:
        return "0"
    
    res = ""
    while num > 0:
        res += DIGITS[num%n]
        num //= n
    
    return res[::-1]

def solution(n, t, m, p):
    full_str = ""
    num = 0
    
    ## e.g.
    ## 2개씩 자르는 것을 3번 수행
    # print("0123456789"[0:3*2:2])
    
    while len(full_str) < t*m:
        full_str += to_base_n(num, n)
        num += 1
        
    answer = full_str[p-1 :t*m :m]
    return answer