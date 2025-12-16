# 아이템 줍기

## 문제 설명
지형이 여러 직사각형들로 이루어져 있습니다.
직사각형들이 겹쳐진 형태의 가장 바깥쪽 테두리를 따라 캐릭터가 이동합니다.
캐릭터 위치 `(cx, cy)`에서 아이템 위치 `(ix, iy)`까지 가는 최단 거리를 구하세요.

## 문제 해결 전략

1. **좌표 2배 확대**:
   - 좌표가 1 단위로 되어 있으면, `ㄷ`자 형태 등에서 바로 옆 칸(1칸 차이)이 연결된 것인지 끊긴 것인지 구분하기 어려울 수 있습니다. (예: (1,1)~(1,2)가 테두리이고 (2,1)~(2,2)가 테두리일 때, (1,1)과 (2,1)은 거리 1이지만 연결되어 있지 않을 수 있음)
   - 모든 좌표를 2배로 늘리면, 중간에 빈 공간(0.5 단위, 즉 확대 후 1 단위)이 생겨 BFS 탐색 시 벽을 뚫고 가는 오류를 막을 수 있습니다.
   - 맵 크기는 최대 50이므로 2배 해도 100x100 (충분히 작음).

2. **맵 생성 (102 x 102)**:
   - 전체를 0으로 초기화.
   - 각 직사각형에 대해 `x1*2` ~ `x2*2`, `y1*2` ~ `y2*2` 범위를 채웁니다.
   - 이때, **테두리는 1, 내부는 0(또는 -1)**로 표시해야 합니다.
   - 단, 이미 내부(-1)로 표시된 곳은 테두리(1)로 덮어쓰지 않도록 주의합니다. (겹쳐진 부분의 내부는 갈 수 없습니다. 겹쳐진 부분의 테두리도 내부에 포함되면 갈 수 없습니다.)
   - 쉬운 방법:
     1. 모든 직사각형의 전체 영역(테두리+내부)을 `1`로 채운다.
     2. 모든 직사각형의 내부 영역(테두리 제외)을 `0`으로 채운다.
     3. 이제 `1`인 곳이 우리가 갈 수 있는 테두리가 된다.
     4. (0,0) 같은 맵 바깥은 원래 0.

3. **BFS 탐색**:
   - `(cx*2, cy*2)`에서 시작해 `(ix*2, iy*2)`까지 최단 거리 탐색.
   - 값이 `1`인 곳만 이동 가능.
   - 이동할 때마다 `visited` 거리 갱신.
   - 찾으면 `거리 // 2` 반환.

## Python 코드

```python
from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 맵 최대 크기 (50 * 2 = 100, 여유있게 102)
    MAX = 102
    grid = [[-1] * MAX for _ in range(MAX)]
    
    # 1. 모든 직사각형 채우기
    # 먼저 전부 1로 채우고,
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, r)
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                # 이미 0(내부)라면 건드리지 않음? 
                # -> 아니, 일단 1로 채우고 나중에 내부 파내기가 쉬움.
                if grid[i][j] == -1:
                    grid[i][j] = 1
                    
    # 2. 내부 파내기 (0으로)
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, r)
        # 테두리 제외한 내부
        for i in range(x1 + 1, x2):
            for j in range(y1 + 1, y2):
                grid[i][j] = 0
                
    # 3. BFS
    q = deque()
    q.append((characterX * 2, characterY * 2, 0))
    visited = [[False] * MAX for _ in range(MAX)]
    visited[characterX * 2][characterY * 2] = True
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    target_x = itemX * 2
    target_y = itemY * 2
    
    while q:
        x, y, dist = q.popleft()
        
        if x == target_x and y == target_y:
            return dist // 2
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < MAX and 0 <= ny < MAX:
                if not visited[nx][ny] and grid[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append((nx, ny, dist + 1))
                    
    return 0
```
