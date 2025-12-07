"""
11053 : 증가수열에서 오름차순 연속 부분수열 중 가장 큰 '길이'
11055 : 증가수열에서 오름차순 연속 부분수열 중 가장 큰 '합'
11722 : 감소수열에서 내림차순 연속 부분수열 중 가장 큰 '길이'
"""

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [-1] * N  # -1은 아직 계산 안됨을 의미

def solve(i):
    """A[i]로 끝나는 가장 긴 증가 부분 수열의 길이"""
    if dp[i] != -1:
        return dp[i]
    
    dp[i] = 1  # 최소 자기 자신만 포함
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], solve(j) + 1)
    
    return dp[i]

# 모든 위치에서 끝나는 LIS 중 최댓값
result = 0
for i in range(N):
    result = max(result, solve(i))

print(result)