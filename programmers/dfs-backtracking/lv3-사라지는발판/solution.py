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