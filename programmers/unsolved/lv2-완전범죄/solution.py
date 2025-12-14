def solution(info, n, m):
    """
    프로그래머스 Lv.2 완전범죄
    
    Args:
        info (list): 각 물건을 훔칠 때 남기는 흔적 [a_trace, b_trace] 리스트
        n (int): A도둑이 잡히는 흔적 누적 한계치 (n 이상이면 잡힘)
        m (int): B도둑이 잡히는 흔적 누적 한계치 (m 이상이면 잡힘)
        
    Returns:
        int: 두 도둑이 잡히지 않고 모든 물건을 훔쳤을 때, A도둑 흔적의 최솟값. 불가능하면 -1.
    """
    # dp[j] = B의 누적 흔적이 j일 때, A의 최소 누적 흔적
    # B의 흔적은 0부터 m-1까지 가능 (m 이상이면 잡히므로 저장할 필요 없음)
    INF = float('inf')
    dp = [INF] * m
    dp[0] = 0  # 초기 상태: B의 흔적 0일 때 A의 흔적 0
    
    for trace_a, trace_b in info:
        new_dp = [INF] * m
        
        for b in range(m):
            if dp[b] == INF:
                continue
            
            current_a = dp[b]
            
            # 1. A가 훔치는 경우
            # A의 흔적이 n 미만이어야 함
            next_a_trace = current_a + trace_a
            if next_a_trace < n:
                # B의 흔적(b)은 그대로 유지
                new_dp[b] = min(new_dp[b], next_a_trace)
            
            # 2. B가 훔치는 경우
            # B의 흔적이 m 미만이어야 함
            next_b_trace = b + trace_b
            if next_b_trace < m:
                # A의 흔적(current_a)은 그대로 유지
                new_dp[next_b_trace] = min(new_dp[next_b_trace], current_a)
        
        dp = new_dp
    
    # 모든 물건을 처리한 후, dp 배열에 있는 값 중 최솟값이 답
    answer = min(dp)
    
    return answer if answer != INF else -1
