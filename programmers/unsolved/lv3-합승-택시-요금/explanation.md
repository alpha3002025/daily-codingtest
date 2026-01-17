# 합승 택시 요금

## 문제 설명
지점 `n`개, 요금 `fares`.
`s`에서 출발하여 `A`, `B` 두 사람이 각각 `a`, `b` 지점으로 가야 합니다.
어느 지점까지 합승한 후 각자 택시를 타고 갈 수 있습니다.
최저 예상 택시 요금을 구하세요.
(아예 합승 안 할 수도 있음 = 출발지부터 바로 갈라짐)

## 문제 해결 전략

**플로이드-워셜(Floyd-Warshall)** 또는 **다익스트라(Dijkstra)**를 사용합니다.
$N$이 최대 200이므로 플로이드-워셜($O(N^3)$)이 가능하고 구현이 간단합니다.

1. **모든 노드 간 최단 거리 구하기 (Dist)**:
   - 초기화: `dist[i][j] = fares`, 자기 자신 0, 연결 안 되면 무한대.
   - 플로이드-워셜 수행.

2. **경유지 탐색**:
   - 어떤 지점 `k`까지 합승하고, `k`에서 `a`와 `b`로 갈라진다고 가정합시다.
   - 비용 = `dist[s][k] + dist[k][a] + dist[k][b]`
   - 모든 노드 `k` (1 ~ $N$)에 대해 위 비용을 계산하고 최솟값을 찾습니다.
   - `k=s`인 경우는 합승 없이 처음부터 따로 가는 경우를 포함합니다 (`dist[s][s]=0`).
   - `k=a` 또는 `k=b`인 경우는 한 명의 목적지까지 같이 가고, 나머지 한 명이 더 가는 경우를 포함합니다.


## Python 코드 (다익스트라(Dijkstra))
```python
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
```
<br/>


## Python 코드 (플로이드 워셜)

```python
def solution(n, s, a, b, fares):
    INF = 10000000
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        dist[i][i] = 0
        
    for u, v, w in fares:
        dist[u][v] = w
        dist[v][u] = w
        
    # Floyd-Warshall
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    
    # 최소 비용 찾기
    min_fare = INF
    
    # 합승 지점 k (1~n)
    for k in range(1, n + 1):
        cost = dist[s][k] + dist[k][a] + dist[k][b]
        if cost < min_fare:
            min_fare = cost
            
    return min_fare
```
