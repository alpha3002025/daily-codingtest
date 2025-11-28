n = int(input())
arr = list(map(int, input().split()))

# dp[i]: i번째 원소를 마지막으로 하는 LIS의 길이
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        # i번째 원소가 j번째 원소보다 크면
        if arr[j] < arr[i]:
            # j번째까지의 LIS에 i번째 원소를 추가
            dp[i] = max(dp[i], dp[j] + 1)

# 모든 위치에서의 LIS 중 최댓값
print(max(dp))