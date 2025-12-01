N = int(input())
dp = [[0] * 10 for _ in range(N + 1)]

for j in range(10):
    dp[1][j] = 1

for i in range(2, N + 1):
    dp[i][0] = dp[i-1][0]
    for j in range(1, 10):
        dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % 10007

print(sum(dp[N]) % 10007)