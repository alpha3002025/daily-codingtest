import sys
input = sys.stdin.readline

N,K = map(int, input().split())
MOD = 1_000_000_000

## "숫자 'N'을 K개의 수로 표한하기"
## k 개의 수로 n 을 표현하는 방법의 수 
dp = [[0]*(N+1) for _ in range(K+1)]

for i in range(N):
    ## 1개의 수로 i 를 표현하는 방법의 수
    dp[1][i] = 1

## dp 테이블 채우기
## 숫자 n 을 k 개의 수로 표현한다.
for k in range(2, K+1): ## k개의 수로
    for n in range(N+1): ## 숫자 n 을 표현하는 방법의 수
        for i in range(n+1): 
            ## dp[k-1][n-1] = k-1 개의 수로 n-1 을 표현하는 방법의 수
            dp[k][n] = (dp[k][n] + dp[k-1][n-1]) % MOD

print(dp[K][N])