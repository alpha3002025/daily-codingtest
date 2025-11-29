import sys
input = sys.stdin.readline

T = int(input())

memo = {}

def dp(n):
    global memo

    if n in memo:
        return memo[n]
    
    if n < 0:
        return 0
    
    if n == 0: ## 1,2,3 중 하나의 합으로 구성될수 있는 경우
        return 1
    
    memo[n] = dp(n-1) + dp(n-2) + dp(n-3)
    return memo[n]

for _ in range(T):
    n = int(input())
    result = dp(n)
    print(result)