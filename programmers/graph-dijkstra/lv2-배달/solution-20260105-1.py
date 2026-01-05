from collections import defaultdict
from heapq import heappop, heappush

def solution(N, road, K):
    graph = defaultdict(list)
    
    for src,dest,cost in road:
        graph[src].append((dest, cost))
        graph[dest].append((src, cost))
    
    distance = [float('inf')] * (N+1)
    
    start_node = 1
    queue = []
    heappush(queue, (start_node, 0)) ## (node,cost)
    
    while queue:
        curr_dest, curr_cost = heappop(queue)
        
        if curr_cost > distance[curr_dest]: ## 이전 텀에서 가정한 경로가 cost 가 더 클 경우 continue
            continue
        # print(f"curr_node = {curr_node}, curr_cost = {curr_cost}")
        
        for next_node, next_cost in graph[curr_dest]:
            another_route_cost = curr_cost + next_cost ## curr -> (next -> dest) (next->dest)는 graph[curr_dest] 로 알수 있다.
            if another_route_cost < distance[next_node]: ## 1 -> next_node가 의 비용이 비효율적일때
                distance[next_node] = another_route_cost
                heappush(queue, (next_node, another_route_cost))
        
    
    d = [i for i in range(1, N+1) if distance[i] <= K]
    
    return len(d)

print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))
print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))