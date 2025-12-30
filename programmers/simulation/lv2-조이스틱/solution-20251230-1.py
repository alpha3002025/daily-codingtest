def solution(name):
    answer = 0
    n = len(name)
    
    ## 알파벳 상하 이동 횟수
    alphabet_move_cnt = 0
    for c in name:
        alphabet_move_cnt += min(abs(ord(c) - ord('A')), abs(ord('Z') - ord(c)) + 1)
    
    ## 문자열 좌우 이동횟수
    horizontal_move_cnt = n - 1
    for i in range(n):
        next_i = i + 1
        while next_i < n and name[next_i] == 'A':
            next_i += 1
            
            ## 오른쪽으로 갔다가 돌아오기 
            ##    e.g. BBBAAZ : 0 → 2(이동2), 2 → 0(복귀2), 0 → 5(이동1) = 2+2+1=5
            dist_right_first = i * 2 + (n - next_i)
            
            ## 왼쪽으로 갔다가 돌아오기 
            ##    e.g. BBBAAZ : 0 → 5(왼쪽1), 5 → 0(오른쪽1), 0 → 1,1 → 2 (오른쪽2) = 1+1+2=4
            dist_left_first = (n - next_i) * 2 + i
            
            ## distance = min(오른쪽 갔다가 돌아오기, 왼쪽으로 갔다가 돌아오기)
            distance = min(dist_right_first, dist_left_first)
            
            ## 최소값 업데이트
            horizontal_move_cnt = min(horizontal_move_cnt, distance)
    
    ## 알파벳 이동횟수 + 좌우 이동횟수
    return alphabet_move_cnt + horizontal_move_cnt

print(solution("JEROEN"))
print(solution("JAN"))
