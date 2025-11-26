import sys

def backtrack(curr_index, selected):
    if len(selected) == 6:
        print(*selected)
        return
    
    for i in range(curr_index, k): ## curr_index 부터 k 개를 고른다.
        selected.append(numbers[i]) ## (1) i번째 수를 추가
        backtrack(i+1, selected) ## (2) (1)에서 i번째 수를 추가했으므로 i+1번째 위치로 이동
        selected.pop() ## (3) 추가했던 i번째 수를 제거 후 다음 재귀로


while True:
    data = list(map(int, sys.stdin.readline().split()))
    k = data[0]
    if k == 0:
        break
    numbers = data[1:]

    backtrack(0, [])