## sol2 와 비슷하다. sol2 의 경우 for j in range(1, 10) 으로 해서 맨앞자리수는 배제하고 for loop 시작 전에 dp[i][0] = dp[i-1][0]으로 초기화


import sys

N = int(sys.stdin.readline().strip())

dp = [[0] * 10 for _ in range(N + 1)]

# 길이가 1일 때 오르막 수 (각 숫자 1개씩)
for j in range(10):
    dp[1][j] = 1

# DP 진행
for i in range(2, N + 1):  # 자리수 2부터 시작
    for j in range(10):  # 끝나는 숫자 0~9
        if j == 0:
            dp[i][j] = dp[i-1][j]  # 0으로 끝나는 경우는 이전 자리도 0
        else:
            dp[i][j] = dp[i][j-1] + dp[i-1][j]  # 점화식 적용

# 정답 계산 (길이가 N이고 끝자리 숫자가 0~9인 모든 경우의 합)
print(sum(dp[N]) % 10007)