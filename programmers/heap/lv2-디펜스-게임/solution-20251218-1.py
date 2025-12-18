import heapq

def solution(n, k, enemy):
    answer = 0
    queue = []
    
    for round_idx, power in enumerate(enemy):
        n -= power
        heapq.heappush(queue, -power)
        
        if n < 0:
            if k > 0: ## 모든 적을 처리 후 나머지 k 개의 무적권을 통해 손실을 메꾼 보정값 추출
                bigger_power = -heapq.heappop(queue)
                n += bigger_power ## 가장 센 적을 무적권으로 처리한 것으로 처리 시 낭비된 병사만큼 복원 (bigger_power - power)
                k-=1
            else:
                return round_idx
    
    return len(enemy) ## 모든 적을 처치했을 경우, 적의 수가 라운드 수가 된다.