def solution(players, m, k):
    answer = 0
    # 각 시간대별로 운영 중인 증설 서버의 개수를 기록할 리스트 (0시 ~ 23시)
    server_status = [0] * 24
    
    for i in range(24):
        # 현재 시간대(i)에 필요한 최소 증설 서버 수 계산
        # players[i]명일 때, 필요한 증설 서버 수는 players[i] // m
        required = players[i] // m
        
        # 현재 운영 중인 서버 수가 부족한 경우 증설 진행
        if server_status[i] < required:
            # 부족한 서버 수만큼 추가
            diff = required - server_status[i]
            answer += diff
            
            # 증설된 서버는 현재 시각 포함 k시간 동안 유지됨
            # i시부터 i+k-1시까지 server_status에 반영
            # 단, 24시를 넘어가면 하루가 끝나므로 min(i + k, 24)로 범위 제한
            for j in range(i, min(i + k, 24)):
                server_status[j] += diff
                
    return answer

if __name__ == "__main__":
    # Test case example
    players = [0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    m = 2
    k = 3
    # t=1: req=1. add 1. active 1, 2, 3. answer=1
    # t=2: req=1. curr=1. ok.
    # t=3: req=1. curr=1. ok.
    # t=4: req=0. ok.
    # t=5: req=1. curr=0. add 1. active 5, 6, 7. answer=2
    print(f"Result: {solution(players, m, k)}")

