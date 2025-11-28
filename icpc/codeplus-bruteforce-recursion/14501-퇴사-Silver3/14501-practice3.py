import sys
input = sys.stdin.readline

N = int(input())
schedule = [tuple(map(int, input().split())) for _ in range(N)]

memo = [-1] * N

def dp(day):
    if day == N:
        return 0
    
    if memo[day] != -1:
        return memo[day]
    
    how_long, pay = schedule[day]
    take_consulting = 0
    if day + how_long <= N:
        take_consulting = pay + dp(day+how_long)

    not_take_consulting = dp(day+1)

    memo[day] = max(take_consulting, not_take_consulting)
    return memo[day]

print(dp(0))