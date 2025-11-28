import sys
input = sys.stdin.readline

N = int(input())
schedule = [tuple(map(int, input().split())) for _ in range(N)]

memo = [-1] * N

def dp(day):
    if day >= N:
        return 0
    
    if memo[day] != -1:
        return memo[day]
    
    duration, pay = schedule[day]

    ## 선택 1: 오늘 상담하는 경우
    if day + duration <= N:
        take = pay + dp(day + duration)
    else:
        take = 0
    
    ## 선택 2: 오늘 상담을 안하는 경우 (내일로 넘어간다)
    skip = dp(day + 1)

    # 두 선택 중 최댓값을 메모이제이션 (오늘 상담 vs 오늘 상담x)
    memo[day] = max(take, skip)

    return memo[day]


print(dp(0))