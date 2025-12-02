import sys
input = sys.stdin.readline

N = int(input())
servers = []
total = 0

for i in range(N):
    row = list(map(int, input().split()))
    servers.append(row)
    total += sum(row)

# 반올림 처리를 위해 (x+1)//2
target = (total + 1)//2

# 이분 탐색 범위
left, right = 0, 10000000

answer = right
while left <= right:
    mid = (left + right) // 2

    ## 매 순간마다 r x c 의 행렬 내의 모든 요소에 대해 mid 만큼의 합산을 해서 카운팅
    count = 0
    for i in range(N):
        for j in range(N):
            count += min(servers[i][j], mid)
        
    if count >= target: ## 약간 크면서 가장 target에 가까운 값
        answer = mid ## 약간 크면서 가장 target에 가까운 값인 mid 로 answer 로 세팅 후 더 작은 범위로 시도
        right = mid-1 ## 조금 더 작은 범위로 시작해본다.
    else:
        left = mid+1

print(answer)