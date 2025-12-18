from collections import deque

def solution(maps):
    rows,cols = len(maps), len(maps[0])
    visited = [[False]*cols for _ in range(rows)]
    answer = []
    
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    SEA = 'X'
    
    for r in range(rows):
        for c in range(cols):
            if maps[r][c] == SEA: continue
            if visited[r][c]: continue
            
            queue = deque([(r,c)])
            visited[r][c] = True
            
            food_cnt = int(maps[r][c])
            
            while queue:
                curr_r, curr_c = queue.popleft()
                
                for dr,dc in directions:
                    nr, nc = curr_r + dr, curr_c + dc
                    
                    if not (0 <= nr < rows and 0 <= nc < cols): continue
                    if visited[nr][nc]: continue
                    if maps[nr][nc] == SEA: continue
                    
                    visited[nr][nc] = True
                    food_cnt += int(maps[nr][nc])
                    queue.append((nr,nc))
            
            answer.append(food_cnt)
    
    if not answer: return [-1]
    
    return sorted(answer)