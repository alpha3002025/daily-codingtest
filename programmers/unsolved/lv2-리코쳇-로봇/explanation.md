# 리코쳇 로봇

## 문제 설명
격자판 모양의 게임판에서 로봇을 목표 지점(G)까지 이동시켜야 합니다.
로봇은 상, 하, 좌, 우 4방향으로 이동할 수 있으며, 한 번 움직이면 장애물(D)이나 맨 끝에 부딪힐 때까지 미끄러져 이동합니다.
시작 지점(R)에서 목표 지점(G)까지 도달하는 최소 이동 횟수를 구합니다. 도달할 수 없으면 -1을 반환합니다.

## 풀이 개념
**BFS (너비 우선 탐색)** 알고리즘을 사용합니다.
일반적인 미로 찾기와 다르게, 한 칸씩 이동하는 것이 아니라 **"미끄러져서 벽이나 장애물 앞에서 멈추는 위치"**가 다음 탐색 노드가 됩니다.

1. 시작 위치(R)를 찾고 큐에 넣습니다 (`dist=0`).
2. 큐에서 현재 위치를 꺼내 4방향으로 이동을 시도합니다.
3. 각 방향으로 이동할 때 `while` 루프를 사용하여 벽이나 'D'를 만날 때까지 좌표를 업데이트합니다.
4. 벽/장애물 바로 앞칸에 멈추면, 그 위치가 방문하지 않은 곳일 경우 큐에 추가하고 거리를 업데이트합니다.
5. 목표 지점(G)에 도달하면 현재 거리를 반환합니다.
6. 큐가 빌 때까지 도달하지 못하면 -1을 반환합니다.

## 코드 (Python)

```python
from collections import deque

def solution(board):
    n = len(board)
    m = len(board[0])
    
    start = None
    goal = None
    
    # 시작점 찾기
    for r in range(n):
        for c in range(m):
            if board[r][c] == 'R':
                start = (r, c)
            elif board[r][c] == 'G':
                goal = (r, c)
                
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    queue = deque()
    queue.append((start[0], start[1], 0))
    visited = [[False]*m for _ in range(n)]
    visited[start[0]][start[1]] = True
    
    while queue:
        r, c, dist = queue.popleft()
        
        if (r, c) == goal:
            return dist
        
        for i in range(4):
            nr, nc = r, c
            # 미끄러지기 이동
            while True:
                next_r = nr + dr[i]
                next_c = nc + dc[i]
                
                # 범위를 벗어나거나 장애물이면 멈춤
                if not (0 <= next_r < n and 0 <= next_c < m) or board[next_r][next_c] == 'D':
                    break
                
                nr, nc = next_r, next_c
                
            # 멈춘 위치가 방문하지 않았다면 큐에 추가
            if not visited[nr][nc]:
                visited[nr][nc] = True
                queue.append((nr, nc, dist + 1))
                
    return -1
```
