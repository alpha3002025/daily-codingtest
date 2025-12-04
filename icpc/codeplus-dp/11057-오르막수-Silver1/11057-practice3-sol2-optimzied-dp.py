import sys
input = sys.stdin.readline

## input
N = int(input())

## init
dp = [[0]*10 for _ in range(N+1)]

## setup
for i in range(10):
    dp[1][i] = 1

## calc
for i in range(2, N+1):
    # 숫자 0 으로 끝나는 케이스
    dp[i][0] = dp[i-1][0]
    for j in range(1,10):
        ## 흠...
        dp[i][j] = (dp[i][j-1] + dp[i-1][j])%10007

## answer
print(sum(dp[N])% 10007)