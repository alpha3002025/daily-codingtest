import sys
input = sys.stdin.readline

N,M = map(int,input().split())
checkers_duration = [int(input()) for _ in range(N)]

## 시간의 총합의 최소,최대(=가장 오래걸리는 심사위원에게 M명이 모두 심사를 받는경우)
left,right = 1, max(checkers_duration)*M

answer = 0
while left <= right:
    ## mid = 현재 가정한 시간의 총합
    mid = (left + right)//2

    passed_cnt = 0
    ## 심사위원 한명이 끝나야 다른 심사위원이 심사를 하는 구조가 아니라
    ## n 명의 심사위원이 있으면 n명이 동시에 심사를 할 수 있기에 각각의 mid//duration 을 합한다.
    ## 즉, 시간 mid 에 대해 n 명의 심사위원 각각이 모두 심사를 마쳤을 때 총합을 구하는 로직
    for duration in checkers_duration:
        passed_cnt += mid//duration
    
    if passed_cnt >= M:
        ## 총 걸리는 시간의 합을 더 줄여서 타이트하게 맞춰봐야 한다.
        right = mid-1
        answer = mid
    else:
        left = mid+1

print(answer)
