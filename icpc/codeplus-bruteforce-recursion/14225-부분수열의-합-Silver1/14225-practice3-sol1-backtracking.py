import sys
input = sys.stdin.readline

N = int(input())
S = list(map(int, input().split()))

sum_set = set()
def backtracking(curr_idx, curr_sum):
    if curr_idx == len(S):
        if curr_sum > 0:
            sum_set.add(curr_sum)
        return

    backtracking(curr_idx+1, curr_sum+S[curr_idx])
    backtracking(curr_idx+1, curr_sum)


backtracking(0,0)

num = 1
while True:
    if num not in sum_set:
        print(num)
        break
    num+=1