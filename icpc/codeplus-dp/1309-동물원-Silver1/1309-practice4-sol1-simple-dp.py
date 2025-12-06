import sys
input = sys.stdin.readline

N = int(input())

NOBODY,LEFT,RIGHT = 0,1,2
dp = [[0]*3 for _ in range(N+1)]

dp[1][NOBODY] = 1
dp[1][LEFT] = 1
dp[1][RIGHT] = 1

for i in range(2, N+1):
    dp[i][NOBODY] = (dp[i-1][LEFT] + dp[i-1][RIGHT] + dp[i-1][NOBODY])%9901
    dp[i][LEFT] = (dp[i-1][NOBODY] + dp[i-1][RIGHT])%9901
    dp[i][RIGHT] = (dp[i-1][NOBODY] + dp[i-1][LEFT])%9901

print(sum(dp[N])%9901)