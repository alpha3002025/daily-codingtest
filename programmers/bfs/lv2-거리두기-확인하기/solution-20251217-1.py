from collections import deque

PERSON,TABLE,PARTITION = 'P','O','X'
N = 5

def check_valid(place):
    people = []
    for r in range(N):
        for c in range(N):
            if place[r][c] == PERSON:
                people.append((r,c))
    
    for r,c in people: ## 각 응시자 마다 주변 체크 
        queue = deque()
        queue.append((r,c,0))
        visited = [[False]*N for _ in range(N)]
        visited[r][c] = True
        
        while queue:
            cr, cc, dist = queue.popleft()
            
            ## -- (1)
            ## 2 이상일 경우 통과 (검사 필요 없다.) 
            if dist >= 2:
                continue
            
            for dr,dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr, nc = cr+dr, cc+dc
                
                if 0 <= nr < 5 and 0 <= nc < 5 and not visited[nr][nc]:
                    if place[nr][nc] == PARTITION: ## OK
                        continue
                    if place[nr][nc] == PERSON: ## 사람
                        ## 거리 2 이내에 사람 발견 했으므로 0 return
                        ## (1) 에서 2 미만인 것들만 bfs 를 수행하도록 했기에 
                        ##     여기에는 거리 1인 사람만 찾게 된다.
                        return 0
                    
                    visited[nr][nc] = True
                    queue.append((nr,nc,dist+1))
    return 1

def solution(places):
    answer = []
    for place in places:
        answer.append(check_valid(place))
    return answer