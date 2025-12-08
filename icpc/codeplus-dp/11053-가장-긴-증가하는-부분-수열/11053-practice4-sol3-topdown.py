import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N = int(input())
A = list(map(int, input().split()))

memo = [-1]*N

def backtracking(curr):
    if memo[curr] != -1:
        return memo[curr]

    memo[curr] = 1

    for j in range(curr):
        if A[j] < A[curr]:
            memo[curr] = max(memo[curr], backtracking(j)+1)
    
    return memo[curr]

for i in range(N):
    backtracking(i)

print(max(memo))