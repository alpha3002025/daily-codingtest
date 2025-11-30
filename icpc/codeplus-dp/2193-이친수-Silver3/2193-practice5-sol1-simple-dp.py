import sys
input = sys.stdin.readline

N = int(input())

## dp[i][j] : i자리수의 숫자중 j=0,1 로 시작하는 경우의 수
dp = [[0]*2 for _ in range(N+1)]

dp[1][0] = 0
dp[1][1] = 1

for i in range(2, N+1):
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    dp[i][1] = dp[i-1][0] ## i 번째가 1로 시작해야 한다면, i-1 번째는 0으로 시작해야 한다. (1 중복(x))

print(dp[N][0] + dp[N][1])