from itertools import permutations
from copy import deepcopy

def rotate(arr, r, c, s):
    """(r, c)를 중심으로 s 크기만큼 회전"""
    for depth in range(1, s + 1):
        r1, c1 = r - depth, c - depth
        r2, c2 = r + depth, c + depth
        
        # 임시 저장
        temp = arr[r1][c1]
        
        # 왼쪽 세로 (위로 이동)
        for i in range(r1, r2):
            arr[i][c1] = arr[i + 1][c1]
        
        # 아래 가로 (왼쪽으로 이동)
        for j in range(c1, c2):
            arr[r2][j] = arr[r2][j + 1]
        
        # 오른쪽 세로 (아래로 이동)
        for i in range(r2, r1, -1):
            arr[i][c2] = arr[i - 1][c2]
        
        # 위 가로 (오른쪽으로 이동)
        for j in range(c2, c1, -1):
            arr[r1][j] = arr[r1][j - 1]
        
        arr[r1][c1 + 1] = temp

def get_min_value(arr):
    """배열의 각 행 합 중 최솟값 반환"""
    return min(sum(row) for row in arr)

# 메인 로직
N, M, K = map(int, input().split())
original = [list(map(int, input().split())) for _ in range(N)]
operations = []
for _ in range(K):
    r, c, s = map(int, input().split())
    operations.append((r - 1, c - 1, s))  # 0-indexed

answer = float('inf')

# 모든 순열 시도
for perm in permutations(operations):
    arr = deepcopy(original)
    
    # 현재 순서대로 회전 수행
    for r, c, s in perm:
        rotate(arr, r, c, s)
    
    # 최솟값 갱신
    answer = min(answer, get_min_value(arr))

print(answer)