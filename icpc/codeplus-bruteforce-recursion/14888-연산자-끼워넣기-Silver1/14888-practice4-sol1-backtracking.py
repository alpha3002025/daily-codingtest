import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
plus,minus,mul,div = map(int, input().split())

max_result = -float('inf')
min_result = float('inf')

def backtracking(curr_idx, acc, plus, minus, mul, div):
    global max_result
    global min_result
    
    if curr_idx == len(A):
        max_result = max(max_result, acc)
        min_result = min(min_result, acc)
        return
    
    if plus > 0:
        backtracking(curr_idx+1, acc+A[curr_idx], plus-1, minus, mul, div)
    if minus > 0:
        backtracking(curr_idx+1, acc-A[curr_idx], plus, minus-1, mul, div)
    if mul > 0:
        backtracking(curr_idx+1, acc*A[curr_idx], plus, minus, mul-1, div)
    if div > 0:
        if acc >= 0:
            backtracking(curr_idx+1, acc//A[curr_idx], plus, minus, mul, div-1)
        else:
            backtracking(curr_idx+1, -(-acc//A[curr_idx]), plus, minus, mul, div-1)


backtracking(1, A[0], plus,minus,mul,div)

print(max_result)
print(min_result)