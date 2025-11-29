import sys
input = sys.stdin.readline

N = int(input())

dp = [0] * (N+1)

for i in range(N+1):
    dp[i] = i ## 최악의 경우 : i를 만들 때 1(1**2=1)을 i개를 이용해서 만드는 경우

    j=0
    while j*j <= i:
        dp[i] = min(dp[i], dp[i-(j*j)]+1)
        j+=1

print(dp[N])