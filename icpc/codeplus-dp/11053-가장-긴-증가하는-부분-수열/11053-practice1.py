import sys
N = int(input())
numbers = list(map(int, sys.stdin.readline().split()))

dp = [1] * len(numbers)

latest_max = numbers[0]
for i in range(1, len(numbers)):
    if latest_max < numbers[i]:
        dp[i]=dp[i-1]+1
    else:
        dp[i]=dp[i-1]
    latest_max = max(latest_max, numbers[i])

print(dp[-1])