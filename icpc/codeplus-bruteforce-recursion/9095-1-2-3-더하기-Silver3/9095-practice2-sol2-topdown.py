import sys
input = sys.stdin.readline

T = int(input())


def dp(num, memo):
    if num < 0:
        return 0
    
    if num == 0:
        return 1
    
    if num in memo:
        return memo[num]
    
    memo[num] = dp(num-1, memo) + dp(num-2, memo) + dp(num-3, memo)
    return memo[num]


for _ in range(T):
    memo = {}
    query = int(input())
    answer = dp(query, memo)
    print(f"{answer}")
