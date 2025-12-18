def solution(dirs):
    x,y = 0,0
    visited_paths = set()
    
    ## x,y 좌표계이다. r,c 좌표계가 아니다. 이런 이유로 조금 헷갈린다.
    move = {'U': (0,1), 'D': (0,-1), 'R': (1,0), 'L': (-1,0)}
    
    for command in dirs:
        dx,dy = move[command]
        nx,ny = x+dx,y+dy
        
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            ## 길의 방향은 체크하지 않기에
            ## (출발,도착),(도착,출발) 모두 set에 넣어두고
            ## 마지막에 //2 를 통해 set 의 길이를 반으로 나눈 것이 정답
            visited_paths.add((x,y,nx,ny))
            visited_paths.add((nx,ny,x,y))
            
            ## 이동
            x,y = nx,ny
    
    ## (출발,도착)(도착,출발)로 좌표들을 넣었기에 //2를 통해 구한 절반값이 답이다.
    return len(visited_paths) // 2