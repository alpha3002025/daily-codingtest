import sys
input = sys.stdin.readline

T = int(input())

MOD = 1_000_000_009
N = 1_000_000
dp = [0]*(N+1)

dp[1] = 1
dp[2] = 2
dp[3] = 4 ## 3, 1+2, 2+1, 1+1+1
### 
# dp[4] = 7 ## 3+1, 1+3, 2+2, 1+1+1+1, 1+1+2, 1+2+1, 2+1+1
# dp[5] = 13 ## dp[2]+dp[3]+dp[4]


for i in range(4, N+1):
    dp[i] = (dp[i-3] + dp[i-2] + dp[i-1])%MOD

for _ in range(T):
    num = int(input())
    print(dp[num])