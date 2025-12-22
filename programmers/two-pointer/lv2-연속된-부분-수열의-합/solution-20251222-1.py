"""
[1,2,3,4,5,6,7]
 0 1 2 3 4 5 6
   l     r
 4-1+1 = 4

 [1,2,3,4,5,6,7]
  0 1 2 3 4 5 6
      l   r
  4-2+1 = 3
"""

def solution(sequence, k):
    curr_range = [0, 0, float('inf')] ## [start, end, 현재 부분수열 길이 k]
    left, right = 0, 0
    curr_sum = sequence[0]
    
    while right < len(sequence): ## right 가 len 에 도달하지 않을 동안에만
        if curr_sum < k:
            ## right 를 오른쪽으로 이동 (수열 길이를 늘려본다.)
            right += 1
            if right < len(sequence):
                curr_sum += sequence[right]
        elif curr_sum > k:
            ## left 를 오른쪽으로 이동 (수열 길이를 줄여본다.)
            curr_sum -= sequence[left]
            left += 1
        else: ## curr_sum == k 
            curr_len = right - left + 1
            if curr_len < curr_range[2]:
                curr_range[2] = curr_len
                curr_range[0] = left
                curr_range[1] = right
            
            ## left 를 오른쪽으로 이동해본다. (수열 길이를 줄여본다.)
            curr_sum -= sequence[left]
            left += 1
    
    return [curr_range[0], curr_range[1]]


print(solution([1, 2, 3, 4, 5], 7))
print(solution([1, 1, 1, 2, 3, 4, 5], 5))
print(solution([2, 2, 2, 2, 2], 6))