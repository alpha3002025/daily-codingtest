import sys
input = sys.stdin.readline

N,M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

visited = [[False]*M for _ in range(N)]
max_sum = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, depth, total):
    global max_sum

    if depth == 4:
        max_sum = max(max_sum, total)
        return
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, depth + 1, total + board[nx][ny])
            visited[nx][ny] = False


def check_t_shape(x,y):
    """
    클로드 주석이 잘못된 거였다. 저번에 풀때 이것때문에 시간 낭비.
    ㅜ = 
    (0,0), (0,1), (0,2)
            (1,1)

    ㅗ =
           (0,1)
    (1,0),(1,1),(1,2)

    ㅏ = 
    (0,0)
    (1,0) (1,1)
    (2,0)

    ㅓ =
          (0,1)
    (1,0) (1,1)
          (2,1)
    """
    global max_sum
    t_shapes = [
        [(0,0), (0,1), (0,2), (1,1)],
        [(1,0), (1,1), (1,2), (0,1)],
        [(0,0), (1,0), (2,0), (1,1)],
        [(0,1), (1,1), (2,1), (1,0)]
    ]

    for shape in t_shapes:
        total = 0
        valid = True

        for dx, dy in shape:
            nx,ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < M:
                total += board[nx][ny]
            else:
                valid = False
                break
        
        if valid:
            max_sum = max(max_sum, total)


for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False

        check_t_shape(i,j)

print(max_sum)