"""
뒤에서부터 체우기
"""
n = int(input())
t = [0] * (n + 1)
p = [0] * (n + 1)

for i in range(1, n + 1):
    t[i], p[i] = map(int, input().split())

dp = [0] * (n + 2)  # dp[i]: i일부터 퇴사일까지 얻을 수 있는 최대 수익

# 뒤에서부터 계산
for i in range(n, 0, -1):
    # i일의 상담이 퇴사 전에 끝나는 경우
    if i + t[i] <= n + 1:
        # 상담을 하는 경우 vs 안 하는 경우
        dp[i] = max(p[i] + dp[i + t[i]], dp[i + 1])
    else:
        # 상담이 퇴사 후에 끝나므로 할 수 없음
        dp[i] = dp[i + 1]

print(dp[1])