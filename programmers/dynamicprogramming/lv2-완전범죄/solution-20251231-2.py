def solution(info, n, m):
    INF = float('inf')
    dp = [INF] * m
    dp[0] = 0
    
    for a_cost, b_cost in info:
        new_dp = [INF] * m
        
        for curr_b_cnt in range(m):
            if dp[curr_b_cnt] == INF:
                continue
            
            ### 현재상태 : A의 흔적 = dp[curr_b_cnt], B의 흔적 = curr_b_cnt
            curr_a_cnt = dp[curr_b_cnt]
            
            if curr_a_cnt + a_cost < n:
                ### A가 훔칠때 (b가 훔치지 않을때 (new_dp[curr_b_cnt]))
                ### = min (A가 훔칠때, A가 훔치지 않을때(=new_dp[curr_b_cnt])
                new_dp[curr_b_cnt] = min(dp[curr_b_cnt] + a_cost, new_dp[curr_b_cnt])
            
            if curr_b_cnt + b_cost < m:
                ### B가 훔칠때 (new_dp[curr_b_cnt + b_cost])
                ### = min (B가 훔칠때, B가 아무것도 안할때(=curr_a_cnt))
                new_dp[curr_b_cnt + b_cost] = min(new_dp[curr_b_cnt + b_cost], curr_a_cnt)
        
        dp = new_dp
    
    answer = min(dp)
    return answer if answer != INF else -1