# 가장 먼 노드

## 문제 설명
1번 노드에서 가장 멀리 떨어진 노드의 개수를 구하세요.
간선은 양방향이며 거리는 간선의 개수입니다.

## 문제 해결 전략

**BFS (너비 우선 탐색)**를 사용하여 1번 노드로부터 모든 노드까지의 최단 거리를 구합니다.
그 후, 최댓값을 가진 노드들의 수를 셉니다.

1. **그래프 구성**: 인접 리스트.
2. **BFS**:
   - `visited` 및 `distance` 배열.
   - 큐에 `(node, dist)` 넣고 탐색.
3. **결과**: `distance` 배열에서 `max(distance)`인 요소 개수 카운트.

## Python 코드

```python
from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    for u, v in edge:
        graph[u].append(v)
        graph[v].append(u)
        
    distance = [-1] * (n + 1)
    distance[1] = 0
    
    q = deque([1])
    
    while q:
        curr = q.popleft()
        
        for next_node in graph[curr]:
            if distance[next_node] == -1: # 방문 안 함
                distance[next_node] = distance[curr] + 1
                q.append(next_node)
                
    max_dist = max(distance)
    return distance.count(max_dist)
```
