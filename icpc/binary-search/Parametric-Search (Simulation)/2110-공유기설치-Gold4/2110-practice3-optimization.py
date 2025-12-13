import sys
input = sys.stdin.readline

N,C = map(int, input().split())
houses = [int(input()) for _ in range(N)]
houses.sort()

## 최대 거리 : 맨뒤의 집에서 첫번째 집까지의 거리
left,right = 1, houses[-1] - houses[0]

while left <= right:
    ## 현재 공유기의 커버리지
    mid = (left + right)//2
    
    cnt=1
    last = houses[0]
    for house in houses[1:]:
        distance = house - last
        if distance >= mid:
            ## mid 거리 밖은 새로 설치 시작해야 함
            cnt+=1
            last = house
    
    if cnt >= C:
        ## 공유기는 C개 이상이 될수 없다. 
        # 따라서 줄이는 수식으로 접근
        ## 공유기의 갯수를 줄이려면, 커버리지를 늘려야 한다.
        left=mid+1
        answer = mid
    else:
        right = mid-1

print(answer)
