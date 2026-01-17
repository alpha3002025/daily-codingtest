# 퍼즐 조각 채우기

## 문제 설명
`game_board`에 빈 공간(0)들이 있고, `table`에 퍼즐 조각(1)들이 있습니다.
모든 퍼즐 조각은 1x1 크기의 단위 정사각형들로 이루어져 있습니다.
- 조각을 회전(90도 단위) 시킬 수 있습니다.
- 뒤집을 수는 없습니다 (문제: "회전시킬 수 있습니다"만 언급). -> "뒤집을 수 없습니다" 조건 있음.
- 빈 공간과 조각의 모양이 완벽하게 일치해야 채울 수 있습니다. (인접한 칸이 비면 안 되고, 조각이 경계 밖으로 나가서도 안 됨. 즉, 덩어리 모양 자체가 완전히 같아야 함)
- 채운 조각의 총 칸 수를 구하세요.

## 문제 해결 전략

1. **덩어리 추출 (BFS/DFS)**:
   - `game_board`에서 빈 공간(0) 덩어리들을 모두 찾습니다.
   - `table`에서 퍼즐 조각(1) 덩어리들을 모두 찾습니다.
   - 각 덩어리는 좌표들의 리스트로 표현합니다.

2. **좌표 정규화 (Normalization)**:
   - 각 덩어리의 좌표들을 `(0, 0)` 기준으로 이동시킵니다.
   - `min_x`, `min_y`를 찾아 모든 좌표에서 빼주어, 좌상단에 밀착시킵니다.
   - 정렬을 수행하여 비교를 쉽게 합니다.

3. **회전 (Rotation)**:
   - 2차원 배열 회전 또는 좌표 회전 변환을 사용합니다.
   - `(x, y)` -> `(y, n-1-x)` (n은 덩어리의 너비/높이)
   - 퍼즐 조각을 0, 90, 180, 270도 회전시켜 가며 빈 공간 덩어리와 비교합니다.

4. **매칭 (Matching)**:
   - 빈 공간 리스트(`spaces`)와 퍼즐 조각 리스트(`puzzles`)를 비교합니다.
   - 각 빈 공간에 대해, 사용되지 않은 퍼즐 조각들 중 모양이 일치하는 것이 있는지 확인합니다.
   - 회전된 4가지 모양 중 하나라도 일치하면 매칭 성공.
   - 매칭된 퍼즐 조각은 `used` 처리하고, 해당 조각의 칸 수만큼 답에 더합니다.

## Python 코드

```python
from collections import deque

def solution(game_board, table):
    n = len(game_board)
    
    # BFS로 덩어리 좌표 추출 함수
    def get_blocks(board, target_val):
        visited = [[False]*n for _ in range(n)]
        blocks = []
        
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        
        for i in range(n):
            for j in range(n):
                if board[i][j] == target_val and not visited[i][j]:
                    q = deque([(i, j)])
                    visited[i][j] = True
                    block = [] # (r, c)
                    
                    while q:
                        cx, cy = q.popleft()
                        block.append((cx, cy))
                        for k in range(4):
                            nx, ny = cx + dx[k], cy + dy[k]
                            if 0 <= nx < n and 0 <= ny < n:
                                if not visited[nx][ny] and board[nx][ny] == target_val:
                                    visited[nx][ny] = True
                                    q.append((nx, ny))
                    blocks.append(block)
        return blocks
        
    # 좌표 정규화: (0,0) 시작으로 평행이동
    def normalize(block):
        min_x = min(b[0] for b in block)
        min_y = min(b[1] for b in block)
        return sorted([(b[0]-min_x, b[1]-min_y) for b in block])
    
    # 90도 회전 함수
    def rotate(block):
        if not block: return []
        # 현재 블록의 크기(범위) 계산 -> 회전 중심? 아님 그냥 좌표 변환 후 다시 정규화하면 됨.
        # 90도 회전: (r, c) -> (c, -r) 혹은 (c, max_r - r)
        # 단순히 (c, -r) 하고 normalize 하면 됨.
        new_block = [(c, -r) for r, c in block]
        return normalize(new_block)
        
    # 1. 덩어리 추출
    # game_board: 빈 공간은 0
    # table: 조각은 1
    empty_blocks = [normalize(b) for b in get_blocks(game_board, 0)]
    puzzle_blocks = [normalize(b) for b in get_blocks(table, 1)]
    
    answer = 0
    puzzle_used = [False] * len(puzzle_blocks)
    
    # 2. 매칭
    for empty in empty_blocks:
        filled = False
        for i, puzzle in enumerate(puzzle_blocks):
            if puzzle_used[i]: continue
            
            # 칸 수가 다르면 패스
            if len(empty) != len(puzzle): continue
            
            # 회전하며 비교
            curr_puzzle = puzzle
            match_found = False
            for _ in range(4):
                if curr_puzzle == empty:
                    match_found = True
                    break
                curr_puzzle = rotate(curr_puzzle)
                
            if match_found:
                answer += len(empty)
                puzzle_used[i] = True
                break # 다음 빈 공간으로
                
    return answer
```
