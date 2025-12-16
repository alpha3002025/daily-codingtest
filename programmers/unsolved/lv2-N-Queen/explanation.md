# N-Queen

## 문제 설명
가로, 세로 길이가 `n`인 체스판 위에 `n`개의 퀸을 서로 공격할 수 없게 배치하는 방법의 수를 구하는 문제입니다. 퀸은 가로, 세로, 대각선으로 이동할 수 있습니다.

### 핵심 개념
1.  **백트래킹 (Backtracking)**: 가능한 모든 배치를 시도하되, 조건에 맞지 않으면(공격 가능하면) 더 이상 탐색하지 않고 되돌아갑니다.
2.  **1차원 배열 활용**: 2차원 배열 대신 1차원 배열 `queens[row] = col` 형태로 퀸의 위치를 저장할 수 있습니다.
    - 각 행(`row`)에는 어차피 퀸이 하나만 놓여야 하기 때문입니다.
3.  **검사 조건**:
    - 같은 열(`col`)에 있으면 안 됨: `queens[i] == queens[row]`
    - 대각선에 있으면 안 됨: `abs(queens[i] - queens[row]) == abs(i - row)` (가로 차이와 세로 차이가 같음)

## Python 풀이

```python
def solution(n):
    answer = 0
    # queens[row] = col : row번째 행의 col번째 열에 퀸이 있음
    queens = [0] * n
    
    def check(row):
        # 현재 row에 놓인 퀸이 이전 row들의 퀸과 충돌하는지 확인
        current_col = queens[row]
        for i in range(row):
            # 1. 같은 열(Vertical)
            if queens[i] == current_col:
                return False
            # 2. 대각선 (Diagonal)
            if abs(queens[i] - current_col) == (row - i):
                return False
        return True
    
    def dfs(row):
        nonlocal answer
        # n개의 퀸을 모두 배치했으면 성공
        if row == n:
            answer += 1
            return
        
        # 현재 행(row)의 각 열(col)에 퀸을 놓아봄
        for col in range(n):
            queens[row] = col
            # 유효하면 다음 행으로 진행
            if check(row):
                dfs(row + 1)
                
    dfs(0)
    return answer
```

### 코드 최적화
PyPy가 아닌 일반 Python에서는 위 코드가 $N=12$일 때 느릴 수 있습니다. 검사 로직을 `visited` 배열 3개로 바꾸면 $O(1)$ 검사가 가능해져 훨씬 빠릅니다.
- `visited_col[c]`: 열 점유 여부
- `visited_diag1[r+c]`: `/` 방향 대각선 점유 여부 (합이 일정)
- `visited_diag2[r-c]`: `\` 방향 대각선 점유 여부 (차가 일정)

```python
def solution(n):
    answer = 0
    v_col = [False] * n
    v_diag1 = [False] * (2 * n) # r + c
    v_diag2 = [False] * (2 * n) # r - c (인덱스 음수 방지 위해 +n 할 수도 있음)
    
    def dfs(row):
        nonlocal answer
        if row == n:
            answer += 1
            return
        
        for col in range(n):
            if not v_col[col] and not v_diag1[row + col] and not v_diag2[row - col + n]:
                v_col[col] = True
                v_diag1[row + col] = True
                v_diag2[row - col + n] = True
                
                dfs(row + 1)
                
                v_col[col] = False
                v_diag1[row + col] = False
                v_diag2[row - col + n] = False
                
    dfs(0)
    return answer
```
