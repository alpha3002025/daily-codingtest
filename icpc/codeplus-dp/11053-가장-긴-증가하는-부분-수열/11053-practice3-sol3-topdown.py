import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [-1] * N

def solve(i):
    """A[i]로 끝나는 가장 긴 증가 부분 수열의 길이"""
    if dp[i] != -1:
        return dp[i]
    
    dp[i] = 1
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], solve(j)+1)
    
    return dp[i]

result = 0
for i in range(N):
    result = max(result, solve(i))
print(result)
