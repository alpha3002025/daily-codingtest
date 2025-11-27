import sys
input = sys.stdin.readline

T = int(input())
MOD = 1000000009
MAX_N = 100000

dp = [[0]*4 for _ in range(MAX_N+1)]

dp[1][1] = 1 ## 1
dp[2][2] = 1 ## 1
dp[3][1] = 1 ## 2+1
dp[3][2] = 1 ## 1+2
dp[3][3] = 1 ## 3

for i in range(4, MAX_N+1):
    ## 마지막이 1로 끝나는 케이스 : 이전 값이 2 또는 3으로 끝나는 경우
    dp[i][1] = (dp[i-1][2] + dp[i-1][3]) % MOD
    ## 마지막이 2로 끝나는 케이스 : 이전 값이 1 또는 3으로 끝나느 경우 
    dp[i][2] = (dp[i-2][1] + dp[i-2][3]) % MOD
    ## 마지막이 3으로 끝나는 케이스 : 이전 값이 1 또는 2로 끝나는 경우
    dp[i][3] = (dp[i-3][1] + dp[i-3][2]) % MOD

for _ in range(T):
    case = int(input())
    result = (dp[case][1] + dp[case][2] + dp[case][3]) % MOD
    print(result)
