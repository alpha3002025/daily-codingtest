n = int(input())
arr = list(map(int, input().split()))

# dp[i]: i번째 원소를 포함하는 최대 연속합
dp = [0] * n
dp[0] = arr[0]

for i in range(1, n):
    # 이전 연속합에 추가 vs 새로 시작
    dp[i] = max(arr[i], dp[i-1] + arr[i])

# 모든 위치 중 최댓값이 답
answer = max(dp)
print(answer)