import sys

def solve():
    memo = {}

    def dp(num):
        if num < 0:
            return 0
        
        if num == 0:
            return 1

        if num in memo:
            return memo[num]
        
        memo[num] = dp(num-1) + dp(num-2) + dp(num-3)
        return memo[num]


    N = int(input())
    for _ in range(N):
        result = dp(int(input()))
        print(f"{result}")

solve()
"""
3
4
7
10
"""