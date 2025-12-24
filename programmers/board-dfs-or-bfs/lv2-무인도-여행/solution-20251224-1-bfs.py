from collections import deque

def solution(maps):
    rows,cols = len(maps), len(maps[0])
    visited = [[False] * cols for _ in range(rows)]
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    
    answer = []
    for r in range(rows):
        for c in range(cols):
            if visited[r][c] or maps[r][c] == 'X': continue
            queue = deque()
            
            queue.append((r,c))
            visited[r][c] = True
            cost = int(maps[r][c])
            
            while queue:
                curr_r, curr_c = queue.popleft()
                
                for dr,dc in directions:
                    nr,nc = curr_r+dr, curr_c+dc
                    if not (0 <= nr < rows and 0 <= nc < cols): continue
                    if maps[nr][nc] == 'X' or visited[nr][nc]: continue
                    cost += int(maps[nr][nc])
                    queue.append((nr,nc))
                    visited[nr][nc] = True
            answer.append(cost)
    
    if not answer: return [-1]
    
    return sorted(answer)