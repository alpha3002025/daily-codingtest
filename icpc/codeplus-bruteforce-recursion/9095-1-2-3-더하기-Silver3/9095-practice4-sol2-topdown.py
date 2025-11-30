import sys
input = sys.stdin.readline

dp = [0] * 11
T = int(input())

def backtracking(n):
    if n < 0:
        return 0
    
    if n == 0: ## 1,2,3 중 하나의 합으로 구성될 수 있는 경우
        return 1
    
    if dp[n] != 0:
        return dp[n]
    
    dp[n] = backtracking(n-1) + backtracking(n-2) + backtracking(n-3)
    return dp[n]

for _ in range(T):
    result = backtracking(int(input()))
    print(result)