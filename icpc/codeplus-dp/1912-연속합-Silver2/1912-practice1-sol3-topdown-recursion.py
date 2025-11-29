import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

memo = [None] * N

def dp(i):
    # i 번째 위치에서 끝나는 연속합
    if i == 0:
        return numbers[0]
    
    if memo[i] is not None:
        return memo[i]
    
    memo[i] = max(dp(i-1) + numbers[i], numbers[i])
    return memo[i]

max_value = max(dp(i) for i in range(N))
print(max_value)