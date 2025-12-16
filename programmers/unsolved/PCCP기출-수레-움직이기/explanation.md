# [PCCP 기출문제] 4번 / 수레 움직이기

## 문제 설명
n x m 크기의 격자에서 빨간 수레와 파란 수레를 각각의 시작 칸에서 도착 칸으로 이동시키는 문제입니다.
두 수레는 동시에 움직이며, 다음과 같은 규칙을 따릅니다.
1.  매 턴마다 상하좌우로 이동 (벽이나 격자 밖 불가).
2.  **자신이 방문했던 칸으로는 이동 불가.**
3.  도착 칸에 도착하면 그 자리에 고정 (더 이상 움직이지 않음).
4.  동시에 같은 칸으로 이동 불가.
5.  서로의 위치를 맞바꾸는 이동(Swap) 불가.
    -   예: Red(0,0)->(0,1) 이고 Blue(0,1)->(0,0) 인 경우 불가.

**목표**: 두 수레가 모두 도착 칸에 도달하는 데 걸리는 **최소 턴 수**를 구하세요. (불가능하면 0 반환)

## 접근법 & 주요 개념

### 1. BFS (너비 우선 탐색)
**최단 거리(최소 턴)**를 구하는 문제이므로 BFS가 적합합니다.
하지만 단순한 좌표(`rx, ry, bx, by`)만으로는 상태를 정의할 수 없습니다. "방문했던 칸으로 이동 불가"라는 조건 때문에, **각 수레가 방문한 경로(mask)**도 상태에 포함되어야 합니다.

-   **State Definition**: `(rx, ry, bx, by, r_mask, b_mask)`
    -   `rx, ry`: 빨간 수레 위치
    -   `bx, by`: 파란 수레 위치
    -   `r_mask`, `b_mask`: 빨간/파란 수레가 방문한 칸들을 비트마스크로 표현 (n, m <= 4 이므로 최대 16비트)

### 2. 비트마스크 (Bitmask)
격자의 크기가 최대 4x4(16칸)이므로, 방문 여부를 정수형 비트마스크로 관리할 수 있습니다.
-   `(i, j)` 좌표의 비트 위치: `i * m + j`
-   방문 처리: `mask |= (1 << (i * m + j))`
-   방문 확인: `mask & (1 << (i * m + j))`

### 3. 이동 규칙 구현
BFS의 각 단계에서 Red와 Blue의 가능한 다음 위치들을 구한 뒤, 두 수레의 조합(Product)에 대해 유효성을 검사합니다.
-   **도착한 경우**: 해당 수레는 현재 위치 유지 (`stay`).
-   **이동 가능한 경우**: 상하좌우 중 벽이 아니고, 자신의 방문 마스크에 없는 곳.
-   **조합 검증**:
    1.  `next_red == next_blue`: 겹침 불가.
    2.  `next_red == curr_blue` and `next_blue == curr_red`: 스위칭(Swap) 불가.

## Python 풀이

```python
from collections import deque

def solution(maze):
    n, m = len(maze), len(maze[0])
    
    # 1. 초기 위치 및 목표 위치 찾기
    rx, ry, bx, by = 0, 0, 0, 0
    tr, tc, tb, ttb = 0, 0, 0, 0 # target (red/blue)
    
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1: rx, ry = i, j
            elif maze[i][j] == 2: bx, by = i, j
            elif maze[i][j] == 3: tr, tc = i, j
            elif maze[i][j] == 4: tb, ttb = i, j
            
    # BFS 초기화
    # State: (rx, ry, bx, by, r_mask, b_mask)
    start_r_mask = 1 << (rx * m + ry)
    start_b_mask = 1 << (bx * m + by)
    
    q = deque()
    q.append((rx, ry, bx, by, start_r_mask, start_b_mask, 0))
    
    visited = set()
    visited.add((rx, ry, bx, by, start_r_mask, start_b_mask))
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    while q:
        crx, cry, cbx, cby, r_mask, b_mask, cost = q.popleft()
        
        # 둘 다 도착했으면 return
        if crx == tr and cry == tc and cbx == tb and cby == ttb:
            return cost
            
        # --- Red의 다음 이동 후보군 생성 ---
        next_reds = []
        if crx == tr and cry == tc:
            # 이미 도착했으면 제자리 유지
            next_reds.append((crx, cry))
        else:
            for i in range(4):
                nr, nc = crx + dx[i], cry + dy[i]
                if 0 <= nr < n and 0 <= nc < m and maze[nr][nc] != 5:
                    # 방문하지 않은 곳만
                    if not (r_mask & (1 << (nr * m + nc))):
                        next_reds.append((nr, nc))
                        
        # --- Blue의 다음 이동 후보군 생성 ---
        next_blues = []
        if cbx == tb and cby == ttb:
            # 이미 도착했으면 제자리 유지
            next_blues.append((cbx, cby))
        else:
            for i in range(4):
                nr, nc = cbx + dx[i], cby + dy[i]
                if 0 <= nr < n and 0 <= nc < m and maze[nr][nc] != 5:
                    # 방문하지 않은 곳만
                    if not (b_mask & (1 << (nr * m + nc))):
                        next_blues.append((nr, nc))
        
        # --- 두 수레의 이동 조합 검증 (Product) ---
        for nrx, nry in next_reds:
            for nbx, nby in next_blues:
                # 1. 동시에 같은 칸 불가
                if nrx == nbx and nry == nby:
                    continue
                # 2. 자리 바꾸기(Swap) 불가
                if nrx == cbx and nry == cby and nbx == crx and nby == cry:
                    continue
                
                # 마스크 업데이트
                # (주의: 도착해서 멈춰있는 경우는 마스크 업데이트 불필요하지만, 
                #  로직상 OR 연산을 해도 값은 변하지 않으므로 그대로 두어도 무방)
                new_r_mask = r_mask | (1 << (nrx * m + nry))
                new_b_mask = b_mask | (1 << (nbx * m + nby))
                
                if (nrx, nry, nbx, nby, new_r_mask, new_b_mask) not in visited:
                    visited.add((nrx, nry, nbx, nby, new_r_mask, new_b_mask))
                    q.append((nrx, nry, nbx, nby, new_r_mask, new_b_mask, cost + 1))
                    
    return 0
```

### 코드 분석
1.  **초기화**: `maze`를 순회하며 시작점과 끝점을 찾습니다.
2.  **BFS 큐**: `(Red좌표, Blue좌표, Red방문기록, Blue방문기록, 현재턴수)`를 저장합니다.
3.  **후보군 생성**: 도착한 수레는 현재 위치만 반환하고, 이동 중인 수레는 4방향 중 유효한(벽X, 미방문) 칸들을 반환합니다.
4.  **조합 및 검증**: 이중 루프를 통해 두 수레의 이동 조합을 만듭니다.
    -   `겹침`과 `스왑` 조건을 체크하여 유효하지 않은 이동을 걸러냅니다.
5.  **방문 체크**: 중복된 상태(좌표 + 마스크)를 큐에 넣지 않도록 `visited` set을 사용합니다.
6.  **결과**: 목표 상태에 도달하면 `cost`를 반환하고, 큐가 빌 때까지 도달 못하면 `0`을 반환합니다.

### 팁
-   격자 크기가 매우 작으므로(4x4), BFS의 상태 공간이 커 보여도 실제 유효한 경로는 제한적이어서 시간 내에 통과합니다.
-   Python의 `set`과 `deque`를 적극 활용하여 효율성을 높였습니다.
