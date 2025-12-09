import sys
input = sys.stdin.readline

N,K,M=map(int,input().split())

kimbobs = []
for _ in range(N):
    kimbob = int(input())
    if K < kimbob < 2*K:
        kimbobs.append(kimbob-K)
    elif kimbob > 2*K:
        kimbobs.append(kimbob-2*K)
    
if len(kimbobs) == 0:
    print(-1)
    exit()

kimbobs.sort()
left,right = 1, kimbobs[-1]

max_length = -1

def backtracking(left, right, M):
    global max_length
    
    if left > right:
        print(max_length)
        return
    
    mid = (left+right)//2

    kimbob_cnt = 0
    for kb in kimbobs:
        kimbob_cnt += kb//mid
    
    if kimbob_cnt >= M:
        ## M개에 도달한 경우 길이를 늘여서 갯수를 줄인다.
        max_length = max(max_length, mid)
        backtracking(mid+1, right, M)
    else:
        ## M개에 도달하지 못한 경우 길이를 줄여서 갯수를 늘린다.
        backtracking(left, mid-1, M)

backtracking(left, right, M)
# print(max_length)