import sys

N,C = map(int, sys.stdin.readline().split())

positions = [int(input()) for _ in range(N)]

positions.sort()

left, right = positions[0], positions[-1]

answer = 0
while left <= right:
    mid = (left + right) // 2

    cnt = 0
    for step in range(0, positions[-1], mid):
        for position in positions:
            if step < position < step + mid:
                cnt+=1
    
    if cnt < C:
        left = mid+1
    else:
        right = mid-1
        answer = mid

print(f"{answer}")