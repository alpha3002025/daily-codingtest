from collections import deque

N,M = map(int, input().split())
board = []
coins = []

## 보드 입력 + 동전 위치 찾기
for r in range(N):
    line = input().strip()
    board.append(line)
    for c in range(M):
        if line[c] == 'o':
            coins.append((r,c))


def bfs(board):
    ## BFS
    #### 상,하,좌,우
    directions = [(-1,0), (1,0), (0,-1), (0,1)] 
    #### [(p1.x, p1.y, p2.x, p2.y, cost)]
    queue = deque([(coins[0][0], coins[0][1], coins[1][0], coins[1][1], 0)]) 

    visited = set()
    visited.add((coins[0][0], coins[0][1], coins[1][0], coins[1][1]))


    while queue:
        r1,c1,r2,c2,cnt = queue.popleft()

        if cnt >= 10:
            continue

        for dr,dc in directions:
            nr1,nc1 = r1+dr, c1+dc
            nr2,nc2 = r2+dr, c2+dc

            out1 = not (0 <= nr1 < N and 0 <= nc1 < M)
            out2 = not (0 <= nr2 < N and 0 <= nc2 < M)

            if out1 and out2:
                continue

            if out1 or out2:
                print(cnt+1)
                return
            
            if board[nr1][nc1] == '#':
                nr1,nc1 = r1,c1
            if board[nr2][nc2] == '#':
                nr2,nc2 = r2,c2

            state = (nr1,nc1, nr2,nc2)
            if state not in visited:
                visited.add(state)
                queue.append((nr1,nc1,nr2,nc2,cnt+1))
    print(-1)


bfs(board)