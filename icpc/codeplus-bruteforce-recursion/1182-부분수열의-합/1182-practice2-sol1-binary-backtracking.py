import sys
n,s = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

count = 0
def backtracking(curr_idx, curr_sum):
    global count

    if curr_idx == n:
        return
    
    curr_sum += numbers[curr_idx]
    if curr_sum == s:
        count+=1
    backtracking(curr_idx+1, curr_sum)
    backtracking(curr_idx+1, curr_sum - numbers[curr_idx])

backtracking(0, 0) ## index, curr_sum
print(count)
