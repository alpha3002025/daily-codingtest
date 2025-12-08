import sys
sys.setrecursionlimit(2000)
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

# dp[i] : A[i]를 마지막 원소로 하는 가장 긴 감소하는 부분 수열의 길이
dp = [-1] * N

def solve(idx):
    # 이미 계산된 값이 있다면 반환 (Memoization)
    if dp[idx] != -1:
        return dp[idx]
    
    # 최소 길이는 자기 자신 하나만 있을 때인 1
    ret = 1
    
    # idx 이전의 원소들을 탐색
    for prev in range(idx):
        # 감소하는 조건 만족 시 (이전 원소가 더 커야 함)
        if A[prev] > A[idx]:
            ret = max(ret, solve(prev) + 1)
    
    dp[idx] = ret
    return dp[idx]

# 모든 위치가 수열의 끝이 될 수 있으므로, 각각에 대해 solve 호출 후 최댓값 찾기
ans = 0
for i in range(N):
    ans = max(ans, solve(i))

print(ans)
