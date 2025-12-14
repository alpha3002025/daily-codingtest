"""
턴수 계산
val = dfs(opponent_pos, [nr,nc], board) + 1
      └──────────┬──────────────────┘     │
            상대방이 움직일 거리          내 이동 1턴
"""
def dfs(my_pos, opponent_pos, board):
    r,c = my_pos
    if board[r][c] == 0:
        return 0
    
    ret = 0
    
    for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
        nr, nc = r + dr, c + dc
        if not (0 <= nr < len(board) and 0 <= nc < len(board[0])):
            continue
        if board[nr][nc] == 0:
            continue
        
        board[r][c] = 0
        val = dfs(opponent_pos, [nr,nc], board) + 1
        board[r][c] = 1
        
        ## 현재까지 탐색한 수들은 모두 지는 수 (ret=짝수), 지금 발견한 수는 이기는 수(val=홀수)
        ## → 즉시 그 수로 교체 (A가 이길 수 있는 경로를 발견했으므로 그 경로의 게임 길이(val)를 선택)
        if ret % 2 == 0 and val % 2 == 1:
            ret = val
        ## 모든 선택지가 지는 경우
        ## → 최대한 오래 버티기 (게임을 길게 끌기)
        elif ret % 2 == 0 and val % 2 == 0:
            ret = max(ret, val)
        ## 모든 선택지가 이기는 경우
        ## → 최대한 오래 버티기 (게임을 길게 끌기)
        elif ret % 2 == 1 and val % 2 == 1:
            ret = min(ret, val)
    
    return ret

def solution(board, aloc, bloc):
    return dfs(aloc, bloc, board)