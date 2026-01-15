from collections import deque

def solution(bridge_length, weight, truck_weights):    
    trucks = deque(truck_weights)
    bridge_queue = deque([0] * bridge_length)
    
    total_weight = 0
    time = 0
    
    while bridge_queue:
        time += 1
        
        ## 진출 (다리를 빠져나간다)
        truck = bridge_queue.popleft()
        total_weight -= truck
        
        if trucks:
            if trucks[0] + total_weight <= weight:
                ## 새로운 트럭을 빼서 다리에 넣는다.
                new_truck = trucks.popleft()
                bridge_queue.append(new_truck)
                ## 중량을 계산한다
                total_weight += new_truck
            
            else: ## 새로 추가하려는 트럭을 추가할 경우 허용치를 넘으면 패딩('0')을 추가
                bridge_queue.append(0)
    
    return time


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))