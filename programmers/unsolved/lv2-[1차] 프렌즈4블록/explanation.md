# [1차] 프렌즈4블록

## 문제 설명
블라인드 공채 문제로, 2x2 형태로 같은 모양의 블록이 모이면 터지는 게임을 구현해야 합니다.
1. `m` x `n` 판이 주어짐.
2. 2x2 같은 모양 찾기.
3. 찾은 블록들 한꺼번에 터뜨리기 (빈 공간 됨).
4. 빈 공간이 생기면 위의 블록들이 아래로 떨어짐.
5. 더 이상 터질 게 없을 때까지 반복.

### 핵심 개념
1.  **시뮬레이션**: 문제에 주어진 순서(검사 -> 삭제 -> 이동)를 정확히 구현해야 합니다.
2.  **동시 삭제**: 2x2 블록이 겹칠 수 있으므로(예: 2x3 크기의 같은 블록들), 검사할 때는 터질 위치를 `Set`에 모아두고, 검사가 끝난 뒤 한꺼번에 지워야 합니다.
3.  **블록 내리기**:
    - 열(Column) 단위로 처리하는 것이 편합니다.
    - 빈 공간을 제외한 블록들을 모은 뒤, 위쪽을 빈 공간으로 채우는 방식 등으로 구현합니다.

## Python 풀이

```python
def solution(m, n, board):
    # 문자열은 수정 불가능하므로 리스트로 변환
    board = [list(row) for row in board]
    total_removed = 0
    
    while True:
        # 1. 터질 블록 위치 찾기 (Set 사용)
        matched = set()
        
        # (0,0) 부터 (m-2, n-2) 까지 순회하며 오른쪽, 아래, 대각선 확인
        for r in range(m - 1):
            for c in range(n - 1):
                block = board[r][c]
                if block == "": # 이미 빈 칸이면 패스
                    continue
                    
                # 2x2 확인
                if (board[r+1][c] == block and
                    board[r][c+1] == block and 
                    board[r+1][c+1] == block):
                    
                    matched.add((r, c))
                    matched.add((r+1, c))
                    matched.add((r, c+1))
                    matched.add((r+1, c+1))
        
        # 더 이상 터질 게 없으면 종료
        if not matched:
            break
            
        # 2. 블록 제거 카운트
        total_removed += len(matched)
        
        # 보드에서 실제로 제거 (빈 문자열로 표시)
        for r, c in matched:
            board[r][c] = ""
            
        # 3. 블록 내리기 (Drop)
        # 열 단위로 처리
        for c in range(n):
            # 빈 칸이 아닌 블록들만 추출
            temp = []
            for r in range(m):
                if board[r][c] != "":
                    temp.append(board[r][c])
            
            # 위쪽(앞쪽)을 빈 칸으로 채우고, 아래쪽(뒤쪽)에 블록 배치
            # 예: temp=['A', 'B'], m=4 -> ['', '', 'A', 'B']
            new_col = [""] * (m - len(temp)) + temp
            
            # 보드에 반영
            for r in range(m):
                board[r][c] = new_col[r]
                
    return total_removed
```

### 코드 설명
- `set`을 사용하여 중복된 좌표((1,1)이 왼쪽 2x2와 오른쪽 2x2에 모두 포함될 때)를 제거하고 정확히 터질 개수를 셉니다.
- **블록 내리기 로직**:
    - 각 열(`col`)에 대해 "살아남은 블록" 리스트를 만듭니다.
    - 리스트의 길이가 `m`보다 작다면, 부족한 만큼 앞에 `""`(빈 공간)을 채워 넣습니다.
    - 다시 `board`의 해당 열을 갱신합니다.
    - 이 방식이 인덱스를 하나씩 옮기는 것보다 구현하기 쉽고 실수할 확률이 적습니다.
