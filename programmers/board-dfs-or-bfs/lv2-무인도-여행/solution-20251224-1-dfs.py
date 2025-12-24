import sys
sys.setrecursionlimit(10**6)

directions = [(-1,0), (1,0), (0,-1), (0,1)]

def dfs(cnt, board, r, c, width, height, visited):
    visited[r][c] = True
    curr_cnt = int(board[r][c])
    
    for dr,dc in directions:
        nr,nc = r+dr, c+dc
        
        if 0 <= nr < height and 0 <= nc < width:
            if visited[nr][nc]: continue
            if board[nr][nc] == 'X': continue
            curr_cnt += dfs(curr_cnt, board, nr, nc, width, height, visited)
    
    return curr_cnt
    

def solution(maps):
    width,height = len(maps[0]), len(maps)
    visited = [[False] * width for _ in range(height)]
    answer = []
    
    for r in range(len(maps)):
        for c in range(len(maps[r])):
            if maps[r][c] == 'X': continue
            if visited[r][c]: continue
            cnt = dfs(0, maps, r, c, width, height, visited)
            answer.append(cnt)
    
    if not answer:
        return [-1]
    return sorted(answer)

print(solution(["X591X","X1X5X","X231X", "1XXX1"]))
print(solution(["XXX", "XXX", "XXX"]))