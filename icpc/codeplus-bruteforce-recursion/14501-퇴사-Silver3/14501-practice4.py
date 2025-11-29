import sys
input = sys.stdin.readline

N = int(input())
schedule = [tuple(map(int, input().split())) for _ in range(N)]

memo = {}

def backtrack(day):
    if day == N:
        return 0
    
    if day in memo:
        return memo[day]
    
    how_long, price = schedule[day]
    take_consulting = 0
    if day + how_long <= N:
        take_consulting = backtrack(day+how_long) + price
    
    not_take_consulting = backtrack(day+1) ## 다음날로 넘어간다

    memo[day] = max(take_consulting, not_take_consulting)
    return memo[day]

answer = backtrack(0)
print(answer)