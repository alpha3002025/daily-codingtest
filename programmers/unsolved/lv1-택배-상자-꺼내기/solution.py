def solution(n, w, num):
    """
    택배 상자 꺼내기
    
    :param n: 전체 택배 상자의 개수 (2 <= n <= 100)
    :param w: 가로로 놓는 상자의 개수 (1 <= w <= 10)
    :param num: 꺼내려는 택배 상자의 번호 (1 <= num <= n)
    :return: 꺼내야 하는 총 상자의 개수
    """
    
    # 1. 찾고자 하는 상자(num)의 위치(행, 열) 계산
    # 행(row)은 0부터 시작한다고 가정 (0층, 1층, ...)
    target_row = (num - 1) // w
    target_col_offset = (num - 1) % w
    
    # 열(col) 위치 계산 (0 ~ w-1)
    # 짝수번째 층(0, 2, ...): 왼쪽 -> 오른쪽 (0 -> w-1)
    # 홀수번째 층(1, 3, ...): 오른쪽 -> 왼쪽 (w-1 -> 0)
    if target_row % 2 == 0:
        target_col = target_col_offset
    else:
        # 홀수 층이므로, offset이 0일 때 w-1, offset이 w-1일 때 0
        target_col = w - 1 - target_col_offset
        
    count = 0
    curr_row = target_row
    
    # 2. 해당 위치(target_col)의 위에 있는 상자들을 확인하며 카운트
    # curr_row부터 층을 하나씩 올리면서 같은 열에 상자가 있는지 확인
    while True:
        # 현재 층의 시작 번호 계산 (Ex: w=6일 때, 0층:1, 1층:7, 2층:13 ...)
        start_num = curr_row * w + 1
        
        # 현재 층의 해당 열(target_col)에 있는 상자 번호 계산
        if curr_row % 2 == 0:
            curr_num = start_num + target_col
        else:
            curr_num = start_num + (w - 1 - target_col)
            
        # 계산된 상자 번호가 전체 상자 개수(n) 이하라면 상자가 존재하는 것임
        if curr_num <= n:
            count += 1
            curr_row += 1
        else:
            # 상자가 존재하지 않으면(범위 초과), 더 이상 위에 상자가 없음
            break
            
    return count
