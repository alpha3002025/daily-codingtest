def solution(players, m, k):
    answer = 0
    
    server_cnt = [0] * 24
    
    for i, player_cnt in enumerate(players):
        required_server_cnt = player_cnt // m
        
        if required_server_cnt > server_cnt[i]:
            diff = required_server_cnt - server_cnt[i]
            answer += diff

            end = min(24, i + k)
            for window_idx in range(i, end):
                server_cnt[window_idx] += diff
    
    return answer


print(solution([0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 4, 2, 0, 6, 0, 4, 2, 13, 3, 5, 10, 0, 1, 5], 3, 5))

print(solution([0, 0, 0, 10, 0, 12, 0, 15, 0, 1, 0, 1, 0, 0, 0, 5, 0, 0, 11, 0, 8, 0, 0, 0], 5, 1))

print(solution([0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 5, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1], 1, 1))