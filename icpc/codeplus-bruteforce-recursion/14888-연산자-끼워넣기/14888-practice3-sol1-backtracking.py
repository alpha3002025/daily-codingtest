import sys
input = sys.stdin.readline

## input
N = int(input())
A = list(map(int, input().split()))
add,sub,mul,div = map(int, input().split())

min_sum = float('inf')
max_sum = float('-inf')

def backtracking(curr_idx, acc, add, sub, mul, div):
    global min_sum, max_sum

    if curr_idx == len(A):
        min_sum = min(min_sum, acc)
        max_sum = max(max_sum, acc)
        return
    
    if add > 0:
        backtracking(curr_idx+1, acc + A[curr_idx], add-1, sub, mul, div)
    if sub > 0:
        backtracking(curr_idx+1, acc - A[curr_idx], add, sub-1, mul, div)
    if mul > 0:
        backtracking(curr_idx+1, acc * A[curr_idx], add, sub, mul-1, div)
    if div > 0:
        if acc >=0:
            backtracking(curr_idx+1, acc // A[curr_idx], add, sub, mul, div-1)
        else:
            backtracking(curr_idx+1, -(-acc // A[curr_idx]), add, sub, mul, div-1)

backtracking(1,A[0],add,sub,mul,div)
print(max_sum)
print(min_sum)