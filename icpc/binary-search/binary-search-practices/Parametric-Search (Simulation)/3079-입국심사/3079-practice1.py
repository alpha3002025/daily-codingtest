import sys

N,M = map(int, sys.stdin.readline().split())

checkers_cost = [int(input()) for _ in range(N)]

## 
left, right = 1, max(checkers_cost) * M

total_time = right

while left <= right:
    mid = (left + right) // 2

    curr = sum(mid // cost for cost in checkers_cost)

    if curr >= M:
        right = mid - 1
        total_time = min(total_time, mid)
    else:
        left = mid + 1

print(f"{total_time}")