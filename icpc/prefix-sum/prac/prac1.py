import sys

N, M = map(int, sys.stdin.readline().strip().split())

numbers = list(map(int, sys.stdin.readline().strip().split()))

queries = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]


section = [0] * len(numbers)
section[0] = numbers[0]
## section[1] = section[0] + numbers[1]

for i in range(1, len(numbers)):
    section[i] = section[i-1] + numbers[i]

# print(f"section = {section}")

for q in queries:
    start, end = q[0]-1, q[1]-1
    if start == 0:
        print(f"{section[end]}")
    elif start == end:
        curr = section[end] - section[end-1]
        print(f"{curr}")
    else:
        curr = section[end]-section[start-1]
        print(f"{curr}")
        


