import sys
input = sys.stdin.readline

K,N = map(int, input().split())
lines = [int(input()) for _ in range(K)]

## 랜선 N개를 만들때 최대 랜선 길이

left,right = 1, max(lines)
max_length = 0
while left <= right:
    mid = (left + right)//2

    cnt = 0
    for line in lines:
        cnt+=line//mid
    
    if cnt >= N:
        ## 랜선의 갯수가 많다. 
        ## 조금 더 타이트하게 되도록 랜선의 갯수를 줄인다.(mid 가 커지도록 범위를 잡는다.)
        left = mid+1
        max_length = mid
    else:
        right = mid-1

print(max_length)