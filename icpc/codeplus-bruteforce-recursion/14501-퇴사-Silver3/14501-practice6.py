import sys
input = sys.stdin.readline

N = int(input())
schedule = [tuple(map(int, input().split())) for _ in range(N)]

memo = {}

def backtracking(day):
    if day == N:
        return 0
    
    if day in memo:
        return memo[day]
    
    how_long, price = schedule[day]
    take = 0
    if day + how_long <= N:
        take = backtracking(day + how_long) + price

    not_take = backtracking(day+1)

    memo[day] = max(take, not_take)
    return memo[day]


maximum_profit = backtracking(0)
print(maximum_profit)