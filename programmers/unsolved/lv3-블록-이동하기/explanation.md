# 블록 이동하기

## 문제 설명
2x1 크기의 로봇을 (1,1)에서 (N,N)까지 이동시킵니다.
- 로봇은 두 칸을 차지하며, 가로 또는 세로 상태일 수 있습니다.
- 상하좌우 이동 가능 (두 칸 모두 빈 칸이어야 함).
- 회전 가능: 로봇의 한 칸을 축으로 90도 회전.
  - 회전 반경(대각선 위치)에 벽이 없어야 함.
  - 가로 -> 세로, 세로 -> 가로.
- 최소 시간을 구하세요.

## 문제 해결 전략

**BFS (너비 우선 탐색)**를 사용합니다.
상태: `{(r1, c1), (r2, c2)}` (집합으로 좌표 쌍 관리, 순서 무관)
또는 정규화하여 `(min_r, min_c, orientation)` 로 관리 가능.

1. **맵 확장 (Padding)**:
   - 인덱스 범위 체크를 편하게 하기 위해 상하좌우에 벽(1)을 두른 `(N+2) x (N+2)` 맵을 만듭니다.

2. **이동/회전 로직**:
   - `get_next_pos(pos)` 함수: 현재 위치(두 좌표 집합)에서 갈 수 있는 다음 위치 목록 반환.
   - **이동**: 상하좌우, 두 칸 다 0이어야 함.
   - **회전**:
     - 가로 상태일 때: 위쪽이나 아래쪽으로 회전 가능. 단, 회전하는 쪽의 두 칸이 모두 비어 있어야 함. (회전 후 위치 + 대각선 체크 = 즉 회전할 방향의 평행한 두 칸이 비어야 함)
     - 세로 상태일 때: 왼쪽이나 오른쪽으로 회전 가능.

3. **BFS 탐색**:
   - `visited` 집합에 `{(r1, c1), (r2, c2)}` (frozenset 이용) 저장.

## Python 코드

```python
from collections import deque

def get_next_pos(pos, board):
    next_pos = []
    pos = list(pos) # set -> list
    pos1_x, pos1_y = pos[0][0], pos[0][1]
    pos2_x, pos2_y = pos[1][0], pos[1][1]
    
    # 4방향 이동
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(4):
        nx1, ny1 = pos1_x + dx[i], pos1_y + dy[i]
        nx2, ny2 = pos2_x + dx[i], pos2_y + dy[i]
        # 보드 범위(패딩됨) 내이고 둘 다 0이면 이동 가능
        if board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
            next_pos.append({(nx1, ny1), (nx2, ny2)})
            
    # 회전
    # 가로(행 같음) -> 세로
    if pos1_x == pos2_x:
        for d in [-1, 1]: # 위(-1), 아래(1)
            # 회전하려는 쪽의 두 칸이 모두 비어있어야 함
            if board[pos1_x + d][pos1_y] == 0 and board[pos2_x + d][pos2_y] == 0:
                # 두 가지 회전 결과 (왼쪽 축, 오른쪽 축)
                next_pos.append({(pos1_x, pos1_y), (pos1_x + d, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x + d, pos2_y)})
                
    # 세로(열 같음) -> 가로
    elif pos1_y == pos2_y:
        for d in [-1, 1]: # 좌(-1), 우(1)
            if board[pos1_x][pos1_y + d] == 0 and board[pos2_x][pos2_y + d] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + d)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + d)})
                
    return next_pos

def solution(board):
    n = len(board)
    # 패딩된 보드 생성
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]
            
    # 시작 위치
    start = {(1, 1), (1, 2)}
    q = deque([(start, 0)])
    visited = [start] # set lookup이 빠르지만 집합(set)은 unhashable 객체라 list안에 넣거나 frozenset 사용
    # frozenset으로 관리하는 visited set
    visited = set([frozenset(start)])
    
    target = (n, n)
    
    while q:
        pos, cost = q.popleft()
        
        if target in pos:
            return cost
        
        for next_p in get_next_pos(pos, new_board):
            frozen_p = frozenset(next_p)
            if frozen_p not in visited:
                visited.add(frozen_p)
                q.append((next_p, cost + 1))
                
    return 0
```
