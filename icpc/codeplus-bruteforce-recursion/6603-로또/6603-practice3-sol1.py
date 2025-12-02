import sys
input = sys.stdin.readline

def backtracking(curr_idx, sub_list, k, A):
    if len(sub_list) == 6:
        print(*sub_list)
        return
    
    for i in range(curr_idx, k): ## [0...k-1], [1...k-1], [2...k-1], ... [k-2,k-1]
                                 ## 이렇게 하는 이유는 '사전순으로 백트래킹을 하기 위해서'임
                                 ## 입력으로 받는 A 배열의 경우 오름차순이라고 문제에 명시되어 있다.
        sub_list.append(A[i])
        backtracking(i+1, sub_list, k, A)
        sub_list.pop()


while True:
    line = list(map(int, input().split()))
    if line[0] == 0:
        break

    K, numbers = line[0], line[1:]
    # numbers.sort()

    backtracking(0, [], K, numbers)