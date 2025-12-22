def solution(x, y, n):
    dp = [float('inf')] * (y+1)
    dp[x] = 0
    
    for curr in range(x, y):
        if dp[curr] == float('inf'):
            continue
            
        if curr + n <= y:
            dp[curr + n] = min(dp[curr] + 1, dp[curr + n])
        if curr * 2 <= y:
            dp[curr * 2] = min(dp[curr] + 1, dp[curr * 2])
        if curr * 3 <= y:
            dp[curr * 3] = min(dp[curr] + 1, dp[curr * 3])
    
    return -1 if dp[y] == float('inf') else dp[y]


print(solution(10,40,5))
print(solution(10,40,30))
print(solution(2,5,4))