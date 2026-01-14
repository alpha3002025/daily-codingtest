from collections import deque

def solution(bridge_length, weight, truck_weights):
    trucks = deque(truck_weights)
    bridge_traffic = deque([0] * bridge_length)
    
    total_weight = 0
    time = 0
    
    while bridge_traffic: ## bridge_traffic 을 시뮬레이션
        time += 1
        
        truck = bridge_traffic.popleft()
        total_weight -= truck
        
        if trucks: 
            if weight >= trucks[0] + total_weight:
                new_truck = trucks.popleft()
                bridge_traffic.append(new_truck)
                total_weight += new_truck
            else: ## 트럭을 더 채울수 없으면 0으로 빈 자리를 메운다.
                bridge_traffic.append(0)
    
        ## 참고) truck 이 empty 일때
        #### 이미 truck 은 모두 썼지만, truck 들이 bridge 를 벗어나지 않은 경우
    return time


print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))