import sys
sys.setrecursionlimit(100001)

n = int(input())

# 메모이제이션 테이블
memo = [-1] * (n + 1)
memo[0] = 0

def solve(x):
    if memo[x] != -1:
        return memo[x]
    
    result = x  # 최악의 경우: 1²을 x번 사용
    
    j = 1
    while j * j <= x:
        result = min(result, solve(x - j*j) + 1)
        j += 1
    
    memo[x] = result
    return result

print(solve(n))