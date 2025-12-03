import sys

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().split()))
plus, minus, multiply, divide = map(int, sys.stdin.readline().split())

max_value = float("-inf")
min_value = float("inf")

def backtracking(curr, acc, plus, minus, multiply, divide):
    global max_value, min_value
    
    if curr == N:
        max_value = max(max_value, acc)
        min_value = min(min_value, acc)
        return
    
    if plus > 0:
        backtracking(curr+1, acc+A[curr], plus-1, minus, multiply, divide)
    if minus > 0:
        backtracking(curr+1, acc-A[curr], plus, minus-1, multiply, divide)
    if multiply > 0:
        backtracking(curr+1, acc*A[curr], plus, minus, multiply-1, divide)
    if divide > 0:
        if acc < 0:
            backtracking(curr+1, -(-acc//A[curr]), plus, minus, multiply, divide-1)
        else:
            backtracking(curr+1, acc//A[curr], plus, minus, multiply, divide-1)


backtracking(1, A[0], plus, minus, multiply, divide)
print(max_value)
print(min_value)