import sys
input = sys.stdin.readline

N = int(input())
budgets = list(map(int, input().split()))
M = int(input())

## right : 최악의 경우 가장 예산이 많이 드는 예산으로 배정
left,right = 1, max(budgets)

anser = 0
while left <= right:
    ## 현재 step 에서의 예산 k 를 가정
    mid = (left + right) // 2
    
    total_used = 0
    for budget in budgets:
        if budget >= mid:
            total_used += mid
        else: ## budget 이 더 작을 경우는 budget 만을 사용 
            total_used += budget
    
    if total_used <= M: ## 예산은 적게 사용할수록 최적 (더 많이 쓰는 것은 불가능)
        ## 예산을 늘여서 최대한 가깝게 맞춰본다.
        left = mid+1
        answer = mid
    else:
        right = mid-1

print(answer)