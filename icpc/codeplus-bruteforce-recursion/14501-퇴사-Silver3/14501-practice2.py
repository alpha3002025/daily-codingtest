"""
N+1 일날 퇴사하고, N 일까지 일하는 개념에 대해 헷갈렸을때 풀었던 방식
"""

import sys

N = int(sys.stdin.readline().strip())

schedule = [(-1,-1)]
for _ in range(N):
    time, price = map(int, input().split())
    schedule.append((time, price))

memo = [-1] * (N+1)


def dp(curr_day):
    if curr_day >= N+1:
        return 0
    
    if memo[curr_day] != -1:
        return memo[curr_day]
    

    how_long, curr_price = schedule[curr_day]

    ## 상담할때
    profit1 = 0
    if curr_day + how_long <= N+1:
        profit1 = curr_price + dp(curr_day + how_long)

    ## 상담 안할때
    profit2 = dp(curr_day+1)

    memo[curr_day] = max(profit1, profit2)
    return memo[curr_day]

print(dp(1))