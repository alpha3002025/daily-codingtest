import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

memo = [-1] * N

def backtracking(curr):
    if memo[curr] != -1:
        return memo[curr]

    result = 1
    for j in range(curr):
        if A[j] > A[curr]:
            result = max(result, backtracking(j)+1)
    
    memo[curr] = result
    return memo[curr]


for i in range(N):
    backtracking(i)

print(max(memo))