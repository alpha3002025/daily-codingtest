N = int(input())

# dp[i][j]: 길이가 i이고 마지막 숫자가 j인 오르막수의 개수
dp = [[0] * 10 for _ in range(N + 1)]

# 초기값: 길이가 1인 경우
for j in range(10):
    dp[1][j] = 1

# DP 테이블 채우기
for i in range(2, N + 1):
    for j in range(10):
        # 마지막 숫자가 j일 때, 이전 숫자는 0~j 가능
        for k in range(j + 1):
            dp[i][j] += dp[i-1][k]
            dp[i][j] %= 10007

# 길이가 N인 모든 오르막수의 합
answer = sum(dp[N]) % 10007
print(answer)