import sys
input = sys.stdin.readline

N = int(input())

servers = []
total_computers_cnt = 0
for _ in range(N):
    row = list(map(int, input().split()))
    servers.append(row)
    total_computers_cnt += sum(row)


## setup
### 절반의 컴퓨터가 최대로 오랫동안 켜질수 있을 때 몇분이 걸리는지
left, right = 0, 10000000 ### ⚡️ 이 부분을 틀렸었다.
limit = (total_computers_cnt+1)//2 ### ⚡️ 이 부분을 틀렸었다.

answer = 0
while left <= right:
    mid = (left+right)//2

    curr_compupter_cnt = 0
    for i in range(N):
        for j in range(N):
            ## mid 가 더 작을 경우 mid 만큼만 킨다. 그리고 다음 셀에서 mid 만큼을 채운다.
            curr_compupter_cnt += min(mid, servers[i][j])

    if curr_compupter_cnt >= limit:
        ## 이미 많은 컴퓨터를 킨 상태
        right = mid-1 ## 컴퓨터 갯수를 줄여본다.
        answer = mid
    else:
        left = mid+1

print(answer)