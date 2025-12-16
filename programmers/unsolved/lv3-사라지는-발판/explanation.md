# 사라지는 발판

## 문제 설명
$N \times M$ 격자 위에서 두 플레이어 A, B가 번갈아 가며 이동합니다.
- 현재 서 있는 발판에서 상하좌우 인접한 발판으로 이동 가능합니다(발판이 있어야 함).
- 이동 후 원래 있던 발판은 **사라집니다** (다시 밟을 수 없음).
- 이동할 수 없으면 패배합니다.
- A와 B는 최적의 플레이를 합니다:
  - 이길 수 있는 플레이어는 **최대한 빨리** 이기려 합니다. (최소 턴 승리)
  - 질 수밖에 없는 플레이어는 **최대한 오래** 버티려 합니다. (최대 턴 패배)
- 두 캐릭터가 움직인 횟수의 총합을 구하세요.

## 문제 해결 전략

**게임 이론(Minimax Algorithm)**과 **DFS(백트래킹)** 문제입니다.
상태 공간이 작으므로($5 \times 5$), 완전 탐색이 가능합니다.

1. **재귀 함수 `solve(board, curx, cury, opx, opy)`**:
   - 현재 플레이어(`cur`)가 이동 가능하다. 상대방(`op`) 위치는 고정.
   - 현재 위치의 발판이 없거나(이미 사라짐), 4방향 모두 갈 곳이 없으면 **패배(턴 0)**를 반환합니다.
   
2. **Minimax 로직**:
   - 현재 플레이어가 갈 수 있는 모든 방향에 대해 재귀 호출하여 결과를 받습니다. (상대방 턴으로 넘어감)
   - 결과(`win/lose`, `turns`)들이 모입니다.
     - 상대방이 진다면(`lose`), 나는 이기는 것(`win`)입니다.
     - 상대방이 이긴다면(`win`), 나는 지는 것(`lose`)입니다.
   
   - **승리 가능성 확인**:
     - 하나라도 이기는 경로가 있으면, 나는 **승리**하는 플레이어입니다.
     - 승리하는 경로들 중 **최단 턴수(min)**를 선택해야 합니다. (빨리 이기려 함)
   
   - **패배 확정**:
     - 모든 경로에서 상대가 이긴다면(나는 짐), 나는 **패배**하는 플레이어입니다.
     - 패배하는 경로들 중 **최대 턴수(max)**를 선택해야 합니다. (오래 버티려 함)

   - 반환값: `(승패 여부, 총 턴수)`

3. **주의사항**:
   - 같은 발판에 두 플레이어가 있을 때, 내가 이동하면 발판이 사라지므로 상대는 즉시 떨어져 죽습니다. (즉, 내가 이동하자마자 상대 패배 -> 나의 승리)

## Python 코드

```python
def solution(board, aloc, bloc):
    n = len(board)
    m = len(board[0])
    
    # 4방향
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    def solve(cur_board, cur_x, cur_y, op_x, op_y):
        # 1. 현재 발판이 없으면 패배
        if cur_board[cur_x][cur_y] == 0:
             return False, 0
             
        can_move = False
        winning_moves = []
        losing_moves = []
        
        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and cur_board[nx][ny] == 1:
                can_move = True
                
                # 이동 처리 (발판 사라짐)
                cur_board[cur_x][cur_y] = 0
                
                # 상대방 턴 호출
                is_op_win, turn_cnt = solve(cur_board, op_x, op_y, nx, ny)
                
                # 복구
                cur_board[cur_x][cur_y] = 1
                
                # 해석: 상대가 이기면 나는 짐, 상대가지면 나는 이김
                if not is_op_win: # 내가 이김
                    winning_moves.append(turn_cnt + 1)
                else: # 내가 짐
                    losing_moves.append(turn_cnt + 1)
                    
        # 2. 갈 곳이 없으면 패배
        if not can_move:
            return False, 0
            
        # 3. 결과 결정
        if winning_moves:
            # 이길 수 있는 경우가 하나라도 있으면, 최소 턴으로 이김
            return True, min(winning_moves)
        else:
            # 다 지는 경우라면, 최대 턴으로 버팀
            return False, max(losing_moves)

    # A 차례로 시작
    result_win, result_turns = solve(board, aloc[0], aloc[1], bloc[0], bloc[1])
    return result_turns
```
