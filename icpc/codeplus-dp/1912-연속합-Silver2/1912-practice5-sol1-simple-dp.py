import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [0] * len(A)
dp[0] = A[0]

for i in range(1,N):
    #       max(연속 x , 연속 o)
    dp[i] = max(A[i], dp[i-1]+A[i])

print(max(dp))