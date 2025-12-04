import sys
input = sys.stdin.readline

## input
N = int(input())

## init
dp = [[0]*3 for _ in range(N)]
NOBODY,LEFT,RIGHT = 0,1,2

## setup
dp[0][NOBODY]=1
dp[0][LEFT]=1
dp[0][RIGHT]=1

## calc
for i in range(1, N):
    dp[i][NOBODY] = (dp[i-1][LEFT] + dp[i-1][RIGHT] + dp[i-1][NOBODY]) % 9901
    dp[i][LEFT] = (dp[i-1][NOBODY] + dp[i-1][RIGHT]) % 9901
    dp[i][RIGHT] = (dp[i-1][NOBODY] + dp[i-1][LEFT]) % 9901

## answer
print(sum(dp[N-1])%9901)