n = int(input())

# dp 테이블 초기화
dp = [0] * (n + 1)

# 각 숫자에 대해 계산
for i in range(1, n + 1):
    dp[i] = i  # 최악의 경우: 1²을 i번 사용
    
    # i보다 작거나 같은 모든 제곱수에 대해 확인
    j = 1
    while j * j <= i:
        dp[i] = min(dp[i], dp[i - j*j] + 1)
        j += 1

print(dp[n])