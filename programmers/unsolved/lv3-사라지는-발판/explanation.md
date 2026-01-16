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

이 문제는 **게임 이론(Game Theory)**과 **최소-최대 알고리즘(Minimax Algorithm)**을 기반으로 한 완전 탐색(DFS + Backtracking) 문제입니다. 상태 공간이 작으므로($5 \times 5$), 완전 탐색이 가능합니다.<br/>

두 플레이어(A, B)가 최적의 전략으로 게임을 진행한다고 가정할 때, 이기는 플레이어는 **최소한의 턴**으로 이기려 하고, 지는 플레이어는 **최대한 많은 턴**을 버티려 합니다.<br/>
<br/>

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


### 핵심 로직: Minimax 변형

1.  **상태 정의**: 현재 플레이어 위치, 상대방 위치, 보드 상태
2.  **종료 조건**:
    *   현재 서 있는 발판이 이미 사라진 경우 (패배)
    *   상하좌우 4방향 중 이동할 수 있는 발판이 없는 경우 (패배)
    *   두 플레이어가 같은 위치에 있다가 한 명이 이동하면, 원래 있던 발판이 사라지므로 남은 플레이어는 즉시 패배하게 됨
3.  **승패 판단 (Recursive Step)**:
    *   현재 플레이어가 이동 가능한 모든 위치에 대해 재귀적으로 함수를 호출합니다.
    *   **내가 이기는 경우 (`can_win = True`)**:
        *   상대방이 지는 경로가 하나라도 있다면, 나는 그 경로를 선택하여 필승할 수 있습니다.
        *   이때의 전략은 **최소 턴 승리** (`min`)입니다.
    *   **내가 지는 경우 (`can_win = False`)**:
        *   어딜 가도 상대방이 이긴다면, 나는 어쩔 수 없이 패배하게 됩니다.
        *   이때의 전략은 **최대 턴 버티기** (`max`)입니다.


<br/>
<br/>

## Python 코드 (상태 분리 풀이) (추천) (2)
```python
def solution(board, aloc, bloc):
    # 상, 하, 좌, 우
    DY = [-1, 1, 0, 0]
    DX = [0, 0, -1, 1]
    R, C = len(board), len(board[0])
    
    # solve: (현재 플레이어 위치, 상대방 위치) -> (이길 수 있는지, 총 턴 수)
    def solve(cur_r, cur_c, opp_r, opp_c):
        # 1. 현재 발판이 없으면 즉시 패배 (이미 떠난 자리)
        if board[cur_r][cur_c] == 0:
            return False, 0
            
        can_win = False
        min_win_turn = float('inf')
        max_lose_turn = 0
        
        move_available = False
        
        for i in range(4):
            nr, nc = cur_r + DY[i], cur_c + DX[i]
            
            # 이동 가능 조건: 범위 내 & 발판 존재
            if 0 <= nr < R and 0 <= nc < C and board[nr][nc] == 1:
                move_available = True
                
                # A. 이동 및 발판 삭제
                board[cur_r][cur_c] = 0
                
                # B. 상대방 턴 진행 (재귀)
                # 상대의 승리 여부 = 나의 패배 여부
                is_opp_win, opp_turn = solve(opp_r, opp_c, nr, nc)
                
                # C. 발판 복구 (백트래킹)
                board[cur_r][cur_c] = 1
                
                # D. 결과 판단
                # 상대가 지면(False) -> 나는 이기는 수 (Winning Move)
                if not is_opp_win:
                    can_win = True
                    # 이기는 경우 중 가장 빨리 이기는 길 선택 (Min)
                    min_win_turn = min(min_win_turn, opp_turn + 1)
                else:
                    # 상대가 이기면 -> 나는 지는 수
                    # 아직 이기는 수를 못 찾았을 때만, 지더라도 최대한 늦게 지는 길 선택 (Max)
                    if not can_win:
                        max_lose_turn = max(max_lose_turn, opp_turn + 1)
        
        # 2. 이동할 곳이 없으면 패배
        if not move_available:
            return False, 0
            
        # 3. 결과 반환
        if can_win:
            return True, min_win_turn
        else:
            return False, max_lose_turn

    # 초기 호출 (A 시작)
    is_a_winner, total_turns = solve(aloc[0], aloc[1], bloc[0], bloc[1])
    return total_turns
```
<br/>


## Python 코드 (상태 분리 풀이) (추천) (2)
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
<br/>

## 참고) 예전 ai-bio 풀이 (변태풀이)
True/False 가 아닌 홀수/짝수 로 승리를 판단했었다. 

반환값을 하나의 정수로 관리하며, 값의 홀/짝 여부(Parity)로 승패를 판단합니다.
- **홀수**: 현재 플레이어의 승리 (1턴 움직여서 상대를 짝수(패배) 상태로 만들었으므로)
- **짝수**: 현재 플레이어의 패배

```python
def dfs(my_pos, opponent_pos, board):
    r, c = my_pos
    if board[r][c] == 0: return 0  # 패배
    
    ret = 0
    for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
        nr, nc = r + dr, c + dc
        # ... 범위 및 발판 체크 ...
        if board[nr][nc] == 0: continue
        
        board[r][c] = 0
        val = dfs(opponent_pos, [nr,nc], board) + 1
        board[r][c] = 1
        
        # 1. 짝수(패배) 상태에서 홀수(승리) 경로 발견 시 -> 무조건 승리 경로 선택(Min)
        if ret % 2 == 0 and val % 2 == 1:
            ret = val
        # 2. 둘 다 패배(짝수)인 경우 -> 최대한 오래 버티기 (Max)
        elif ret % 2 == 0 and val % 2 == 0:
            ret = max(ret, val)
        # 3. 둘 다 승리(홀수)인 경우 -> 최대한 빨리 이기기 (Min)
        elif ret % 2 == 1 and val % 2 == 1:
            ret = min(ret, val)
            
    return ret
```

## 정리
- **승리 조건**: 내 턴에 상대를 "패배" 상태로 만들 수 있는 수가 하나라도 있으면 승리. (전략: **최단 거리**)
- **패배 조건**: 모든 수가 상대를 "승리" 상태로 만들어 주거나, 움직일 곳이 없으면 패배. (전략: **최장 거리**)
- 추천 풀이인 **상태 분리 방식**이 코드의 의도를 파악하기 훨씬 쉬우며, 실전에서도 실수를 줄일 수 있습니다.

