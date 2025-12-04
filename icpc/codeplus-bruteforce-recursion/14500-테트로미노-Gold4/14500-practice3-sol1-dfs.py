import sys
input = sys.stdin.readline

N,M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

dir = [
    (-1,0), (1,0), (0,-1), (0,1)
]

max_sum = float('-inf')
def backtracking(r, c, depth, acc):
    global max_sum

    if depth == 4:
        max_sum = max(max_sum, acc)
        return
    
    for dr,dc in dir:
        nr,nc = r+dr,c+dc
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
            visited[nr][nc] = True
            backtracking(nr, nc, depth+1, acc+board[nr][nc])
            visited[nr][nc] = False


def check_t_shape(r,c):
    global max_sum

    t_shapes = [
        ## ㅏ
        [(0,0), (1,0), (2,0), (1,1)],
        ## ㅓ
        [(1,0), (0,1), (1,1), (2,1)],
        ## ㅜ
        [(0,0), (0,1), (0,2), (1,1)],
        ## ㅗ
        [(1,0), (1,1), (1,2), (0,1)]
    ]

    for shape in t_shapes:
        total = 0
        valid = True

        for dr,dc in shape:
            nr,nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < M:
                total += board[nr][nc]
            else:
                valid = False
                break
        if valid:
            max_sum = max(max_sum, total)


for i in range(N):
    for j in range(M):
        ## (i,j) 에 대해 dfs 를 모두 1번씩 실행해본다.
        visited[i][j] = True
        backtracking(i,j,1,board[i][j])
        visited[i][j] = False

        check_t_shape(i,j)

print(max_sum)