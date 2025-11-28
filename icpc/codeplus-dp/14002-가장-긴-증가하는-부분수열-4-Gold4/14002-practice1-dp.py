n = int(input())
arr = list(map(int, input().split()))

# DP 초기화
dp = [1] * n  # 모든 원소는 최소 길이 1
prev = [-1] * n  # 이전 인덱스 추적

# DP 수행
for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            prev[i] = j  # i의 이전 원소는 j

# 최대 길이와 그 위치 찾기
max_length = max(dp)
max_idx = dp.index(max_length)

# 역추적으로 수열 복원
lis = []
idx = max_idx
while idx != -1:
    lis.append(arr[idx])
    idx = prev[idx]

lis.reverse()  # 역순이므로 뒤집기

# 출력
print(max_length)
print(*lis)