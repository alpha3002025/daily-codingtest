import sys
input = sys.stdin.readline

N = int(input())
servers = []
total = 0

for i in range(N):
    row = list(map(int, input().split()))
    servers.append(row)
    total += sum(row)

# 절반 이상 (올림 처리)
target = (total + 1) // 2

# 이분 탐색 범위
left, right = 0, 10000000

answer = right
while left <= right:
    mid = (left + right) // 2
    
    # mid분일 때 작동하는 컴퓨터 수 계산
    count = 0
    for i in range(N):
        for j in range(N):
            count += min(servers[i][j], mid)
    
    if count >= target:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)