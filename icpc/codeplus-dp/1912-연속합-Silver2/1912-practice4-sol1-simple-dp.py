import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

dp = [0] * (N)

for i in range(N):
    dp[i] = max(dp[i-1] + numbers[i], numbers[i])

print(max(dp))