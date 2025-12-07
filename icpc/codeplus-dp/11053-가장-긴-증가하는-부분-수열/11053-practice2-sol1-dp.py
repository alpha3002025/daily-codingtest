"""
11053 : 증가수열에서 오름차순 연속 부분수열 중 가장 큰 '길이'
11055 : 증가수열에서 오름차순 연속 부분수열 중 가장 큰 '합'
11722 : 감소수열에서 내림차순 연속 부분수열 중 가장 큰 '길이'
"""

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))