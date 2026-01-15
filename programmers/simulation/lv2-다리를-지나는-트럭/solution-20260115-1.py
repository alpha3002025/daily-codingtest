from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    
    curr_bridge_weight = 0
    time = 0
    
    while bridge:
        time += 1
        from_bridge = bridge.popleft()
        curr_bridge_weight -= from_bridge
        
        if trucks:
            if trucks[0] + curr_bridge_weight <= weight:
                new_truck = trucks.popleft()
                bridge.append(new_truck)
                curr_bridge_weight += new_truck
            else:
                bridge.append(0)
    
    return time


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))