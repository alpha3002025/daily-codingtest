"""
11053 : 증가수열에서 오름차순 연속 부분수열 중 가장 큰 '길이'
11055 : 증가수열에서 오름차순 연속 부분수열 중 가장 큰 '합'
11722 : 감소수열에서 내림차순 연속 부분수열 중 가장 큰 '길이'
"""

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [0]*N

for i in range(N):
    dp[i] = 1
    for j in range(i):
        if A[j] > A[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))