import sys
input = sys.stdin.readline

N,M = map(int, input().split())
woods = list(map(int, input().split()))

left,right = 1, max(woods)

answer = 0
while left <= right:
    mid = (left + right)//2
    remain_total = 0

    for wood in woods:
        if wood >= mid:
            remain_total += wood-mid

    ## 남아있는 나무의 길이를 최대로 하되, 자르려는 나무의 길이도 최대여야 한다.
    if remain_total >= M: 
        left = mid+1 ## 남아있는 나무의 길이를 더 줄여서 M에 최대한 근접하도록 left 를 큰 범위로 이동
    else:
        right = mid-1 ## M개에 도달하지 못했다. 현재 나무의 길이가 너무 크다는 이야기다.

print(right) ## 나무를 최소로 잘라야 한다.