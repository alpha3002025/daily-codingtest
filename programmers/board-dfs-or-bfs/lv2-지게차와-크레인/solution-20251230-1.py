from collections import deque

def solution(storage, requests):
    n,m = len(storage),len(storage[0])
    
    grid = [[0] * (m+2) for _ in range(n+2)]
    for r in range(n):
        for c in range(m):
            grid[r+1][c+1] = storage[r][c]
            
    total_cnt = n*m
    
    for req in requests:
        target = req[0]
        
        outside = set() ## 외부 연결 공간
        queue = deque([(0,0)])
        visited = [[False]*(m+2) for _ in range(n+2)]
        visited[0][0] = True
        outside.add((0,0))
        
        while queue:
            r,c = queue.popleft()
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr,nc = r+dr, c+dc
                if 0 <= nr < n+2 and 0 <= nc < m+2 and not visited[nr][nc]:
                    if grid[nr][nc] == 0:
                        visited[nr][nc] = True
                        outside.add((nr,nc))
                        queue.append((nr,nc))
        
        removed = []
        is_crane = len(req) == 2
        
        for r in range(1, n+1):
            for c in range(1, m+1):
                if grid[r][c] == target:
                    if is_crane:
                        removed.append((r,c))
                    else:
                        for dr,dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                            if (r+dr, c+dc) in outside:
                                removed.append((r,c))
                                break
        for r,c in removed:
            grid[r][c] = 0
        
    answer = 0
    for r in range(1, n+1):
        for c in range(1, m+1):
            if grid[r][c] != 0:
                answer += 1
    
    return answer