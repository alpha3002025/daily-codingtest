import sys

N,M = map(int, sys.stdin.readline().split())
woods = list(map(int, sys.stdin.readline().split()))

left,right = 1, max(woods)

while left <= right:
    mid = (left + right) // 2
    total = 0 

    for wood in woods:
        if wood >= mid:
            total+= wood - mid ## 큰 나무를 찾아서 벤다.

    ## 목표값보다 크면
    if total >= M: 
        left = mid+1
    ## 그 외의 경우
    else:
        right = mid-1


print(f"{right}")