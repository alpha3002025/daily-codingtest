def solution(x, y, n):
    INF = float('inf')
    dp = [INF] * (y + 1)
    
    dp[x] = 0
    
    for i in range(x, y):
        # 도달할 수 없는 숫자는 건너뜀
        if dp[i] == INF:
            continue
            
        # 3가지 경우의 수 갱신
        if i + n <= y:
            dp[i + n] = min(dp[i + n], dp[i] + 1)
        if i * 2 <= y:
            dp[i * 2] = min(dp[i * 2], dp[i] + 1)
        if i * 3 <= y:
            dp[i * 3] = min(dp[i * 3], dp[i] + 1)
            
    if dp[y] == INF:
        return -1
        
    return dp[y]


print(solution(10,40,5))
print(solution(10,40,30))
print(solution(2,5,4))