import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [0]*N
for i in range(N):
    dp[i] = A[i]
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], A[i]+dp[j])

print(max(dp))
