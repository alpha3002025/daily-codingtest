import sys

sys.setrecursionlimit(10**6)

def solution(grid):
    R,C = len(grid), len(grid[0])
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    
    ## 3차원 방문 배열
    visited = [[[False] * 4 for _ in range(C)] for _ in range(R)]
    answer = []
    
    for r in range(R):
        for c in range(C):
            for d in range(4):
                if not visited[r][c][d]:
                    ## 새로운 사이클 탐색
                    cnt = 0
                    cr,cc,cd = r,c,d
                    
                    while not visited[cr][cc][cd]:
                        visited[cr][cc][cd] = True
                        cnt += 1
                        
                        cmd = grid[cr][cc]
                        if cmd == 'S':
                            nd = cd
                        elif cmd == 'L':
                            if cd == 0: nd = 2
                            elif cd == 1: nd = 3
                            elif cd == 2: nd = 1
                            else: nd = 0
                        elif cmd == 'R':
                            if cd == 0: nd = 3
                            elif cd == 1: nd = 2
                            elif cd == 2: nd = 0
                            else: nd = 1
                        
                        ## 다음 좌표 이동
                        nr = (cr + directions[nd][0]) % R
                        nc = (cc + directions[nd][1]) % C
                        
                        cr,cc,cd = nr,nc,nd
                    answer.append(cnt)
    return sorted(answer)
    