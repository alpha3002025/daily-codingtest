# 부대복귀

## 문제 설명
강철부대가 복귀를 하려 합니다.
- 총 $N$개의 지역, 양방향 도로 (가중치 1).
- 각 부대원은 서로 다른 지역(`sources`)에 흩어져 있습니다.
- 모든 부대원은 본부(`destination`)로 최단 시간내에 복귀해야 합니다.
- 복귀 불가능하면 -1.

## 문제 해결 전략

각 부대원의 위치(`sources`)가 여러 개입니다.
모든 source에 대해 destination까지 BFS를 각각 돌리면 비효율적입니다(Sources 개수 * N).
도로가 양방향(무방향)이므로, **Destination에서 시작하여 모든 노드까지의 최단 거리를 한 번의 BFS로 구하는 것**이 효율적입니다.
그 후 `sources`에 해당하는 거리를 조회하면 됩니다.

## Python 코드

```python
from collections import deque

def solution(n, roads, sources, destination):
    # 그래프 생성
    graph = [[] for _ in range(n + 1)]
    for u, v in roads:
        graph[u].append(v)
        graph[v].append(u)
        
    # 거리 배열 (-1로 초기화)
    distance = [-1] * (n + 1)
    distance[destination] = 0
    
    # BFS (역방향)
    queue = deque([destination])
    
    while queue:
        curr = queue.popleft()
        
        for next_node in graph[curr]:
            if distance[next_node] == -1:
                distance[next_node] = distance[curr] + 1
                queue.append(next_node)
                
    # 결과 추출
    return [distance[s] for s in sources]
```
