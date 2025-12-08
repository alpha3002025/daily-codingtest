"""
출처 : https://deveun.tistory.com/entry/Python%EB%B0%B1%EC%A4%80-18113%EA%B7%B8%EB%A5%B4%EB%8B%A4-%EA%B9%80%EA%B0%80%EB%86%88
"""

import sys

def binary(start, end):
    global maxP

    if start > end:
        print(maxP)
        return

    mid = (start + end) // 2

    sum = 0
    for k in kimbob:
        sum += k // mid

    if sum >= M:
        maxP = max(mid, maxP)
        binary(mid+1, end) ## start = mid+1 길이를 늘려서 갯수를 줄여본다.
    else:
        binary(start, mid-1) ## end = mid-1 : 길이를 줄여서 갯수를 늘려본다.

### MAIN
N, K, M = map(int, sys.stdin.readline().strip().split())

kimbob, maxP = [], -1
for _ in range(N):
    L = int(sys.stdin.readline())
    
    # 김밥 손질
    if L > 2 * K:
        kimbob.append(L - 2 * K)
    elif L > K and L < 2 * K:
        kimbob.append(L - K)


if len(kimbob) == 0 : # 전부 폐기하고 남은 김밥 없음
    print(-1)
    exit()

kimbob.sort()
binary(1, kimbob[-1])
 # 최소로 자를 수 있는 김밥조각의 크기 == 1
 # 최대로 자를 수 있는 김밥조각의 크기 == 제일 큰 김밥의 길이