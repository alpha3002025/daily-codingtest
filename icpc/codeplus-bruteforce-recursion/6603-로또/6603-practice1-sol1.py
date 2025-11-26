def backtracking(start, selected):
    if len(selected) == 6:
        print(*selected)
        return
    
    for i in range(start, k): ## start 부터 k 개를 고른다.
        selected.append(numbers[i])
        backtracking(i, selected)
        selected.pop()

while True:
    data = list(map(int, input().split()))
    k = data[0]
    if k == 0:
        break
    numbers = data[1:]
    backtracking(0, [])
    print()