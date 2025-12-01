import sys
input = sys.stdin.readline

N = int(input())
prev = list(map(int, input().split())) ## 첫번째 집을 먼저 입력 받는다.

R,G,B = 0,1,2
for _ in range(N-1):
    cost = list(map(int, input().split())) ## 입력을 받으면서 계속 cost 와 prev 를 함께 점화식을 생성해서 curr 를 생성
    curr = [0] * 3 ## 새로 계산할 배열
    
    ## R 선택 (cost[R])
    curr[R] = cost[R] + min(prev[G], prev[B])
    ## G 선택 (cost[G])
    curr[G] = cost[G] + min(prev[R], prev[B])
    ## B 선택 (cost[B])
    curr[B] = cost[B] + min(prev[R], prev[G])
    
    prev = curr ## 다음값을 받기 위해 prev 를 curr 로 변경

print(min(prev))