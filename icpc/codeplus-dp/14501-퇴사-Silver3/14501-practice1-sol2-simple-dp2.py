"""
앞에서부터 채우기
"""
n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * (n + 1)  # dp[i]: i일까지의 최대 수익

for i in range(n):
    # 현재까지의 최대 수익을 다음 날로 전달
    dp[i + 1] = max(dp[i + 1], dp[i])
    
    # i일의 상담을 선택하는 경우
    if i + schedule[i][0] <= n:
        dp[i + schedule[i][0]] = max(dp[i + schedule[i][0]], ## 상담을 안할때 (다음 회차로 이동)
                                      dp[i] + schedule[i][1]) ## 상담을 할때

print(dp[n])