import sys
input = sys.stdin.readline

N,S = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0

def dfs(curr_idx, sublist):
    global cnt
    
    if len(sublist)>=1 and sum(sublist)==S:
        cnt+=1
    
    for i in range(curr_idx, N):
        sublist.append(A[i]) ## i 를 선택했으니
        dfs(i+1, sublist) ## i+1 로 넘어간다.
        sublist.pop() ## 선택한 i 는 제거하고 다음 dfs 를 위한 for loop 로 돌아간다.

dfs(0, [])

print(cnt)