import sys
board = [list(map(str, sys.stdin.readline().split())) for _ in range(5)]

offset = [
    (-1,0), (1,0), (0,-1), (0,1)
]

result = set()
def dfs(r, c, curr):
    if len(curr) == 6:
        result.add(curr)
        return
    
    for dr,dc in offset:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 5 and 0 <= nc < 5:
            dfs(nr, nc, curr + board[nr][nc])

for r in range(5):
    for c in range(5):
        dfs(r,c,board[r][c])

        
print(f"{len(result)}")