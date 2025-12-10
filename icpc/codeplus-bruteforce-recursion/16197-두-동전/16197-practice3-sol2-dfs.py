import sys
input = sys.stdin.readline

N,M = map(int, input().split())

COIN,EMPTY,WALL = "o",".","#"
board = []
coins = []

for i in range(N):
    row = input()
    board.append(row)
    for j in range(len(row)):
        if row[j] == COIN:
            coins.append((i,j))

directions = [(-1,0),(1,0),(0,-1),(0,1)]

min_move_cnt = float('inf')
def backtracking(board, coin1_pos, coin2_pos, move_cnt):
    global min_move_cnt

    if move_cnt >= 10 or move_cnt >= min_move_cnt:
        return
    
    for dr,dc in directions:
        nr1,nc1 = coin1_pos[0]+dr, coin1_pos[1]+dc
        nr2,nc2 = coin2_pos[0]+dr, coin2_pos[1]+dc

        out1 = not (0 <= nr1 < N and 0 <= nc1 < M)
        out2 = not (0 <= nr2 < N and 0 <= nc2 < M)

        if out1 and out2:
            continue
        if out1 or out2:
            min_move_cnt = min(min_move_cnt, move_cnt+1)
            continue
        
        (nr1,nc1) = (nr1,nc1) if board[nr1][nc1] != WALL else coin1_pos
        (nr2,nc2) = (nr2,nc2) if board[nr2][nc2] != WALL else coin2_pos

        backtracking(board, (nr1,nc1), (nr2,nc2), move_cnt+1)


backtracking(board, coins[0], coins[1], 0)

if min_move_cnt > 10:
    print(-1)
else:
    print(min_move_cnt if min_move_cnt != float('inf') else -1)
