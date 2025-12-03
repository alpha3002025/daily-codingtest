import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

## init
R,G,B = 0,1,2
dp = [[0]*3 for _ in range(N)]

## setup
dp[0][R] = board[0][R]
dp[0][G] = board[0][G]
dp[0][B] = board[0][B]

## calc
total = 0
for i in range(1, N):
    dp[i][R] = min(dp[i-1][G], dp[i-1][B]) + board[i][R]
    dp[i][G] = min(dp[i-1][R], dp[i-1][B]) + board[i][G]
    dp[i][B] = min(dp[i-1][R], dp[i-1][G]) + board[i][B]

## answer
print(min(dp[N-1]))