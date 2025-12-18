"""bfs"""

from collections import deque

def solution(board):
    n,m = len(board), len(board[0])
    start,dest = None,None
    
    EMPTY,ROBOT,BLOCK,DEST = '.','R','D','G'
    
    for r in range(n):
        for c in range(m):
            if board[r][c] == ROBOT:
                start = (r,c)
            if board[r][c] == DEST:
                dest = (r,c)
    
    dir = [(-1,0),(1,0),(0,-1),(0,1)]
    visited = [[False]*m for _ in range(n)]
    
    queue = deque()
    queue.append((start[0], start[1],0))
    visited[start[0]][start[1]] = True
    
    while queue:
        r,c,cost = queue.popleft()
        
        if (r,c) == dest:
            return cost
        
        for dr,dc in dir:
            curr = (r,c) ## 시작
            
            while True: ## 미끄러지는 이동 구현
                nr,nc = curr[0]+dr, curr[1]+dc
                
                if not (0 <= nr < n and 0 <= nc < m):
                    break
                if board[nr][nc] == BLOCK:
                    break
                    
                curr = (nr,nc)
            
            if not visited[curr[0]][curr[1]]:
                visited[curr[0]][curr[1]] = True
                queue.append((curr[0], curr[1], cost+1))
    
    return -1