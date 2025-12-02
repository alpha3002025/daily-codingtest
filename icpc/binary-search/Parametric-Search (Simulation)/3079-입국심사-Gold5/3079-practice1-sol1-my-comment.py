"""
특이하다고 느낀 것은 '심사에 걸리는 시간'의 총합의 최적값을 binary search 로 찾는 다는 점 이었다.
"""
import sys

N,M = map(int, sys.stdin.readline().split())

checkers_cost = [int(input()) for _ in range(N)]

## 최소=1, 최대=심사위원들중 가장 많은 시간이 걸리는 경우xM (최악의 경우)
left, right = 1, max(checkers_cost) * M
## 구하려는 값의 초기값은 최악의 경우로 세팅
total_time = right

while left <= right:
    ## 상담을 하는 데 걸리는 시간들의 최적의 총합 (최소 심사시간)
    mid = (left + right) // 2
    ## curr_passed = 현재 상담시간의 총합에 대해 각 심사위원들의 상담시간을 적용했을때의 심사를 통과한 사람의 수(상근이의 친구들)
    curr_passed = sum(mid // cost for cost in checkers_cost)

    ## 통과한 사람의 수가 M을 넘을때 (상근이의 친구들이 모두 통과할때)
    if curr_passed >= M:
        right = mid - 1 ## 시간을 더 타이트하게 잡아본다.
        total_time = min(total_time, mid) ## 일단 현재 최적값(최소 심사시간)을 저장한다.
    else: ## 통과한 사람의 수가 M을 못넘으면 (상근이의 친구들이 모두 통과하지 못했을 때)
        left = mid + 1 ## 시간을 늘려잡아서 M 근처에 도달하게 잡아본다.

print(f"{total_time}")