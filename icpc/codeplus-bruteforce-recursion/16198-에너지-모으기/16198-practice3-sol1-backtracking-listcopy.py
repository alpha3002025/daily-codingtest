import sys
input = sys.stdin.readline

N = int(input())
W = list(map(int, input().split()))

def backtracking(curr_w):
    if len(curr_w) == 2:
        return 0

    max_power = 0
    for i in range(1, len(curr_w)-1):
        generated = curr_w[i-1]*curr_w[i+1]
        new_w = curr_w[:i] + curr_w[i+1:]
        power = backtracking(new_w)
        max_power = max(max_power, power + generated)
    return max_power

result = backtracking(W)
print(result)
