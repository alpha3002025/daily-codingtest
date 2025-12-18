def solution(players, m, k):
    answer = 0
    ## 0시 ~ 23시
    server_status = [0] * 24
    
    for i in range(24):
        ## 현재 접속 사용자 수에 대해 m명당 1개의 서버를 배치할때 필요한 서버의 수
        required_cnt = players[i] // m
        
        ## 현재 서버의 수가 필요한 서버의 수(=required_cnt)를 넘어설 경우
        if server_status[i] < required_cnt:
            diff = required_cnt - server_status[i]
            answer += diff
            
            ## k 시간 동안 증설한 서버의 수를 +
            ## 범위 : i ~ i+k-1
            for j in range(i, min(i+k, 24)):
                server_status[j] += diff
    
    return answer