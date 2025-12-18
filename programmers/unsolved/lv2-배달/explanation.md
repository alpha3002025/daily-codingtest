# 배달
- 다익스트라로 start node = 1 에서부터의 모든 지점까지의 거리를 계산한다.
- 정답 제출 시에는 distance 배열 내에 K 이하인 것들의 개수만 세어 그 개수를 return 한다.


## 문제 설명
`N`개의 마을과 이를 연결하는 양방향 도로 정보(`road`: u, v, w)가 주어집니다. 1번 마을에서 출발하여 배달을 가는데, 이동 시간이 `K` 이하인 마을의 개수를 구하는 문제입니다.

### 핵심 개념
1.  **다익스트라 알고리즘 (Dijkstra)**: 가중치가 양수인 그래프에서 한 정점(1번)으로부터 모든 정점까지의 최단 거리를 구하는 표준 알고리즘입니다.
2.  **그래프 구성**: 도로 정보에 중복이 있을 수 있습니다(두 마을 사이 도로가 여러 개). 인접 리스트에 모두 추가하거나, 더 짧은 것만 저장합니다.
3.  **우선순위 큐 (Heap)**: 현재 갈 수 있는 가장 가까운 노드를 효율적으로 선택하기 위해 사용합니다.

## Python 풀이

```python
import heapq

def solution(N, road, K):
    # 1. 인접 리스트 생성
    graph = [[] for _ in range(N + 1)]
    for u, v, w in road:
        graph[u].append((v, w))
        graph[v].append((u, w))
        
    # 2. 최단 거리 테이블 초기화 (무한대)
    dist = [float('inf')] * (N + 1)
    dist[1] = 0 # 시작점 거리 0
    
    # 3. 다익스트라 수행
    queue = []
    heapq.heappush(queue, (0, 1)) # (비용, 노드)
    
    while queue:
        current_cost, current_node = heapq.heappop(queue)
        
        # 이미 처리된 적이 있고, 더 짧은 경로라면 패스
        if current_cost > dist[current_node]:
            continue
            
        for next_node, weight in graph[current_node]:
            next_cost = current_cost + weight
            if next_cost < dist[next_node]:
                dist[next_node] = next_cost
                heapq.heappush(queue, (next_cost, next_node))
                
    # 4. 거리 K 이하인 마을 개수 세기
    count = 0
    for d in dist:
        if d <= K:
            count += 1
            
    return count
```

### 코드 설명
- 다익스트라의 시간 복잡도는 $O(E \log V)$입니다. $N=50$, $E=2000$ 정도이므로 매우 빠르게 동작합니다.
- `heapq`에는 `(비용, 노드)` 순서로 넣어야 비용 기준으로 정렬됩니다.
- 두 마을을 연결하는 도로가 여러 개여도 다익스트라는 알아서 최단 경로를 찾아가므로 별도의 필터링은 필요 없습니다.
