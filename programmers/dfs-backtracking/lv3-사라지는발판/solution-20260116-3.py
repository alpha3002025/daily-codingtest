def solution(board, aloc, bloc):
    directions = [[-1,0], [1,0], [0,-1], [0,1]]
    R,C = len(board), len(board[0])
    
    def solve (curr_r, curr_c, opp_r, opp_c):
        if board[curr_r][curr_c] == 0:
            return False, 0
        
        can_win = False
        move_available = False
        min_win_turn, max_lose_turn = float('inf'), 0
        
        for dr, dc in directions:
            nr, nc = curr_r + dr, curr_c + dc
            
            if 0 <= nr < R and 0 <= nc < C and board[nr][nc] == 1:
                move_available = True
                
                board[curr_r][curr_c] = 0
                is_opp_win, opp_turns = solve(opp_r, opp_c, nr, nc)
                board[curr_r][curr_c] = 1
                
                if is_opp_win == True:
                    if not can_win:
                        max_lose_turn = max(max_lose_turn, opp_turns + 1)
                else:
                    can_win = True
                    min_win_turn = min(min_win_turn, opp_turns + 1)
        
        if not move_available:
            return False, 0
        
        if can_win:
            return True, min_win_turn
        else:
            return False, max_lose_turn
    
    is_win, optimal_cnt = solve(aloc[0], aloc[1], bloc[0], bloc[1])
    return optimal_cnt