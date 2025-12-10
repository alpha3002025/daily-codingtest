import sys
input = sys.stdin.readline

N,M = map(int, input().split())

durations = [int(input()) for _ in range(N)]

## M 명이 심사를 받는데, 시간이 최소가 되도록 하는 최소시간 
left,right = 1,max(durations)*M

while left < right:
    mid = (left+right)//2 ## 걸리는 총 시간 합을 가정
    
    passed_person_cnt = 0
    time_total = 0
    for duration in durations:
        passed_person_cnt += mid//duration
    
    ## 통과한 사람이 M 을 넘어서면, 지나치게 설정한 시간을 줄여야 함
    if passed_person_cnt >= M:
        right = mid-1
        answer = mid
    else:
        left = mid+1

print(answer)



