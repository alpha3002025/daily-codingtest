def solution(sequence, k):
    left, right = 0,0
    curr_window = [left, right, float('inf')] ## left, right, 수열의 개수
    curr_sum = sequence[0]
    
    while right < len(sequence):
        if curr_sum < k:
            right += 1
            if right < len(sequence):
                curr_sum += sequence[right]
        elif curr_sum > k:
            curr_sum -= sequence[left]
            left += 1
        else:
            curr_cnt = right - left + 1
            
            if curr_cnt < curr_window[2]:
                curr_window[0] = left
                curr_window[1] = right
                curr_window[2] = curr_cnt
            
            curr_sum -= sequence[left]
            left += 1
    
    return [curr_window[0], curr_window[1]]

print(solution([1, 2, 3, 4, 5], 7))
print(solution([1, 1, 1, 2, 3, 4, 5], 5))
print(solution([2, 2, 2, 2, 2], 6))