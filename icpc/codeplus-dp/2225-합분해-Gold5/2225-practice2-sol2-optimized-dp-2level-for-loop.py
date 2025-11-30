import sys
input = sys.stdin.readline

N,K = map(int, input().split())
MOD = 1_000_000_000

## N 을 K 개의 수로 표현하는 경우
dp = [[0]*(N+1) for _ in range(K+1)]

for i in range(N+1):
    # 1개의 수로 i를 만드는 방법은 1개 = 자기자신
    dp[1][i] = 1


for k in range(2, K+1):
    dp[k][0] = 1 ## k 개의 수로 0을 포현하는 방법
    for n in range(1, N+1):
        dp[k][n] = (dp[k][n-1] + dp[k-1][n]) % MOD ## k개의 수로 n-1 을 만드는 방법 + k-1 개의 수로 n 을 만드는 방법

print(dp[K][N])