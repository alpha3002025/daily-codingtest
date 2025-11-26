import sys

k = int(input().strip())
signs = input().split()


global used
used = [False] * (10) ## [0,1,2,3,4,5,6,7,8,9]

global min_num, max_num
min_num = ""
max_num = ""


def is_valid(a, b, sign):
    if sign == '<':
        return a < b
    else:
        return a > b


def backtracking(depth, num_str):
    global min_num, max_num
    if depth == k+1:
        if not min_num:
            min_num = num_str
        max_num = num_str
        return
    
    for i in range(10): # depth 에 대해 0 ~ 9 숫자 조합
        if used[i]:
            continue

        if depth == 0 or is_valid(int(num_str[-1]), i, signs[depth-1]):
            used[i] = True
            backtracking(depth+1, num_str + str(i))
            # backtracking(depth+1, num_str + i)
            used[i] = False



backtracking(0, "")
print(max_num)
print(min_num)