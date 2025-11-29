import sys
input = sys.stdin.readline


N = int(input())

## i 자리수의 수 일때 j=0 으로 끝나는 수, j=1로 끝나는 수
dp = [[0]*2 for _ in range(N)]

dp[1][0] = 0
dp[1][1] = 1

for i in range(2, N+1):
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    dp[i][1] = dp[i-1][0] ## 1 은 연속될수 없다. 따라서 이전 자리의 수가 0 이어야 한다.

print(f"{dp[N][0] + dp[N][1]}")