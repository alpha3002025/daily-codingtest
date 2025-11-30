N, K = map(int, input().split())
MOD = 1000000000

dp = [[0] * (N + 1) for _ in range(K + 1)]

for i in range(N + 1):
    dp[1][i] = 1

for k in range(2, K + 1):
    dp[k][0] = 1
    for n in range(1, N + 1):
        dp[k][n] = (dp[k][n-1] + dp[k-1][n]) % MOD

print(dp[K][N])