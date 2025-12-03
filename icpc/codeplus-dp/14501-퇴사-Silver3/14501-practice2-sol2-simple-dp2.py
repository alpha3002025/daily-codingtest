import sys
input = sys.stdin.readline

N = int(input())
schedule = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0] * (N+1)

for i in range(N):
    dp[i+1] = max(dp[i], dp[i+1])
    duration, pay = schedule[i]

    if i + duration <= N:
        dp[i + duration] = max(dp[i + duration], dp[i]+pay)


print(dp[N])