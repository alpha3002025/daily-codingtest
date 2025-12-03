import sys
input = sys.stdin.readline

N = int(input())
budgets = list(map(int, input().split()))
M = int(input())

left,right = 1, max(budgets)
answer = right

while left <= right:
    mid = (left + right) // 2
    used_budget = 0

    for budget in budgets:
        if budget >= mid:
            used_budget += mid
        else:
            used_budget += budget
    
    ## 사용된 예산이 M 이내의 범위일 경우 더 줄여본다.
    if used_budget <= M:
        answer = mid
        left = mid+1 ## 예산액 이내일 경우 더 땡겨서(올려서) 타이트하게 맞춰본다.
    else:
        right = mid-1 ## 예산액을 넘어서는 경우 예산액의 범위를 작은 범위로 조정한다.

print(answer)