import sys

N,C = map(int, sys.stdin.readline().split())

positions = [int(input()) for _ in range(N)]
positions.sort()

## 라우터 개수의 최소/최대
left, right = 1, positions[-1] - positions[0]

answer = 0
while left <= right:
    mid = (left + right) // 2
    curr = positions[0]
    router_cnt = 1

    for i in range(len(positions)):
        if positions[i] >= curr + mid:
            router_cnt += 1
            curr = positions[i]
    
    if router_cnt < C:
        ## 다음 mid 계산시 mid 를 낮아지게 해서 라우터 갯수를 늘릴수 있도록 만든다.
        right = mid-1
    else: ## router_cnt >= C
        ## 다음 mid 계산시 mid 를 더 키울수 있게 해서 라우터 갯수를 최소화한다.
        left = mid+1
        answer = mid

print(f"{answer}")