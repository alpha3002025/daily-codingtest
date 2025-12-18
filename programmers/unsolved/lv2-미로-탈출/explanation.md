# 미로 탈출
이 문제는 Gemini 의 풀이보다 이전에 풀었던 풀이가 더 직관적이다.<br/>
근데... 시험에 board 탐색하는 문제가 굳이 나올까?<br/>
<br/>


## 문제 설명
직사각형 격자 형태의 미로에서 출발 지점(`S`)에서 레버(`L`)를 당긴 후, 출구(`E`)로 탈출해야 합니다.
- `S`: 시작 지점
- `E`: 출구
- `L`: 레버
- `O`: 통로
- `X`: 벽

한 칸을 이동하는 데 1초가 걸립니다. 레버를 당기지 않으면 출구가 열리지 않으므로, 반드시 **S $\rightarrow$ L** 이동 후 **L $\rightarrow$ E**로 이동해야 합니다. 탈출에 걸리는 최소 시간을 구하고, 불가능하면 -1을 반환합니다.

## 풀이 개념
**BFS (너비 우선 탐색)**를 두 번 나누어 진행하는 것이 핵심입니다.
1.  **Phase 1**: 시작 지점(`S`)에서 레버(`L`)까지의 최단 거리 구하기.
2.  **Phase 2**: 레버(`L`)에서 출구(`E`)까지의 최단 거리 구하기.
3.  두 거리의 합이 정답입니다. 둘 중 하나라도 도달할 수 없다면 `-1`입니다.

한 번의 BFS로 상태(레버 당김 여부)를 포함하여 visited 배열을 3차원(`visited[row][col][has_lever]`)으로 관리할 수도 있지만, 단순히 목적지가 다른 두 번의 BFS가 구현하기 더 직관적이고 간단합니다.

## my
이 풀이가 더 직관적이다.
```python
from collections import deque

def solution(maps):
    answer = 0
    
    lever = (0,0)
    exit = (0,0)
    start = (0,0)
    
    for r in range(len(maps)):
        for c in range(len(maps[r])):
            if maps[r][c] == 'L':
                lever = (r,c)
            elif maps[r][c] == 'E':
                exit = (r,c)
            elif maps[r][c] == 'S':
                start = (r,c)
    
    d1 = bfs(start, lever, maps)
    d2 = bfs(lever, exit, maps)
    
    if d1 == -1 or d2 == -1:
        return -1
    
    return d1+d2

def bfs(src, dest, maps):
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    queue = deque()
    queue.append((src,0))
    visited[src[0]][src[1]] = True
    
    while queue:
        (r,c), curr_cost = queue.popleft()
        
        if (r,c) == dest:
            return curr_cost
        
        for dr,dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr,nc = r + dr, c + dc
            if not (0 <= nr < len(maps) and 0 <= nc < len(maps[0])):
                continue
            if maps[nr][nc] == 'X':
                continue
            if visited[nr][nc] == True:
                continue
            
            visited[nr][nc] = True
            queue.append(((nr,nc), curr_cost+1))
    return -1
```
<br/>


## Python 풀이

```python
from collections import deque

def bfs(start, end, maps):
    rows, cols = len(maps), len(maps[0])
    visited = [[False] * cols for _ in range(rows)]
    
    # 시작점 찾기 (좌표만 주어지면 생략 가능)
    sr, sc = -1, -1
    for r in range(rows):
        for c in range(cols):
            if maps[r][c] == start:
                sr, sc = r, c
                break
    
    # BFS 초기화
    queue = deque([(sr, sc, 0)]) # r, c, cost
    visited[sr][sc] = True
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    while queue:
        r, c, cost = queue.popleft()
        
        # 목적지 도착
        if maps[r][c] == end:
            return cost
        
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            
            # 범위 체크 및 벽 체크
            if 0 <= nr < rows and 0 <= nc < cols:
                if maps[nr][nc] != 'X' and not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc, cost + 1))
                    
    return -1

def solution(maps):
    # 1. Start('S') -> Lever('L')
    path1 = bfs('S', 'L', maps)
    if path1 == -1:
        return -1
        
    # 2. Lever('L') -> Exit('E')
    path2 = bfs('L', 'E', maps)
    if path2 == -1:
        return -1
        
    return path1 + path2
```

## 코드 설명
- `bfs` 함수를 분리하여 재사용성을 높였습니다. 
    - `start` 문자와 `end` 문자를 인자로 받아 해당 지점 간의 최단 거리를 반환합니다.
- `solution` 함수에서:
    - 먼저 `S`에서 `L`까지 이동합니다. 불가능하면 즉시 `-1` 반환.
    - 성공했다면, `L`에서 `E`까지 이동합니다.
    - 최종적으로 두 경로의 길이를 합산하여 반환합니다.
