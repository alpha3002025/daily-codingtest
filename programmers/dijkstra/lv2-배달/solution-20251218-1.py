import heapq

START_NODE = 1
def solution(N, road, K):
    ## 1. 그래프 생성
    graph = [[] for _ in range(N+1)]
    for u,v,w in road:
        graph[u].append((v,w))
        graph[v].append((u,w))
    
    ## 2. distance 테이블
    distance = [float('inf')] * (N+1)
    distance[START_NODE] = 0
    
    ## 3. 다익스트라
    queue = []
    heapq.heappush(queue, (0, START_NODE))
    
    while queue:
        curr_cost, curr_node = heapq.heappop(queue)
        
        if curr_cost > distance[curr_node]:
            continue
        
        for next_node, next_weight in graph[curr_node]:
            another_route_cost = curr_cost + next_weight
            if another_route_cost < distance[next_node]:
                distance[next_node] = another_route_cost
                heapq.heappush(queue, (another_route_cost, next_node))
    
    count = 0
    for d in distance:
        if d <= K:
            count += 1
    
    return count