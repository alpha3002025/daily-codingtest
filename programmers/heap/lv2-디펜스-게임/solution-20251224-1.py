from heapq import heappush, heappop

def solution(n, k, enemy):
    answer = 0
    max_heap = []
    
    for i, power in enumerate(enemy):
        heappush(max_heap, -power)
        n -= power
        
        if n < 0:
            if k > 0:
                removed = -heappop(max_heap)
                n += removed ### 무적권을 통해 넘치는 만큼 복원
                             ### 과거에 과도하게 사용한 병사만큼을 부활시킴
                k -= 1 ## 무적권 횟수 차감
            else:
                return i ### # k-1번째 라운드에서 최종으로 막지 못했다.(0 based index)
        
        
    return len(enemy) ## 병사 수가 충분한 경우 무적권 사용 없이 모두 처치 
                      ## 즉, 모든 라운드(len(enemy))를 통과 가능

print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]))
print(solution(2, 4, [3, 3, 3, 3]))