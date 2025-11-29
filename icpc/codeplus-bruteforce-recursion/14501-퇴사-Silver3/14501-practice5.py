import sys
input = sys.stdin.readline

N = int(input())
schedule = [tuple(map(int, input().split())) for i in range(N)]

memo = {}

def backtracking(day):
    if day == N:
        return 0
    
    if day in memo:
        return memo[day]
    
    how_long, pay = schedule[day]
    take = 0
    if day + how_long <= N:
        take = backtracking(day + how_long) + pay
    not_take = backtracking(day+1)

    memo[day] = max(take, not_take)
    return memo[day]


result = backtracking(0)
print(f"{result}")