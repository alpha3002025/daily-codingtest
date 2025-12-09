import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
positions = list(map(int, input().split()))

## hights min, max
left,right = 1, N
min_length = float('inf')

def is_valid(height):
    l,r = positions[0]-height, positions[-1]+height
    if l > 0 or r < N:
        return False
    for i in range(len(positions)-1):
        if positions[i+1] - positions[i] > 2*height:
            return False
    return True

while left <= right:
    mid = (left+right)//2

    if is_valid(mid): ## 기준을 통과할 때, 높이를 줄여서 타이트하게 맞춰보고 
        min_length = mid
        right = mid-1
    else: ## 기준을 통과하지 못할 때, 높이를 늘려서 더 넓게 맞춰본다.
        left = mid+1

print(min_length)