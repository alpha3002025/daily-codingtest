import sys
input = sys.stdin.readline

def can_fit(A, N, L, W, H):
    """크기가 A인 박스를 N개 이상 넣을 수 있는지 확인"""
    if A == 0:
        return True
    
    # 각 방향으로 넣을 수 있는 박스 개수
    count_L = int(L // A)
    count_W = int(W // A)
    count_H = int(H // A)
    
    total = count_L * count_W * count_H
    return total >= N

def solve():
    N, L, W, H = map(int, input().split())
    
    # 탐색 범위 설정
    lo = 0.0
    hi = min(L, W, H)
    
    # 실수 이분 탐색 (100회 반복으로 충분한 정밀도 확보)
    for _ in range(100):
        mid = (lo + hi) / 2
        
        if can_fit(mid, N, L, W, H):
            lo = mid  # 가능하면 더 큰 값 탐색
        else:
            hi = mid  # 불가능하면 더 작은 값 탐색
    
    print(lo)

solve()