def solution(board, aloc, bloc):
    directions = [[-1,0], [1,0], [0,-1], [0,1]]
    R,C = len(board), len(board[0])
    
    def solve(curr_r, curr_c, opp_r, opp_c):
        ## 1. 현재 발판이 없으면 즉시 패배
        if board[curr_r][curr_c] == 0:
            return False, 0
        
        can_win = False
        move_available = False
        min_win_turn, max_lose_turn = float('inf'), 0
        
        for dr,dc in directions:
            nr, nc = curr_r + dr, curr_c + dc
            
            ## 이동 가능 조건: 범위 내 & 발판 존재
            if 0 <= nr < R and 0 <= nc < C and board[nr][nc] == 1:
                move_available = True
                
                ## A. 이동 & 발판 삭제
                board[curr_r][curr_c] = 0
                
                ## B. 상대방 턴 진행 (재귀)
                ## 상대의 승리여부 = 나의 패배 여부
                is_opp_win, opp_turn = solve(opp_r, opp_c, nr, nc)
                
                ## C. 발판 복구 (백트래킹)
                board[curr_r][curr_c] = 1
                
                ## D. 결과 판단
                ## 상대가 지면(False) -> 나는 이기는 수 (Winning Move)
                if not is_opp_win:
                    can_win = True
                    ## 이기는 경우 중 가장 빨리 이기는 길 선택 (Min)
                    min_win_turn = min(min_win_turn, opp_turn + 1)
                else:
                    ## 상대가 이기면 : 나는 지는 수
                    ## 아직 이기는 경우를 못 찾았을 때만, 지더라도 최대한 늦게 지는 길 선택 (Max)
                    if not can_win:
                        max_lose_turn = max(max_lose_turn, opp_turn + 1)
        
        ## 2. 이동할 곳이 없을 경우 패배
        if not move_available:
            return False, 0
        
        ## 3. 결과 반환
        if can_win:
            return True, min_win_turn
        else:
            return False, max_lose_turn
    
    is_a_winner, total_turns = solve(aloc[0], aloc[1], bloc[0], bloc[1])
    return total_turns