import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N = int(input())

memo = {}
memo[1] = 1

def backtracking(curr):
    if curr in memo:
        return memo[curr]
    
    result = curr
    
    j=1
    while j*j <= curr:
        result = min(result, backtracking(curr-j*j)+1)
        j+=1
    
    memo[curr] = result
    return result

answer = backtracking(N)
print(answer)
