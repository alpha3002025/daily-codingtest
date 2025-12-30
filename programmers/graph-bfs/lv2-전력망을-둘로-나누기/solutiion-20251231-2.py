from collections import defaultdict
from collections import deque

def solution(n, wires):
    
    min_diff = float('inf')
    for curr in range(len(wires)):
        graph = defaultdict(list)
        except_u, except_v = wires[curr]
        
        for u,v in wires:
            if except_u == u and except_v == v: continue
            graph[u].append(v)
            graph[v].append(u)
        
        queue = deque([1]) ## 1부터 시작하라고 정해진건 아니지만 그냥 편의상 임의로 1 부터 시작
        visited = [False] * (n + 1)
        visited[1] = True
        curr_tower_cnt = 1
        
        
        while queue:
            curr = queue.popleft()
            ## 실수한 부분 (1)
            ## visited[curr] = True
            
            for next_node in graph[curr]:
                if visited[next_node]: continue
                curr_tower_cnt += 1
                queue.append(next_node)
                visited[next_node] = True ## 자꾸 빼먹네...
                ## 실수한 부분 (2)
                ## visited[next_node] = True 를 빼먹었었다.
        
        the_others_cnt = abs(n - curr_tower_cnt)
        min_diff = min(min_diff, abs(curr_tower_cnt - the_others_cnt))
    
    return min_diff