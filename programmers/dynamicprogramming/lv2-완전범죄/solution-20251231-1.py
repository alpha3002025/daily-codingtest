def solution(info, n, m):
    # dp[j] = B의 누적 흔적이 j일 때, A의 최소 누적 흔적
    # 초기화: 불가능한 상태는 INF로 설정
    INF = float('inf')
    dp = [INF] * m
    dp[0] = 0  # 초기 상태: 아무것도 훔치지 않았을 때 (A=0, B=0)
    
    for trace_a, trace_b in info:
        new_dp = [INF] * m  # 이번 아이템을 처리한 후의 상태를 저장할 배열
        
        for b in range(m):
            if dp[b] == INF:  # 도달 불가능한 상태는 건너뜀
                continue
            
            # 현재 상태: A의 흔적 = dp[b], B의 흔적 = b
            current_a = dp[b]
            
            # 1. A가 훔치는 경우
            if current_a + trace_a < n:
                new_dp[b] = min(new_dp[b], current_a + trace_a)
            
            # 2. B가 훔치는 경우
            if b + trace_b < m:
                new_dp[b + trace_b] = min(new_dp[b + trace_b], current_a)
        
        dp = new_dp  # DP 테이블 업데이트

    # 모든 아이템 처리 후, 가능한 상태 중 A의 최소 흔적 찾기
    answer = min(dp)
    
    return answer if answer != INF else -1