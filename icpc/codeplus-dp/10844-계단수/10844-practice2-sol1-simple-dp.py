import sys
input = sys.stdin.readline

N = int(input())
MOD = 1000000000
## i 자리수(자리수 = N)이면서 j로 끝나는 숫자의 개수
dp = [[0] * 10 for _ in range(N+1)]

for i in range(1,10): ## 0으로 시작하는 경우는 배제
    dp[1][i] = 1

for i in range(2, N+1): ## N자리수
    for j in range(10): ## j 로 끝나는 숫자의 개수
        if j > 0:
            dp[i][j] += dp[i-1][j-1]
        if j < 9:
            dp[i][j] += dp[i-1][j+1]
        dp[i][j] %= MOD

answer = sum(dp[N]) % MOD
print(f"{answer}")