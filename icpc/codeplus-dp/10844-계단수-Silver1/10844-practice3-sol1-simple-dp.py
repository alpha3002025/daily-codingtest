import sys
input = sys.stdin.readline

N = int(input())
MOD = 1000000000

dp = [[0]*(10) for _ in range(N+1)]

for i in range(10):
    dp[1][i] = 1

for i in range(2, N+1):
    for j in range(10):
        if j > 0:
            dp[i][j] += dp[i-1][j-1] ## (i-1 자리수에서 j-1 로 끝나는 수의 갯수)
        if j < 9:
            dp[i][j] += dp[i-1][j+1] ## (i-1 자리수에서 j+1 로 끝나는 수의 갯수)

        dp[i][j] %= MOD

answer = sum(dp[N]) % MOD
print(f"{answer}")