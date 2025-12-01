import sys
input = sys.stdin.readline
INF = float('inf')

def build(node, start, end):
    if start == end:
        min_tree[node] = arr[start]
        max_tree[node] = arr[start]
        return
    
    mid = (start + end) // 2
    build(node * 2, start, mid)
    build(node * 2 + 1, mid + 1, end)
    
    min_tree[node] = min(min_tree[node * 2], min_tree[node * 2 + 1])
    max_tree[node] = max(max_tree[node * 2], max_tree[node * 2 + 1])

def query(node, start, end, left, right):
    # 범위를 완전히 벗어난 경우
    if right < start or end < left:
        return (INF, -INF)
    
    # 범위에 완전히 포함된 경우
    if left <= start and end <= right:
        return (min_tree[node], max_tree[node])
    
    # 일부만 겹치는 경우
    mid = (start + end) // 2
    left_result = query(node * 2, start, mid, left, right)
    right_result = query(node * 2 + 1, mid + 1, end, left, right)
    
    return (min(left_result[0], right_result[0]), 
            max(left_result[1], right_result[1]))

N, M = map(int, input().split())
arr = [0] + [int(input()) for _ in range(N)]  # 1-indexed

min_tree = [INF] * (4 * N)
max_tree = [-INF] * (4 * N)

build(1, 1, N)

result = []
for _ in range(M):
    a, b = map(int, input().split())
    min_val, max_val = query(1, 1, N, a, b)
    result.append(f"{min_val} {max_val}")

print('\n'.join(result))