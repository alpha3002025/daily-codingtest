import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

dp = [0] * N
dp[0] = numbers[0]

for i in range(1, N):
    dp[i] = max(dp[i-1] + numbers[i], numbers[i])

max_value = max(dp)
print(max_value)