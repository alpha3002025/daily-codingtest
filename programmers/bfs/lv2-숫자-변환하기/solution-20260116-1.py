from collections import deque

def solution(x, y, n):
    if x == y: 
        return 0
    
    visited = [False] * (y+1)
    
    queue = deque([(x, 0)]) ## 숫자, 비용
    visited[1] = True
    
    while queue:
        curr_num, curr_cost = queue.popleft()
        
        for next_num in [curr_num + n, curr_num * 2, curr_num * 3]:
            if next_num == y:
                return curr_cost + 1
            
            if not (1 <= next_num < y+1): continue
            if visited[next_num]: continue
            
            queue.append((next_num, curr_cost+1))
            visited[next_num] = True
    
    return -1


print(solution(10, 40, 5))
print(solution(10, 40, 30))
print(solution(2, 5, 4))
