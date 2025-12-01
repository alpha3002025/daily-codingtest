n = int(input())
cost = []
for _ in range(n):
    cost.append(list(map(int, input().split())))

# DP 테이블 초기화
dp = [[0] * 3 for _ in range(n)]

# 첫 번째 집 초기화
dp[0][0] = cost[0][0]  # 빨강
dp[0][1] = cost[0][1]  # 초록
dp[0][2] = cost[0][2]  # 파랑

# 두 번째 집부터 N번째 집까지
for i in range(1, n):
    # i번째 집을 빨강으로 칠할 때
    dp[i][0] = cost[i][0] + min(dp[i-1][1], dp[i-1][2])
    # i번째 집을 초록으로 칠할 때
    dp[i][1] = cost[i][1] + min(dp[i-1][0], dp[i-1][2])
    # i번째 집을 파랑으로 칠할 때
    dp[i][2] = cost[i][2] + min(dp[i-1][0], dp[i-1][1])

# 마지막 집을 세 가지 색으로 칠한 경우 중 최솟값
print(min(dp[n-1][0], dp[n-1][1], dp[n-1][2]))