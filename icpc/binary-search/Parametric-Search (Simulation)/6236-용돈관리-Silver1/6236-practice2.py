import sys
input = sys.stdin.readline

N,M = map(int,input().split())
money_list = [int(input()) for _ in range(N)]


left,right = max(money_list), sum(money_list)
answer = 0

while left <= right:
    mid = (left + right) // 2
    
    total = 0
    cnt = 0

    for money in money_list:
        if total + money <= mid:
            total += money
        else:
            total = 0 ## 초기화 (다음번 인출 케이스를 카운팅하기 위한 초기화)
            cnt+=1
            total += money
    
    if cnt > M:
        left = mid+1
    else:
        answer = mid
        right = mid-1

print(answer)

