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

print(solution([0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 4, 2, 0, 6, 0, 4, 2, 13, 3, 5, 10, 0, 1, 5], 3, 5))

print(solution([0, 0, 0, 10, 0, 12, 0, 15, 0, 1, 0, 1, 0, 0, 0, 5, 0, 0, 11, 0, 8, 0, 0, 0], 5, 1))

print(solution([0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 5, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1], 1, 1))
