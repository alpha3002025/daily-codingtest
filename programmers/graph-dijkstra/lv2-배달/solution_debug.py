from collections import defaultdict
from heapq import heappush, heappop

def solution(N, road, K):
    graph = defaultdict(list)
    for u,v,cost in road:
        graph[u].append((v, cost))
        graph[v].append((u, cost))
        
    distance = dijkstra(1, graph, N)
    
    cnt = 0
    # BUG 2: enumerate starts from 0 by default, but graph nodes are 1-based.
    # distance[0] is inf (unused), distance[1] is 0. 
    # If using enumerate(distance), index 0 will be included in the check.
    # It's safer to slice or iterate range(1, N+1).
    for i, cost in enumerate(distance):
        if cost <= K:
            cnt += 1
    
    # But since distance[0] is INF, it won't be <= K anyway, so it might not affect the count if K < INF.
    # Still, good to be precise.
    
    return cnt


def dijkstra(start, graph, n):
    distance = [float('inf')] * (n+1)
    
    # BUG 1: Start node distance initialization missing!
    # distance[start] must be set to 0.
    # distance[start] = 0
    
    queue = []
    heappush(queue, (0, start)) ## cost, 노드번호
    
    while queue:
        curr_cost, curr_node = heappop(queue)
        
        if distance[curr_node] < curr_cost:
            continue
        
        for neighbor, neighbor_cost in graph[curr_node]:
            another_route_cost = curr_cost + neighbor_cost
            if distance[neighbor] > another_route_cost:
                distance[neighbor] = another_route_cost
                heappush(queue, (another_route_cost, neighbor))
    
    return distance

# Test cases
print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3)) # Expected: 4
print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4)) # Expected: 4
