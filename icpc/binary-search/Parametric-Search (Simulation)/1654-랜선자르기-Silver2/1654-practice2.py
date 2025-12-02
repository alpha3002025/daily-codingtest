import sys

K,N = map(int, sys.stdin.readline().split())
cables = [int(input()) for _ in range(K)]


left, right = 1, max(cables)

answer = 0
while left <= right:
    mid = (left + right) // 2
    cnt = sum(c // mid for c in cables)

    if cnt >= N:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)