import sys
input = sys.stdin.readline

N,L,W,H = map(int, input().split())

left, right = 0.0, min(L,W,H)
answer = 0

def check(limit, L,W,H):
    if limit == 0:
        return True
    width_cnt = int(W//limit)
    height_cnt = int(H//limit)
    length_cnt = int(L//limit)
    
    total_cnt = width_cnt * height_cnt * length_cnt
    return total_cnt >= N ## ⚡️ ## limit 이 충분히 커서 N개 이상을 수용가능

for _ in range(100):
    mid = (left+right)/2

    if check(mid, L,W,H):
        left = mid
    else:
        right = mid

print(left)
    
