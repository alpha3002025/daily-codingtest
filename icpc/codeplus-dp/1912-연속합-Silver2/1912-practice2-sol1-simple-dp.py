import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

dp = [0] * N

for i in range(1, N):
    dp[i] = max(dp[i], dp[i-1] + numbers[i])

max_value = max(dp)
print(-1 if max_value == 0 else max_value)