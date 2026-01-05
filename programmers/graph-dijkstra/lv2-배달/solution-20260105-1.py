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
    distance[start] = 0
    
    queue = []
    heappush(queue, (0, start))
    
    while queue:
        curr_cost, curr_dest = heappop(queue)
        
        ## 이전 텀에서 가정한 경로가 cost 가 더 클 경우 continue
        if curr_cost > distance[curr_dest]: 
            continue
        
        ## for loop 은 현재 경로를 판단하기보다는 
        ## next_node 로의 경로를 최적화하는 용도이며, 다음번 loop 에서 최적값으로 업데이트 될수도 있다.
        for next_node, next_cost in graph[curr_dest]:
            another_route_cost = curr_cost + next_cost ## 1 -> curr_dest -> next_node
            if another_route_cost < distance[next_node]: ## 1 -> next_node 의 비용이 비효율적일때
                distance[next_node] = another_route_cost

                ## 다음 턴에서 next_node 로 경로를 선택했을때를 계산하기 위해 새로운 경로에 대한 가중치를 push
                heappush(queue, (another_route_cost, next_node)) 
                
    count = 0
    for d in distance:
        if d <= K:
            count += 1
    return count

print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))
print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))