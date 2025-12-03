"""
2025/12/03
"""

import sys
input = sys.stdin.readline

N,C = map(int, input().split())
houses = [int(input()) for _ in range(N)]
houses.sort()

left,right = 1, houses[-1] - houses[0]
right_end = houses[-1]

answer = 0

while left <= right:
    mid = (left + right)//2

    ## plain : 단순 for loop 은 시간제한 가능성 있다.
    ## optimized : step (거리)으로 계산하되 그 거리에 포함되는 house 의 갯수 
    count = 1
    last = houses[0]

    for house in houses[1:]:
        if house - last >= mid:
            count += 1
            last = house
    
    if count >= C:
        answer = mid # 가능하면 저장
        left = mid+1 # 더 큰 간격 시도
    else:
        right = mid-1 # 간격 줄이기

print(answer)