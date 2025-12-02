import sys
n,s = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
count = 0

def backtracking(curr_idx, curr_sum):
    global count

    for i in range(curr_idx, n):
        curr_sum += numbers[i]
        if curr_sum == s:
            count+=1
        backtracking(i+1, curr_sum)
        curr_sum -= numbers[i]


backtracking(0,0)
print(count)