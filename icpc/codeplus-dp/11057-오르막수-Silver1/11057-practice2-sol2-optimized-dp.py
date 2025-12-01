import sys
input = sys.stdin.readline

N = int(input())
MOD = 10007

## i 자리수, j 로 끝나는 수
dp = [[0]*10 for _ in range(N+1)]

for i in range(10):
    dp[1][i] = 1

for i in range(2, N+1):
    dp[i][0] = dp[i-1][0]
    for j in range(1, 10):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1])%MOD

print(sum(dp[N])%MOD)