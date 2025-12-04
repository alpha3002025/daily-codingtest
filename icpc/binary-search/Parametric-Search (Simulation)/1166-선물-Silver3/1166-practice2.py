import sys
input = sys.stdin.readline

N,L,W,H = map(int, input().split())

left,right = 0.0, min(L,W,H)

def can_fit(A,L,W,H):
    if A == 0:
        return True
    
    length_cnt = int(L//A)
    width_cnt = int(W//A)
    height_cnt = int(H//A)

    cnt = length_cnt * width_cnt * height_cnt
    return N <= cnt

for _ in range(100):
    mid = (left + right)/2

    if can_fit(mid, L,W,H):
        left = mid
    else:
        right = mid

print(left)