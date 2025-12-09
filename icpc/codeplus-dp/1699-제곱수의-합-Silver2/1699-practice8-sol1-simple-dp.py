import sys
input = sys.stdin.readline

N = int(input())

dp = [0] * (N+1)
dp[1] = 1

for i in range(1,N+1):
    dp[i]=i ### 1 로 모두 합하는 경우
    j=1
    while j*j <= i:
        dp[i] = min(dp[i], dp[i - j*j]+1)
        j+=1

print(dp[N])