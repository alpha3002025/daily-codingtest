import sys
input = sys.stdin.readline

## k 명에게 분배할 수 있는 최대 용량
N,K = map(int, input().split())
drinks = [int(input()) for _ in range(N)]

left,right = 1, max(drinks)

answer = 0
while left <= right:
    mid = (left+right)//2

    cnt = 0
    for drink in drinks:
        cnt += drink // mid
    
    if cnt >= K: ## 더 키워본다. 최대한 많아야 한다는 조건을 맞추기 위해.
        left = mid+1
        answer = mid
    else:
        right = mid-1

print(answer)