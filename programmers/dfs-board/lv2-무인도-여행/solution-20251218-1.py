import sys
sys.setrecursionlimit(10**6)

def solution(maps):
    rows,cols = len(maps),len(maps[0])
    visited = [[False]*cols for _ in range(rows)]
    answer = []
    
    def dfs(r, c):
        visited[r][c] = True
        total = int(maps[r][c])
        
        for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr,nc = r+dr,c+dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if maps[nr][nc] != 'X' and not visited[nr][nc]:
                    total += dfs(nr,nc)
        
        return total
    
    for r in range(rows):
        for c in range(cols):
            if maps[r][c] != 'X' and not visited[r][c]:
                answer.append(dfs(r,c))
    
    if not answer:
        return [-1]
    
    return sorted(answer)