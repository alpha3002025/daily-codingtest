# 카드 짝 맞추기

## 문제 설명
4x4 크기의 격자에 최대 6종류(1~6)의 카드들이 무작위로 두 장씩 놓여 있습니다.
카드를 모두 제거하는 최소 조작 횟수를 구하세요.
조작:
- 방향키, Ctrl+방향키(끝까지 이동) 1회 조작.
- Enter: 카드 뒤집기 1회 조작.
- 두 카드를 뒤집어서 같으면 제거, 다르면 다시 뒤집힘.

## 문제 해결 전략

두 단계로 나누어 생각합니다.
1. **카드 제거 순서 결정 (Permutation)**:
   - 카드의 종류가 최대 6개이므로, 제거 순서는 $6! = 720$가지밖에 안 됩니다.
   - 모든 순서를 시도해봅니다.

2. **최단 거리 이동 (BFS)**:
   - 순서가 정해졌다면(예: 1 -> 3 -> 2), 현재 커서 위치에서 1번 카드로 이동 -> 뒤집기 -> 다른 1번 카드로 이동 -> 뒤집기... 를 반복합니다.
   - 각 단계마다 BFS를 사용해 최단 이동 횟수를 구합니다.
   - 주의: 같은 종류의 카드가 두 장 있는데, A를 먼저 뒤집고 B를 뒤집을지, B를 먼저 뒤집고 A를 뒤집을지에 따라 거리가 달라집니다. 이것도 경우의 수에 포함해야 합니다. (각 카드 종류마다 2가지 경우 -> $2^K$)

**종합 접근**:
- `permutations`로 카드 종류의 순서를 정합니다.
- 재귀 또는 반복문으로 해당 순서대로 카드를 제거합니다.
- `(현재 위치, 현재 제거된 카드 상태)` -> `BFS`로 다음 카드 위치까지 거리 계산.

## Python 코드

```python
from collections import deque
from itertools import permutations

def solution(board, r, c):
    # 1. 카드 종류 및 위치 파악
    card_pos = {}
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                if board[i][j] not in card_pos:
                    card_pos[board[i][j]] = []
                card_pos[board[i][j]].append((i, j))
                
    card_types = list(card_pos.keys())
    min_moves = float('inf')
    
    # BFS: 현재(start)에서 목표(end)까지 최단 거리 (Ctrl 이동 포함)
    def bfs(curr, target, current_board):
        q = deque([(curr[0], curr[1], 0)])
        visited = set([(curr[0], curr[1])])
        
        while q:
            x, y, dist = q.popleft()
            if x == target[0] and y == target[1]:
                return dist
            
            # 4방향 이동
            dx = [0, 0, 1, -1]
            dy = [1, -1, 0, 0]
            
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                
                # 1. 일반 이동
                if 0 <= nx < 4 and 0 <= ny < 4:
                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        q.append((nx, ny, dist + 1))
                        
                # 2. Ctrl 이동
                cx, cy = x, y
                while True:
                    nx, ny = cx + dx[i], cy + dy[i]
                    if not (0 <= nx < 4 and 0 <= ny < 4):
                        break # 맵 밖으로 나가면 멈춤 (이전 위치 유지)
                    cx, cy = nx, ny
                    if current_board[cx][cy] != 0:
                        break # 카드 만나면 멈춤
                
                if (cx, cy) not in visited:
                    visited.add((cx, cy))
                    q.append((cx, cy, dist + 1))
                    
        return float('inf')

    # 카드 제거 순열
    for order in permutations(card_types):
        # 이번 순서대로 제거할 때의 최소 조작 횟수
        # 각 단계마다 (현재 커서 위치) -> (첫번째 카드) -> (두번째 카드) 거리 합산
        # 두 카드 중 어느 것을 먼저 방문할지 모든 경우를 따져야 함. -> 재귀 or 큐?
        # 카드가 K개면 2^K 경우의 수. K<=6 이므로 64가지. 괜찮음.
        
        # Q: (현재 커서 위치, 누적 거리, 제거 단계)
        q = deque([(r, c, 0, 0)]) # r, c, dist, stage_idx
        
        # 보드 상태는 어떻게? -> 매번 복사? 비효율적.
        # 사실 보드 상태는 '제거된 카드'만 0으로만 알면 됨.
        # order[0]~order[stage_idx-1] 까지는 0임.
        
        local_min = float('inf')
        
        while q:
            cr, cc, dist, idx = q.popleft()
            
            if idx == len(order):
                local_min = min(local_min, dist)
                continue
                
            # 가지치기
            if dist >= min_moves: continue
            
            card_type = order[idx]
            pos1, pos2 = card_pos[card_type]
            
            # 현재 보드 상태 생성 (이미 제거된 애들 0 처리)
            # board는 전역 변수 참조하되, 지워진 것만 체크
            # 매번 board copy해서 0 만드는 것보다,
            # BFS 안에서 board[r][c]가 현재 제거 대상 또는 이미 제거된 대상인지 확인하면 됨.
            # 하지만 Ctrl 이동 때문에 실제 0인지가 중요함.
            # -> 간단하게: 임시 보드 생성
            temp_board = [row[:] for row in board]
            for k in range(idx):
                t = order[k]
                for pr, pc in card_pos[t]:
                    temp_board[pr][pc] = 0
            
            # Case 1: pos1 -> pos2
            # 거리: curr -> pos1 (move) + enter + pos1 -> pos2 (move) + enter
            dist1 = bfs((cr, cc), pos1, temp_board)
            # pos1 제거된 상태 반영 (Ctrl 이동 위해) -> pos1만 0으로
            temp_board[pos1[0]][pos1[1]] = 0 
            dist2 = bfs(pos1, pos2, temp_board)
            
            # 복구할 필요 없이 Case 2 계산을 위해선 다시 만들어야 함?
            # 아니면 BFS 함수는 보드 수정 안하니 괜찮음.
            # 단 dist2 계산시 pos1이 0이어야 함.
            
            q.append((pos2[0], pos2[1], dist + dist1 + dist2 + 2, idx + 1))
            
            # Case 2: pos2 -> pos1
            # 보드 다시 원복
            temp_board[pos1[0]][pos1[1]] = card_type # 원래 값 (0아님)
            
            dist3 = bfs((cr, cc), pos2, temp_board)
            temp_board[pos2[0]][pos2[1]] = 0 
            dist4 = bfs(pos2, pos1, temp_board)
            
            q.append((pos1[0], pos1[1], dist + dist3 + dist4 + 2, idx + 1))
            
        min_moves = min(min_moves, local_min)
        
    return min_moves
```
