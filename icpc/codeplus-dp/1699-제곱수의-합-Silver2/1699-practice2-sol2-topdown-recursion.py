import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
memo = [-1] * (N+1)

def backtracking(curr):
    if memo[curr] != -1:
        return memo[curr]
    
    result = curr

    j=1
    while j*j <= N:
        result = min(result, backtracking(curr - j*j)+1)
        j += 1
    
    memo[curr] = result
    return memo[curr]

print(backtracking(N))