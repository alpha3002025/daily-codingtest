import sys
input = sys.stdin.readline

## input
N = int(input())

## setup
#### i 자리수의 숫자에서 j로 시작하는 수를 구성하는 방법의 수
dp = [[0]*10 for _ in range(N+1)]
for i in range(10):
    dp[1][i] = 1

## calc
for i in range(2, N+1):
    for j in range(10): # j=0,1,2,... 일차원적인 구성이기에 for loop 하나 더 필요
        for k in range(j+1): # k=[0],[0,1],[0,1,2], ... 
            dp[i][j] += dp[i-1][k] ## i-1 자리수에 대해 k로 시작하는 경우의 수를 합산
            dp[i][j] %= 10007

## answer
answer = sum(dp[N]) % 10007
print(answer)