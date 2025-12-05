import sys
input = sys.stdin.readline

N = int(input())

dp = [0] * (N+1)

for i in range(N+1):
    dp[i] = i
    
    j=1
    while j*j <= i:
        dp[i] = min(dp[i - j*j]+1, dp[i])
        j+=1

print(dp[N])