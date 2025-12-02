"""
2025.12.03
"""
import sys
input = sys.stdin.readline

N,M = map(int, input().split())
testers = [int(input()) for _ in range(N)]

left,right = 1, max(testers)*M
min_duration = right

while left <= right:
    ## 걸리는 시간의 총합 가정
    mid = (left + right)//2

    passed_person_cnt = 0
    for tester in testers:
        passed_cnt = mid//tester
        passed_person_cnt += passed_cnt
    
    if passed_person_cnt >= M:
        right = mid-1
        min_duration = min(min_duration, mid)
    else:
        left = mid+1

print(min_duration)