from collections import deque

def solution(numbers, target):
    ## 실수했던 것 (초기값을 잘못잡음)
    ## queue = deque([(0, numbers[0])]) ## index, sum
    
    ## 정상이라면 다음과 같이 해야 한다
    queue = deque([(0, 0)]) ## index, sum
    
    cnt = 0
    while queue:
        (curr_idx, curr_sum) = queue.popleft()
        
        ## 실수했던 부분
        # if curr_idx < len(numbers):
        #     ...
        
        ## 정상이라면 다음과 같이 해야 한다
        if curr_idx == len(numbers):
            if curr_sum == target:
                cnt += 1
            continue
                
        queue.append((curr_idx+1, curr_sum - numbers[curr_idx]))
        queue.append((curr_idx+1, curr_sum + numbers[curr_idx]))
    
    return cnt