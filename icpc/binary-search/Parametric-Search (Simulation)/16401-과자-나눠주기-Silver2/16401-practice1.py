import sys
input = sys.stdin.readline

def can_distribute(snacks, M, length):
    """길이 length로 M명에게 나눠줄 수 있는지 확인"""
    count = 0
    for snack in snacks:
        count += snack // length
        if count >= M:  # 조기 종료 최적화
            return True
    return count >= M

def solve():
    M, N = map(int, input().split())
    snacks = list(map(int, input().split()))
    
    # 예외 처리: 과자가 조카보다 적으면 불가능
    if N < M and sum(snacks) < M:
        print(0)
        return
    
    left, right = 1, max(snacks)
    answer = 0
    
    while left <= right:
        mid = (left + right) // 2
        
        if can_distribute(snacks, M, mid):
            answer = mid  # 가능하면 답 갱신
            left = mid + 1  # 더 긴 길이 시도
        else:
            right = mid - 1  # 더 짧은 길이 시도
    
    print(answer)

solve()