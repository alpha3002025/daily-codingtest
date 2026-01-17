def solution(n, m, x, y, r, c, k):
    dist = abs(x - r) + abs(y - c)
    
    if dist > k or (k - dist) % 2 == 1:
        return "impossible"
    
    ## No!!! (사전순으로 정렬해야 함)
    # d_char = ['u', 'd', 'l', 'r']
    # directions = [[-1,0], [1,0], [0,-1], [0,1]]
    
    ## 사전순
    d_char = ['d','l','r','u']
    directions = [[1,0], [0,-1], [0,1], [-1,0]]
    
    answer = []
    curr_r, curr_c = x,y
    
    for _ in range(k):
        for (dr,dc), d_ch in zip(directions, d_char):
            nr = curr_r + dr
            nc = curr_c + dc
            
            if 1 <= nr <= n and 1 <= nc <= m:
                remain_turns = k - (len(answer) + 1)
                dist_to_target = abs(nr - r) + abs(nc - c)
                
                if (dist_to_target <= remain_turns and 
                    (remain_turns - dist_to_target) % 2 == 0): 
                    answer.append(d_ch)
                    curr_r, curr_c = nr, nc
                    break
    
    return "".join(answer)