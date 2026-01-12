def solution(sequence, k):
    answer = []
    
    left, right = 0,0
    curr_window = [left, right, float('inf')]
    
    current_sum = sequence[0]
    
    """
    [0,1,2,3,4,5]
     l   r
     r - l + 1 = 3 (길이(요소의 갯수))
    """
    while right < len(sequence): ## right 가 len 에 도달하지 않을 동안에만
        if current_sum > k: ## left 를 오른쪽으로 이동 (수열 길이를 줄여본다)
            current_sum -= sequence[left]
            left += 1
        elif current_sum < k: ## right 를 오른쪽으로 이동 (수열 길이를 늘려본다.)
            right += 1
            if right < len(sequence):
                current_sum += sequence[right]
        else: ## curr_sum == k
            """
             0 1 2 3 4 5
               *   *
            """
            curr_cnt = right - left + 1
            if curr_cnt < curr_window[2]:
                curr_window[0] = left
                curr_window[1] = right
                curr_window[2] = curr_cnt
            
            ## left 를 오른쪽으로 이동 (수열 길이를 줄여본다)
            current_sum -= sequence[left]
            left += 1
    
    return [curr_window[0], curr_window[1]]

print(solution([1, 2, 3, 4, 5], 7))
print(solution([1, 1, 1, 2, 3, 4, 5], 5))
print(solution([2, 2, 2, 2, 2], 6))
