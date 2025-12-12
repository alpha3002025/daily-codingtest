import sys
input = sys.stdin.readline

N = int(input())
budgets = list(map(int, input().split()))
M = int(input())


left,right = 1, max(budgets)

answer = 0
while left <= right:
    mid = (left + right) // 2
    
    total = 0
    for budget in budgets:
        total+=min(budget,mid)
    
    if total <= M:
        left = mid+1
        answer = mid
    else:
        right = mid-1

print(answer)