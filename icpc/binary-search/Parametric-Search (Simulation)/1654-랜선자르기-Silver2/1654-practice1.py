import sys

K, N = map(int, sys.stdin.readline().split())
cables = [int(input()) for _ in range(K)]

left, right = 1, max(cables)
answer = 0

while left <= right:
    mid = (left + right) // 2
    
    # mid 길이로 잘랐을 때 만들 수 있는 케이블 개수
    count = sum(c // mid for c in cables)
    
    if count >= N:  # N개 이상 만들 수 있으면
        answer = mid  # 가능한 답 저장
        left = mid + 1  # 더 긴 길이 시도
    else:  # N개 미만이면
        right = mid - 1  # 더 짧은 길이로

print(answer)