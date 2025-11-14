import sys

N,K = map(int, sys.stdin.readline().split())
bottles = [int(input()) for _ in range(N)]
bottles.sort()

## 최소용량,최대용량
left,right = 1, bottles[-1] ## 1 씩 나눠줘서 K를 채우게 되는 케이스도 있을수 있기에 최소값을 1로 지정

answer = 0
while left <= right:
    mid = (left + right) // 2

    person_cnt = 0
    for bottle in bottles:
        person_cnt += (bottle//mid) ## 몇명에게 줄수 있는지 누적
    
    if K <= person_cnt:
        left = mid+1 ## 더 큰 용량을 찾는다.
        answer = mid
    else:
        right = mid-1 ## 


print(f"{answer}")