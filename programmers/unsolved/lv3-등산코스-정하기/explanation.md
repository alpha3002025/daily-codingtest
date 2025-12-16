# 등산코스 정하기

## 문제 설명
XX산에는 여러 지점(`n`개)과 등산로(`paths`)가 있습니다. 등산로에는 시간(가중치)이 존재합니다.
- 출입구(`gates`) 중 하나에서 시작하여, 산봉우리(`summits`) 중 **하나**를 방문하고, 다시 원래의 출입구로 돌아와야 합니다.
- 이 코스에 포함된 가장 긴 등산로의 시간(가중치)을 `intensity`라고 합니다.
- `intensity`가 최소가 되는 등산코스를 찾고 그 때의 `[산봉우리 번호, intensity]`를 반환하세요.
- 같은 intensity라면 산봉우리 번호가 낮은 것을 선택합니다.

## 문제 해결 전략

1. **문제 단순화**:
   - 출입구 -> 산봉우리 -> 원래 출입구
   - 가는 길과 오는 길은 같은 경로를 역순으로 이용하면 intensity가 같으므로, **"출입구 -> 산봉우리" 편도 구간**의 최소 intensity만 구하면 됩니다.

2. **변형된 다익스트라 (Min-Max Path)**:
   - 일반적인 다익스트라는 "경로의 합"을 최소화하지만, 여기서는 **"경로 상의 최대 가중치(BottleNeck)"를 최소화**해야 합니다.
   - `distance[i]` = 출발지(어떤 gate든 상관없음)에서 `i`번 지점까지 오는 경로 중 최소 `intensity`.
   - 초기화: `distance[gate] = 0` (모든 게이트), 나머지는 무한대. 큐에 모든 게이트를 넣고 시작.
   - 완화(Relax): `new_intensity = max(distance[curr], weight)`. `if new_intensity < distance[next]: update`.

3. **제약 사항 처리**:
   - 산봉우리는 도착지이므로, 산봉우리를 거쳐서 다른 곳으로 가면 안 됩니다. 즉, 산봉우리에 도달하면 거기서 멈춥니다(큐에 넣지 않음).
   - `gates`도 출발지이므로, 다른 경로를 통해 `gate`에 다시 도착하는 경우는 고려할 필요 없습니다. (단, 초기 셋팅에서 처리됨)

4. **결과 도출**:
   - 다익스트라가 끝난 후, `distance[summit]` 값들 중 최소값을 찾습니다.

## Python 코드

```python
import heapq

def solution(n, paths, gates, summits):
    # 그래프 생성
    graph = [[] for _ in range(n + 1)]
    for i, j, w in paths:
        graph[i].append((j, w))
        graph[j].append((i, w))
        
    # 산봉우리 집합 (빠른 조회를 위해)
    summits_set = set(summits)
    
    # 다익스트라 준비
    # intensity[i]: i까지 가는 경로의 최소 intensity
    intensities = [float('inf')] * (n + 1)
    queue = []
    
    # 모든 출입구를 시작점으로 설정
    for gate in gates:
        intensities[gate] = 0
        heapq.heappush(queue, (0, gate)) # (intensity, node)
        
    while queue:
        curr_int, curr_node = heapq.heappop(queue)
        
        # 산봉우리면 더 이상 이동하지 않음 (도착)
        if curr_node in summits_set:
            continue
            
        if curr_int > intensities[curr_node]:
            continue
            
        for next_node, weight in graph[curr_node]:
            # 다음 노드까지의 intensity는 (현재까지 intensity)와 (이번 간선 가중치) 중 큰 값
            new_int = max(curr_int, weight)
            
            if new_int < intensities[next_node]:
                intensities[next_node] = new_int
                heapq.heappush(queue, (new_int, next_node))
                
    # 결과 찾기
    # summits를 번호 순으로 정렬해두면, 최소 intensity 찾을 때 유리
    summits.sort()
    
    ans_summit = -1
    min_intensity = float('inf')
    
    for s in summits:
        if intensities[s] < min_intensity:
            min_intensity = intensities[s]
            ans_summit = s
            
    return [ans_summit, min_intensity]
```
