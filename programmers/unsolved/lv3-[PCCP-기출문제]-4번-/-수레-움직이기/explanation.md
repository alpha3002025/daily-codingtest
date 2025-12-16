# [PCCP 기출문제] 4번 / 수레 움직이기

## 문제 설명
`n x m` 크기의 격자판에 빨간 수레와 파란 수레가 있습니다. 각 수레는 시작 위치에서 출발하여 도착 위치로 이동해야 합니다. 
- 수레는 상하좌우로 한 칸씩 이동합니다.
- 벽이나 격자 밖으로 나갈 수 없습니다.
- 자신이 방문했던 칸으로 다시 돌아갈 수 없습니다.
- 두 수레가 동시에 같은 칸에 있을 수 없습니다.
- 두 수레가 서로 자리를 바꿀 수 없습니다(Swapping 불가).
- 도착한 수레는 움직이지 않고 고정됩니다.

두 수레가 모두 도착하는 데 필요한 최소 턴 수를 구하세요.

## 문제 해결 전략

격자 크기가 최대 4x4로 매우 작습니다. 이는 **BFS(너비 우선 탐색)** 또는 **백트래킹**을 통한 완전 탐색이 가능함을 의미합니다. 상태 복잡도는 `(4x4) * (4x4) * visited_masks` 정도이나, 방문 체크가 경로 의존적이므로 단순 BFS보다는 **상태 기반 BFS**나 **백트래킹**이 적합합니다. 최단 거리를 구해야 하므로 BFS가 유리합니다.

### 상태 정의 (BFS)
- `(rx, ry, bx, by, r_visited, b_visited)`
- `r_visited`, `b_visited`: 비트마스크 또는 집합으로 방문한 좌표 관리.

### 이동 규칙
1. 매 턴마다 아직 도착하지 않은 수레는 4방향 이동 시도. 이미 도착한 수레는 제자리 유지(`dir=(0,0)`).
2. 두 수레의 다음 위치 `(nrx, nry)`, `(nbx, nby)` 결정.
3. **유효성 검사**:
   - 범위 체크, 벽 체크.
   - 자신의 `visited` 체크 (단, 도착한 수레는 예외).
   - **충돌 체크 1**: `(nrx, nry) == (nbx, nby)` (동일 위치 불가).
   - **충돌 체크 2**: `(nrx, nry) == (bx, by)` AND `(nbx, nby) == (rx, ry)` (자리 교환 불가).
4. 유효하면 큐에 추가. `visited` 업데이트.

## Python 코드

```python
from collections import deque

def solution(maze):
    n, m = len(maze), len(maze[0])
    
    rx, ry, bx, by = 0, 0, 0, 0
    rtx, rty, btx, bty = 0, 0, 0, 0
    
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1: rx, ry = i, j
            elif maze[i][j] == 2: bx, by = i, j
            elif maze[i][j] == 3: rtx, rty = i, j
            elif maze[i][j] == 4: btx, bty = i, j
            
    # BFS
    # state: rx, ry, bx, by, r_mask, b_mask
    start_r_mask = 1 << (rx * m + ry)
    start_b_mask = 1 << (bx * m + by)
    
    q = deque([(rx, ry, bx, by, start_r_mask, start_b_mask, 0)])
    visited_states = set()
    visited_states.add((rx, ry, bx, by, start_r_mask, start_b_mask))
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    while q:
        crx, cry, cbx, cby, crm, cbm, step = q.popleft()
        
        if crx == rtx and cry == rty and cbx == btx and cby == bty:
            return step
        
        # Red Moves
        r_moves = []
        if crx == rtx and cry == rty:
            r_moves.append((crx, cry))
        else:
            for i in range(4):
                nrx, nry = crx + dx[i], cry + dy[i]
                if 0 <= nrx < n and 0 <= nry < m and maze[nrx][nry] != 5:
                    if not (crm & (1 << (nrx * m + nry))):
                        r_moves.append((nrx, nry))
                        
        # Blue Moves
        b_moves = []
        if cbx == btx and cby == bty:
            b_moves.append((cbx, cby))
        else:
            for i in range(4):
                nbx, nby = cbx + dx[i], cby + dy[i]
                if 0 <= nbx < n and 0 <= nby < m and maze[nbx][nby] != 5:
                    if not (cbm & (1 << (nbx * m + nby))):
                        b_moves.append((nbx, nby))
                        
        # Combine Moves
        for nrx, nry in r_moves:
            for nbx, nby in b_moves:
                # Condition 1: Same position
                if nrx == nbx and nry == nby:
                    continue
                # Condition 2: Swap
                if nrx == cbx and nry == cby and nbx == crx and nby == cry:
                    continue
                
                nrm = crm
                nbm = cbm
                if not (nrx == rtx and nry == rty): # Only update visited if not arrived (or arriving now)
                     nrm |= (1 << (nrx * m + nry))
                     # wait, logic: "Cannot revisit". Once arrived, it stays. 
                     # Should we mark target as visited? Yes.
                     # Arrived cart stays at target. It counts as occupying.
                
                if not (nbx == btx and nby == bty):
                     nbm |= (1 << (nbx * m + nby))
                
                # Correction: Arrived cart doesn't add new visited bits but checking existing bits is fine.
                # Actually, the problem says "cannot revisit".
                # If arrived, it stays at P. It technically visits P every turn.
                # But treating "Arrived" as a special state is easier.
                # The mask update logic: if it moved to a NEW cell, add mask.
                # If it stayed because it's already there, mask doesn't change (already there).
                
                if (nrx, nry, nbx, nby, nrm, nbm) not in visited_states:
                    visited_states.add((nrx, nry, nbx, nby, nrm, nbm))
                    q.append((nrx, nry, nbx, nby, nrm, nbm, step + 1))
                    
    return 0
```
