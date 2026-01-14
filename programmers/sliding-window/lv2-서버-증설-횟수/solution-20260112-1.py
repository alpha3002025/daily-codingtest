def solution(players, m, k):
    answer = 0
    
    server_status_cnt = [0] * 24
    
    for i, player in enumerate(players):
        required_server_cnt = player // m
        
        if required_server_cnt > server_status_cnt[i]:
            to_add = required_server_cnt - server_status_cnt[i]
            if to_add > 0:
                answer += to_add
        
            end = min(i + k, 24)
            for j in range(i, end):
                server_status_cnt[j] += to_add
    
    return answer


print(solution([0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 4, 2, 0, 6, 0, 4, 2, 13, 3, 5, 10, 0, 1, 5], 3, 5))

print(solution([0, 0, 0, 10, 0, 12, 0, 15, 0, 1, 0, 1, 0, 0, 0, 5, 0, 0, 11, 0, 8, 0, 0, 0], 5, 1))

print(solution([0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 5, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1], 1, 1))
