from collections import deque

def solution(queue1, queue2):
    
    sum1,sum2 = sum(queue1), sum(queue2)
    total_sum = sum1+sum2
    
    if total_sum % 2 == 1:
        return -1
    
    half = total_sum//2
    q1,q2 = deque(queue1),deque(queue2)
    
    cnt = 0
    
    while cnt < len(queue1)*3:
        if sum1 == sum2:
            return cnt
        
        if sum1 < half:
            n2 = q2.popleft()
            q1.append(n2)
            sum1 += n2
            sum2 -= n2
        else:
            n1 = q1.popleft()
            q2.append(n1)
            sum1 -= n1
            sum2 += n1
        
        cnt+=1
    
    if cnt >= len(queue1)*3:
        return -1
        
    return cnt