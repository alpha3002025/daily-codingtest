# 지게차와 크레인

## 문제 설명
`n x m` 크기의 창고에 알파벳으로 표시된 컨테이너가 있습니다.
`requests` 배열에 따라 컨테이너를 출고합니다.
- 길이가 1인 요청(예: "A"): **지게차**를 사용. **외부와 연결된** 해당 알파벳 컨테이너만 꺼낼 수 있습니다.
- 길이가 2인 요청(예: "BB"): **크레인**을 사용. 위치와 상관없이 해당 알파벳 컨테이너를 **모두** 꺼냅니다.
모든 요청 처리 후 남은 컨테이너 개수를 구합니다.
"외부와 연결된"이란 상하좌우로 빈 공간을 통해 창고 밖으로 나갈 수 있는 상태를 말합니다.

## 풀이 개념
**BFS (너비 우선 탐색)**를 이용한 시뮬레이션입니다.

1. **패딩(Padding)**: 창고 외곽을 쉽게 처리하기 위해 `(n+2) x (m+2)` 크기로 확장하고 테두리를 빈 공간으로 채웁니다. 이렇게 하면 `(0, 0)`에서 BFS를 했을 때 도달 가능한 빈 공간이 곧 "외부"가 됩니다.
2. **요청 처리**:
   - **크레인**: 전체 그리드를 스캔하여 해당 알파벳을 모두 빈 공간으로 바꿉니다.
   - **지게차**:
     1. 외부와 연결된 빈 공간을 파악합니다. (매번 BFS를 수행하거나 갱신).
     2. 해당 알파벳을 가진 칸 중, 상하좌우 중 하나라도 "외부와 연결된 빈 공간"과 맞닿아 있다면 제거 대상입니다.
     3. 제거 대상들을 빈 공간으로 바꿉니다.
3. 탐색 효율화:
   - 외부와 연결된 상태를 매번 전체 BFS로 갱신하는 것이 안전합니다. (격자 크기 50x50으로 작음).
   - "외부 연결 빈 공간"은 `visited` 배열로 관리하며, `(0, 0)`에서 시작해 빈 공간만 따라갑니다.

## 코드 (Python)

```python
from collections import deque

def solution(storage, requests):
    n = len(storage)
    m = len(storage[0])
    
    # 패딩된 격자 생성 (테두리 0으로 채움)
    grid = [[0] * (m + 2) for _ in range(n + 2)]
    for r in range(n):
        for c in range(m):
            grid[r+1][c+1] = storage[r][c]
            
    # 전체 컨테이너 수
    total_cnt = n * m
    
    for req in requests:
        target = req[0]
        
        # 외부 연결 공간 확인을 위한 BFS
        # (매 요청마다 갱신: 이전 작업으로 인해 새로운 길이 열릴 수 있음)
        outside = set()
        q = deque([(0, 0)])
        visited = [[False]*(m+2) for _ in range(n+2)]
        visited[0][0] = True
        outside.add((0, 0))
        
        while q:
            r, c = q.popleft()
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n+2 and 0 <= nc < m+2 and not visited[nr][nc]:
                    # 빈 공간(0)이라면 이동 계속
                    if grid[nr][nc] == 0:
                        visited[nr][nc] = True
                        outside.add((nr, nc))
                        q.append((nr, nc))
        
        removed = []
        is_crane = len(req) == 2
        
        for r in range(1, n + 1):
            for c in range(1, m + 1):
                if grid[r][c] == target:
                    if is_crane:
                        removed.append((r, c))
                    else:
                        # 지게차: 4방향 중 하나라도 outside에 포함되면 제거 가능
                        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                            if (r+dr, c+dc) in outside:
                                removed.append((r, c))
                                break
                                
        # 일괄 제거
        for r, c in removed:
            grid[r][c] = 0
            
    # 남은 개수 카운트
    # 패딩 제외한 내부만
    answer = 0
    for r in range(1, n + 1):
        for c in range(1, m + 1):
            if grid[r][c] != 0:
                answer += 1
                
    return answer
```
