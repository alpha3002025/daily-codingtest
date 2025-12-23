def solution(players, m, k):
    answer = 0
    server_status = [0] * 24
    
    for i in range(len(players)):
        curr_player_cnt = players[i]
        required_server_cnt = curr_player_cnt // m
        
        if server_status[i] < required_server_cnt:
            diff = required_server_cnt - server_status[i]
            answer += diff
            
            end = min(i+k, 24)
            for j in range(i, end):
                server_status[j] += diff
    
    return answer

print(solution([0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 4, 2, 0, 6, 0, 4, 2, 13, 3, 5, 10, 0, 1, 5], 3, 5))
print(solution([0, 0, 0, 10, 0, 12, 0, 15, 0, 1, 0, 1, 0, 0, 0, 5, 0, 0, 11, 0, 8, 0, 0, 0], 5, 1))
print(solution([0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 5, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1], 1, 1))