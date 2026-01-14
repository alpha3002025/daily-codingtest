from collections import deque

def solution(queue1, queue2):
    s1, s2 = sum(queue1), sum(queue2)
    total = s1 + s2
    half = total // 2
    
    if total % 2 == 1:
        return -1
    
    q1, q2 = deque(queue1), deque(queue2)
    limit = max(len(queue1), len(queue2)) * 3
    
    cnt = 0
    while cnt < limit:
        if s1 == half:
            return cnt
        
        if s1 > half:
            n = q1.popleft()
            q2.append(n)
            s1 -= n
            s2 += n
            
        else:
            n = q2.popleft()
            q1.append(n)
            s2 -= n
            s1 += n
        
        cnt += 1
    
    if cnt >= limit:
        return -1
    
    return cnt