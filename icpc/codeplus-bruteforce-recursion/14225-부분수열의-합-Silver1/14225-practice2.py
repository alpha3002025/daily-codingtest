N = int(input())
S = list(map(int, input().split()))

sum_set = set()

def backtracking(curr_idx, curr_sum):
    if curr_idx == N:
        if curr_sum > 0:
            sum_set.add(curr_sum) ## 나올수 있는 모든 합을 구하는 것이기에... (이번 풀이(첫번째 풀이)때는 이 부분을 틀렸음)
        return

    ## 항상 여기가 허접스럽다.
    backtracking(curr_idx+1, curr_sum+S[curr_idx])
    backtracking(curr_idx+1, curr_sum)


backtracking(0, 0)

answer = 1
while True:
    if answer not in sum_set:
        print(answer)
        break
    answer+=1
