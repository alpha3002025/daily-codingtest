def solution(players, m, k):
    server_cnt_status = [0] * 24
    
    answer = 0
    for i in range(len(players)):
        curr_users = players[i]
        required_server_cnt = curr_users // m
        
        if required_server_cnt > server_cnt_status[i]:
            to_add = abs(server_cnt_status[i] - required_server_cnt) 
            answer += to_add
            
            end = min(24, i+k)
            for j in range(i, end):
                server_cnt_status[j] += to_add
    
    return answer