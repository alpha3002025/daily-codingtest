# 퍼즐 조각 채우기

## 문제 설명
게임 보드(`game_board`)의 빈 칸(0)들을 테이블(`table`) 위에 있는 퍼즐 조각(1)들로 채워 넣는 문제입니다.
- 조각은 회전 가능하지만 뒤집을 수는 없습니다.
- 조각을 채웠을 때 **빈 공간이 남거나, 조각이 경계를 넘어가거나, 인접한 다른 빈 공간이 있으면 안 됩니다.**
- 즉, **빈 칸 모양과 퍼즐 조각 모양이 완전히 일치**해야 합니다.

## 접근법 & 주요 개념

### 1. BFS/DFS (영역 추출)
게임 보드의 빈 공간과 테이블의 퍼즐 조각을 각각 하나의 "모양(Shape)"으로 추출해야 합니다.
- `game_board`에서 값이 `0`인 연결된 영역을 찾습니다.
- `table`에서 값이 `1`인 연결된 영역을 찾습니다.
- BFS를 사용하여 상하좌우로 연결된 좌표들을 리스트로 수집합니다.

### 2. 좌표 정규화 (Normalization)
추출된 모양들은 보드 상의 절대 좌표를 가지고 있으므로, 서로 비교하기 위해 **(0, 0)을 기준**으로 하는 상대 좌표로 변환해야 합니다.
- 모양을 구성하는 좌표 중 가장 작은 행(min_r)과 가장 작은 열(min_c)을 찾습니다.
- 모든 좌표에서 `(min_r, min_c)`를 빼서 평행 이동시킵니다.
- 비교를 용이하게 하기 위해 좌표 리스트를 정렬합니다.

### 3. 회전 (Rotation)
퍼즐 조각은 90도씩 회전이 가능하므로, 4가지 방향에 대해 모두 확인해야 합니다.
- 90도 회전 변환 공식: `(r, c) -> (c, -r)`
- 회전 후 다시 정규화 과정을 거쳐야 올바르게 비교할 수 있습니다.

## Python 풀이

```python
from collections import deque

def solution(game_board, table):
    answer = 0
    N = len(game_board)
    
    # 1. 보드에서 빈 공간(0) 추출
    empty_spaces = extract_shapes(game_board, 0)
    # 2. 테이블에서 퍼즐 조각(1) 추출
    puzzle_pieces = extract_shapes(table, 1)
    
    visited_pieces = [False] * len(puzzle_pieces)
    
    for space in empty_spaces:
        filled = False
        for i, piece in enumerate(puzzle_pieces):
            if visited_pieces[i]:
                continue
            
            # 퍼즐 조각과 빈 공간의 칸 수가 다르면 검사할 필요 없음
            if len(space) != len(piece):
                continue
            
            # 4번 회전하며 매칭 시도
            target_piece = piece
            for _ in range(4):
                target_piece = rotate(target_piece)
                # 정규화하여 비교
                if normalize(space) == normalize(target_piece):
                    answer += len(piece)
                    visited_pieces[i] = True
                    filled = True
                    break
            if filled:
                break
                
    return answer


def extract_shapes(board, target_value):
    N = len(board)
    visited = [[False] * N for _ in range(N)]
    shapes = []
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    for i in range(N):
        for j in range(N):
            if board[i][j] == target_value and not visited[i][j]:
                queue = deque([(i, j)])
                visited[i][j] = True
                shape = [(i, j)]
                
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < N and 0 <= ny < N:
                            if board[nx][ny] == target_value and not visited[nx][ny]:
                                visited[nx][ny] = True
                                queue.append((nx, ny))
                                shape.append((nx, ny))
                shapes.append(shape)
    return shapes


def normalize(shape):
    # 좌표 정렬 (행 우선, 열 차선)
    shape.sort()
    # 기준점 (가장 위, 가장 왼쪽)
    min_r, min_c = shape[0]
    
    normalized = []
    for r, c in shape:
        normalized.append((r - min_r, c - min_c))
    return normalized


def rotate(shape):
    # 90도 회전 변환: (r, c) -> (c, -r)
    rotated = []
    for r, c in shape:
        rotated.append((c, -r))
    return normalize(rotated)
```

### 코드 분석
1.  **`extract_shapes`**: BFS를 이용해 연결된 좌표들을 추출합니다. `game_board`에서는 `0`이 타겟, `table`에서는 `1`이 타겟입니다.
2.  **`normalize`**: 추출된 좌표들을 `(0, 0)` 기준으로 평행 이동시키고 정렬하여, 모양 비교가 가능하도록 만듭니다.
3.  **`rotate`**: 좌표를 90도 회전시킵니다. 회전 후 다시 `normalize`를 호출해야 일관된 비교가 가능합니다.
4.  **`solution`**: 모든 빈 공간(`empty_spaces`)에 대해 사용하지 않은 퍼즐 조각(`puzzle_pieces`)들을 회전시켜가며 맞춰봅니다. 딱 맞는 조각을 찾으면 개수를 더하고 해당 조각을 사용 처리합니다.


## 개념 설명

### 행렬 회전 (Matrix Rotation)
2차원 배열이나 좌표를 다룰 때 회전 변환은 매우 빈번하게 사용되는 테크닉입니다. `(r, c)` 좌표를 기준으로 한 회전 공식은 다음과 같습니다.

#### 기본 원리
일반적으로 N x N 행렬에서의 회전을 생각하면 이해가 쉽지만, 여기서는 좌표 리스트를 다루므로 상대적인 위치 변화에 집중합니다. `(r, c)`는 `(행, 열)` 또는 `(y, x)`를 의미합니다.

