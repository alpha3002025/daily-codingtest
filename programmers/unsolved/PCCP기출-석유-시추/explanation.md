# [PCCP 기출문제] 2번 / 석유 시추

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/250136)

주어진 `n x m` 격자 모양의 땅에서 석유가 묻혀있는 위치가 주어집니다. 석유는 상, 하, 좌, 우로 연결된 덩어리 형태로 존재합니다.
우리는 수직으로 단 하나의 시추관을 뚫을 수 있으며, 시추관이 지나가는 모든 석유 덩어리의 석유를 뽑을 수 있습니다.
가장 많은 석유를 뽑을 수 있는 시추관의 위치(열)를 찾고, 그때 뽑을 수 있는 석유량을 반환해야 합니다.

## 핵심 개념
### 1. 연결 요소 (Connected Component) 탐색
이 문제는 그래프 이론의 **연결 요소(Connected Component)** 개념을 사용합니다. 인접해 있는 `1`들은 하나의 덩어리로 취급되므로, **BFS(너비 우선 탐색)** 또는 **DFS(깊이 우선 탐색)** 알고리즘을 사용하여 각 덩어리를 탐색하고 그 크기를 구해야 합니다.

### 2. 열(Column) 기준 집계
시추관은 **열(Column)** 단위로 뚫습니다. 따라서 각 열별로 시추관을 뚫었을 때 얻을 수 있는 총 석유량을 계산해야 합니다.
단순히 시뮬레이션하면 시간 복잡도가 높아질 수 있으므로, 다음과 같은 최적화된 접근이 필요합니다:
1. 전체 격자를 순회하며 방문하지 않은 석유 덩어리를 찾습니다.
2. BFS/DFS로 덩어리의 **크기(석유량)** 를 구하고, 해당 덩어리가 포함하는 **열의 집합(Set of Columns)** 을 구합니다.
3. 해당 덩어리에 속한 열의 인덱스에 덩어리의 크기를 누적합니다. (예: `oil_sum[col] += component_size`)
4. 모든 덩어리 탐색 후, `oil_sum` 배열에서 최댓값을 찾습니다.

*주의: 한 덩어리가 같은 열에 여러 번 걸쳐 있을 수 있으므로(예: `ㄷ`자 형태), 덩어리 탐색 시 해당 덩어리가 차지하는 열을 중복 없이 기록('Set' 자료구조 활용)해야 합니다.*

## 추천 풀이 (Python)

```python
from collections import deque

def solution(land):
    n, m = len(land), len(land[0])
    visited = [[False] * m for _ in range(n)]
    oil_sum = [0] * m  # 각 열(column)별 얻을 수 있는 총 석유량
    
    # 상, 하, 좌, 우 방향 벡터
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 모든 위치를 순회하며 석유 덩어리 탐색
    for i in range(n):
        for j in range(m):
            # 석유가 있고 아직 방문하지 않은 경우 BFS 시작
            if land[i][j] == 1 and not visited[i][j]:
                queue = deque([(i, j)])
                visited[i][j] = True
                
                size = 0            # 현재 덩어리의 석유량
                cols = set()        # 현재 덩어리가 포함하는 열들의 집합 (중복 제거)
                
                while queue:
                    r, c = queue.popleft()
                    size += 1
                    cols.add(c)
                    
                    for k in range(4):
                        nr, nc = r + dx[k], c + dy[k]
                        
                        if 0 <= nr < n and 0 <= nc < m:
                            if land[nr][nc] == 1 and not visited[nr][nc]:
                                visited[nr][nc] = True
                                queue.append((nr, nc))
                
                # 현재 덩어리가 차지하는 모든 열에 석유량 추가
                for col in cols:
                    oil_sum[col] += size
                    
    return max(oil_sum)
```

## 코드 설명
1.  **초기화**: `visited` 배열로 방문 여부를 체크하고, `oil_sum` 배열로 각 열에서 얻을 수 있는 석유량을 저장합니다.
2.  **순회 및 탐색**: 이중 루프를 통해 모든 격자를 확인하며, 석유가 있고(`1`) 미방문인 경우 BFS를 시작합니다.
3.  **BFS 내부**:
    *   큐(deque)를 사용하여 연결된 모든 석유 칸을 방문합니다.
    *   `size` 변수로 덩어리의 크기를 셉니다.
    *   `cols` 세트(set)로 덩어리가 존재하는 열(column) 인덱스를 저장합니다. `set`을 사용함으로써 같은 열이 여러 번 카운트되는 것을 방지합니다.
4.  **결과 누적**: 하나의 덩어리 탐색이 끝나면, `cols`에 포함된 모든 열 인덱스(`col`)에 대해 `oil_sum[col]`에 `size`를 더해줍니다. 이렇게 하면 해당 열을 시추했을 때 이 덩어리를 캘 수 있음이 반영됩니다.
5.  **최댓값 반환**: 모든 탐색이 끝난 후 `oil_sum` 중 가장 큰 값을 반환합니다.
