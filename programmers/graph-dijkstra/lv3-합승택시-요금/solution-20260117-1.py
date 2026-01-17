from heapq import heappush, heappop
from collections import defaultdict

def solution(n, s, a, b, fares):
    graph = defaultdict(list)
    
    for u,v,cost in fares:
        graph[u].append((v, cost))
        graph[v].append((u, cost))
    
    
    distance_s = dijkstra(s, n, graph)
    distance_a = dijkstra(a, n, graph) ## a 에서 각 지점까지의 거리
    distance_b = dijkstra(b, n, graph) ## b 에서 각 지점까지의 거리
    
    curr_cost = float('inf')
    for i in range(1, n+1):
        curr_cost = min(curr_cost, distance_s[i] + distance_a[i] + distance_b[i])
        
    return curr_cost


def dijkstra(u, n, graph):
    distance = [float('inf')] * (n+1)
    distance[u] = 0
    
    queue = []
    heappush(queue, (0, u)) ## 참고) 맨 앞 요소가 숫자여야 가중치가 먹는다.
    
    while queue:
        curr_cost, curr_node = heappop(queue)
        
        ## 이전 선택지에서 구한 경로가 더 비싸면, continue
        ## s → curr_node < s → k → curr_node 
        if distance[curr_node] < curr_cost:
            continue
        
        ## neighbor 까지 가는 방법이 curr_cost + neighbor_cost 가 더 최적일 경우를 검사
        for neighbor, neighbor_cost in graph[curr_node]:
            # another_route_cost = distance[curr_node] + neighbor_cost
            ## 또는 다음과 같이 지정 (아래 식이 비교적 실수를 안한다.)
            another_route_cost = curr_cost + neighbor_cost
            if distance[neighbor] > another_route_cost:
                distance[neighbor] = another_route_cost
                heappush(queue, (another_route_cost, neighbor))
        
    return distance


print(solution(6,4,6,2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))

print(solution(7,3,4,1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))

print(solution(6,4,5,6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))