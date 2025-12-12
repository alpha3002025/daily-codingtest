import sys
input = sys.stdin.readline

N,M = map(int,input().split())
durations = [int(input()) for _ in range(N)]

## 상근이와 친구들이 심사를 마치는데 걸리는 시간의 최솟값


## 걸리는 시간의 총합의 최소,최대
left, right = 1, max(durations)*M

answer = 0
while left <= right:
    mid = (left+right)//2

    cnt = 0
    for duration in durations:
        cnt += mid//duration

    if cnt >= M:
        ## 시간의 총합이 줄면 cnt 은 줄어들고
        ## 시간의 총합이 늘어나면 cnt 는 늘어난다.
        right = mid-1
        answer = mid
    else:
        left = mid+1

print(answer)