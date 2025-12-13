import sys
input = sys.stdin.readline

N,K = map(int, input().split())
wines = [int(input()) for _ in range(N)]

left,right = 0, max(wines)

answer = 0
while left <= right:
    mid = (left + right) // 2
    
    drink_cnt = 0
    for wine in wines:
        drink_cnt += wine//mid ## (// : 남는 것은 버린다.)

    ## 최대한 많은 양을 분배해야 한다
    if drink_cnt >= K:
        left = mid+1
        answer = mid
    else:
        right = mid-1

print(answer)