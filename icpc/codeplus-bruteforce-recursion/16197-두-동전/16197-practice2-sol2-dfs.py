import sys
input = sys.stdin.readline

N,M = map(int, input().split())
board = []
coins = []


for r in range(N):
    row = input().strip()
    board.append(row)
    for c in range(M):
        if row[c] == 'o':
            coins.append((r,c))


directions = [(-1,0), (1,0), (0,-1), (0,1)]
min_moves = float('inf')


def dfs(r1, c1, r2, c2, depth):
    global min_moves

    if depth >= 10 or depth >= min_moves:
        return
    
    for dr, dc in directions:
        nr1, nc1 = r1+dr, c1+dc
        nr2, nc2 = r2+dr, c2+dc

        out1 = not (0 <= nr1 < N and 0 <= nc1 < M)
        out2 = not (0 <= nr2 < N and 0 <= nc2 < M)

        if out1 and out2:
            continue

        if out1 or out2:
            min_moves = min(min_moves, depth+1)
            continue

        ## 벽 처리
        if board[nr1][nc1] == '#': ## 벽
            nr1,nc1 = r1,c1
        if board[nr2][nc2] == '#': ## 벽
            nr2,nc2 = r2,c2

        dfs(nr1,nc1,nr2,nc2,depth+1)


dfs(coins[0][0], coins[0][1], coins[1][0], coins[1][1], 0)
print(min_moves if min_moves != float('inf') else -1)