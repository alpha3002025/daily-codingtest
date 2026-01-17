from collections import defaultdict
from heapq import heappush, heappop
from math import inf

def solution(n, s, a, b, fares):
    graph = defaultdict(list)
    
    for src,dest,fare in fares:
        graph[src-1].append((dest-1, fare))
        graph[dest-1].append((src-1, fare))
    
    
    distance_from_s = dijkstra(s-1, n, graph)
    distance_from_a = dijkstra(a-1, n, graph)
    distance_from_b = dijkstra(b-1, n, graph)
    
    
    best_cost = inf
    for i in range(n):
        curr = distance_from_s[i] + distance_from_a[i] + distance_from_b[i]
        best_cost = min(curr, best_cost)
    
    return best_cost


def dijkstra(start, size, graph):
    distance = [inf] * size
    distance[start] = 0
    
    queue = []
    heappush(queue, (0, start)) ## (cost, node)
    
    while queue:
        curr_cost, curr_node = heappop(queue)
        
        # s -> curr_node < s -> k -> curr_node (미리 구해놓은 답이 이미 최적이면 skip)
        if distance[curr_node] < curr_cost:
            continue
            
        for next_node, next_cost in graph[curr_node]:
            another_route_cost = distance[curr_node] + next_cost
            
            if another_route_cost < distance[next_node]:
                distance[next_node] = another_route_cost
                heappush(queue, (another_route_cost, next_node))
    return distance


print(solution(6,4,6,2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))

print(solution(7,3,4,1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))

print(solution(6,4,5,6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))
