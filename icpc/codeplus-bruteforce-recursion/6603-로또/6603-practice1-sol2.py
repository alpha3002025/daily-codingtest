from itertools import combinations

while True:
    data = list(map(int, input().split()))
    k = data[0]

    if k == 0:
        break

    numbers = data[1:]

    for combination in combinations(numbers, 6):
        print(*combination)
    
    print()