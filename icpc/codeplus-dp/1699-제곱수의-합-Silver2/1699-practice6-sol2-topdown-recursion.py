import sys
input = sys.stdin.readline

N = int(input())
memo = [-1] * (N+1)
memo[0] = 0

def backtracking(curr):
    if memo[curr] != -1:
        return memo[curr]
    
    total_cnt = curr
    j=1
    while j*j <= curr:
        total_cnt = min(total_cnt, backtracking(curr - j*j) + 1)
        j+=1
    
    memo[curr] = total_cnt
    return memo[curr]

result = backtracking(N)
print(result)
