N, K = map(int, input().split())
MOD = 1000000000

# dp[k][n] = k개로 n을 만드는 경우의 수
dp = [[0] * (N + 1) for _ in range(K + 1)]

# 초기 조건
for i in range(N + 1):
    dp[1][i] = 1

# DP 테이블 채우기
for k in range(2, K + 1):
    for n in range(N + 1):
        for i in range(n + 1):
            dp[k][n] = (dp[k][n] + dp[k-1][n-i]) % MOD

print(dp[K][N])