from collections import deque

def solution(queue1, queue2):
    s1,s2 = sum(queue1),sum(queue2)
    total = s1 + s2
    
    if total % 2 == 1:
        return -1
    
    q1,q2 = deque(queue1), deque(queue2)
    limit = min(len(queue1), len(queue2)) * 3
    
    target = total // 2
    
    count = 0
    while count < limit:
        if s1 == target:
            return count
        
        if s1 > target:
            n = q1.popleft()
            q2.append(n)
            s1 -= n
            s2 += n
        
        else:
            n = q2.popleft()
            q1.append(n)
            s1 += n
            s2 -= n
        
        count += 1
    
    return -1