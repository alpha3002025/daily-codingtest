import sys
input = sys.stdin.readline
INF = float('inf')

N, M = map(int, input().split())

# 트리 크기: 2의 거듭제곱으로 맞춤
size = 1
while size < N:
    size *= 2

min_tree = [INF] * (2 * size)
max_tree = [-INF] * (2 * size)

# 리프 노드에 값 저장
for i in range(N):
    val = int(input())
    min_tree[size + i] = val
    max_tree[size + i] = val

# 내부 노드 구축 (bottom-up)
for i in range(size - 1, 0, -1):
    min_tree[i] = min(min_tree[2 * i], min_tree[2 * i + 1])
    max_tree[i] = max(max_tree[2 * i], max_tree[2 * i + 1])

def query(left, right):
    left += size - 1  # 0-indexed를 1-indexed 리프로 변환
    right += size - 1
    
    result_min = INF
    result_max = -INF
    
    while left <= right:
        if left % 2 == 1:  # 왼쪽이 오른쪽 자식이면
            result_min = min(result_min, min_tree[left])
            result_max = max(result_max, max_tree[left])
            left += 1
        if right % 2 == 0:  # 오른쪽이 왼쪽 자식이면
            result_min = min(result_min, min_tree[right])
            result_max = max(result_max, max_tree[right])
            right -= 1
        left //= 2
        right //= 2
    
    return result_min, result_max

result = []
for _ in range(M):
    a, b = map(int, input().split())
    min_val, max_val = query(a, b)
    result.append(f"{min_val} {max_val}")

print('\n'.join(result))