import sys
input = sys.stdin.readline

N = int(input())
NA,L,R = 0,1,2
MOD = 9901

dp = [[0]*3 for _ in range(N+1)]

dp[1][NA] = 1
dp[1][L] = 1
dp[1][R] = 1


for i in range(2, N+1):
    dp[i][NA] = (dp[i-1][NA] + dp[i-1][L] + dp[i-1][R]) % MOD
    dp[i][L] = (dp[i-1][NA] + dp[i-1][R]) % MOD
    dp[i][R] = (dp[i-1][NA] + dp[i-1][L]) % MOD

print(sum(dp[N])%MOD)