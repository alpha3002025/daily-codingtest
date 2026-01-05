from collections import defaultdict
from heapq import heappush, heappop

def solution(N, road, K):
    answer = 0
    graph = defaultdict(list)
    
    for u,v,cost in road:
        graph[u].append((v, cost))
        graph[v].append((u, cost))
    
    start = 1
    distance = [float('inf')] * (N+1)
    
    queue = []
    heappush(queue, (0, start))
    
    while queue:
        curr_cost, curr_dest = heappop(queue)
        
        if curr_cost > distance[curr_dest]:
            continue
        
        for next_node, next_cost in graph[curr_dest]:
            another_route_cost = curr_cost + next_cost ## 1 -> curr_dest -> next_node
            if another_route_cost < distance[next_node]: ## 1 -> next_node 의 비용이 비효율적일때
                distance[next_node] = another_route_cost
                heappush(queue, (another_route_cost, next_node))
                
    count = 0
    for d in distance:
        if d <= K:
            count += 1
    return count