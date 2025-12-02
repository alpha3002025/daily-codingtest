import sys
input = sys.stdin.readline

N,S = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0

def dfs(curr_idx, curr_sum, A,S,N):
    global cnt

    if curr_idx == N:
        return
    
    if curr_sum + A[curr_idx]== S:
        cnt+=1
    

    dfs(curr_idx+1, curr_sum + A[curr_idx], A,S,N)
    dfs(curr_idx+1, curr_sum, A,S,N)

dfs(0,0, A,S,N)

print(cnt)