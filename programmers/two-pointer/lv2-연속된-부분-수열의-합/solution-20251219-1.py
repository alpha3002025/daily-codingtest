def solution(sequence, k):
    n,left,right = len(sequence),0,0
    current_sum = sequence[0]
    
    best_range = [0, 0, float('inf')] ## [start,end,length]
    
    while right < n:
        if current_sum < k:
            right += 1
            if right < n:
                current_sum += sequence[right]
        elif current_sum > k:
            current_sum -= sequence[left]
            left += 1
        else: ## current_sum == k
            ## 현재 구간이 최적 구간보다 짧을 경우에만 갱신
            if (right - left + 1) < best_range[2]:
                best_range = [left, right, right - left + 1]
            
            # 다음 탐색을 위해 left 이동
            current_sum -= sequence[left] ## left 값을 빼서 left+=1 을 하기 위한 준비를 한다.
            left+=1
    
    return [best_range[0], best_range[1]]