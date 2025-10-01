import sys

N, M = map(int, sys.stdin.readline().strip().split())

board = []
board.append([0]*(N+1))
for _ in range(N+1):
    board.append([0] + list(map(int, sys.stdin.readline().strip().split())))

queries = []
for _ in range(M):
    r1, c1, r2, c2 = map(int, sys.stdin.readline().strip().split())
    queries.append((r1,c1,r2,c2))

D = [[0]*(N+1)]*(N+1)

# for c in range(N):
#     D[1][c] += board[0][c]
#     D[c][1] += board[c][0]

for r in range(1, len(D)):
    for c in range(1, len(D[r])):
        D[r][c] = D[r-1][c] + D[r][c-1] - D[r-1][c-1] + board[r][c]

for query in queries:
    r1,c1,r2,c2 = query ## 22, 34 -> (2-1,4), (3, 2-1)
    s1 = D[r1-1][c2]
    s2 = D[r2][c1-1]
    section_sum = D[r2][c2] - s1 - s2 + D[r1-1][c1-1]
    print(section_sum)





