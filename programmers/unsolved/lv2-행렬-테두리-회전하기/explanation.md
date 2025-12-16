# 행렬 테두리 회전하기

## 문제 설명
rows x columns 크기의 행렬에 1부터 순서대로 숫자가 채워져 있습니다. 직사각형 범위 `(x1, y1, x2, y2)` 가 주어질 때, 해당 테두리에 있는 숫자들을 시계 방향으로 한 칸씩 회전시킵니다. 회전할 때마다 **위치가 바뀐 숫자들 중 가장 작은 수**를 구해서 배열에 담아 반환해야 합니다.

### 핵심 개념
1.  **시뮬레이션 / 구현**: 복잡한 알고리즘 없이 문제의 요구사항을 그대로 구현하면 됩니다.
2.  **좌표 관리**: 문제의 좌표는 (1, 1)부터 시작하므로, 배열 인덱스 (0, 0)과 매칭할 때 `-1` 처리를 주의해야 합니다.
3.  **값 이동**: 배열의 값을 덮어쓰지 않고 이동시키려면,
    - 임시 변수에 하나를 저장해두고 밀거나,
    - `deque`의 `rotate`를 쓰거나,
    - 하나씩 덮어씌우는 순서를 잘 정해야 합니다 (시계 방향 회전이면, 반시계 방향으로 값을 끌어오거나 빈 공간을 활용 등).
    - 가장 쉬운 방법: **첫 번째 값을 변수에 저장(`temp`)해두고, 역순(반시계 방향)으로 값을 당겨와서 덮어쓰기**를 수행한 뒤, 마지막 빈 자리에 `temp`를 넣습니다.

## Python 풀이

```python
def solution(rows, columns, queries):
    # 1부터 순서대로 채워진 행렬 생성
    board = [[(r * columns + c + 1) for c in range(columns)] for r in range(rows)]
    answer = []
    
    for x1, y1, x2, y2 in queries:
        # 0-based index로 변환
        x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
        
        # 시작점(왼쪽 위) 값 저장
        temp = board[x1][y1]
        min_val = temp
        
        # 1. 왼쪽 세로줄 위로 이동 (Left side: move up)
        # (x1, y1) 자리는 나중에 덮어쓸 것이므로, (x1+1, y1)부터 시작해서 위로 올림
        for r in range(x1, x2):
            board[r][y1] = board[r+1][y1]
            min_val = min(min_val, board[r][y1])
            
        # 2. 아래쪽 가로줄 왼쪽으로 이동 (Bottom side: move left)
        for c in range(y1, y2):
            board[x2][c] = board[x2][c+1]
            min_val = min(min_val, board[x2][c])
            
        # 3. 오른쪽 세로줄 아래로 이동 (Right side: move down)
        for r in range(x2, x1, -1):
            board[r][y2] = board[r-1][y2]
            min_val = min(min_val, board[r][y2])
            
        # 4. 위쪽 가로줄 오른쪽으로 이동 (Top side: move right)
        for c in range(y2, y1, -1):
            board[x1][c] = board[x1][c-1]
            min_val = min(min_val, board[x1][c])
            
        # 마지막 빈 칸에 temp 값 넣기
        # 위 4번 과정에서 board[x1][y1+1] = board[x1][y1] 이 실행되었음.
        # board[x1][y1] 값은 이미 temp에 보관 중.
        # 회전 논리상 board[x1][y1+1] 자리에 원래 board[x1][y1]이 들어가야 함.
        # 4번 루프의 마지막 실행은 'c=y1+1'일 때 'board[x1][y1+1] = board[x1][y1]' 인데,
        # 이미 1번 루프에서 board[x1][y1]이 덮어쓰여짐?
        
        # *** 수정된 로직 ***
        # 덮어쓰기를 할 때는 '이동하는 방향의 역순'으로 처리하는 게 데이터 손실 방지에 좋습니다.
        # 예를 들어 시계방향 회전이면:
        # (1) [상단] 왼쪽 <- 오른쪽 당기기
        # (2) [우측] 위 <- 아래 당기기
        # (3) [하단] 오른쪽 <- 왼쪽 당기기
        # (4) [좌측] 아래 <- 위 당기기
        # 이 순서로 하면 맨 처음 좌표(x1, y1) 하나만 따로 빼두면 됩니다.
        
        # 다시 작성 (반시계 방향으로 값 당기기)
        
    return answer

# 재작성된 올바른 풀이
def solution(rows, columns, queries):
    board = [[(r * columns + c + 1) for c in range(columns)] for r in range(rows)]
    answer = []
    
    for x1, y1, x2, y2 in queries:
        x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
        
        temp = board[x1][y1] # 왼쪽 위 값 보관
        min_val = temp
        
        # 1. 왼쪽 열: 아래 -> 위 당기기 (board[x][y1] = board[x+1][y1])
        for r in range(x1, x2):
            board[r][y1] = board[r+1][y1]
            min_val = min(min_val, board[r][y1])
            
        # 2. 아래 행: 오른쪽 -> 왼쪽 당기기
        for c in range(y1, y2):
            board[x2][c] = board[x2][c+1]
            min_val = min(min_val, board[x2][c])
            
        # 3. 오른쪽 열: 위 -> 아래 당기기
        for r in range(x2, x1, -1):
            board[r][y2] = board[r-1][y2]
            min_val = min(min_val, board[r][y2])
            
        # 4. 위쪽 행: 왼쪽 -> 오른쪽 당기기
        for c in range(y2, y1, -1):
            board[x1][c] = board[x1][c-1]
            min_val = min(min_val, board[x1][c])
            
        # 마지막으로 빼둔 값을 (x1, y1 + 1)에 넣기
        # 시계방향 회전이므로 (x1, y1)에 있던 값은 (x1, y1+1)로 가야 함.
        board[x1][y1+1] = temp
        
        answer.append(min_val)
        
    return answer
```

### 코드 검증
- `temp` = `(x1, y1)` 값.
- 왼쪽 줄을 위로 당김 -> `(x1, y1)` 자리에 `(x1+1, y1)` 값이 들어옴. OK.
- ... 순차적으로 빈 공간을 메움.
- 마지막 윗줄: `(x1, y1+1)` 자리에 `(x1, y1)`(temp) 값이 들어가야 시계 방향 회전이 완성됨. `board[x1][y1+1] = temp`. OK.
- `min_val`은 이동되는 모든 숫자들과 `temp` 중에서 최솟값을 찾습니다. (temp는 코드상 `answer.append` 직전에 포함하거나 초기값으로 설정)

