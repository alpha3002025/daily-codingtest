import sys
input = sys.stdin.readline

K,N = map(int, input().split())
lines = [int(input()) for _ in range(K)]

left,right = 1, max(lines)
answer = 0

while left <= right:
    mid = (left + right)//2

    curr_k = 0
    for line in lines:
        cnt = line // mid
        if cnt >= 1:
            curr_k += cnt
    
    if curr_k >= N: ## 이미 충분하다. 랜선의 크기가 작아서 이미 충분하게 갯수를 충족한 케이스를 생각해야 한다.
        answer = mid
        left += 1 ## 랜선의 크기를 더 늘려서 타이트하게 더 맞는 지점을 향해 출발하도록 지정해본다.
    else: ## 랜선의 갯수가 부족하다.
        right = mid-1 ## 범위를 줄여서 랜선의 갯수를 늘려본다.

print(answer) ## 랜선의 최대 길이