DIGITS = "0123456789ABCDEF"

def to_base_n(n, base):
    if n == 0:
        return "0"
    
    result = ""
    while n > 0:
        result += DIGITS[n % base]
        n //= base
    
    return result[::-1]


def solution(n, t, m, p):
    full_str = ""
    num = 0
    
    while len(full_str) < t*m:
        full_str += to_base_n(num, n)
        num += 1
        
    answer = full_str[p-1: t*m: m]
    
    return answer