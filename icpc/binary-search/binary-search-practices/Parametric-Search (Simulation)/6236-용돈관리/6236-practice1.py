import sys

N,M = map(int, sys.stdin.readline().split())
moneys = [int(input()) for _ in range(N)]

moneys.sort()

left,right = max(moneys),sum(moneys)

answer = 0
while left <= right:
    mid = (left + right) // 2

    cnt = 0
    total = 0
    for money in moneys:
        if total + money <= mid: ## 이전 값 + money 가 K 미만일때, 모두 소모
            total += money
        else: ## K 를 초과할때 (목표값도달) 카운팅
            cnt += 1
            total = 0
            total += money
    
    if cnt > M: ## M 번을 넘어간다면 최대한 더 소모할수 있도록 더 큰 영역으로 넘어가본다.
        left = mid+1
    else: ## M 번 이하일경우 금액이 너무 큰 것이기에 작은 영역으로 이동
        right = mid-1
        answer = mid

print(f"{answer}")