1.  **90도 회전 (시계 방향)**
    -   **공식**: `(r, c) -> (c, -r)`
    -   행(Row)은 열(Col)이 되고, 열(Col)은 부호를 바꿔서 행(Row)이 됩니다.
    -   배열 인덱스 기준(`N x N`): `(r, c) -> (c, N - 1 - r)`
    -   **예시**: `(0, 0) -> (0, 0)`, `(0, 1) -> (1, 0)`, `(1, 0) -> (0, -1)`
        -   원래: `[(0,0), (0,1)]` (가로 막대)
        -   90도: `[(0,0), (1,0)]` (세로 막대) (이후 정규화 필요)

2.  **180도 회전**
    -   90도 회전을 두 번 한 것과 같습니다.
    -   **공식**: `(r, c) -> (-r, -c)`
    -   모든 좌표의 부호가 반대로 바뀝니다. (원점 대칭)
    -   배열 인덱스 기준(`N x N`): `(r, c) -> (N - 1 - r, N - 1 - c)`
    -   **예시**: `[(0,0), (0,1), (1,1)]` ('ㄱ' 모양)
        -   180도: `[(0,0), (0,-1), (-1,-1)]` (`-` 처리 후 정규화하면 'ㄴ' 뒤집은 모양)

3.  **270도 회전 (반시계 90도)**
    -   90도 회전을 세 번 한 것과 같습니다.
    -   **공식**: `(r, c) -> (-c, r)`
    -   행(Row)은 열(Col)이 되면서 부호가 바뀌고, 열(Col)은 그대로 행(Row)이 됩니다.
    -   배열 인덱스 기준(`N x N`): `(r, c) -> (N - 1 - c, r)`

> **Tip**: 이 문제에서는 좌표 `(r, c)`를 `(c, -r)`로 변환하는 90도 회전 로직 하나만 구현해두고, 이를 반복해서 호출(`rotate` -> `rotate` -> ...)하는 방식으로 90도, 180도, 270도를 모두 쉽게 처리할 수 있습니다. 그래서 별도의 180도/270도 공식을 코드로 짤 필요는 없습니다.


### 행렬 회전 (N x M 행렬) 개념
정사각형(N x N)이 아닌 직사각형(N x M) 행렬을 회전할 때는 행(`r`)과 열(`c`)의 크기가 서로 바뀌는 점을 주의해야 합니다.

*   원본 행렬: `N`행 `M`열 (`N x M`)
*   행 인덱스 `r`: `0` ~ `N-1`
*   열 인덱스 `c`: `0` ~ `M-1`

#### 1. 90도 회전 (시계 방향)
회전 후에는 `M`행 `N`열 (`M x N`) 행렬이 됩니다.
-   **공식**: `new_matrix[c][N - 1 - r] = matrix[r][c]`
-   새 좌표: `(c, N - 1 - r)`
-   원본의 `0`행은 결과의 `N-1`열(마지막 열)이 됩니다.

#### 2. 180도 회전
회전 후 크기는 그대로 `N`행 `M`열 (`N x M`) 입니다.
-   **공식**: `new_matrix[N - 1 - r][M - 1 - c] = matrix[r][c]`
-   새 좌표: `(N - 1 - r, M - 1 - c)`
-   완전히 뒤집힌 상하좌우 대칭 형태가 됩니다.

#### 3. 270도 회전 (반시계 90도)
회전 후에는 `M`행 `N`열 (`M x N`) 행렬이 됩니다.
-   **공식**: `new_matrix[M - 1 - c][r] = matrix[r][c]`
-   새 좌표: `(M - 1 - c, r)`
-   원본의 `0`열은 결과의 `M-1`행(마지막 행)이 됩니다.

#### Python 구현 예시 (90도 회전)

```python
def rotate_NxM_90(matrix):
    N = len(matrix)
    M = len(matrix[0])
    new_matrix = [[0] * N for _ in range(M)] # M x N 크기 생성
    
    for r in range(N):
        for c in range(M):
            new_matrix[c][N - 1 - r] = matrix[r][c]
            
    return new_matrix
```



### 좌표 정규화 개념
서로 다른 위치에 있는 두 모양이 **같은 모양인지** 비교하기 위해서는, 모양을 구성하는 좌표들의 **기준점(Reference Point)**을 통일시켜야 합니다. 이를 '좌표 정규화'라고 합니다.

#### 원리
1.  **목표**: 모양의 절대적인 위치(Absolute Position) 정보를 제거하고, **상대적인 형태(Relative Shape)** 정보만 남기기 위함입니다.
2.  **방법**:
    -   가장 위쪽, 그리고 가장 왼쪽에 있는 점을 `(0, 0)`으로 만듭니다.
    -   이를 위해 모양을 구성하는 모든 좌표들 중 **가장 작은 행(min_r)**과 **가장 작은 열(min_c)** 값을 찾습니다.
    -   모든 좌표 `(r, c)`에서 `(min_r, min_c)`를 뺍니다.
    -   변환 공식: `(r - min_r, c - min_c)`
3.  **예시**:
    -   `board`의 빈 공간 좌표: `[(2, 3), (2, 4), (3, 3)]` (ㄱ 모양)
    -   `table`의 퍼즐 조각 좌표: `[(5, 1), (5, 2), (6, 1)]` (같은 ㄱ 모양)
    
    이 두 리스트를 그대로 비교하면 숫자가 다르므로 `Different`로 판별됩니다. 하지만 정규화를 수행하면:
    -   `empty`: min=(2,3) -> `[(0, 0), (0, 1), (1, 0)]`
    -   `piece`: min=(5,1) -> `[(0, 0), (0, 1), (1, 0)]`
    
    이제 두 리스트가 **완벽히 일치**하게 되어 같은 모양임을 알 수 있습니다. 반드시 비교 전에 좌표를 **정렬(Sort)**해야 순서 문제 없이 비교할 수 있습니다.



